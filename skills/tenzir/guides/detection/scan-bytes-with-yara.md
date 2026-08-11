---
title: "Scan bytes with YARA"
description: "Run YARA rules on files and byte streams in the pipeline and turn matches into OCSF Detection Findings"
canonical: https://tenzir.com/docs/guides/detection/scan-bytes-with-yara
source: https://tenzir.com/docs/guides/detection/scan-bytes-with-yara.md
section: "Docs"
---

# Scan bytes with YARA

> Run YARA rules on files and byte streams in the pipeline and turn matches into OCSF Detection Findings

This guide shows you how to run [YARA](https://virustotal.github.io/yara/) rules with the [`yara`](https://tenzir.com/docs/reference/operators/yara.md) operator. YARA covers the one detection input that the rest of this group does not: raw bytes. Where Sigma and TQL predicates match structured event fields, YARA matches file and payload content. Like Sigma, this is a bring-your-own-content integration: existing YARA rule sets run in the pipeline unchanged.

Start with YARA’s finite-input execution model, then scan one file or a watched set of files and convert each match into the shared OCSF finding contract.

## Understand the execution model

The [`yara`](https://tenzir.com/docs/reference/operators/yara.md) operator treats its entire input as one contiguous byte sequence: it buffers everything and scans when the input ends. That has one hard consequence: **the input must be finite**. Scan per file or per carved payload, never an unbounded stream.

Three options matter operationally:

* A rule path that points to a directory loads every contained file as a rule, so you can run a whole rule repository at once.
* `compiled_rules=true` skips compilation for pre-compiled rule sets on hot paths. Only use it with rules you compiled yourself; loading third-party compiled rules is a code execution risk.
* `fast_scan=true` enables YARA’s fast matching mode, trading match detail for throughput.

## Scan a file

Start with a rule that detects marker strings of a hypothetical malware dropper:

dropper.yara

```yara
rule SuspiciousDropper {
  meta:
    author = "Tenzir"
    description = "Detects marker strings of the demo dropper family"
  strings:
    $marker = "DROPPER-STAGE-2"
    $c2 = "callback.badcdn.example"
  condition:
    $marker or $c2
}
```

Feed a file into the scan with [`from_file`](https://tenzir.com/docs/reference/operators/from_file.md). The `mmap=true` flag maps the file into memory so [`yara`](https://tenzir.com/docs/reference/operators/yara.md) scans one contiguous chunk without an extra copy:

```tql
from_file "invoice.pdf.exe", mmap=true {
  yara "dropper.yara"
}
```

```tql
{
  rule: {
    identifier: "SuspiciousDropper",
    namespace: "default",
    tags: [],
    meta: {
      author: "Tenzir",
      description: "Detects marker strings of the demo dropper family",
    },
    strings: {
      "$marker": "DROPPER-STAGE-2",
      "$c2": "callback.badcdn.example",
    },
  },
  matches: {
    "$marker": [
      {
        data: b"DROPPER-STAGE-2",
        base: 0,
        offset: 26,
        match_length: 15,
      },
    ],
    "$c2": [
      {
        data: b"callback.badcdn.example",
        base: 0,
        offset: 61,
        match_length: 23,
      },
    ],
  },
}
```

Each matching rule produces one `yara.match` event describing the rule and every string occurrence with its offset and matched bytes.

## Scan files continuously

A watched glob scans each matching file separately, which keeps every scan finite while the pipeline checks for new files:

```tql
from_file "/srv/quarantine/*.exe", watch=10s, mmap=true {
  yara "/etc/tenzir/yara/"
}
```

Files without a match stay silent, so the pipeline emits exactly the sightings. The `watch=10s` option checks the directory for new files every ten seconds, which turns a quarantine folder into a continuous detection source. The same shape works for payloads that other tools carve out of network traffic, such as files extracted by Suricata.

## Turn matches into Detection Findings

A `yara.match` is rule context, not yet a finding. Reshape it into an OCSF [Detection Finding](https://schema.ocsf.io/classes/detection_finding) so byte-level detections flow through the same downstream processing as every other detection in this group:

```tql
from_file "invoice.pdf.exe", mmap=true {
  yara "dropper.yara"
}
// Reshape each yara.match into a Detection Finding.
this = {
  time: 2026-07-01T12:00:00Z, // use now() in a live pipeline
  metadata: {
    product: {name: "Tenzir", vendor_name: "Tenzir"},
    uid: f"finding-create-yara-{rule.namespace}-{rule.identifier}-invoice.pdf.exe",
    version: "1.9.0",
  },
  class_uid: 2004,
  category_uid: 2,
  activity_id: 1,
  severity_id: 4,
  status_id: 1,
  is_alert: true,
  finding_info: {
    uid: f"yara-{rule.namespace}-{rule.identifier}-invoice.pdf.exe",
    title: f"YARA match: {rule.identifier}",
    desc: rule.meta?.description?,
    analytic: {
      name: rule.identifier,
      uid: f"yara:{rule.namespace}:{rule.identifier}",
      type_id: 1,
    },
  },
  evidences: [{
    file: {
      name: "invoice.pdf.exe",
      path: "/srv/quarantine/invoice.pdf.exe",
      type_id: 1,
    },
  }],
  unmapped: {
    matched_strings: matches.keys(),
  },
}
type_uid = class_uid * 100 + activity_id
```

```tql
{
  time: 2026-07-01T12:00:00Z,
  metadata: {
    product: {
      name: "Tenzir",
      vendor_name: "Tenzir",
    },
    uid: "finding-create-yara-default-SuspiciousDropper-invoice.pdf.exe",
    version: "1.9.0",
  },
  class_uid: 2004,
  category_uid: 2,
  activity_id: 1,
  severity_id: 4,
  status_id: 1,
  is_alert: true,
  finding_info: {
    uid: "yara-default-SuspiciousDropper-invoice.pdf.exe",
    title: "YARA match: SuspiciousDropper",
    desc: "Detects marker strings of the demo dropper family",
    analytic: {
      name: "SuspiciousDropper",
      uid: "yara:default:SuspiciousDropper",
      type_id: 1,
    },
  },
  evidences: [
    {
      file: {
        name: "invoice.pdf.exe",
        path: "/srv/quarantine/invoice.pdf.exe",
        type_id: 1,
      },
    },
  ],
  unmapped: {
    matched_strings: [
      "$marker",
      "$c2",
    ],
  },
  type_uid: 200401,
}
```

The conventions mirror the other guides in this group, with byte-specific touches:

* `evidences[].file` carries the scanned file so analysts see what matched without re-fetching it. When your ingestion also produces OCSF [File System Activity](https://schema.ocsf.io/classes/file_activity) events (`class_uid: 1001`) for the same file, populate `file.hashes` from them and list the hash in `observables` (`type_id: 8`) so downstream indicator lookups can pivot on it. Fold that identity into both `finding_info.uid` and `metadata.uid`: the name-based identifiers shown here collide when a path is reused for new content or two scanned files share a basename.
* `finding_info.analytic` identifies the YARA rule by namespace and identifier with `type_id: 1` (`Rule`), and the rule’s `meta.description` becomes the finding description.
* The matched string identifiers travel in `unmapped`, since OCSF has no schema field for YARA match details.

## See Also

* [Detections](../../explanations/detections.md)
* [`yara`](https://tenzir.com/docs/reference/operators/yara.md)
* [`from_file`](https://tenzir.com/docs/reference/operators/from_file.md)
* [Match events with TQL](match-events-with-tql.md)
* [Model detections in OCSF](model-detections-in-ocsf.md)
* [Execute Sigma rules](execute-sigma-rules.md)
* [Create multi-stage detectors](create-multi-stage-detectors.md)
