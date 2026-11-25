---
title: "join"
canonical: https://tenzir.com/docs/reference/operators/join
source: https://tenzir.com/docs/reference/operators/join.md
section: "Docs"
---

# join

> Combines events from the pipeline input with events from a finite source subpipeline on matching keys.

Combines events from the pipeline input with events from a finite source subpipeline on matching keys.

```tql
join key:expr|left==right..., [kind=string, into=field, max_memory=int] { … }
```

## Description

The `join` operator performs a hash join between the upstream event stream (the left side) and a finite source subpipeline (the right side). It reads the right subpipeline to completion, builds an in-memory index keyed by the right-side expressions, and then streams left events through the index.

Use `join` for self-contained relational joins within a single pipeline, including one-to-many and many-to-many matches as well as semi and anti filtering. For persistent, mutable lookup tables shared across pipelines, use [`context_enrich`](context_enrich.md) instead.

### `key: expr|left==right...`

One or more comma-separated join key expressions.

* A single expression such as `user_id` evaluates identically on both the input stream and the right-hand subpipeline.
* An equality condition `lhs == rhs` evaluates `lhs` on the input stream (left) and `rhs` on the right-hand subpipeline (right). Parentheses do not change this rule, and only `==` is supported.
* Multiple comma-separated keys form a composite key where every component must match. You can freely mix shared and asymmetric keys, for example `join tenant_id, src_ip == host_ip { … }`.

### `kind = string (optional)`

The relational join kind. Supported values are:

* `"inner"` (default): Emits one event for every matching pair of left and right rows. Unmatched left rows are dropped.
* `"left"`: Emits every matching pair, plus unmatched left rows with a `null` right side.
* `"semi"`: Emits each left event that matches at least one right row, at most once and unchanged.
* `"anti"`: Emits each left event that matches no right rows, unchanged.

### `into = field (optional)`

A target field path on the left event where the matched right record is placed (or `null` when unmatched in a `"left"` join). If the target field already exists on the left event, it is overwritten.

When `into` is omitted, `"inner"` and `"left"` joins emit a record with two fields: `{left: <left_record>, right: <right_record | null>}`.

The `into` option cannot be used with `kind="semi"`, `kind="anti"`, or `this`.

### `max_memory = int (optional)`

The upper memory bound in bytes for retaining the right-hand build index, including buffered right records, materialized keys, and index overhead. When exceeded, the operator aborts the pipeline with an error.

Defaults to `512Mi` (512 MiB).

### `{ … }`

A finite source subpipeline that produces the right-hand events. It must start with a source operator (such as [`from_file`](from_file.md) or [`from_http`](from_http.md)) and output events.

The right-hand subpipeline must terminate before `join` emits any output. For `"semi"` and `"anti"` joins, only distinct right keys are retained and non-key payload fields are discarded.

### Key matching semantics

* **Null and `NaN` values:** Any top-level key component that evaluates to `null` (including missing fields) or `NaN` never matches. Rows with nested `NaN` inside a list or record key also never match. Nested `null` values inside a record or list key compare structurally.
* **Numeric types:** Integers, unsigned integers, and floating-point numbers compare by exact numeric value across types, so `1`, `uint(1)`, and `1.0` match while `9007199254740993` does not match `9007199254740992.0`.
* **Structured keys:** Record keys match regardless of field order. List keys compare element by element in order.
* **Secrets:** Secret-valued keys emit a warning and never match.
* **Ordering and metadata:** Output preserves left arrival order and, for each left event, right arrival order. Output events keep the left event’s metadata (`@name` and `@import_time`).

## Examples

### Enrich alerts with user records

```tql
from {id: 1, alert: "login"}, {id: 2, alert: "scan"}, {id: 3, alert: "exec"}
join id, kind="left", into=user {
  from {id: 1, name: "alice"}, {id: 3, name: "carol"}
}
```

```tql
{
  id: 1,
  alert: "login",
  user: {
    id: 1,
    name: "alice",
  },
}
{
  id: 2,
  alert: "scan",
  user: null,
}
{
  id: 3,
  alert: "exec",
  user: {
    id: 3,
    name: "carol",
  },
}
```

### Join on asymmetric expressions with default `{left, right}` output

```tql
from {src: "10.0.0.1", bytes: 100}, {src: "10.0.0.2", bytes: 200}
join src.ip() == host_ip {
  from {host_ip: 10.0.0.1, role: "web"}
}
```

```tql
{
  left: {
    src: "10.0.0.1",
    bytes: 100,
  },
  right: {
    host_ip: 10.0.0.1,
    role: "web",
  },
}
```

### Filter out allowlisted IPs with an anti join

```tql
from {src_ip: 10.0.0.1, event: "conn"},
     {src_ip: 10.0.0.2, event: "conn"}
join src_ip == ip, kind="anti" {
  from {ip: 10.0.0.1}
}
```

```tql
{
  src_ip: 10.0.0.2,
  event: "conn",
}
```

### Enrich live OCSF flows from an S3 asset snapshot

```tql
subscribe "ocsf.network-activity"
join src_endpoint.ip == ip, kind="left", into=_asset {
  from_s3 "s3://sec-inventory/assets/latest.parquet" {
    read_parquet
  }
  select ip, hostname, owner, zone
}
if _asset != null {
  src_endpoint.hostname = _asset.hostname
  src_endpoint.owner = {name: _asset.owner}
  src_endpoint.zone = _asset.zone
}
drop _asset
to_clickhouse table="ocsf_network_enriched",
              host="clickhouse.internal",
              password=secret("CLICKHOUSE_PASSWORD")
```

## See Also

* [Join event streams](../../guides/enrich/join-event-streams.md)
* [`context_enrich`](context_enrich.md)
* [`merge`](merge.md)
* [`group`](group.md)
