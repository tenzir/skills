---
title: "join"
canonical: https://tenzir.com/docs/reference/operators/join
source: https://tenzir.com/docs/reference/operators/join.md
section: "Docs"
---

# join

> Combines events from the pipeline input with events from a source subpipeline on matching keys.

Combines events from the pipeline input with events from a source subpipeline on matching keys.

```tql
join key:expr|left==right..., [kind=string, into=field, max_memory=int,
     refresh=duration, before=duration, after=duration, within=duration,
     on=expr|left==right, tolerance=duration, idle_timeout=duration,
     pick=string] { … }
```

## Description

The `join` operator performs a hash join between the upstream event stream (the left side) and a source subpipeline (the right side). Depending on the options provided, it runs in one of three modes:

* **Finite build (default):** Reads the right subpipeline to completion, builds an in-memory index keyed by the right-side expressions, and streams left events through that index.
* **Periodic snapshot (`refresh`):** Blocks until the initial right snapshot finishes, then periodically rebuilds a shadow snapshot in the background and swaps it atomically on clean completion.
* **Streaming windowed (`before`, `after`, or `within`):** Maintains bounded state on both sides and matches events from two live streams whenever the right event falls within `[L.time - before, L.time + after]` of a left event. The guide on [correlating live streams in time windows](../../guides/enrich/join-event-streams.md#correlate-live-streams-in-time-windows) illustrates the window, `pick`, and watermark finalization.

Use `join` for self-contained relational joins within a single pipeline, including one-to-many and many-to-many matches, backward as-of lookups, periodically reloaded snapshots, and semi or anti filtering. For persistent, mutable lookup tables shared across pipelines, use [`context_enrich`](context_enrich.md) instead.

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

The upper memory bound in bytes for retained join state, including buffered records, materialized keys, and index overhead.

* In finite build mode and streaming windowed mode, exceeding `max_memory` aborts the pipeline with an error.
* In periodic snapshot mode (`refresh`), `max_memory` covers the active and shadow snapshots combined during a reload. If the initial load exceeds `max_memory`, the pipeline fails; if a subsequent refresh exceeds `max_memory`, the operator emits a warning and keeps the previous snapshot.

Defaults to `512Mi` (512 MiB).

### `refresh = duration (optional)`

Enables periodic snapshot mode and sets the interval between background reloads of the right-hand subpipeline. Must be positive.

* The operator blocks left input until the initial snapshot completes. If the initial load fails, the pipeline fails.
* Each subsequent reload runs in the background without overlapping an in-flight reload. Expressions inside `{ … }` such as `now()` evaluate freshly on every reload.
* When a reload completes cleanly (including with zero events), the new index atomically replaces the previous snapshot.
* When a reload fails or exceeds `max_memory`, the operator emits a warning and retains the previous snapshot.

The `refresh` option cannot be combined with `before`, `after`, `within`, `on`, `tolerance`, `idle_timeout`, or `pick`.

### `before = duration (optional)`

Enables streaming windowed mode and sets how far *before* each left event’s timestamp a right event may occur and still match. Must be non-negative. Defaults to `0s` when `after` is specified.

Cannot be combined with `within` or `refresh`.

### `after = duration (optional)`

Enables streaming windowed mode and sets how far *after* each left event’s timestamp a right event may occur and still match. Must be non-negative. Defaults to `0s` when `before` is specified.

Cannot be combined with `within` or `refresh`.

### `within = duration (optional)`

Enables streaming windowed mode with a symmetric window. Setting `within=D` is shorthand for `before=D, after=D`, matching right events in `[L.time - D, L.time + D]` (inclusive). Must be non-negative.

Cannot be combined with `before`, `after`, or `refresh`.

### `on = expr|left==right (optional)`

Selects event-time windowing in streaming mode by specifying the timestamp expression for each event. Requires `before`, `after`, or `within`.

* A single expression such as `on=ts` evaluates on both sides.
* An asymmetric expression such as `on=flow_ts == lease_ts` evaluates the left operand on the input stream and the right operand on the right-hand subpipeline.
* When `on` is omitted in streaming mode, the operator uses monotonic processing time (arrival time) and expires windows automatically on wall-clock timers.
* Events whose `on` expression evaluates to `null` or a non-`time` value emit a warning once per side and never match (emitting `null` right values in `"left"` mode or passing through in `"anti"` mode).
* Each side tracks an independent event-time watermark `max_ts - tolerance`. Right entries expire once the left watermark exceeds `R.time + before`; open left entries finalize once the right watermark exceeds `L.time + after` (or when the right stream ends). Late left events emit a warning once, probe retained state, and are not dropped in `"left"` or `"anti"` joins. Late right events emit a warning once and still match left rows that remain open, but cannot match left rows that already finalized.
* Neither stream waits for the other. When one stream runs far ahead, for example a historical replay joined against a live stream, its events stay buffered until the other stream’s watermark catches up, and they count toward `max_memory`.

### `tolerance = duration (optional)`

Allows events to arrive out of timestamp order by up to `tolerance` without triggering late-event warnings or premature window finalization. Must be non-negative. Defaults to `0s`.

Requires `on` and a time bound (`before`, `after`, or `within`).

### `idle_timeout = duration (optional)`

Sets a wall-clock timeout for event-time streaming joins when one stream stops producing events. Must be positive. Disabled by default.

When the opposite stream has been silent for at least `idle_timeout` and a buffered row has waited at least `idle_timeout`, open left rows finalize and old right rows expire so memory stays bounded and unmatched `"left"` or `"anti"` events do not stall indefinitely.

Requires `on` and a time bound (`before`, `after`, or `within`).

### `pick = string (optional)`

Selects which matching right event to emit for each left event in streaming windowed mode. Requires `before`, `after`, or `within`, and cannot be used with `kind="semi"` or `kind="anti"`.

Supported values are:

* `"all"` (default): Emits every matching pair within the window as soon as both events have arrived.
* `"latest"`: Emits the single matching right event with the greatest timestamp in the window, finalizing once the window closes. On equal timestamps, the later-arriving right event wins.
* `"earliest"`: Emits the single matching right event with the smallest timestamp in the window. On equal timestamps, the earlier-arriving right event wins.
* `"nearest"`: Emits the single matching right event closest in time to the left event. On equal distance, a past event (`R.time <= L.time`) beats a future event; on equal timestamps, the later-arriving right event wins.

### `{ … }`

A source subpipeline that produces the right-hand events. It must start with a source operator (such as [`from_file`](from_file.md), [`from_s3`](from_s3.md), or [`subscribe`](subscribe.md)) and output events.

* In finite build mode and periodic snapshot mode, the subpipeline must terminate for each build.
* In streaming windowed mode, the subpipeline may run indefinitely. If the left stream finishes and all open left rows have finalized, the operator cancels the right subpipeline cleanly.
* For `"semi"` and `"anti"` joins, only distinct right keys are retained and non-key payload fields are discarded.

### Key matching semantics

* **Null and `NaN` values:** Any top-level key component that evaluates to `null` (including missing fields) or `NaN` never matches. Rows with nested `NaN` inside a list or record key also never match. Nested `null` values inside a record or list key compare structurally.
* **Numeric types:** Integers, unsigned integers, and floating-point numbers compare by exact numeric value across types, so `1`, `uint(1)`, and `1.0` match while `9007199254740993` does not match `9007199254740992.0`.
* **Structured keys:** Record keys match regardless of field order. List keys compare element by element in order.
* **Secrets:** Secret-valued keys emit a warning and never match.
* **Ordering and metadata:** In finite build and periodic snapshot modes, output preserves left arrival order and, for each left event, right arrival order. In streaming windowed mode, output emits in match and finalization order. Output events always keep the left event’s metadata (`@name` and `@import_time`).

### Query optimization

The compiler pushes downstream [`select`](select.md) projections, infallible [`where`](where.md) filters, equivalence-class predicates across plain `lhs == rhs` key pairs, and [`head`](head.md) limits (for `kind="left"`) through `join` into upstream and right-hand sources where semantically safe. For `kind="semi"` and `kind="anti"`, the right-hand source projects down to key fields only. When `pick` is not `"all"`, right-side filters stay after `join` so candidate selection remains exact; when event-time streaming (`on`) is active, filters stay after `join` on both sides so filtered events still advance watermarks (projections still push down to both sources).

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

### Attribute dynamic IPs with a backward as-of join

Use `before=1h` with `pick="latest"` and `on=ts` to match each flow against the most recent DHCP lease issued up to one hour before the flow:

```tql
from {ip: 10.0.12.45, dst_port: 443, ts: 2026-07-15T10:30:00Z},
     {ip: 10.0.12.99, dst_port: 53,  ts: 2026-07-15T10:35:00Z}
join ip, kind="left", before=1h, on=ts, pick="latest", into=lease {
  from {ip: 10.0.12.45, host: "ws-old", ts: 2026-07-15T09:40:00Z},
       {ip: 10.0.12.45, host: "ws-fin-04", ts: 2026-07-15T10:15:00Z},
       {ip: 10.0.12.45, host: "ws-later", ts: 2026-07-15T10:45:00Z}
}
sort ts
```

```tql
{
  ip: 10.0.12.45,
  dst_port: 443,
  ts: 2026-07-15T10:30:00Z,
  lease: {
    ip: 10.0.12.45,
    host: "ws-fin-04",
    ts: 2026-07-15T10:15:00Z,
  },
}
{
  ip: 10.0.12.99,
  dst_port: 53,
  ts: 2026-07-15T10:35:00Z,
  lease: null,
}
```

### Enrich live OCSF flows from a periodically refreshed S3 asset snapshot

```tql
subscribe "ocsf.network-activity"
join src_endpoint.ip == ip, kind="left", refresh=15m, into=_asset {
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
