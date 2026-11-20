---
title: "SentinelOne"
canonical: https://tenzir.com/docs/reference/optimizations/sentinelone
source: https://tenzir.com/docs/reference/optimizations/sentinelone.md
section: "Docs"
---

# SentinelOne

> The SentinelOne source fromsentinelonedatalake hands SentinelOne the operators that follow it by spelling them in PowerQuery, the pipe language of the Singularity Data Lake, so that SentinelOne returns only what the pipeline keeps. SentinelOne takes over those operators, which leave the pipeline and run in SentinelOne with SentinelOne’s semantics, and the rest of the pipeline runs in Tenzir. This page describes which operators SentinelOne takes over, which functions it computes, and how its results can differ from Tenzir’s. Our optimizations overview compares the targets and describes the rules that all sources share.

The SentinelOne source [`from_sentinelone_data_lake`](../operators/from_sentinelone_data_lake.md) hands SentinelOne the operators that follow it by spelling them in PowerQuery, the pipe language of the Singularity Data Lake, so that SentinelOne returns only what the pipeline keeps. SentinelOne takes over those operators, which leave the pipeline and run in SentinelOne with SentinelOne’s semantics, and the rest of the pipeline runs in Tenzir. This page describes which operators SentinelOne takes over, which functions it computes, and how its results can differ from Tenzir’s. Our [optimizations overview](../optimizations.md) compares the targets and describes the rules that all sources share.

## When it applies

The operator reads in one of two ways:

* **Without `query`**, Tenzir writes the whole request from the operators that follow.
* **With `query`**, the operator runs your PowerQuery and appends the operators that follow as further stages. The appended stages apply to the result of your query, so they also work after commands such as `group`.

The operator takes over no operator if your query does not end where stages may follow, such as a query that ends in `|`, has an unterminated string or comment, or ends in a `//` comment. It also takes over nothing with `pushdown=false`, which runs every operator in Tenzir with TQL semantics.

## Operators that SentinelOne takes over

