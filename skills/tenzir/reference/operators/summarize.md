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

Set `options` to emit enriched results after a number of input events or to emit summaries periodically in processing time. Event-count emission preserves the triggering input event and adds the current aggregate values. Periodic and final emission produce summary events that contain only group and aggregate fields.

The order of summary fields follows the sequence of the provided arguments. In event mode, aggregate fields are assigned in argument order with the same nested field and collision behavior as normal assignments.

Potentially high memory usage

Each group keeps aggregation state until an emission resets it or the pipeline ends. Streams with many unique group keys can therefore consume significant memory.

### `group`

To group by a certain field, use the syntax `<field>` or `<field>=<field>`. For each unique combination of the `group` fields, a single output event will be returned.

### `aggregation`

The [aggregation functions](../functions.md#aggregation) applied to each group are specified with `f(…)` or `<field>=f(…)`, where `f` is the name of an aggregation function (see below) and `<field>` is an optional name for the result. The aggregation function will produce a single result for each group.

If no name is specified, the aggregation function call will automatically generate one. If processing continues after `summarize`, we strongly recommend to specify a custom name.

### `options`

The optional `options` record controls when `summarize` emits results and whether it retains aggregation state:

| Options                       | Behavior                                                                                                          |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| No options or `options={}`    | Emit one final summary when the input ends.                                                                       |
| `mode: "reset"`               | Emit every input event with aggregates for that event.                                                            |
| `mode: "cumulative"`          | Emit every input event with running aggregates.                                                                   |
| `emit: <int>` and `mode`      | Emit an enriched event after the specified number of input events and emit the final event of a partial interval. |
| `emit: <duration>` and `mode` | Emit summaries periodically in processing time and emit a final partial summary.                                  |

Setting `emit` without `mode` produces an error.

#### `emit: int | duration`

`emit` defines an event-count or processing-time cadence.

Use a positive `int` to emit after a number of input events. Tenzir includes the triggering event in the aggregation, preserves that event, and adds the current aggregate values. For example, `emit: 1` enriches every input event, while `emit: 100` enriches every 100th event. When the input ends before reaching the next boundary, Tenzir enriches and emits the final input event. Empty input produces no output.

Use a positive duration to emit summaries on a processing-time interval. The interval must be at least 10ms. Timer mode emits a final partial summary when the input ends and emits nothing for empty input.

#### `mode: "reset" | "cumulative"`

Choose how aggregation state behaves after each emission:

* `"reset"`: Clear state at every event-count or timer boundary.
* `"cumulative"`: Retain state and produce running values.

When you specify `mode` without `emit`, `emit` defaults to `1`.

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

### Emit running totals every 100 events

Preserve every 100th event and add the running event count for its source IP:

```tql
summarize events=count(), src_ip,
  options={emit: 100, mode: "cumulative"}
```

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
* [Work with time](../../guides/transformation/work-with-time.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
