---
title: "Aggregate event streams"
canonical: https://tenzir.com/docs/guides/analytics/aggregate-event-streams
source: https://tenzir.com/docs/guides/analytics/aggregate-event-streams.md
section: "Docs"
---

# Aggregate event streams

> This guide shows you how to aggregate event streams with summarize and window. You’ll learn to count, group, compute statistics, and apply bounded time and count windows to streaming data.

This guide shows you how to aggregate event streams with [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) and [`window`](https://tenzir.com/docs/reference/operators/window.md). You’ll learn to count, group, compute statistics, and apply bounded time and count windows to streaming data.

## Understanding the summarize operator

The [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) operator groups events and applies aggregation functions. Its syntax is:

```plaintext
summarize <aggregation>, <aggregation>, ..., <group>, <group>, ...
```

Where:

* Aggregations are expressions like [`sum`](https://tenzir.com/docs/reference/functions/sum.md), [`count`](https://tenzir.com/docs/reference/functions/count.md), [`mean`](https://tenzir.com/docs/reference/functions/mean.md), etc.
* Groups are field names to group by

## Basic aggregations

Start with fundamental aggregation functions on event streams.

### Count events

Count total events and unique values with [`count`](https://tenzir.com/docs/reference/functions/count.md) and [`count_distinct`](https://tenzir.com/docs/reference/functions/count_distinct.md):

```tql
from {product: "apple", price: 100, category: "fruit"},
     {product: "banana", price: 250, category: "fruit"},
     {product: "carrot", price: 175, category: "vegetable"},
     {product: "apple", price: 120, category: "fruit"},
     {product: "banana", price: 225, category: "fruit"}
summarize total_count = count(), unique_products = count_distinct(product)
```

```tql
{
  total_count: 5,
  unique_products: 3
}
```

### Sum and average

Calculate totals and averages:

```tql
from {product: "apple", price: 100, quantity: 2},
     {product: "banana", price: 250, quantity: 1},
     {product: "carrot", price: 175, quantity: 3},
     {product: "apple", price: 120, quantity: 2},
     {product: "banana", price: 225, quantity: 1}
summarize total_revenue = sum(price * quantity), avg_price = mean(price), total_quantity = sum(quantity)
```

```tql
{
  total_revenue: 1440,
  avg_price: 174.0,
  total_quantity: 9
}
```

### Min and max

Find extreme values with [`min`](https://tenzir.com/docs/reference/functions/min.md) and [`max`](https://tenzir.com/docs/reference/functions/max.md):

```tql
from {sensor: "A", temperature: 72, timestamp: 2024-01-15T10:00:00},
     {sensor: "B", temperature: 68, timestamp: 2024-01-15T10:05:00},
     {sensor: "A", temperature: 75, timestamp: 2024-01-15T10:10:00},
     {sensor: "B", temperature: 82, timestamp: 2024-01-15T10:15:00},
     {sensor: "A", temperature: 71, timestamp: 2024-01-15T10:20:00}
summarize min_temp = min(temperature), max_temp = max(temperature), earliest = min(timestamp), latest = max(timestamp)
```

```tql
{
  min_temp: 68,
  max_temp: 82,
  earliest: 2024-01-15T10:00:00.000000,
  latest: 2024-01-15T10:20:00.000000
}
```

## Grouping data

Group events by one or more fields to calculate aggregations per group.

### Group by single field

Calculate statistics per category:

```tql
from {product: "apple", price: 100, category: "fruit"},
     {product: "banana", price: 250, category: "fruit"},
     {product: "carrot", price: 175, category: "vegetable"},
     {product: "lettuce", price: 125, category: "vegetable"},
     {product: "orange", price: 225, category: "fruit"}
summarize avg_price = mean(price), item_count = count(), category
```

```tql
{
  avg_price: 191.66666666666666,
  item_count: 3,
  category: "fruit",
}
{
  avg_price: 150.0,
  item_count: 2,
  category: "vegetable",
}
```

### Group by multiple fields

Group by multiple dimensions:

```tql
from {user: "alice", action: "login", duration: 45, date: "2024-01-15"},
     {user: "bob", action: "login", duration: 38, date: "2024-01-15"},
     {user: "alice", action: "view", duration: 12, date: "2024-01-15"},
     {user: "alice", action: "login", duration: 52, date: "2024-01-16"},
     {user: "bob", action: "edit", duration: 89, date: "2024-01-16"}
summarize avg_duration = mean(duration), action_count = count(), user, action
```

```tql
{
  avg_duration: 38.0,
  action_count: 1,
  user: "bob",
  action: "login",
}
{
  avg_duration: 89.0,
  action_count: 1,
  user: "bob",
  action: "edit",
}
{
  avg_duration: 48.5,
  action_count: 2,
  user: "alice",
  action: "login",
}
{
  avg_duration: 12.0,
  action_count: 1,
  user: "alice",
  action: "view",
}
```

## Add running statistics to events

Choose between incremental aggregation and a bounded trailing window based on whether old events must expire from the result.

Use cumulative event emission from [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) for unbounded running aggregates. It preserves each event and updates compact aggregate state:

```tql
from {user: "alice", bytes: 10},
     {user: "bob", bytes: 5},
     {user: "alice", bytes: 20}
summarize running_bytes=sum(bytes), events=count(), user,
  options={mode: "cumulative"}
```

```tql
{user: "alice", bytes: 10, running_bytes: 10, events: 1}
{user: "bob", bytes: 5, running_bytes: 5, events: 1}
{user: "alice", bytes: 20, running_bytes: 30, events: 2}
```

This corresponds to Splunk `streamstats` without `window` or `time_window`:

```spl
... | streamstats sum(bytes) AS running_bytes count AS events BY user
```

With the default per-event cadence, `options={mode: "reset"}` calculates the aggregate fields from each input event independently. For example, `sum(bytes)` contains the current event’s `bytes` value instead of a running total. Event emission preserves input fields, treats grouping fields only as state keys, emits nothing for empty input, and doesn’t add a duplicate summary when the input ends.

Set `emit` to a positive `int` to emit less frequently. For example, `options={emit: 100, mode: "cumulative"}` enriches every 100th input event with running aggregates. If the input ends before the next boundary, `summarize` enriches and emits the final input event.

Use a trailing [`window`](https://tenzir.com/docs/reference/operators/window.md) when only a bounded count or time horizon should contribute. By default, a trailing window runs an arbitrary subpipeline once per input event and exposes that event as `$window.event`:

```tql
group user {
  window size=5min, trailing=true, on=ts {
    summarize rolling_bytes=sum(bytes), events=count()
    this = {
      ...$window.event,
      rolling_bytes: rolling_bytes,
      events: events,
    }
  }
}
```

Keep trailing history keyed

The outer `group` is intentional. Each event enters one user subpipeline, so the trailing window replays only that user’s retained history. Moving `group` inside the trailing window would replay the stream-wide history for every event and could emit one result for every user in that history. The recommendation to put `window` outside `group` applies to fixed windows that should share one stream clock, not to keyed trailing windows.

This form corresponds to Splunk `streamstats time_window=5m ... BY user`. Use `size=100, trailing=true` for the count-based equivalent of `streamstats window=100`. Generic trailing windows replay their retained history for every invocation, so prefer incremental `summarize` when you don’t need a bounded horizon or arbitrary subpipeline logic.

Set `every` to evaluate retained history less frequently. For example, `window size=10_000, every=100, trailing=true` evaluates the latest 10,000 events after every 100 inputs. Unlike event-count emission from `summarize`, a trailing `window` doesn’t fire a final partial cadence when its input ends.

A `summarize` without options emits one final result from each trailing window. If you also set `options.emit`, that inner cadence starts fresh for every window invocation and can emit multiple prefix results while consuming the replayed history. Leave `options.emit` unset when you want one result per `window` cadence.

## Emit processing-time summaries

Set `emit` to a duration and choose `"reset"` or `"cumulative"` mode to emit on a processing-time cadence. Reset mode reports only events received since the previous boundary:

```tql
summarize src_ip, events=count(), options={emit: 30s, mode: "reset"}
```

Cumulative mode retains state and reports the total so far:

```tql
summarize src_ip, events=count(), options={emit: 30s, mode: "cumulative"}
```

Both forms emit a final partial summary when the input ends. They differ from [`window`](https://tenzir.com/docs/reference/operators/window.md) because arrival time, not an event timestamp, determines the boundary.

## Aggregate periodic snapshots

Use [`every`](https://tenzir.com/docs/reference/operators/every.md) when the aggregation is tied to a wall-clock schedule, such as polling an inventory API every 10 minutes and publishing a current count of endpoint states. This pattern works well for dashboards, reports, cache refreshes, and external API polling where each run describes the current snapshot.

Don’t use [`every`](https://tenzir.com/docs/reference/operators/every.md) for streaming detections where delayed or out-of-order events can change the answer. Use [`window`](https://tenzir.com/docs/reference/operators/window.md) for event-time detections.

```tql
every 10min {
  from {host: "laptop-1", status: "healthy"},
       {host: "server-1", status: "healthy"},
       {host: "laptop-2", status: "stale"}
  summarize status, endpoint_count=count()
  snapshot_time = now()
}
head 2
sort status
```

Each run fetches a fresh snapshot, groups endpoints by current status, and adds the run time. The `from` block stands in for an inventory API response; in a long-running pipeline, replace it with [`from_http`](https://tenzir.com/docs/reference/operators/from_http.md), remove [`head`](https://tenzir.com/docs/reference/operators/head.md), and publish the compact summary to a channel or destination.

The wall-clock schedule is not an event-time window. If the pipeline starts at 09:00, [`every`](https://tenzir.com/docs/reference/operators/every.md) runs the subpipeline for `[09:00, 09:10)`, then restarts it for `[09:10, 09:20)`, and so on. The boundaries depend on when the pipeline starts, not on timestamps in the fetched data.

## Window event streams

Use [`window`](https://tenzir.com/docs/reference/operators/window.md) when an aggregation needs bounded time or event-count state. Tumbling and hopping windows create one subpipeline per aligned range. By default, trailing windows create one subpipeline per event. Set `every` or `trigger` to restrict which events fire one. Inside any form, use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) to compute counts, distinct values, and statistics.

For duration windows, specify `on` to assign events by event time and accept out-of-order data with `tolerance`. Omit `on` for processing-time windows that close on their wall-clock boundary. Use an unsigned integer `size` for windows that close after a number of events rather than an amount of time.

Put [`group`](https://tenzir.com/docs/reference/operators/group.md) outside [`window`](https://tenzir.com/docs/reference/operators/window.md) only when each key needs its own event-time clock or trailing history. For aligned fixed detections, an outer `window` with groups inside usually bounds high-cardinality state more predictably.

For complete streaming detections built on these mechanics, such as brute-force login thresholds and statistical traffic-spike baselines with alert suppression, follow the guide on [detecting over time windows](../detection/detect-over-time-windows.md).

### Compare TQL with KQL, SPL, and Cribl Stream

The following sections compare aggregation and windowing capabilities across TQL, Microsoft KQL, Splunk SPL, and Cribl Stream. They cover Tenzir’s [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), [`every`](https://tenzir.com/docs/reference/operators/every.md), [`group`](https://tenzir.com/docs/reference/operators/group.md), and [`window`](https://tenzir.com/docs/reference/operators/window.md) operators. Cribl Stream entries refer to pipeline Functions, especially [Aggregations](https://docs.cribl.io/stream/aggregations-function/), not Cribl Search.

#### Complete-input aggregation

Complete-input aggregation waits for the full input and then emits final aggregate results. Use it for batch summaries where intermediate updates and event-time boundaries do not matter.

| System       | Support | Notes                                                                                                  |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------ |
| TQL          | ✅       | [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) consumes the input by default. |
| KQL          | ✅       | Use `summarize`.                                                                                       |
| SPL          | ✅       | Use `stats`.                                                                                           |
| Cribl Stream | ⚠️      | Aggregations are time-windowed.                                                                        |

#### Grouped aggregation

Grouped aggregation computes separate aggregate results for each key, such as one count per user or host. The grouping key partitions aggregate state, but it does not add time boundaries unless you combine it with a windowing mechanism.

| System       | Support | Notes                                                                                             |
| ------------ | ------- | ------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) with grouping fields. |
| KQL          | ✅       | Use `summarize ... by key`.                                                                       |
| SPL          | ✅       | Use `stats ... BY key`.                                                                           |
| Cribl Stream | ⚠️      | Use time-windowed `Group by fields`.                                                              |

#### Periodic processing-time aggregation

Periodic processing-time aggregation emits results on a wall-clock or processing-time cadence. Use it for live dashboards and operational metrics when arrival time matters more than event timestamps.

| System       | Support | Notes                                                                                                                                                                                                                                                                 |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) without `on`, [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) `options={emit: 30s, mode: "reset"}`, or [`every`](https://tenzir.com/docs/reference/operators/every.md). |
| KQL          | ⚠️      | Use scheduled or continuous query patterns.                                                                                                                                                                                                                           |
| SPL          | ⚠️      | Use real-time or scheduled searches.                                                                                                                                                                                                                                  |
| Cribl Stream | ⚠️      | Use Scheduled Collectors; Aggregations use event-time buckets.                                                                                                                                                                                                        |

#### Periodic running stats

Periodic running stats emit accumulated values repeatedly instead of waiting for the stream to end. They show the total so far, not a bounded rolling lookback.

| System       | Support | Notes                                                                                                                  |
| ------------ | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) `options={emit: 30s, mode: "cumulative"}`. |
| KQL          | ⚠️      | Use scheduled or continuous query patterns.                                                                            |
| SPL          | ⚠️      | Use `streamstats` or scheduled searches.                                                                               |
| Cribl Stream | ⚠️      | Enable `Cumulative aggregations` in Aggregations.                                                                      |

#### Wall-clock subpipeline batches

Wall-clock subpipeline batches rerun a block of work on a fixed schedule. This is useful when the work fetches or refreshes data, rather than grouping existing events by event time.

| System       | Support | Notes                                                                                            |
| ------------ | ------- | ------------------------------------------------------------------------------------------------ |
| TQL          | ✅       | Use [`every`](https://tenzir.com/docs/reference/operators/every.md) to rerun an arbitrary block. |
| KQL          | ❌       | No direct query-language block equivalent.                                                       |
| SPL          | ❌       | No direct query-language block equivalent.                                                       |
| Cribl Stream | ⚠️      | Scheduled Collectors schedule collection work.                                                   |

#### Tumbling event-time windows

Tumbling event-time windows split events into adjacent, non-overlapping time ranges based on event timestamps. Each event belongs to one window, and each window produces its own result.

| System       | Support | Notes                                                                                   |
| ------------ | ------- | --------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `size=1h, on=ts`. |
| KQL          | ✅       | Use `summarize ... by bin(ts, 1h)`.                                                     |
| SPL          | ✅       | Use `timechart span=1h` or `bin _time`.                                                 |
| Cribl Stream | ✅       | Use Aggregations `Time window`.                                                         |

#### Hopping event-time windows

Hopping event-time windows use a window size that is larger than the step between window starts. This gives rolling context with repeated overlapping windows, so one event can contribute to several results.

| System       | Support | Notes                                                                                             |
| ------------ | ------- | ------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `size=1h, every=5m, on=ts`. |
| KQL          | ⚠️      | Use manual expansion or plugins for specific metrics.                                             |
| SPL          | ⚠️      | Use manual expansion or bucketing.                                                                |
| Cribl Stream | ❌       | No hopping window option.                                                                         |

#### Fixed count windows

Fixed count windows close after a bounded number of arriving events rather than at a time boundary. They are useful for batching and sample-based analytics where table-slice boundaries must not affect the result.

| System       | Support | Notes                                                                                                     |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `size=100` or `size=100, every=10`. |
| KQL          | ⚠️      | Use row numbering and manual bucketing.                                                                   |
| SPL          | ⚠️      | Use `streamstats window=...` for per-event results.                                                       |
| Cribl Stream | ⚠️      | Batch controls exist without a general count-window block.                                                |

#### Per-input-event running and rolling stats

Per-input-event statistics update a calculation for each arriving event. This is different from periodic emission because the output cadence follows events, not a timer. Running statistics retain unbounded aggregate state, while rolling statistics expire events outside a trailing count or time horizon.

| System       | Support | Notes                                                                                                                                                                                                                                                           |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use cumulative event emission from [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) for unbounded state or `trailing=true` with a duration or count [`window`](https://tenzir.com/docs/reference/operators/window.md) for bounded state. |
| KQL          | ⚠️      | Use manual expansion or row-window functions.                                                                                                                                                                                                                   |
| SPL          | ✅       | Use `streamstats`; `window` and `time_window` add bounded history.                                                                                                                                                                                              |
| Cribl Stream | ❌       | Aggregations emit window events.                                                                                                                                                                                                                                |

For unbounded running aggregates, TQL’s cumulative event emission from [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) avoids replaying a trailing history. This is the direct counterpart to `streamstats` without either bound.

#### Per-key event-time windows

Per-key event-time windows keep separate windowed results for each entity. Events from one noisy key cannot advance or close windows for another key.

| System       | Support | Notes                                                                                                                                           |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Compose [`group`](https://tenzir.com/docs/reference/operators/group.md) with [`window`](https://tenzir.com/docs/reference/operators/window.md). |
| KQL          | ✅       | Use `summarize ... by key, bin(ts, ...)`.                                                                                                       |
| SPL          | ✅       | Use `BY key` or split-by.                                                                                                                       |
| Cribl Stream | ✅       | Use `Group by fields` with `Time window`.                                                                                                       |

#### Streaming late-event tolerance

Streaming late-event tolerance controls how long a window remains open for out-of-order events. It lets a pipeline accept delayed data without holding every window until the input ends.

| System       | Support | Notes                                                                                  |
| ------------ | ------- | -------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `tolerance=...`. |
| KQL          | ❌       | Mostly batch or query-time semantics.                                                  |
| SPL          | ⚠️      | Depends on search order.                                                               |
| Cribl Stream | ✅       | Use Aggregations `Lag tolerance`.                                                      |

#### Independent per-key event-time clocks

Independent per-key clocks let each group advance event time based only on its own events. This prevents a busy key from making sparse keys late, but sparse windows may also close later.

| System       | Support | Notes                                                                                                                                                  |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TQL          | ✅       | Put [`window`](https://tenzir.com/docs/reference/operators/window.md) inside an outer [`group`](https://tenzir.com/docs/reference/operators/group.md). |
| KQL          | ❌       | No streaming clock per key in ad hoc KQL.                                                                                                              |
| SPL          | ⚠️      | Requires search-order dependent workarounds.                                                                                                           |
| Cribl Stream | ⚠️      | Grouped buckets exist, but no documented per-key clock.                                                                                                |

#### Arbitrary subpipeline per key

An arbitrary per-key subpipeline can do more than compute a fixed aggregate list. It can reshape, filter, enrich, or sink each group’s stream independently.

| System       | Support | Notes                                                                              |
| ------------ | ------- | ---------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`group`](https://tenzir.com/docs/reference/operators/group.md) `key { ... }`. |
| KQL          | ❌       | No direct equivalent.                                                              |
| SPL          | ❌       | No direct equivalent.                                                              |
| Cribl Stream | ❌       | No grouped Function block.                                                         |

#### Arbitrary subpipeline per window

An arbitrary per-window subpipeline runs custom logic inside each time range, count range, or per-event trailing history. It covers detections that need more than a fixed aggregate list, such as post-aggregation filtering or alert formatting.

| System       | Support | Notes                                                                            |
| ------------ | ------- | -------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `{ ... }`. |
| KQL          | ❌       | No direct equivalent.                                                            |
| SPL          | ❌       | No direct equivalent.                                                            |
| Cribl Stream | ❌       | Aggregations only emit configured outputs.                                       |

#### Sink per key or per window

A sink per key or window sends results from inside the grouped or windowed scope. This supports local alerting or routing decisions without merging all results back into a shared stream first.

| System       | Support | Notes                                                                                                                                                          |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | [`group`](https://tenzir.com/docs/reference/operators/group.md) and [`window`](https://tenzir.com/docs/reference/operators/window.md) blocks can end in sinks. |
| KQL          | ❌       | No direct query-language equivalent.                                                                                                                           |
| SPL          | ❌       | No direct query-language equivalent.                                                                                                                           |
| Cribl Stream | ⚠️      | Route emitted aggregate events downstream.                                                                                                                     |

#### Empty window padding

Empty window padding emits rows for time ranges that have no events. This is useful for charts and time-series joins that need an explicit zero or null for missing intervals.

| System       | Support | Notes                                   |
| ------------ | ------- | --------------------------------------- |
| TQL          | ❌       | Empty windows are not emitted.          |
| KQL          | ⚠️      | Use manual `range` and `union` padding. |
| SPL          | ✅       | Use `timechart cont=true`.              |
| Cribl Stream | ❌       | No documented empty buckets.            |

#### Session windows

Session windows group events by gaps in activity rather than fixed boundaries. They are useful for user sessions, transactions, and bursts where the end time depends on silence.

| System       | Support | Notes                                                      |
| ------------ | ------- | ---------------------------------------------------------- |
| TQL          | ❌       | Requires precomputed session IDs or custom stateful logic. |
| KQL          | ✅       | Use `row_window_session()`.                                |
| SPL          | ✅       | Use `transaction maxpause` and `maxspan`.                  |
| Cribl Stream | ❌       | Not native.                                                |

#### Custom alignment or calendar windows

Custom alignment or calendar windows anchor boundaries to a chosen origin or calendar unit. This matters for reports that must align to local business days, weeks, months, or other non-epoch boundaries.

| System       | Support | Notes                                                                                                                                       |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ⚠️      | Fixed [`window`](https://tenzir.com/docs/reference/operators/window.md) buckets are epoch-anchored; no custom origin or calendar alignment. |
| KQL          | ✅       | Use `bin_at()`.                                                                                                                             |
| SPL          | ✅       | Use `aligntime` and calendar spans.                                                                                                         |
| Cribl Stream | ⚠️      | Fixed `Time window` buckets; no documented custom origin or calendar alignment.                                                             |

Legend: ✅ native or covered, ⚠️ partial or workaround, ❌ missing.

Cribl Stream’s Aggregations Function runs independently per Worker Process, so aggregate state is not shared globally across workers. [Scheduled Collector jobs](https://docs.cribl.io/stream/collectors/) can run on a recurrence, but they schedule collection work rather than provide a general pipeline Function block.

## Statistical functions

Use statistical aggregation functions for deeper analysis.

### Percentiles and median

Calculate distribution statistics with [`quantile`](https://tenzir.com/docs/reference/functions/quantile.md):

```tql
from {endpoint: "/api/users", latency: 120},
     {endpoint: "/api/users", latency: 135},
     {endpoint: "/api/users", latency: 110},
     {endpoint: "/api/orders", latency: 245},
     {endpoint: "/api/orders", latency: 225},
     {endpoint: "/api/orders", latency: 280}
summarize p50 = quantile(latency, q=0.5),
          p90 = quantile(latency, q=0.9),
          p95 = quantile(latency, q=0.95),
          endpoint
```

```tql
{
  p50: 245.0,
  p90: 280.0,
  p95: 280.0,
  endpoint: "/api/orders",
}
{
  p50: 120.0,
  p90: 135.0,
  p95: 135.0,
  endpoint: "/api/users",
}
```

### Standard deviation and variance

Measure data spread with [`stddev`](https://tenzir.com/docs/reference/functions/stddev.md) and [`variance`](https://tenzir.com/docs/reference/functions/variance.md):

```tql
from {server: "web1", cpu: 45},
     {server: "web1", cpu: 52},
     {server: "web1", cpu: 48},
     {server: "web2", cpu: 85},
     {server: "web2", cpu: 92},
     {server: "web2", cpu: 88}
summarize avg_cpu = mean(cpu),
          cpu_stddev = stddev(cpu),
          cpu_variance = variance(cpu),
          server
```

```tql
{
  avg_cpu: 48.333333333333336,
  cpu_stddev: 2.8674417556808622,
  cpu_variance: 8.222222222222145,
  server: "web1",
}
{
  avg_cpu: 88.33333333333333,
  cpu_stddev: 2.8674417556810217,
  cpu_variance: 8.22222222222306,
  server: "web2",
}
```

### Mode and distinct values

Find most common values and collect unique values with [`mode`](https://tenzir.com/docs/reference/functions/mode.md), [`distinct`](https://tenzir.com/docs/reference/functions/distinct.md), and [`count_if`](https://tenzir.com/docs/reference/functions/count_if.md):

```tql
from {user: "alice", browser: "chrome", action: "login"},
     {user: "bob", browser: "firefox", action: "view"},
     {user: "alice", browser: "chrome", action: "edit"},
     {user: "charlie", browser: "chrome", action: "login"},
     {user: "alice", browser: "safari", action: "login"}
summarize most_common_browser = mode(browser),
          unique_browsers = distinct(browser),
          login_count = count_if(action, x => x == "login")
```

```tql
{
  most_common_browser: "chrome",
  unique_browsers: [
    "chrome",
    "firefox",
    "safari",
  ],
  login_count: 3,
}
```

### Value frequencies and entropy

Analyze value distributions with [`value_counts`](https://tenzir.com/docs/reference/functions/value_counts.md) and [`entropy`](https://tenzir.com/docs/reference/functions/entropy.md):

```tql
from {category: "A", value: 10},
     {category: "B", value: 20},
     {category: "A", value: 15},
     {category: "B", value: 25},
     {category: "C", value: 30}
summarize frequencies = value_counts(category),
          info_entropy = entropy(category)
```

```tql
{
  frequencies: [
    {
      value: "A",
      count: 2,
    },
    {
      value: "B",
      count: 2,
    },
    {
      value: "C",
      count: 1,
    },
  ],
  info_entropy: 1.0549201679861442,
}
```

## Collecting values

Use [`collect`](https://tenzir.com/docs/reference/functions/collect.md) and [`distinct`](https://tenzir.com/docs/reference/functions/distinct.md) to gather values:

```tql
from {user: "alice", action: "login", timestamp: 2024-01-15T10:00:00},
     {user: "bob", action: "view", timestamp: 2024-01-15T10:01:00},
     {user: "alice", action: "edit", timestamp: 2024-01-15T10:02:00},
     {user: "charlie", action: "login", timestamp: 2024-01-15T10:03:00},
     {user: "alice", action: "logout", timestamp: 2024-01-15T10:04:00}
summarize all_actions = collect(action),
          unique_users = distinct(user),
          event_count = count()
```

```tql
{
  all_actions: [
    "login",
    "view",
    "edit",
    "login",
    "logout",
  ],
  unique_users: [
    "alice",
    "charlie",
    "bob",
  ],
  event_count: 5,
}
```

### First and last values

Get boundary values with [`first`](https://tenzir.com/docs/reference/functions/first.md) and [`last`](https://tenzir.com/docs/reference/functions/last.md):

```tql
from {sensor: "temp1", reading: 72, time: 2024-01-15T09:00:00},
     {sensor: "temp1", reading: 75, time: 2024-01-15T10:00:00},
     {sensor: "temp1", reading: 78, time: 2024-01-15T11:00:00},
     {sensor: "temp2", reading: 68, time: 2024-01-15T09:00:00},
     {sensor: "temp2", reading: 71, time: 2024-01-15T10:00:00}
summarize first_reading = first(reading),
          last_reading = last(reading),
          avg_reading = mean(reading),
          sensor
```

```tql
{
  first_reading: 72,
  last_reading: 78,
  avg_reading: 75.0,
  sensor: "temp1",
}
{
  first_reading: 68,
  last_reading: 71,
  avg_reading: 69.5,
  sensor: "temp2",
}
```

### Group and collect values

Use [`collect`](https://tenzir.com/docs/reference/functions/collect.md) with grouping to build hierarchical structures:

```tql
from {dept: "Engineering", team: "Backend", member: "Alice"},
     {dept: "Engineering", team: "Backend", member: "Bob"},
     {dept: "Engineering", team: "Frontend", member: "Charlie"},
     {dept: "Sales", team: "Direct", member: "David"}
summarize dept, team, members=collect(member)
```

```tql
{
  dept: "Sales",
  team: "Direct",
  members: [
    "David",
  ],
}
{
  dept: "Engineering",
  team: "Frontend",
  members: [
    "Charlie",
  ],
}
{
  dept: "Engineering",
  team: "Backend",
  members: [
    "Alice",
    "Bob",
  ],
}
```

## Boolean aggregations

Use [`all`](https://tenzir.com/docs/reference/functions/all.md) and [`any`](https://tenzir.com/docs/reference/functions/any.md) for boolean checks:

```tql
from {test: "unit", passed: true, duration: 45},
     {test: "integration", passed: true, duration: 120},
     {test: "e2e", passed: false, duration: 300},
     {test: "performance", passed: true, duration: 180}
summarize all_passed = all(passed),
          any_failed = any(not passed),
          total_duration = sum(duration)
```

```tql
{
  all_passed: false,
  any_failed: true,
  total_duration: 645
}
```

## Conditional aggregation

Collect values conditionally during aggregation:

```tql
from {src_ip: 10.0.0.5, dst_port: 22, bytes: 1024},
     {src_ip: 192.168.1.10, dst_port: 80, bytes: 2048},
     {src_ip: 10.0.0.5, dst_port: 443, bytes: 4096},
     {src_ip: 192.168.1.10, dst_port: 22, bytes: 512}


let $critical_ports = [22, 3389, 5985]


summarize src_ip,
  total_bytes=sum(bytes),
  // Collect all unique ports
  all_ports=collect(dst_port),
  // Collect with conditional transformation
  port_types=collect("HIGH" if dst_port in $critical_ports else "LOW")
```

```tql
{src_ip: 192.168.1.10, total_bytes: 2560, all_ports: [80, 22], port_types: ["LOW", "HIGH"]}
{src_ip: 10.0.0.5, total_bytes: 5120, all_ports: [22, 443], port_types: ["HIGH", "LOW"]}
```

This pattern enables:

* Building risk profiles during aggregation
* Transforming values during collection based on conditions
* Creating categorical metrics from raw data

## Practical examples

### Analyze API response times

```tql
from {
  requests: [
    {endpoint: "/api/users", method: "GET", duration: 45, status: 200},
    {endpoint: "/api/users", method: "POST", duration: 120, status: 201},
    {endpoint: "/api/orders", method: "GET", duration: 89, status: 200},
    {endpoint: "/api/users", method: "GET", duration: 38, status: 200},
    {endpoint: "/api/orders", method: "GET", duration: 156, status: 500}
  ]
}
unroll requests
summarize endpoint=requests.endpoint,
          count=count(),
          avg_duration=mean(requests.duration)
```

```tql
{
  endpoint: "/api/orders",
  count: 2,
  avg_duration: 122.5,
}
{
  endpoint: "/api/users",
  count: 3,
  avg_duration: 67.66666666666667,
}
```

### Calculate sales metrics

```tql
from {
  sales: [
    {date: "2024-01-01", amount: 1200, region: "North"},
    {date: "2024-01-01", amount: 800, region: "South"},
    {date: "2024-01-02", amount: 1500, region: "North"},
    {date: "2024-01-02", amount: 950, region: "South"},
    {date: "2024-01-03", amount: 1100, region: "North"}
  ]
}
// Calculate totals by date
unroll sales
summarize date=sales.date, total=sum(sales.amount)
```

```tql
{date: "2024-01-01", total: 2000}
{date: "2024-01-02", total: 2450}
{date: "2024-01-03", total: 1100}
```

### Monitor system health

```tql
from {
  metrics: [
    {timestamp: "10:00", cpu: 45, memory: 62, disk: 78},
    {timestamp: "10:01", cpu: 52, memory: 64, disk: 78},
    {timestamp: "10:02", cpu: 89, memory: 71, disk: 79},
    {timestamp: "10:03", cpu: 67, memory: 68, disk: 79},
    {timestamp: "10:04", cpu: 48, memory: 65, disk: 80}
  ]
}
cpu_alert = metrics.map(m => m.cpu > 80).any()
avg_memory = metrics.map(m => m.memory).mean()
disk_trend = metrics.last().disk - metrics.first().disk
health_summary = {
  cpu_max: metrics.map(m => m.cpu).max(),
  memory_avg: avg_memory,
  disk_growth: disk_trend,
  critical: cpu_alert
}
```

```tql
{
  metrics: [ ... ],
  cpu_alert: true,
  avg_memory: 66.0,
  disk_trend: 2,
  health_summary: {
    cpu_max: 89,
    memory_avg: 66.0,
    disk_growth: 2,
    critical: true,
  },
}
```

## Complex aggregations

Combine multiple aggregation functions for comprehensive analysis:

```tql
from {method: "GET", endpoint: "/api/users", status: 200, duration: 45},
     {method: "POST", endpoint: "/api/users", status: 201, duration: 120},
     {method: "GET", endpoint: "/api/orders", status: 200, duration: 89},
     {method: "GET", endpoint: "/api/users", status: 200, duration: 38},
     {method: "GET", endpoint: "/api/orders", status: 500, duration: 156},
     {method: "DELETE", endpoint: "/api/users/123", status: 204, duration: 67}
summarize request_count = count(),
          avg_duration = mean(duration),
          error_count = count_if(status, s => s >= 400),
          unique_endpoints = count_distinct(endpoint),
          method
error_rate = error_count / request_count
```

```tql
{
  request_count: 1,
  avg_duration: 120.0,
  error_count: 0,
  unique_endpoints: 1,
  method: "POST",
  error_rate: 0.0,
}
{
  request_count: 1,
  avg_duration: 67.0,
  error_count: 0,
  unique_endpoints: 1,
  method: "DELETE",
  error_rate: 0.0,
}
{
  request_count: 4,
  avg_duration: 82.0,
  error_count: 1,
  unique_endpoints: 2,
  method: "GET",
  error_rate: 0.25,
}
```

## Best practices

1. **Choose appropriate functions**: Use [`mean`](https://tenzir.com/docs/reference/functions/mean.md) for averages, [`median`](https://tenzir.com/docs/reference/functions/median.md) for skewed data
2. **Handle empty collections**: Check if lists are empty before aggregating
3. **Consider memory usage**: Large collections can consume significant memory
4. **Combine aggregations**: Calculate multiple statistics in one pass for efficiency

## See also

* [`every`](https://tenzir.com/docs/reference/operators/every.md)
* [`group`](https://tenzir.com/docs/reference/operators/group.md)
* [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md)
* [`window`](https://tenzir.com/docs/reference/operators/window.md)
* [Shape lists](../transformation/shape-lists.md)
* [Filter and select data](../transformation/filter-and-select-data.md)
* [Slice and sample data](../optimization/slice-and-sample-data.md)
