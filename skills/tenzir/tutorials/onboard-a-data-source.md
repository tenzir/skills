---
title: "Onboard a data source"
canonical: https://tenzir.com/docs/tutorials/onboard-a-data-source
source: https://tenzir.com/docs/tutorials/onboard-a-data-source.md
section: "Docs"
---

# Onboard a data source

> Onboarding a data source means turning one product’s output into events that every later stage of the data lifecycle can use. It has two jobs. Parsing produces structured events that keep the product’s own field names, and mapping translates them into a target schema, which for us means OCSF first.

Onboarding a data source means turning one product’s output into events that every later stage of the [data lifecycle](learn-the-data-lifecycle.md) can use. It has two jobs. **Parsing** produces structured events that keep the product’s own field names, and **mapping** translates them into a target schema, which for us means [OCSF](../explanations/normalization.md) first.

This tutorial starts with five log lines and ends with an installable [package](../explanations/packages.md). We use Amazon VPC Flow Logs, and everything here applies to any product that arrives as text.

## Look at the data

Start where the source does. Amazon writes VPC Flow Logs to S3 as gzipped text, one record per line:

```text
2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 198.51.100.20 51514 443 6 10 840 1767225600 1767225660 ACCEPT OK
2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 93.184.216.34 44231 80 6 4 216 1767225601 1767225661 REJECT OK
2 123456789012 eni-0a1b2c3d4e5f67890 10.0.2.20 198.51.100.30 51515 443 6 12 980 1767225720 1767225780 ACCEPT OK
2 123456789012 eni-0a1b2c3d4e5f67890 172.31.0.5 10.0.1.10 53 40194 17 2 148 1767225725 1767225725 ACCEPT OK
2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 198.51.100.20 51514 443 6 0 0 1767225780 1767225840 ACCEPT NODATA
```

Every line is 14 space-separated fields in an order Amazon documents: version, account, interface, the two addresses, the two ports, protocol, packets, bytes, start, end, action, and status. Position carries all the meaning. `443` is a port because it sits seventh, `6` means TCP, and the two long numbers are Unix epochs.

Two details bite later. `NODATA` in the last line means Amazon captured no traffic in that window, so its zero counters are not measurements. And `-` appears wherever Amazon cannot fill a field.

## Parse it in the pipeline

Take the first line into a pipeline, split it on the documented field order with `parse_ssv`, and turn the two epochs into timestamps:

```tql
from {
  message: "2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 198.51.100.20 51514 443 6 10 840 1767225600 1767225660 ACCEPT OK",
}
flow = message.parse_ssv(
  header="version account_id interface_id srcaddr dstaddr srcport dstport protocol packets bytes start end action log_status",
  null_value="-",
)
flow.start = flow.start.seconds().from_epoch()
flow.end = flow.end.seconds().from_epoch()
```

```tql
{
  message: "2 123456789012 eni-0a1b2c3d4e5f67890 …",
  flow: {
    version: 2,
    account_id: 123456789012,
    interface_id: "eni-0a1b2c3d4e5f67890",
    srcaddr: 10.0.1.10,
    dstaddr: 198.51.100.20,
    srcport: 51514,
    dstport: 443,
    protocol: 6,
    packets: 10,
    bytes: 840,
    start: 2026-01-01T00:00:00Z,
    end: 2026-01-01T00:01:00Z,
    action: "ACCEPT",
    log_status: "OK",
  },
}
```

That is parsing, complete. Addresses are `ip` values, ports and counters are numbers, and `start` and `end` are timestamps. The `parse_ssv` call produced the fields, and the last two lines produced the types. Both halves are necessary: `where flow.start > now() - 1h` needs a `time`, and `where flow.srcaddr in 10.0.0.0/8` needs an `ip`.

Cleaning is parsing

Fixing types belongs to parsing, not to a cleanup stage afterwards. So does resolving the `-` that Amazon writes for a field it cannot fill, which `null_value="-"` handled above, along with the placeholders other products emit such as `"None"` and `"N/A"`, strings that should be numbers or durations, and values that need trimming or a default. Our guide on [cleaning up values](../guides/normalization/clean-up-values.md) works through each conversion.

