---
title: "Add operators"
canonical: https://tenzir.com/docs/guides/packages/add-operators
source: https://tenzir.com/docs/guides/packages/add-operators.md
section: "Docs"
---

# Add operators

> This guide shows you how to create user-defined operators (UDOs) for your package. You’ll learn how to define operators with positional and named arguments, and how to test them with the Test Framework.

This guide shows you how to create user-defined operators (UDOs) for your package. You’ll learn how to define operators with positional and named arguments, and how to test them with the Test Framework.

For a worked parser, follow the tutorial on [parsing logs into events](../../tutorials/onboard-a-data-source.md#parse-it-in-the-pipeline). The tutorial on [mapping events to OCSF](../../tutorials/onboard-a-data-source.md#map-it-to-ocsf) shows how to compose a public mapper with internal mapping UDOs. The tutorial on [packaging a use case](../../tutorials/onboard-a-data-source.md) combines both behind an end-to-end normalizer.

## Create a user-defined operator

**User-defined operators (UDOs)** are reusable building blocks that you can use in your pipelines. Place operator files in the `operators` directory of your package.

Tenzir names operators using the convention `<package>::[dirs...]::<basename>`. For example, a file at `operators/ocsf/map.tql` in a package with ID `vendor` becomes the operator `vendor::ocsf::map`. The `::` separator forms a [module](../../explanations/packages.md#modules), which only packages use, so no builtin can shadow your operators.

operators/ocsf/auth.tql

```tql
// Normalize authentication logs to OCSF Authentication event class
class_uid = 3002
category_uid = 3
activity_id = 1 if outcome == "success" else 2
actor.user.name = username
actor.user.uid = user_id
src_endpoint.ip = src_ip
dst_endpoint.ip = dst_ip
drop username, user_id, src_ip, dst_ip, outcome
```

After installing the package, use the operator in any pipeline:

```tql
from_file "auth.json"
vendor::ocsf::auth
publish "ocsf-events"
```

### Choose a namespace

Name the package after the vendor and give each of the vendor’s products a directory below it, so operator names read `vendor::product::<operator>`. Our `amazon` package does this: `amazon::vpc_flow::parse_v2` sits next to `amazon::route53::ocsf::map`, and adding another AWS service means adding a directory rather than renaming anything.

Drop the product level when the vendor ships one thing, or when vendor and product are the same name. Our `zeek` package is `zeek::ocsf::map`, not `zeek::zeek::ocsf::map`.

Examples in these guides use the single-level form, as in `vendor::ocsf::map`, because a second placeholder segment adds length without teaching anything. Read them as the one-product case, and insert your product level where a vendor package needs it.

## Add parameters to operators

Operators can accept positional and named arguments, enabling you to create flexible, reusable building blocks that match the calling conventions of built-in operators. Define parameters in a YAML frontmatter block at the beginning of the `.tql` file.

### Parameter schema

Each parameter supports the following fields:

| Field         | Required | Description                                          |
| ------------- | -------- | ---------------------------------------------------- |
| `name`        | Yes      | Parameter name, used as `$name` in the operator body |
| `type`        | No       | Type constraint for the parameter value              |
| `description` | No       | Documentation string for the parameter               |
| `default`     | No       | Default value if the argument is not provided        |

### Supported types

The `type` field constrains what values the parameter accepts. It uses TQL type definition syntax:

| Type       | Description                                                                   |
| ---------- | ----------------------------------------------------------------------------- |
| `field`    | A field selector (for example, `name`). Defaults must be `null` or a selector |
| `string`   | A string literal or expression                                                |
| `int`      | A signed integer value                                                        |
| `uint`     | An unsigned integer value                                                     |
| `float`    | A floating-point value                                                        |
| `bool`     | A boolean value                                                               |
| `duration` | A duration value                                                              |
| `time`     | A timestamp value                                                             |
| `ip`       | An IP address                                                                 |
| `subnet`   | A subnet value                                                                |
| `blob`     | A blob value                                                                  |
| `secret`   | A secret string (accepts string literals)                                     |

If you omit the `type` field, the parameter accepts any value.

Null values

All typed parameters accept `null` values regardless of their declared type.

### Type checking

Tenzir validates parameter types at compile time when possible:

* **Compile-time checking** occurs when arguments are constant values
* **Runtime checking** defers validation for expressions containing runtime data

If a type mismatch occurs, Tenzir reports an error with the expected type and shows usage information for the operator.

## Work with operator parameters

This section shows common patterns for defining and using operator parameters.

### Define positional arguments

Positional arguments are passed in order when calling the operator. Define them under the `args.positional` key:

operators/tag.tql

```tql
---
args:
  positional:
    - name: field
      type: field
    - name: value
      type: string
---


$field = $value
```

Call this operator with positional arguments:

```tql
from {x: 1}
vendor::tag name, "Alice"
```

```tql
{x: 1, name: "Alice"}
```

### Define named arguments

Named arguments use the `name=value` syntax and can have default values. Define them under the `args.named` key:

operators/tag.tql

```tql
---
args:
  positional:
    - name: field
      type: field
    - name: value
      type: string
  named:
    - name: prefix
      type: string
      default: ""
---


$field = f"{$prefix}{$value}"
```

Call this operator with both positional and named arguments:

```tql
from {x: 1}
vendor::tag name, "Alice", prefix="User: "
```

```tql
{x: 1, name: "User: Alice"}
```

### Make arguments optional

Positional arguments with a `default` value become optional. Callers can omit them, and Tenzir substitutes the default:

operators/greet.tql

```tql
---
args:
  positional:
    - name: name
      type: string
      default: "World"
---


greeting = f"Hello, {$name}!"
```

Calling the operator without arguments uses the default value:

```tql
from {}
vendor::greet
```

```tql
{greeting: "Hello, World!"}
```

Passing an explicit argument overrides the default:

```tql
from {}
vendor::greet "Alice"
```

```tql
{greeting: "Hello, Alice!"}
```

### Use field parameters

The `field` type enables dynamic field selection. The caller passes a field path, and the operator uses it to read or write data:

operators/double\_value.tql

```tql
---
args:
  positional:
    - name: target
      type: field
---


$target = $target * 2
```

Using the operator:

```tql
from {count: 5, score: 10}
vendor::double_value count
```

```tql
{count: 10, score: 10}
```

To update a child field of the selected target, access it like any other field. Use dot syntax for ordinary field names, string-literal bracket syntax for names with punctuation, or an index expression that resolves to a field name:

operators/tag\_nested.tql

```tql
---
args:
  positional:
    - name: target
      type: field
    - name: name
      type: string
    - name: value
      type: string
---


$target.status = $value
$target["mapped-status"] = $value
$target[$name] = $value
```

Using the operator:

```tql
from {event: {}}
vendor::tag_nested event, "dynamic-status", "ok"
```

```tql
{
  event: {
    status: "ok",
    "mapped-status": "ok",
    "dynamic-status": "ok",
  },
}
```

### Default to a selector

Field parameters accept a selector as default value, such as `this`, `this.name`, or `foo.bar`. This makes it easy to write operators that work on the entire event by default but can be scoped to a specific field on demand:

operators/wrap.tql

```tql
---
args:
  named:
    - name: field
      type: field
      default: this
---


this = {wrapped: $field}
```

Calling the operator without arguments wraps the whole event:

```tql
from {name: "Alice"}
vendor::wrap
```

```tql
{
  wrapped: {
    name: "Alice",
  },
}
```

Passing an explicit selector wraps just that field:

```tql
from {name: "Alice"}
vendor::wrap field=name
```

```tql
{
  wrapped: "Alice",
}
```

### Detect whether an argument was provided

Any typed parameter supports `default: null`, making it optional without requiring a concrete fallback value. Inside the operator body, compare the parameter against `null` to check whether the caller provided it.

This is especially useful for `field` parameters whose behavior should change entirely depending on whether the caller selected a field:

operators/redact.tql

```tql
---
args:
  positional:
    - name: input
      type: field
  named:
    - name: target
      type: field
      default: null
      description: "Optional field to redact"
---


if $target != null {
  $target = "REDACTED"
}
$input = $input
```

When the caller omits `target`, the operator skips the redaction:

```tql
from {message: "hello", secret: "s3cret"}
vendor::redact message
```

```tql
{message: "hello", secret: "s3cret"}
```

When the caller provides `target`, the operator redacts that field:

```tql
from {message: "hello", secret: "s3cret"}
vendor::redact message, target=secret
```

```tql
{message: "hello", secret: "REDACTED"}
```

The same pattern works for other types. For example, an optional `string` parameter that only applies when provided:

operators/tag.tql

```tql
---
args:
  positional:
    - name: field
      type: field
  named:
    - name: suffix
      type: string
      default: null
---


if $suffix != null {
  $field = f"{$field}{$suffix}"
}
```

Note

Callers cannot pass `null` explicitly for a `field` parameter. Writing `target=null` produces a compile-time error because `null` is not a valid field selector. The `null` default applies only when the argument is omitted entirely. Other parameter types do accept explicit `null` values.

### Call other operators

Parameterized operators can call other operators, including passing through their own parameters:

operators/transform.tql

```tql
---
args:
  positional:
    - name: field
      type: field
  named:
    - name: multiplier
      type: int
      default: 2
---


utils::scale $field, factor=$multiplier
```

## Build layered normalization APIs

Complex packages benefit from one call that covers the common case and composable operators for users who need control between stages. We use *parse* for string to record, *map* for record to record, and *normalize* for the product’s end-to-end path over a raw payload. A normalizer parses, maps, and adds provenance, while callers that already hold a structured event call the mapper directly. For a product that targets OCSF, expose these layers:

| Operator                  | Purpose                                                             |
| ------------------------- | ------------------------------------------------------------------- |
| `vendor::parse_*`         | Turn one known raw format into a structured source event.           |
| `vendor::parse`           | Classify the raw format and delegate to the matching parser.        |
| `vendor::ocsf::map`       | Map one structured source event to minimal OCSF.                    |
| `vendor::ocsf::normalize` | Apply the product’s complete standard procedure to one raw payload. |
| `vendor::ocsf::events::*` | Map specific event types such as DNS, HTTP, or authentication.      |

Skip the parse layer, and with it the normalizer, when a built-in reader already produces events. A package for a product that Tenzir reads natively, such as Zeek with [`read_zeek_tsv`](https://tenzir.com/docs/reference/operators/read_zeek_tsv.md), starts at the mapper.

This hierarchy maps directly to your directory structure:

* operators/

  * parse.tql

  * parse\_csv.tql

  * parse\_json.tql

  * ocsf/

    * map.tql

    * normalize.tql

    * events/

      * dns.tql
      * http.tql
      * auth.tql

### Map events

Give the public mapper an optional positional event and a named output. Both default to `this`, so `vendor::ocsf::map` maps the current event in place. Set the product identity first, then dispatch, and let the fallback arm produce an OCSF Base Event. That arm catches both an unrecognized event type and a `null` event, which is what a parser yields when it recognized no format:

operators/ocsf/map.tql

```tql
---
args:
  positional:
    - name: event
      description: The structured event to map.
      type: field
      default: this
  named:
    - name: into
      description: The field that receives the OCSF event.
      type: field
      default: this
---


$into = {
  event: $event,
  ocsf: {},
}


// Every event carries the product identity, whatever its class.
$into.ocsf.metadata = {
  product: {
    name: "Product",
    vendor_name: "Vendor",
  },
  version: "1.9.0",
}
$into.ocsf.severity_id = 1


match $into.event.event_type? {
  "dns" => {
    vendor::ocsf::events::dns $into
  }
  "http" | "https" => {
    vendor::ocsf::events::http $into
  }
  "auth" => {
    vendor::ocsf::events::auth $into
  }
  _ => {
    // Unsupported event type, or a payload that no parser understood: all we
    // can say is that an event happened.
    @name = "ocsf.base_event"
    $into.ocsf.category_uid = 0
    $into.ocsf.class_uid = 0
    $into.ocsf.activity_id = 0
    $into.ocsf.type_uid = 0
  }
}


$into = {...$into.ocsf, unmapped: $into.event}
```

Use `|` to give one arm several patterns. The event-specific operators `move` fields out of `$into.event` as they map them, so the closing statement returns whatever they left behind. An unsupported event type therefore keeps its complete source record in `unmapped`, and a `null` event leaves `unmapped` null.

TQL evaluates `$event` before assigning `$into`. Exact aliasing such as `vendor::ocsf::map this, into=this` is therefore well-defined. After initializing the output, access the source only through `$into.event`.

Do not set the Base Event classification before the dispatcher. It reads as if the anomaly were the normal case, it costs work on every event that a recognized type immediately overwrites, and a dispatcher that falls back to `@name` as its discriminator would read the name the operator just wrote.

A `match` puts its wildcard arm last, so one fallback arm covers both an unrecognized event type and a `null` event. A mapper without a dispatcher instead guards the `null` case first, as `amazon::vpc_flow::ocsf::map` does, which keeps the remaining statements free of the exceptional case.

The Base Event needs no `time`, and [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md) accepts an event without one, and a payload nobody parsed has no timestamp to report, so inventing one with [`now`](https://tenzir.com/docs/reference/functions/now.md) would cost a clock call per event and make baselines non-deterministic.

Internal mapping operators accept their working scope as a required positional argument. Each leaf operator handles one specific event type:

operators/ocsf/events/dns.tql

```tql
---
args:
  positional:
    - name: scope
      description: The active mapping scope.
      type: field
---


@name = "ocsf.dns_activity"
$scope.ocsf.category_uid = 4
$scope.ocsf.class_uid = 4003
$scope.ocsf.activity_id = 1
$scope.ocsf.type_uid = $scope.ocsf.class_uid * 100 + $scope.ocsf.activity_id


$scope.ocsf.query.hostname = move $scope.event.query_name
$scope.ocsf.query.type = move $scope.event.query_type
$scope.ocsf.answers = move $scope.event.dns_answers
// ... additional field mappings
```

### Classify raw formats in one parser

Give each raw format its own parser, then add `vendor::parse` to classify the format and delegate. Classifying in one place keeps the classifier next to the parsers it selects and keeps every caller, including the normalizer, free of format logic:

operators/parse.tql

```tql
---
args:
  positional:
    - name: log
      description: The field holding the raw log line.
      type: field
  named:
    - name: into
      description: The field that receives the parsed event.
      type: field
      default: this
---


if $log.starts_with("{") {
  vendor::parse_json $log, into=$into
} else if $log.match_regex(vendor::$csv_classifier) {
  vendor::parse_csv $log, into=$into
} else {
  $into = null
}
```

Classify exact known formats rather than guessing from a version token that custom formats may share, and add branches as the package learns more formats. A `null` output says “no supported format matched”, which is all a caller needs to know.

### Normalize a raw payload end to end

Add `vendor::ocsf::normalize` as the stable entry point for users who want the product’s standard OCSF result from a raw payload. It takes the payload positionally and writes to `into=this` by default:

operators/ocsf/normalize.tql

```tql
---
args:
  positional:
    - name: input
      description: The raw payload to normalize.
      type: field
  named:
    - name: into
      description: The field that receives the OCSF event.
      type: field
      default: this
---


assert type_of($input).kind == "string", message="expected a raw payload"


// Parsing yields null for an unsupported format, which the mapper turns into an
// OCSF Base Event.
vendor::parse $input, into=$into.event
vendor::ocsf::map $into.event, into=$into.event


$into = {
  ...$into.event,
  raw_data: $input,
  raw_data_size: $input.length_bytes(),
}
```

The normalizer composes the layers below it and owns exactly one decision: that the payload becomes `raw_data`. Because a raw payload is a string and the result is a record, the input can never alias the output, so no snapshot is needed.

Restricting the normalizer to raw payloads keeps the layers honest. A pipeline that already holds a structured event, whether from a JSON reader or from a package parser it called itself, continues with the mapper:

```tql
vendor::parse_json message, into=event
event.tenant = "production"
vendor::ocsf::map event, into=ocsf
this = {
  ...ocsf,
  raw_data: message,
  raw_data_size: message.length_bytes(),
}
```

After normalization or mapping, callers can run the shared OCSF helpers. The package produces minimal OCSF, [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) adds derived sibling fields, and [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md) validates the final shape:

```tql
vendor::ocsf::normalize line
ocsf_derive
ocsf_cast
```

If a caller writes the result into an envelope, flatten it before running the current stream-oriented OCSF helpers:

```tql
vendor::ocsf::normalize message, into=ocsf
this = move ocsf
ocsf_derive
ocsf_cast
```

### Design principles

When building operator hierarchies, follow these guidelines:

* **Expose one standard call**: Provide one `target::normalize` operator that applies the complete transformation for one raw payload.
* **Keep the layers reachable**: Expose parsers and a mapper independently for users who need control between stages.
* **Use positional inputs and named outputs**: Make data flow read from left to right, with `into=this` as the output default.
* **Snapshot before writing**: Initialize `$into` from every input before changing the output, then use only fields below `$into`.
* **Name the target schema first**: Use `vendor::ocsf::map` for source-to-OCSF mapping and `vendor::cim::ocsf::map` for OCSF-to-CIM mapping.
* **Keep cleanup close to mapping**: Put source-specific cleanup and shared OCSF setup in the main mapper before dispatch.
* **Produce minimal OCSF**: Set identifiers and source-derived attributes in the mapper, then use [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) for derived sibling fields.
* **Use dispatchers for routing**: Route raw formats in `parse` and event types in the mapper, so the normalizer only composes the layers.
* **Fall back to the Base Event**: Let the dispatcher’s final arm produce a Base Event, so unsupported formats and unrecognized event types still yield a valid OCSF event that carries its payload.

## See also

* [Create a package](create-a-package.md)
* [Add pipelines](add-pipelines.md)
* [Add constants](add-constants.md)
* [Test packages](test-packages.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)
