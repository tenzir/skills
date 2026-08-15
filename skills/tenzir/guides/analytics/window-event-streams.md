---
title: "Window event streams"
canonical: https://tenzir.com/docs/guides/analytics/window-event-streams
source: https://tenzir.com/docs/guides/analytics/window-event-streams.md
section: "Docs"
---

# Window event streams

> Use window when an aggregation needs bounded time or event-count state. Tumbling and hopping windows create one subpipeline per aligned range. By default, trailing windows create one subpipeline per event. Set every or trigger to restrict which events fire one. Inside any form, use summarize to compute counts, distinct values, and statistics.

Use [`window`](https://tenzir.com/docs/reference/operators/window.md) when an aggregation needs bounded time or event-count state. Tumbling and hopping windows create one subpipeline per aligned range. By default, trailing windows create one subpipeline per event. Set `every` or `trigger` to restrict which events fire one. Inside any form, use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) to compute counts, distinct values, and statistics.

The same window model covers eight combinations. The left column shows duration windows, while the right column shows event-count windows. Blue marks fixed windows, green marks trailing windows, and highlighted events show the reduced firing cadence of sampled trailing windows.

For duration windows, specify `on` to assign events by event time and accept out-of-order data with `tolerance`. Fixed windows delay closure by the tolerance, while trailing windows reorder events within it before evaluating event-anchored history. Omit `on` for processing-time windows that close on their wall-clock boundary. Use an unsigned integer `size` for windows that close after a number of events rather than an amount of time.

Put [`group`](https://tenzir.com/docs/reference/operators/group.md) outside [`window`](https://tenzir.com/docs/reference/operators/window.md) only when each key needs its own event-time clock or trailing history. For aligned fixed detections, an outer `window` with groups inside usually bounds high-cardinality state more predictably.

For complete streaming detections built on these mechanics, such as brute-force login thresholds and statistical traffic-spike baselines with alert suppression, follow the guide on [detecting over time windows](../detection/detect-over-time-windows.md).

## Compare TQL with KQL, SPL, and Cribl Stream

The following sections compare aggregation and windowing capabilities across TQL, Microsoft KQL, Splunk SPL, and Cribl Stream. They cover Tenzir’s [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), [`every`](https://tenzir.com/docs/reference/operators/every.md), [`group`](https://tenzir.com/docs/reference/operators/group.md), and [`window`](https://tenzir.com/docs/reference/operators/window.md) operators. Cribl Stream entries refer to pipeline Functions, especially [Aggregations](https://docs.cribl.io/stream/aggregations-function/), not Cribl Search.

### Complete-input aggregation

Complete-input aggregation waits for the full input and then emits final aggregate results. Use it for batch summaries where intermediate updates and event-time boundaries do not matter.

| System       | Support | Notes                                                                                                  |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------ |
| TQL          | ✅       | [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) consumes the input by default. |
| KQL          | ✅       | Use `summarize`.                                                                                       |
| SPL          | ✅       | Use `stats`.                                                                                           |
| Cribl Stream | ⚠️      | Aggregations are time-windowed.                                                                        |

### Grouped aggregation

Grouped aggregation computes separate aggregate results for each key, such as one count per user or host. The grouping key partitions aggregate state, but it does not add time boundaries unless you combine it with a windowing mechanism.

| System       | Support | Notes                                                                                             |
| ------------ | ------- | ------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) with grouping fields. |
| KQL          | ✅       | Use `summarize ... by key`.                                                                       |
| SPL          | ✅       | Use `stats ... BY key`.                                                                           |
| Cribl Stream | ⚠️      | Use time-windowed `Group by fields`.                                                              |

### Periodic processing-time aggregation

Periodic processing-time aggregation emits results on a wall-clock or processing-time cadence. Use it for live dashboards and operational metrics when arrival time matters more than event timestamps.

| System       | Support | Notes                                                                                                                                                                                                                                                                 |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) without `on`, [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) `options={emit: 30s, mode: "reset"}`, or [`every`](https://tenzir.com/docs/reference/operators/every.md). |
| KQL          | ⚠️      | Use scheduled or continuous query patterns.                                                                                                                                                                                                                           |
| SPL          | ⚠️      | Use real-time or scheduled searches.                                                                                                                                                                                                                                  |
| Cribl Stream | ⚠️      | Use Scheduled Collectors; Aggregations use event-time buckets.                                                                                                                                                                                                        |

### Periodic running stats

Periodic running stats emit accumulated values repeatedly instead of waiting for the stream to end. They show the total so far, not a bounded rolling lookback.

| System       | Support | Notes                                                                                                                  |
| ------------ | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) `options={emit: 30s, mode: "cumulative"}`. |
| KQL          | ⚠️      | Use scheduled or continuous query patterns.                                                                            |
| SPL          | ⚠️      | Use `streamstats` or scheduled searches.                                                                               |
| Cribl Stream | ⚠️      | Enable `Cumulative aggregations` in Aggregations.                                                                      |

### Wall-clock subpipeline batches

Wall-clock subpipeline batches rerun a block of work on a fixed schedule. This is useful when the work fetches or refreshes data, rather than grouping existing events by event time.

| System       | Support | Notes                                                                                            |
| ------------ | ------- | ------------------------------------------------------------------------------------------------ |
| TQL          | ✅       | Use [`every`](https://tenzir.com/docs/reference/operators/every.md) to rerun an arbitrary block. |
| KQL          | ❌       | No direct query-language block equivalent.                                                       |
| SPL          | ❌       | No direct query-language block equivalent.                                                       |
| Cribl Stream | ⚠️      | Scheduled Collectors schedule collection work.                                                   |

### Tumbling event-time windows

Tumbling event-time windows split events into adjacent, non-overlapping time ranges based on event timestamps. Each event belongs to one window, and each window produces its own result.

| System       | Support | Notes                                                                                   |
| ------------ | ------- | --------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `size=1h, on=ts`. |
| KQL          | ✅       | Use `summarize ... by bin(ts, 1h)`.                                                     |
| SPL          | ✅       | Use `timechart span=1h` or `bin _time`.                                                 |
| Cribl Stream | ✅       | Use Aggregations `Time window`.                                                         |

### Hopping event-time windows

Hopping event-time windows use a window size that is larger than the step between window starts. This gives rolling context with repeated overlapping windows, so one event can contribute to several results.

| System       | Support | Notes                                                                                             |
| ------------ | ------- | ------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `size=1h, every=5m, on=ts`. |
| KQL          | ⚠️      | Use manual expansion or plugins for specific metrics.                                             |
| SPL          | ⚠️      | Use manual expansion or bucketing.                                                                |
| Cribl Stream | ❌       | No hopping window option.                                                                         |

### Fixed count windows

Fixed count windows close after a bounded number of arriving events rather than at a time boundary. They are useful for batching and sample-based analytics where table-slice boundaries must not affect the result.

| System       | Support | Notes                                                                                                     |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `size=100` or `size=100, every=10`. |
| KQL          | ⚠️      | Use row numbering and manual bucketing.                                                                   |
| SPL          | ⚠️      | Use `streamstats window=...` for per-event results.                                                       |
| Cribl Stream | ⚠️      | Batch controls exist without a general count-window block.                                                |

### Per-input-event running and rolling stats

Per-input-event statistics update a calculation for each arriving event. This is different from periodic emission because the output cadence follows events, not a timer. Running statistics retain unbounded aggregate state, while rolling statistics expire events outside a trailing count or time horizon.

| System       | Support | Notes                                                                                                                                                                                                                                                           |
| ------------ | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use cumulative event emission from [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) for unbounded state or `trailing=true` with a duration or count [`window`](https://tenzir.com/docs/reference/operators/window.md) for bounded state. |
| KQL          | ⚠️      | Use manual expansion or row-window functions.                                                                                                                                                                                                                   |
| SPL          | ✅       | Use `streamstats`; `window` and `time_window` add bounded history.                                                                                                                                                                                              |
| Cribl Stream | ❌       | Aggregations emit window events.                                                                                                                                                                                                                                |

For unbounded running aggregates, TQL’s cumulative event emission from [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) avoids replaying a trailing history. This is the direct counterpart to `streamstats` without either bound.

### Per-key event-time windows

Per-key event-time windows keep separate windowed results for each entity. Events from one noisy key cannot advance or close windows for another key.

| System       | Support | Notes                                                                                                                                           |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | Compose [`group`](https://tenzir.com/docs/reference/operators/group.md) with [`window`](https://tenzir.com/docs/reference/operators/window.md). |
| KQL          | ✅       | Use `summarize ... by key, bin(ts, ...)`.                                                                                                       |
| SPL          | ✅       | Use `BY key` or split-by.                                                                                                                       |
| Cribl Stream | ✅       | Use `Group by fields` with `Time window`.                                                                                                       |

### Streaming late-event tolerance

Streaming late-event tolerance lets a pipeline accept delayed data without holding every window until the input ends. Fixed windows stay open for the tolerance, while trailing windows buffer and reorder events within it before evaluation.

| System       | Support | Notes                                                                                  |
| ------------ | ------- | -------------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `tolerance=...`. |
| KQL          | ❌       | Mostly batch or query-time semantics.                                                  |
| SPL          | ⚠️      | Depends on search order.                                                               |
| Cribl Stream | ✅       | Use Aggregations `Lag tolerance`.                                                      |

### Independent per-key event-time clocks

Independent per-key clocks let each group advance event time based only on its own events. This prevents a busy key from making sparse keys late, but sparse windows may also close later.

| System       | Support | Notes                                                                                                                                                  |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TQL          | ✅       | Put [`window`](https://tenzir.com/docs/reference/operators/window.md) inside an outer [`group`](https://tenzir.com/docs/reference/operators/group.md). |
| KQL          | ❌       | No streaming clock per key in ad hoc KQL.                                                                                                              |
| SPL          | ⚠️      | Requires search-order dependent workarounds.                                                                                                           |
| Cribl Stream | ⚠️      | Grouped buckets exist, but no documented per-key clock.                                                                                                |

### Arbitrary subpipeline per key

An arbitrary per-key subpipeline can do more than compute a fixed aggregate list. It can reshape, filter, enrich, or sink each group’s stream independently.

| System       | Support | Notes                                                                              |
| ------------ | ------- | ---------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`group`](https://tenzir.com/docs/reference/operators/group.md) `key { ... }`. |
| KQL          | ❌       | No direct equivalent.                                                              |
| SPL          | ❌       | No direct equivalent.                                                              |
| Cribl Stream | ❌       | No grouped Function block.                                                         |

### Arbitrary subpipeline per window

An arbitrary per-window subpipeline runs custom logic inside each time range, count range, or per-event trailing history. It covers detections that need more than a fixed aggregate list, such as post-aggregation filtering or alert formatting.

| System       | Support | Notes                                                                            |
| ------------ | ------- | -------------------------------------------------------------------------------- |
| TQL          | ✅       | Use [`window`](https://tenzir.com/docs/reference/operators/window.md) `{ ... }`. |
| KQL          | ❌       | No direct equivalent.                                                            |
| SPL          | ❌       | No direct equivalent.                                                            |
| Cribl Stream | ❌       | Aggregations only emit configured outputs.                                       |

### Sink per key or per window

A sink per key or window sends results from inside the grouped or windowed scope. This supports local alerting or routing decisions without merging all results back into a shared stream first.

| System       | Support | Notes                                                                                                                                                          |
| ------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ✅       | [`group`](https://tenzir.com/docs/reference/operators/group.md) and [`window`](https://tenzir.com/docs/reference/operators/window.md) blocks can end in sinks. |
| KQL          | ❌       | No direct query-language equivalent.                                                                                                                           |
| SPL          | ❌       | No direct query-language equivalent.                                                                                                                           |
| Cribl Stream | ⚠️      | Route emitted aggregate events downstream.                                                                                                                     |

### Empty window padding

Empty window padding emits rows for time ranges that have no events. This is useful for charts and time-series joins that need an explicit zero or null for missing intervals.

| System       | Support | Notes                                   |
| ------------ | ------- | --------------------------------------- |
| TQL          | ❌       | Empty windows are not emitted.          |
| KQL          | ⚠️      | Use manual `range` and `union` padding. |
| SPL          | ✅       | Use `timechart cont=true`.              |
| Cribl Stream | ❌       | No documented empty buckets.            |

### Session windows

Session windows group events by gaps in activity rather than fixed boundaries. They are useful for user sessions, transactions, and bursts where the end time depends on silence.

| System       | Support | Notes                                                      |
| ------------ | ------- | ---------------------------------------------------------- |
| TQL          | ❌       | Requires precomputed session IDs or custom stateful logic. |
| KQL          | ✅       | Use `row_window_session()`.                                |
| SPL          | ✅       | Use `transaction maxpause` and `maxspan`.                  |
| Cribl Stream | ❌       | Not native.                                                |

### Custom alignment or calendar windows

Custom alignment or calendar windows anchor boundaries to a chosen origin or calendar unit. This matters for reports that must align to local business days, weeks, months, or other non-epoch boundaries.

| System       | Support | Notes                                                                                                                                       |
| ------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| TQL          | ⚠️      | Fixed [`window`](https://tenzir.com/docs/reference/operators/window.md) buckets are epoch-anchored; no custom origin or calendar alignment. |
| KQL          | ✅       | Use `bin_at()`.                                                                                                                             |
| SPL          | ✅       | Use `aligntime` and calendar spans.                                                                                                         |
| Cribl Stream | ⚠️      | Fixed `Time window` buckets; no documented custom origin or calendar alignment.                                                             |

Legend: ✅ native or covered, ⚠️ partial or workaround, ❌ missing.

Cribl Stream’s Aggregations Function runs independently per Worker Process, so aggregate state is not shared globally across workers. [Scheduled Collector jobs](https://docs.cribl.io/stream/collectors/) can run on a recurrence, but they schedule collection work rather than provide a general pipeline Function block.

## See also

* [`window`](https://tenzir.com/docs/reference/operators/window.md)
* [`group`](https://tenzir.com/docs/reference/operators/group.md)
* [Aggregate event streams](aggregate-event-streams.md)
* [Shape aggregation results](shape-aggregation-results.md)
* [Detect over time windows](../detection/detect-over-time-windows.md)