What parsing does not do is rename anything. The field names are still Amazon’s, and the `NODATA` record’s zero counters stay zeroes, because the parser reports what the source said. No schema decision has happened yet, which is what lets the same parsing feed OCSF today and something else tomorrow.

## Map it to OCSF

VPC Flow Logs describe network connections, so they map to [OCSF Network Activity](https://schema.ocsf.io/1.9.0/classes/network_activity). Continue the same pipeline:

```tql
unmapped = move flow
@name = "ocsf.network_activity"
metadata = {
  version: "1.9.0",
  product: {name: "Amazon VPC", vendor_name: "AWS"},
}
category_uid = 4
class_uid = 4001
severity_id = 1
activity_id = 6
if unmapped.action == "REJECT" {
  action_id = 2
  disposition_id = 2
} else {
  action_id = 1
  disposition_id = 1
}
type_uid = class_uid * 100 + activity_id
time = move unmapped.start
end_time = move unmapped.end
src_endpoint = {ip: move unmapped.srcaddr, port: move unmapped.srcport}
dst_endpoint = {ip: move unmapped.dstaddr, port: move unmapped.dstport}
traffic = {bytes: move unmapped.bytes, packets: move unmapped.packets}
raw_data = move message
ocsf_derive
```

Two fields carry what the mapping did not translate. Every source field with no OCSF home stays in `unmapped`, so nothing disappears silently and the residue tells you what to map next. The original line stays in `raw_data`, so an analyst can compare the mapped event against what Amazon sent.

The [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) operator fills in the labels that follow from the identifiers, such as `activity_name` and `class_name`, and [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md) enforces OCSF types when a destination needs them. Our guide on [mapping to OCSF](../guides/normalization/map-to-ocsf.md) covers choosing a class and working through the attribute groups.

## Extract the parsing into an operator

This pipeline cannot be shared. Every colleague who needs VPC Flow Logs copies those five lines, and a header fix has to reach all of them.

Move it into a user-defined operator. The file path becomes the operator name, so `operators/vpc_flow/parse_v2.tql` is `amazon::vpc_flow::parse_v2`. Start with what goes in and out:

amazon/operators/vpc\_flow/parse\_v2.tql

```tql
---
description: |
  Parses AWS VPC Flow Logs in the default v2 format (14 fields). The operator
  reads the selected log line and writes the parsed record to `into`.
args:
  positional:
    - name: log
      type: field
      description: The field holding the VPC Flow Log line.
  named:
    - name: into
      type: field
      default: this
      description: The field that receives the parsed event.
---
```

The opaque input is a required positional argument, and `into` is a named output that defaults to the whole event, so a call reads from left to right. The body is the pipeline code with `$log` and `$into` in place of the field names:

amazon/operators/vpc\_flow/parse\_v2.tql

```tql
$into = $log.parse_ssv(
  header=amazon::$vpc_flow_v2_header,
  null_value="-",
)
// AWS account IDs are 12-digit strings, and `parse_ssv` infers an integer
// that drops leading zeroes.
$into.account_id = $into.account_id?.string().pad_start(12, "0")
// Convert Unix epoch seconds to timestamps.
$into.start = $into.start?.seconds().from_epoch()
$into.end = $into.end?.seconds().from_epoch()
```

TQL evaluates `$log` before writing `$into`, and no statement reads the input again afterwards, so `parse_v2 this, into=this` is well-defined. The header moved to `constants.tql` as `amazon::$vpc_flow_v2_header`, which a pipeline with an unsupported layout can pass to a plain `parse_ssv` call.

The pipeline now names the layout instead of repeating it:

```tql
from {message: "2 123456789012 eni-0a1b2c3d4e5f67890 …"}
amazon::vpc_flow::parse_v2 message, into=flow
```

Each layout gets its own operator, so the 24-field v7 format is `amazon::vpc_flow::parse_v7_ecs`, and `amazon::vpc_flow::parse` classifies a line and delegates, yielding `null` when it recognizes neither. Our guide on [adding operators](../guides/packages/add-operators.md) covers frontmatter, arguments, and the rules for operators that need scratch state.

## Extract the mapping

The mapper follows the same contract, with an input that is already structured:

amazon/operators/vpc\_flow/ocsf/map.tql

```tql
---
description: |
  AWS VPC Flow Log events → OCSF Network Activity (class 4001).
  Transforms parsed VPC Flow Log records into OCSF-compliant Network Activity
  events with support for traffic path, flow direction, and security control
  dispositions.
args:
  positional:
    - name: event
      description: The structured VPC Flow Log event to map.
      type: field
      default: this
  named:
    - name: into
      description: The field that receives the OCSF event.
      type: field
      default: this
---
```

Both arguments default to `this`, so the common call maps in place:

```tql
amazon::vpc_flow::ocsf::map
```

Name them when the event carries more than the flow record, which is what the next step needs:

```tql
amazon::vpc_flow::ocsf::map event, into=ocsf
```

The body copies the source under `$into.event`, builds OCSF under `$into.ocsf`, and emits the OCSF fields with the residue under `unmapped`. A `null` input, which is what the dispatcher yields for an unknown layout, becomes an OCSF Base Event that still carries its payload, so no line is dropped.

The mapper never sets `raw_data`. Only the caller knows which representation is worth keeping, so provenance is the caller’s decision. Two calls and one composition now do what the inline pipeline did:

```tql
amazon::vpc_flow::parse_v2 message, into=event
amazon::vpc_flow::ocsf::map event, into=ocsf
this = {...ocsf, raw_data: message, raw_data_size: message.length_bytes()}
```

## Combine them into one call

Most users want the result, not the steps. Our [library](https://github.com/tenzir/library) gives every source one operator that runs the whole path, and it stays short because each layer below it does one job:

amazon/operators/vpc\_flow/ocsf/normalize.tql

```tql
---
description: |
  Normalizes supported Amazon VPC Flow Log input to OCSF Network Activity
  (class 4001).
  One call takes a raw VPC Flow Log line all the way: it parses the line, maps
  the structured event, and stores the line as provenance. A line in an
  unsupported layout becomes an OCSF Base Event that carries the payload.
  Callers that already hold a structured VPC Flow Log event use
  `amazon::vpc_flow::ocsf::map` instead.
args:
  positional:
    - name: input
      type: field
      description: The VPC Flow value to normalize.
  named:
    - name: into
      type: field
      default: this
      description: The field that receives the OCSF event.
---


assert type_of($input).kind == "string", message="expected a raw VPC Flow Log line"


// Parsing yields null for an unsupported layout, which the mapper turns into an
// OCSF Base Event.
amazon::vpc_flow::parse $input, into=$into.event
amazon::vpc_flow::ocsf::map $into.event, into=$into.event


$into = {
  ...$into.event,
  raw_data: $input,
  raw_data_size: $input.length_bytes(),
}
```

Onboarding the source is then a single call:

```tql
amazon::vpc_flow::ocsf::normalize message
```

The parser and the mapper stay public next to it, for pipelines that have to inspect, enrich, or route the structured event before mapping.

## Make it a package

A manifest turns the files you created into a package:

amazon/package.yaml

```yaml
id: amazon
name: Amazon Web Services
author: Tenzir
description: |
  Parse Amazon VPC Flow Logs and map them to OCSF Network Activity.
categories:
  - sources
  - mappings
```

* amazon/

  * changelog/unreleased/

    * …

  * examples/

    * vpc-flow-line-to-ocsf.tql
    * vpc-flow-line-to-ocsf-staged.tql

  * operators/vpc\_flow/

    * parse.tql

    * parse\_v2.tql

    * parse\_v7\_ecs.tql

    * ocsf/

      * map.tql
      * normalize.tql

  * tests/vpc\_flow/

    * …

  * constants.tql

  * package.yaml

Ship the pipelines you wrote as examples. They run the public API on a fixed input, with no AWS access:

amazon/examples/vpc-flow-line-to-ocsf.tql

```tql
---
name: Map a VPC Flow Log line to OCSF
description: |
  Normalizes one default-format VPC Flow Log line to OCSF Network Activity. The
  normalizer selects the parser, maps the structured record, and preserves the
  line as OCSF provenance.
---


from {
  message: "2 123456789012 eni-0a1b2c3d4e5f67890 10.0.1.10 198.51.100.20 51514 443 6 10 840 1767225600 1767225660 ACCEPT OK",
}
amazon::vpc_flow::ocsf::normalize message
ocsf_derive
```

The second example, `vpc-flow-line-to-ocsf-staged.tql`, is the three-line staged version from above. Both produce the same event.

Deployment stays out. The pipeline that reads a bucket and picks a topic belongs to whoever deploys it:

```tql
from_file "s3://example-flow-logs/AWSLogs/**/*.log.gz", watch=true {
  decompress_gzip
  read_lines
}
amazon::vpc_flow::ocsf::normalize line
publish "ocsf"
```

Expose what varies as operator arguments rather than installation inputs. Arguments are typed, checked when a pipeline compiles, and free to differ per call.

## Test it

Every public operator needs a test with a fixed input and a recorded output. The parser test reads that input and writes the result to its own field:

amazon/tests/vpc\_flow/parse-default.tql

```tql
from_file env("TENZIR_INPUT") {
  read_ndjson
}
amazon::vpc_flow::parse_v2 message, into=vpc_flow
this = move vpc_flow
sort start
```

The end-to-end test feeds raw lines to the normalizer, so one run covers layout classification, parsing, mapping, and provenance:

amazon/tests/vpc\_flow/normalize.tql

```tql
from_file env("TENZIR_INPUT") {
  read_lines
}
amazon::vpc_flow::ocsf::normalize line
ocsf_cast
sort time, type_uid
```

Three more tests cover the rest: `normalize-unsupported.tql` checks that an unknown layout becomes an OCSF Base Event with its payload, `parse-v7-ecs.tql` pins the second parser, and `map-structured.tql` calls the mapper on records that arrive already structured.

Record the baselines, then compare against them:

```sh
uvx tenzir-test amazon --passthrough
uvx tenzir-test amazon --update
uvx tenzir-test amazon
```

The guide to [testing packages](../guides/packages/test-packages.md) covers inline inputs, shared fixtures, expected errors, and ordered suites.

## Ship it

Record the new capability from the package directory:

```sh
uvx tenzir-ship add \
  --title "VPC Flow Log normalization" \
  --type feature
```

Then install it by putting the directory where Tenzir looks for packages, which is the `packages` directory next to `tenzir.yaml`:

* /opt/tenzir/etc/tenzir/

  * packages/

    * amazon/ The directory you just built

      * …

  * tenzir.yaml

The directory name matches the package id, and the operators arrive under the `amazon` namespace on the next start. Installing this way keeps the package in version control with everything else that defines the deployment, so a review precedes every change and a fresh machine gets the same set of packages from the same commit.

Check what registered:

```tql
package_list
where id == "amazon"
```

Run both examples to check the transformation without AWS access, then point your own collection pipeline at the normalizer. Our guides on [maintaining a changelog](../guides/packages/maintain-a-changelog.md) and [installing a package](../guides/packages/install-a-package.md) cover releases, the Library, and the remaining install paths, including [`package_add`](https://tenzir.com/docs/reference/operators/package_add.md) for trying something out interactively.

## Next

* [Add contexts for enrichment](add-contexts-for-enrichment.md) adds a context package and enriches the endpoints you just mapped.
* Our guide on [mapping to OCSF](../guides/normalization/map-to-ocsf.md) goes deeper on classes, attribute groups, and validation.
* Our guides on [normalizing data](../guides/normalization.md) cover the other target schemas, which start from the OCSF event this package produces.
