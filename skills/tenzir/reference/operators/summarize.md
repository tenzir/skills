---
title: "summarize"
canonical: https://tenzir.com/docs/reference/operators/summarize
source: https://tenzir.com/docs/reference/operators/summarize.md
section: "Docs"
---

# summarize

> Groups events and applies aggregate functions to each group.

Groups events and applies aggregate functions to each group.

```tql
summarize (group|aggregation)..., [options={...}]
```

## Description

The `summarize` operator groups events according to certain fields and applies [aggregation functions](../functions.md#aggregation) to each group. By default, the operator consumes the entire input before producing a final summary and may reorder the event stream.

Set `options` to control three independent aspects of aggregation: `emit` defines when a result becomes complete, `mode` defines which events contribute to the result, and `output` defines which rows represent it. Event-count emission preserves the event that reaches the boundary by default. Final event output preserves every input event and adds the completed aggregate values for its group. Periodic and final summary output produces records that contain only group and aggregate fields.

The order of summary fields follows the sequence of the provided arguments. Aggregate fields are assigned in argument order with the same nested field and collision behavior as normal assignments. Trigger and event output use grouping fields only as state keys. A renamed group such as `key=user` doesn’t add or replace `key` in an enriched event.

Potentially high memory usage

Each group keeps aggregation state until an emission resets it or the pipeline ends. Streams with many unique group keys can therefore consume significant memory.

The `events` output policy currently buffers every input event until the finite input ends. Tenzir warns once the buffered input reaches approximately 512 MiB, but it doesn’t truncate the input or enforce a hidden limit. Use `window` or reduce the input population when you need a memory bound.

### `group`

To group by a certain field, use the syntax `<field>` or `<field>=<field>`. For each unique combination of the `group` fields, a single output event will be returned.

### `aggregation`

The [aggregation functions](../functions.md#aggregation) applied to each group are specified with `f(…)` or `<field>=f(…)`, where `f` is the name of an aggregation function (see below) and `<field>` is an optional name for the result. The aggregation function will produce a single result for each group.

If no name is specified, the aggregation function call will automatically generate one. If processing continues after `summarize`, we strongly recommend to specify a custom name.

### `options`

The optional `options` record separates the emission boundary, aggregation state, and output policy:

| Options                       | Behavior                                                                                                             |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| No options or `options={}`    | Emit one final summary when the input ends.                                                                          |
| `mode: "reset"`               | Emit every input event with aggregates for that event.                                                               |
| `mode: "cumulative"`          | Emit every input event with running aggregates.                                                                      |
| `emit: <int>` and `mode`      | Emit the triggering event after the specified number of input events and emit the final event of a partial interval. |
| `emit: <duration>` and `mode` | Emit summaries periodically in processing time and emit a final partial summary.                                     |
| `output: "events"`            | Buffer the finite input, then emit every event with the final aggregates for its group.                              |

Setting a count or duration `emit` value without `mode` produces an error.

#### `emit: int | duration | "final"`

`emit` defines when an aggregate result becomes complete. Set it to `"final"` to wait until the input ends and produce one completed result. On an unbounded stream, this boundary doesn’t occur unless an enclosing operator such as `window` supplies a finite input.

Use a positive `int` to emit after a number of input events. Tenzir includes the triggering event in the aggregation, preserves that event, and adds the current aggregate values. For example, `emit: 1` enriches every input event, while `emit: 100` enriches every 100th event. When the input ends before reaching the next boundary, Tenzir enriches and emits the final input event. Empty input produces no output.

Use a positive duration to emit summaries on a processing-time interval. The interval must be at least 10ms. Timer mode emits a final partial summary when the input ends and emits nothing for empty input.

Defaults to `"final"`.

#### `mode: "reset" | "cumulative"`

Choose which events contribute to each result:

* `"reset"`: Clear state at every event-count or timer boundary.
* `"cumulative"`: Retain state and produce running values.

When you specify `mode` without `emit` or `output`, `emit` defaults to `1` to preserve the existing event-by-event shorthand. State mode doesn’t affect a final result because the input has only one boundary.

#### `output: "summary" | "trigger" | "events"`

Choose which rows represent a completed result:

* `"summary"`: Emit one aggregate record per group. Final and duration boundaries use this policy by default. Choose this policy when you need the aggregate results, not the original events.
* `"trigger"`: Enrich only the event that reaches a count boundary. Count boundaries use this policy by default. This treats one real input event as a checkpoint carrying interval or cumulative statistics without replaying the other events.
* `"events"`: Emit every input event exactly once with the final aggregate values for its group. Choose this policy when every original event needs the completed statistics. Empty input produces no output.

The current implementation accepts `summary` at final and duration boundaries, `trigger` at count boundaries, and `events` at the final input boundary. It rejects other combinations. In particular, `events` cannot be combined with a count or duration `emit` value or the legacy `frequency` option.

A count boundary applies to the entire input of one `summarize` instance, not independently to each grouping key. With `trigger`, only the triggering event’s group is represented in the output. In reset mode, state for the other groups is also cleared at that boundary. Put `summarize` inside an outer `group` subpipeline when each key needs an independent count and checkpoint.

Inside `window`, the window lifecycle supplies a finite input boundary. Event output preserves the order in which its `summarize` invocation receives events. Outputs from concurrent `window` subpipelines can still interleave, as described in the `window` reference.

## Examples

### Compute the sum of a field over all events

```tql
from {x: 1}, {x: 2}
summarize x=sum(x)
```

```tql
{x: 3}
```

Group over `y` and compute the sum of `x` for each group:

```tql
from {x: 0, y: 0, z: 1},
     {x: 1, y: 1, z: 2},
     {x: 1, y: 1, z: 3}
summarize y, x=sum(x)
```

```tql
{y: 0, x: 0}
{y: 1, x: 2}
```

### Gather unique values in a list

Group the input by `src_ip` and aggregate all unique `dest_port` values into a list:

```tql
summarize src_ip, distinct(dest_port)
```

Same as above, but produce a count of the unique number of values instead of a list:

```tql
summarize src_ip, count_distinct(dest_port)
```

### Compute min and max of a group

Compute minimum and maximum of the `timestamp` field per `src_ip` group:

```tql
summarize min(timestamp), max(timestamp), src_ip
```

Compute minimum and maximum of the `timestamp` field over all events:

```tql
summarize min(timestamp), max(timestamp)
```

### Check if any value of a group is true

Create a boolean flag `originator` that is `true` if any value in the `src_ip` group is `true`:

```tql
summarize src_ip, originator=any(is_orig)
```

### Create 1-hour time buckets

Create 1-hour groups and produce a summary of network traffic between host pairs:

```tql
ts = round(ts, 1h)
summarize ts, src_ip, dest_ip, sum(bytes_in), sum(bytes_out)
```

### Add running totals to every event

Preserve each event and add a running byte total for its source:

```tql
summarize total_bytes=sum(bytes), src_ip, options={mode: "cumulative"}
```

This behavior corresponds to Splunk’s `streamstats sum(bytes) BY src_ip`. Grouping fields select independent state buckets; they don’t replace or remove fields in the input event.

Use reset mode to compute aggregates from only the current event:

```tql
summarize event_bytes=sum(bytes), options={mode: "reset"}
```

### Add final statistics to every event

Preserve the input and add the final average and sample count for each user:

```tql
from {user: "alice", value: 10},
     {user: "alice", value: 20},
     {user: "bob", value: 5}
summarize user,
          avg=mean(value),
          samples=count(),
          options={output: "events"}
```

```tql
{user: "alice", value: 10, avg: 15.0, samples: 2}
{user: "alice", value: 20, avg: 15.0, samples: 2}
{user: "bob", value: 5, avg: 5.0, samples: 1}
```

This behavior corresponds to Splunk’s `eventstats`. Compose event output with `window` to attach final statistics for each fixed, trailing, count, or event-time window.

### Emit a checkpoint every 100 events

Preserve every 100th event as a checkpoint and add stream-wide running totals:

```tql
summarize events=count(), total_bytes=sum(bytes),
  options={emit: 100, mode: "cumulative", output: "trigger"}
```

The output retains the triggering event’s fields, including its timestamp and source metadata. Only that event represents the checkpoint; the other 99 events aren’t emitted.

### Emit aggregations every 5 seconds

Count events per source IP and emit results every 5 seconds, resetting the count after each emission:

```tql
summarize count(this), src_ip, options={emit: 5s, mode: "reset"}
```

### Emit cumulative totals periodically

Sum bytes and emit running totals every minute:

```tql
summarize sum(bytes), options={emit: 1min, mode: "cumulative"}
```

Timer emission uses processing time. For fixed or hopping event-time ranges, use [`window`](https://tenzir.com/docs/reference/operators/window.md). `summarize` doesn’t keep a bounded trailing history, so a Splunk `streamstats` query with `window` or `time_window` still requires a windowing strategy.

## See Also

* [`group`](https://tenzir.com/docs/reference/operators/group.md)
* [`rare`](https://tenzir.com/docs/reference/operators/rare.md)
* [`top`](https://tenzir.com/docs/reference/operators/top.md)
* [`sum`](https://tenzir.com/docs/reference/functions/sum.md)
* [`count`](https://tenzir.com/docs/reference/functions/count.md)
* [Aggregate event streams](../../guides/analytics/aggregate-event-streams.md)
* [Shape aggregation results](../../guides/analytics/shape-aggregation-results.md)
* [Work with time](../../guides/transformation/work-with-time.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