SentinelOne takes over the [longest run of operators](../optimizations.md#the-run-of-operators-after-the-source) directly after the source that PowerQuery can spell:

* [`where`](../operators/where.md), as the [filters and functions](sentinelone.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of fields, including renames and nested fields, which becomes `columns`.
* [`summarize`](../operators/summarize.md) with the group keys and functions that the [summaries](sentinelone.md#summaries) section lists, which becomes `group … by`. This includes [`top`](../operators/top.md) and [`rare`](../operators/rare.md). The summary may follow [`select`](../operators/select.md) and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](../operators/sort.md) by fields after a [`select`](../operators/select.md) or [`summarize`](../operators/summarize.md), which becomes `sort`. PowerQuery returns only `timestamp` and `message` of whole events, so a [`sort`](../operators/sort.md) of whole events runs in Tenzir.
* [`head`](../operators/head.md), which becomes `limit`, with at most 1,600,000 rows.

A [`drop`](../operators/drop.md), which PowerQuery has no form for, also ends the run. For example, the pipeline

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token"),
  start=2024-01-01, end=2024-01-02
select event.kind=event.type, t=timestamp
where event.kind == "DNS Resolved"
sort -t
head 2
```

sends this PowerQuery:

```text
| filter (event.type == "DNS Resolved") | columns __tenzir_column_0 = event.type, __tenzir_column_1 = timestamp | sort -__tenzir_column_1 | limit 2
```

Tenzir arranges the result columns into the fields of the pipeline, such as `event.kind` and `t`. A column that holds SentinelOne’s `timestamp`, also under another name or as a group key, becomes a time. Counts become integers, also with `raw=true`.

## Summaries

SentinelOne computes these aggregation functions of a [`summarize`](../operators/summarize.md), of fields:

| TQL                 | PowerQuery             | Notes                                                     |
| ------------------- | ---------------------- | --------------------------------------------------------- |
| `count()`           | `count()`              |                                                           |
| `count(x)`          | `count(x)`             | Counts the events where `x` has a value                   |
| `count_distinct(x)` | `estimate_distinct(x)` | Approximate, since PowerQuery has no exact distinct count |

A summary with `min`, `max`, `count_if`, `sum`, `mean`, or other functions runs in Tenzir, since PowerQuery computes `min`, `max`, `sum`, and `mean` only for numbers and returns a timestamp’s minimum as a floating-point number. The `group` stage puts events without a group key into the group `null`.

Group keys are fields or time buckets. A summary of other computed keys or arguments, such as values that a [`set`](../operators/set.md) assigns, runs in Tenzir. A time bucket, such as in

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-token"),
  start=2026-11-16T00:00:00Z,
  end=2026-11-17T00:00:00Z
bucket = floor(timestamp, 7h)
summarize bucket, events=count()
```

runs in SentinelOne as `timebucket(timestamp, "25200s")` for these widths:

| Width                                  | SentinelOne                                                         |
| -------------------------------------- | ------------------------------------------------------------------- |
| Whole seconds, such as `1h`            | Runs as `timebucket(x, "<w>s")` of a field, which arrives as a time |
| Fractions of a second, such as `250ms` | Runs in Tenzir                                                      |
| Multiples of a week or a month         | Runs in Tenzir, since TQL aligns them to the calendar               |

The buckets count from the epoch in UTC, as in TQL.

## Filters and functions

Filters become `filter` stages of PowerQuery or the filter of a LOG query. They consist of fields, literals (strings, numbers up to 2^53, booleans, and times compared with `timestamp`), comparisons, `in` with a list, `and`, `or`, `not`, and `== null` and `!= null`:

| TQL                       | PowerQuery                           |
| ------------------------- | ------------------------------------ |
| `x == "a"`                | `(x == "a")`                         |
| `x != 1`                  | `(x != 1)`                           |
| `x in ["a", 1]`           | `(x in ("a", 1))`                    |
| `not (x in ["a"])`        | `!((x in ("a")))`                    |
| `x == null`, `x != null`  | `!(x = *)`, `(x = *)`                |
| `timestamp >= 2024-01-01` | `(timestamp >= 1704067200000000000)` |

Filters can also call these functions:

| TQL                | PowerQuery                  | Notes                                                       |
| ------------------ | --------------------------- | ----------------------------------------------------------- |
| `x.starts_with(y)` | `x starts_with:matchcase y` | In filters only, on a field with a string that is not empty |
| `x.ends_with(y)`   | `x ends_with:matchcase y`   | In filters only, on a field with a string that is not empty |

SentinelOne has no durations, so `x.since_epoch()` runs in Tenzir.

Regular expressions, IP addresses and subnets, durations, arithmetic, other functions, named arguments such as `ignore_case`, bare fields such as `where flag`, the literal `null` outside a comparison, strings with control characters, and optional fields such as `x?` run in Tenzir. A time compares only with SentinelOne’s own `timestamp`, not with a field that holds a time as text, nor with `timestamp` after a [`select`](../operators/select.md) that renames it or after a `query` with `|`.

## SentinelOne semantics

The operators that SentinelOne takes over run as SentinelOne runs them, which can differ from TQL:

* The filters `x != "a"` and `not (x in […])` also match events without `x`.
* Numbers are doubles. A time compares as nanoseconds since the epoch, exact to a few hundred nanoseconds.
* SentinelOne keeps nested fields as flat fields with dotted names, such as `event.type`. A [`select`](../operators/select.md) of a record, such as `select event`, returns `null`. Select its fields instead.
* PowerQuery’s `sort` puts `null` first in ascending and last in descending order.
* A query that SentinelOne rejects fails the pipeline with the error of SentinelOne, as the overview’s [diagnostics](../optimizations.md#diagnostics) describe. The diagnostic shows SentinelOne’s response.

### Retrieval and row limits

The operators that SentinelOne takes over decide how the operator reads:

* **Whole events.** Without `query`, when SentinelOne takes over only [`where`](../operators/where.md) and a final [`head`](../operators/head.md), the operator reads with a LOG query, which returns complete events, including the fields that the pipeline never names, and pages through them without a cap. The operator applies the [`head`](../operators/head.md) itself and sends no request for `head 0`.
* **PowerQuery.** Every other read is a PowerQuery. Unless it ends in a [`head`](../operators/head.md), Tenzir appends `| limit 1600000`, the largest limit that SentinelOne accepts, since PowerQuery otherwise returns at most 1,000 rows. A result with 1,600,000 rows may therefore be incomplete, and the operator warns about it.
* **Your query.** With `query` and no operator that SentinelOne takes over, the operator sends your query unchanged, so SentinelOne’s default cap of 1,000 rows applies unless your query has a `limit`.

Without `query`, `start`, and `end`, SentinelOne must take over a [`where`](../operators/where.md), [`head`](../operators/head.md), or [`summarize`](../operators/summarize.md). Otherwise the operator reports an error before contacting SentinelOne. The generated query adds at most 10,000 bytes to the request.

### Time window

Without `query`, comparisons of `timestamp` with times in the filters before any summary, limit, or sort also narrow the time window of the request, rounded outward to whole milliseconds plus one more on each side, since SentinelOne compares times as floating-point numbers. An `or` of time ranges selects their enclosing range. When you omit `start` or `end`, these comparisons supply them, so a historical search needs no explicit bounds; otherwise, they narrow the bounds that you set and never widen them. The comparisons stay in the query in every case. A narrowed window that cannot contain an event, such as for a strict comparison beyond the range of a time, completes the read without a request, unless a summary still yields a row for it. With `query`, the window stays as you set it.

### Warnings

SentinelOne’s warnings, such as the default cap of 1,000 rows, become warnings of the pipeline, as do results that SentinelOne reports as partial, with omitted events, or with discarded array items. The results still arrive.

## Verify an optimization

To see which operators SentinelOne takes over in a pipeline, print the optimized pipeline, as the overview’s section on [verifying an optimization](../optimizations.md#verify-an-optimization) shows.
