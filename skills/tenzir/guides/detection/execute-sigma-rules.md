---
title: "Execute Sigma rules"
description: "Run Sigma v2.1 rules on structured events and emit OCSF Detection Findings with causal match evidence"
canonical: https://tenzir.com/docs/guides/detection/execute-sigma-rules
source: https://tenzir.com/docs/guides/detection/execute-sigma-rules.md
section: "Docs"
---

# Execute Sigma rules

> Run Sigma v2.1 rules on structured events and emit OCSF Detection Findings with causal match evidence

This guide shows you how to execute [Sigma](https://sigmahq.io/) detection rules with the [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md) operator. Sigma is a bring-your-own-content integration for structured events: you can run rules from the SigmaHQ corpus, a content vendor, or your own detection team inside a TQL pipeline.

Tenzir evaluates Sigma v2.1 detection rules and global filters. Every match becomes an OCSF Detection Finding by default, so Sigma output can share the same routing, storage, and triage path as findings from YARA-X and native TQL.

## Run a self-contained rule

Use `rules=` when the rule belongs to the pipeline. The following example matches an OCSF Process Activity event whose PowerShell command line contains an encoded-command argument:

```tql
from {
  time: 2026-08-14T10:00:00Z,
  metadata: {uid: "process-activity-52517", version: "1.9.0"},
  class_uid: 1007,
  activity_id: 1,
  device: {hostname: "workstation-17"},
  actor: {user: {name: "alice"}},
  process: {
    name: "PowerShell.EXE",
    cmd_line: "powershell.exe /EncodedCommand SQBFAFgA",
  },
}
sigma rules=r#"
title: Encoded PowerShell Command
id: 7f01f6b8-9f1e-48f5-bab9-2d1f7040c6a1
status: experimental
logsource:
  category: process_creation
  product: windows
detection:
  selection:
    class_uid: 1007
    activity_id: 1
    process.name|endswith: 'powershell.exe'
    process.cmd_line|windash|contains:
      - ' -enc '
      - ' -EncodedCommand '
  condition: selection
level: high
tags:
  - attack.execution
  - attack.t1059.001
"#
select title=finding_info.title,
       severity_id,
       event=evidences[0].data,
       traits=finding_info.traits,
       fields=evidences[1].sigma.fields
```

The `windash` modifier lets the values that contain `-enc` and `-EncodedCommand` also match the Windows `/enc` and `/EncodedCommand` forms. String matching is case-insensitive unless a rule adds `cased`.

The selected result has this shape:

```tql
{
  title: "Encoded PowerShell Command",
  severity_id: 4,
  event: {
    time: 2026-08-14T10:00:00Z,
    metadata: {uid: "process-activity-52517", version: "1.9.0"},
    class_uid: 1007,
    activity_id: 1,
    device: {hostname: "workstation-17"},
    actor: {user: {name: "alice"}},
    process: {
      name: "PowerShell.EXE",
      cmd_line: "powershell.exe /EncodedCommand SQBFAFgA",
    },
  },
  traits: [{name: "selection", type: "sigma:search-identifier"}],
  fields: [
    {
      field: "class_uid",
      matcher: "equals",
      case: "insensitive",
      polarity: "positive",
      value: "1007",
      path: null,
    },
    // The remaining causal field matches follow in rule order.
  ],
}
```

One input event can match multiple rules. The operator emits one finding per matching rule in deterministic source order.

## Choose a rule source

Use `path=` for a managed repository and `rules=` for content embedded in the pipeline. The two forms use the same parser, validation, filter resolution, and matching semantics.

### Load rules from files and directories

A `path=` value can name one file, one directory, or a non-empty list that mixes both:

```tql
subscribe "ocsf.process-activity"
sigma path=[
  "/etc/tenzir/sigma/windows/",
  "/etc/tenzir/sigma/local/encoded-powershell.yml",
], refresh_interval=30s
publish "detections.sigma"
```

Directories are searched recursively in lexical order and include `.yaml` and `.yml` files. An explicitly named rule file can use another extension. Overlapping entries are deduplicated. A file can contain several `---`-separated YAML documents, which lets you keep detection rules and their global filters together.

Filesystem rules refresh without restarting the pipeline. A broken change does not replace a valid active rule: Tenzir keeps that document’s last valid version, reports the new error once, and still updates unrelated rules. Removing a source file from a successfully inspected directory removes its rules.

### Embed one or more rules

A `rules=` value accepts one constant string or a list of constant strings. Each string can itself contain multiple YAML documents:

```tql
let $login_rule = r#"
title: Administrator login
id: 522a07df-a6ac-43db-85d6-f005f86ea777
logsource:
  category: authentication
detection:
  selection:
    user.name: administrator
  condition: selection
level: medium
"#


from {user: {name: "administrator"}}
sigma rules=[$login_rule]
```

Tenzir validates inline rules when it constructs the pipeline and includes the content in the operator plan. Inline rules do not access the filesystem at runtime and cannot use `refresh_interval`.

## Align rule fields with event fields

The operator applies Sigma field names directly to each input record. It does not normalize a field taxonomy or infer a log source from the event.

### Understand field lookup

For a field name such as `process.name`, Tenzir first checks whether the event has an exact top-level key named `"process.name"`. Only when that key is absent does it traverse the nested path `process.name`. This rule makes collisions deterministic for telemetry that mixes flattened and nested fields.

Keyword selections have no field name. They recursively inspect every string leaf in records and lists and match when any leaf satisfies the keyword. They do not serialize complete events or compare numbers as strings.

### Map fields before matching

When an imported rule expects generic Windows names such as `Image` and `CommandLine`, map the parsed source fields before applying it:

```tql
from_file "windows-security.xml" {
  read_delimited "</Event>\n", include_separator=true
}
this = data.parse_winlog()


Image = EventData.NewProcessName
CommandLine = EventData.CommandLine
ParentImage = EventData.ParentProcessName
User = EventData.SubjectUserName


sigma path="rules/windows/process-creation.yml"
```

The original parsed record remains available because these assignments add fields rather than replacing the event. Alternatively, rewrite the rule once against OCSF paths so the same detection works for every source that you normalize to OCSF.

### Treat `logsource` as metadata

A rule’s `logsource` does not filter input events. Tenzir has no universal way to infer Sigma’s `category`, `product`, and `service` classifiers from an arbitrary record, so automatic filtering could silently discard valid input. Gate the stream in TQL, for example by `class_uid`, and use Sigma fields for the remaining predicates.

The operator still preserves `logsource` in the finding and uses it to decide whether a global filter is compatible with a target rule.

## Use Sigma v2.1 behavior

The operator implements the Sigma v2.1 detection surface for the default `sigma` taxonomy. This includes list-valued conditions, keyword selections, `1 of` and `all of` search-identifier quantifiers, and validated modifier chains.

### Use supported modifiers

The standard v2.1 modifiers are supported except `expand`, which requires an external placeholder mapping. Important groups include:

* String matching: `contains`, `startswith`, `endswith`, `cased`, and `windash`.
* Regular expressions: `re` followed by the optional sub-modifiers `i`, `m`, and `s`.
* Encodings: `base64`, `base64offset`, `utf16le`/`wide`, `utf16be`, and `utf16`. A UTF-16 modifier must feed a Base64 modifier.
* Comparisons: `lt`, `lte`, `gt`, `gte`, `neq`, `cidr`, and `fieldref`.
* Structure and time: `exists`, `all`, `minute`, `hour`, `day`, `week`, `month`, and `year`.

Modifier order and value types matter. The operator rejects unknown modifiers, invalid chains, unresolved `expand` placeholders, and custom taxonomies with a diagnostic tied to the affected document. It never drops a modifier silently. The complete compatibility table lives in the [`sigma`](https://tenzir.com/docs/reference/operators/sigma.md) reference.

Use `windash` when a rule must recognize both Windows argument prefixes:

```yaml
CommandLine|windash|contains: ' -EncodedCommand '
```

For a native TQL translation of the same concept, the equivalent predicate is a case-insensitive regex such as `r"(?i)[/-]encodedcommand"`.

### Apply global filters

A Sigma v2.1 global filter can tune one or more rules without changing their source documents. This inline collection suppresses known administrator accounts from a process rule:

```tql
from {Image: "C:\\Temp\\evil.exe", User: "adm_backup"},
     {Image: "C:\\Temp\\evil.exe", User: "alice"}
sigma rules=r#"
title: Suspicious process
id: 6f3e2987-db24-4c78-a860-b4f4095a7095
logsource:
  category: process_creation
detection:
  selection:
    Image|endswith: '\evil.exe'
  condition: selection
---
title: Ignore administrator accounts
logsource:
  category: process_creation
filter:
  rules:
    - 6f3e2987-db24-4c78-a860-b4f4095a7095
  selection:
    User|startswith: 'adm_'
  condition: not selection
"#
select event=evidences[0].data
```

Only the event that does not match the administrator filter remains:

```tql
{
  event: {
    Image: "C:\\Temp\\evil.exe",
    User: "alice",
  },
}
```

The filter condition is AND-linked with the target detection. Targets resolve by unique `id` or `name`; `rules: any` selects every logsource-compatible rule. Compatibility requires every `category`, `product`, and `service` value in the filter to match the target, while the target may declare additional values.

Sigma v3

An omitted `sigma-version` resolves to major 2. Declaring major 2 explicitly is also accepted. A different major is rejected instead of being interpreted with v2 semantics. Provisional Sigma v3 array selectors such as `[any]`, `[all]`, `[none]`, `[all_or_empty]`, and positional indices are therefore not part of the current operator contract.

Sigma correlation documents are also rejected. Express temporal and aggregate correlations with [`window`](https://tenzir.com/docs/reference/operators/window.md), [`group`](https://tenzir.com/docs/reference/operators/group.md), and [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), as our guide on [creating multi-stage detectors](create-multi-stage-detectors.md) shows.

## Consume the OCSF finding

The default result separates normalized analytic identity, the applied policy, the original evidence, and causal match details.

### Inspect the mapping

Every match has the fixed OCSF Detection Finding classification `class_uid: 2004`, `activity_id: 1`, and `type_uid: 200401`. The Security Control profile adds `action_id: 3` (Observed) and `disposition_id: 15` (Detected). Sigma `level` maps from Unknown through Critical to `severity_id: 0` through `5`.

The operator uses the remaining fields for distinct purposes:

* `finding_info.analytic` identifies the rule by Sigma `id`, or by a stable content fingerprint when the ID is absent.
* `policy.data` preserves the complete applied rule, including global-filter adjustments.
* `evidences[0].data` preserves the original event without normalizing it into another OCSF activity class.
* `finding_info.traits` records the search identifiers that causally established the match.
* `observables` records positive matched values with paths back into the source evidence.
* `evidences[1].sigma` carries the condition trace and field-level matcher, path, case, polarity, and value details that have no dedicated OCSF field.
* ATT\&CK tags populate `finding_info.attacks` and the Security Control profile’s top-level `attacks` field.

This mapping makes the finding interoperable while retaining the information needed to explain the match. It does not set `is_alert`, because a Sigma match has no universal alerting posture. Add that policy downstream.

### Recover the lightweight representation

Use `format="plain"` when a pipeline only needs the matched event and rule:

```tql
sigma path="rules/windows.yml", format="plain"
```

The operator emits this shape without constructing an OCSF finding:

```tql
{
  event: {/* original event */},
  rule: {/* complete applied rule */},
}
```

You can also project the plain shape from the default output when one pipeline branch needs the complete OCSF finding and another needs only the event and rule:

```tql
this = {
  event: evidences[0].data,
  rule: policy.data,
}
```

## See Also

* [Detections](../../explanations/detections.md)
* [Match events with TQL](match-events-with-tql.md)
* [Model detections in OCSF](model-detections-in-ocsf.md)
* [Create multi-stage detectors](create-multi-stage-detectors.md)
* [Add operators](../packages/add-operators.md)
* [Map to OCSF](../normalization/map-to-ocsf.md)
* [Microsoft Windows Event Logs](../../integrations/microsoft/windows-event-logs.md)
