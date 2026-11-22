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
| filter (event.type == "DNS Resolved")
| columns __tenzir_column_0 = event.type, __tenzir_column_1 = timestamp
| sort -__tenzir_column_1
| limit 2
```

For a [`summarize`](../operators/summarize.md) with a computed group key, PowerQuery evaluates the expression in a `let` stage before `group`. For example, the pipeline

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token"),
  start=2024-01-01, end=2024-01-02
kind = event.type.to_lower()
summarize kind, events=count()
sort -events
head 10
```

sends this PowerQuery:

```text
| let __tenzir_column_0 = lower(event.type)
| group __tenzir_column_1 = count() by __tenzir_column_0
| sort -__tenzir_column_1
| limit 10
```

Tenzir arranges the result columns into the fields of the pipeline, such as `event.kind` and `t`. A column that holds SentinelOne’s `timestamp`, also under another name or as a group key, becomes a time. Counts become integers, also with `raw=true`.

## Summaries

The table shows which aggregation functions run in SentinelOne and which run in Tenzir:

| TQL                   | PowerQuery                                            | Notes                                                                                                                                                      |
| --------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `count()`             | `count()`                                             |                                                                                                                                                            |
| `count(x)`            | `count(x)`                                            | Counts the events where `x` has a value                                                                                                                    |
| `min(x)`              | `min(x)`                                              | Yields `Infinity` without values                                                                                                                           |
| `max(x)`              | `max(x)`                                              | Yields `-Infinity` without values                                                                                                                          |
| `count_if(x, v => p)` | `count(((x != null) and p))`                          | Skips `null` values                                                                                                                                        |
| `count_distinct(x)`   | `group … by …, x \| group count(x) by …`              | Exact via two `group` stages, excluding `null`; falls back to approximate `estimate_distinct(x)` alongside `stddev`, `variance`, or another distinct field |
| `sum(x)`              | `sum(x)`                                              | Yields `0.0` without values                                                                                                                                |
| `mean(x)`             | `avg(x)`                                              | Yields `0.0` without values                                                                                                                                |
| `stddev(x)`           | `stddev(x) * sqrt((count(x) - 1) / count(x))`         | Rescales PowerQuery's sample `stddev` to population form                                                                                                   |
| `variance(x)`         | `stddev(x) * stddev(x) * ((count(x) - 1) / count(x))` | Rescales PowerQuery's sample `stddev` to population variance                                                                                               |
| `all(x)`              | `count(x == false) == 0`                              | Skips `null` values; yields `true` without values                                                                                                          |
| `any(x)`              | `count(x == true) > 0`                                | Skips `null` values; yields `false` without values                                                                                                         |

PowerQuery computes group keys and aggregate arguments in a `let` stage before `group`. They can use arithmetic and the functions listed in [Filters and functions](sentinelone.md#filters-and-functions). A group key using `+` runs in Tenzir if Tenzir cannot tell whether it returns a number or a string. The `group` stage puts events without a group key into the group `null`.

For example, the following summary groups events into time buckets:

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-token"),
  start=2026-11-16T00:00:00Z,
  end=2026-11-17T00:00:00Z
bucket = floor(timestamp, 7h)
summarize bucket, events=count()
```

PowerQuery computes the key as `timebucket(timestamp, "25200s")`. It supports these widths:

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
| `x == null`, `x != null`  | `!(x != null)`, `(x != null)`        |
| `timestamp >= 2024-01-01` | `(timestamp >= 1704067200000000000)` |

PowerQuery can also compute arithmetic. The table shows which functions PowerQuery can call and which run in Tenzir. LOG queries do not compute values: they support only `starts_with` and `ends_with` from this table, and use `!(x = *)` and `(x = *)` for `x == null` and `x != null`, respectively.

| TQL                       | PowerQuery                         | Notes                                                                                                          |
| ------------------------- | ---------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `x.starts_with(y)`        | `x starts_with:matchcase y`        | As a predicate with a non-empty string; in LOG queries, `x` must be a field                                    |
| `x.ends_with(y)`          | `x ends_with:matchcase y`          | As a predicate with a non-empty string; in LOG queries, `x` must be a field                                    |
| `x.length_chars()`        | `len(x)`                           |                                                                                                                |
| `x.to_lower()`            | `lower(x)`                         |                                                                                                                |
| `x.to_upper()`            | `upper(x)`                         |                                                                                                                |
| `x.trim()`                | `trim(x)`                          |                                                                                                                |
| `x.trim_start()`          | `ltrim(x)`                         |                                                                                                                |
| `x.trim_end()`            | `rtrim(x)`                         |                                                                                                                |
| `x.replace(y, z)`         | Runs in Tenzir                     | PowerQuery treats the pattern as a case-insensitive regex                                                      |
| `x.is_empty()`            | `isempty(x)`                       | As a predicate only; yields `true` for `null`                                                                  |
| `x.slice(begin=b, end=e)` | `substr(x, b, e - b)`              | With constant `begin` and `end` that are not negative; uses `substr(x, b)` or `substr(x, 0, e)` with one bound |
| `x.abs()`                 | `abs(x)`                           |                                                                                                                |
| `x.ceil()`                | `ceiling(x)`                       |                                                                                                                |
| `x.floor()`               | `floor(x)`                         |                                                                                                                |
| `x.sqrt()`                | `sqrt(x)`                          |                                                                                                                |
| `x.exp()`                 | `exp(x)`                           |                                                                                                                |
| `x.log()`, `x.log(base)`  | `ln(x)`, `log(x, base)`            |                                                                                                                |
| `x.year()`                | `number(strftime(x, "%Y", "UTC"))` |                                                                                                                |
| `x.month()`               | `number(strftime(x, "%m", "UTC"))` |                                                                                                                |
| `x.day()`                 | `number(strftime(x, "%d", "UTC"))` |                                                                                                                |
| `x.hour()`                | `number(strftime(x, "%H", "UTC"))` |                                                                                                                |
| `x.minute()`              | `number(strftime(x, "%M", "UTC"))` |                                                                                                                |

SentinelOne has no hash functions, so `x.hash_md5()`, `x.hash_sha1()` and `x.hash_sha256()` run in Tenzir.

SentinelOne has no durations, so `x.since_epoch()` runs in Tenzir.

Regular expressions, IP addresses and subnets, durations, unsupported functions or named arguments, bare fields such as `where flag`, the literal `null` outside a comparison, strings with control characters, and optional fields such as `x?` run in Tenzir. A time compares only with SentinelOne’s own `timestamp`, not with a field that holds a time as text, nor with `timestamp` after a [`select`](../operators/select.md) that renames it or after a `query` with `|`.

## SentinelOne semantics

The operators that SentinelOne takes over run as SentinelOne runs them, which can differ from TQL:

* The filters `x != "a"` and `not (x in […])` also match events without `x`.
* Functions and arithmetic can coerce `null` to `0` or `""`. A nonzero number divided by zero yields an infinity. The `+` operator also concatenates strings.
* Computed numeric keys and numeric aggregates return doubles. For example, `year` can return `2026.0`. The `min(timestamp)` and `max(timestamp)` aggregates return times. Time comparisons use nanoseconds as doubles.
* An ungrouped summary over no events returns no rows.
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
