---
title: "SentinelOne"
canonical: https://tenzir.com/docs/v7.0.0/reference/optimizations/sentinelone
source: https://tenzir.com/docs/v7.0.0/reference/optimizations/sentinelone.md
section: "Docs"
---

# SentinelOne

> The SentinelOne source fromsentinelonedatalake hands SentinelOne the operators that follow it by spelling them in PowerQuery, the pipe language of the Singularity Data Lake, so that SentinelOne returns only what the pipeline keeps. Those operators leave the pipeline and run in SentinelOne, with SentinelOne’s semantics. This page describes which operators SentinelOne takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our optimizations overview explains how Tenzir optimizes pipelines in general.

The SentinelOne source [`from_sentinelone_data_lake`](https://tenzir.com/docs/v7.0.0/reference/operators/from_sentinelone_data_lake.md) hands SentinelOne the operators that follow it by spelling them in PowerQuery, the pipe language of the Singularity Data Lake, so that SentinelOne returns only what the pipeline keeps. Those operators leave the pipeline and run in SentinelOne, with SentinelOne’s semantics. This page describes which operators SentinelOne takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator reads in one of two ways:

* **Without `query`**, Tenzir writes the whole request from the operators that follow.
* **With `query`**, the operator runs your PowerQuery and appends the operators that follow as further stages. The appended stages apply to the result of your query, so they also work after commands such as `group`.

The operator takes over no operator if your query does not end where stages may follow, such as a query that ends in `|`, has an unterminated string or comment, or ends in a `//` comment. It also takes over nothing with `pushdown=false`, which keeps every operator in Tenzir with TQL semantics.

## Operators that SentinelOne takes over

The operator takes over the longest run of operators directly after it that PowerQuery can spell:

* [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), as the [filters](sentinelone.md#filters) section describes.
* [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of fields, including renames and nested fields, which becomes `columns`.
* [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) with group keys on fields and `count()` and `count(x)` of fields, which becomes `group … by`. This includes [`top`](https://tenzir.com/docs/v7.0.0/reference/operators/top.md) and [`rare`](https://tenzir.com/docs/v7.0.0/reference/operators/rare.md). The summary may follow [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) by fields after a [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) or [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md), which becomes `sort`. PowerQuery returns only `timestamp` and `message` of whole events, so a [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) of whole events stays in Tenzir.
* [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), which becomes `limit`, with at most 1,600,000 rows.

The first operator that PowerQuery cannot spell ends the run, and so does [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), which PowerQuery has no form for. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) at `and`, so SentinelOne can still take over the conjuncts that it spells. For example, the pipeline

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

## Retrieval

The operators that SentinelOne takes over decide how the operator reads:

* **Whole events.** Without `query`, when SentinelOne takes over only [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) and a final [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), the operator reads with a LOG query, which returns complete events, including the fields that the pipeline never names, and pages through them without a cap. The operator applies the [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) itself and sends no request for `head 0`.
* **PowerQuery.** Every other read is a PowerQuery. Unless it ends in a [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), Tenzir appends `| limit 1600000`, the largest limit that SentinelOne accepts, since PowerQuery otherwise returns at most 1,000 rows. A result with 1,600,000 rows may therefore be incomplete, and the operator warns about it.
* **Your query.** With `query` and no operator that SentinelOne takes over, the operator sends your query unchanged, so SentinelOne’s default cap of 1,000 rows applies unless your query has a `limit`.

Without `query`, `start`, and `end`, SentinelOne must take over a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), or [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md). Otherwise the operator reports an error before contacting SentinelOne. The generated query adds at most 10,000 bytes to the request.

## Filters

Filters become `filter` stages of PowerQuery or the filter of a LOG query. They consist of fields, literals (strings, numbers up to 2^53, booleans, and times compared with `timestamp`), comparisons, `in` with a list, `and`, `or`, `not`, `== null` and `!= null`, and the functions `starts_with` and `ends_with`, without named arguments such as `ignore_case`:

| TQL                       | PowerQuery                           |
| ------------------------- | ------------------------------------ |
| `x == "a"`                | `(x == "a")`                         |
| `x != 1`                  | `(x != 1)`                           |
| `x in ["a", 1]`           | `(x in ("a", 1))`                    |
| `not (x in ["a"])`        | `!((x in ("a")))`                    |
| `x == null`, `x != null`  | `!(x = *)`, `(x = *)`                |
| `x.starts_with("a")`      | `(x starts_with:matchcase "a")`      |
| `timestamp >= 2024-01-01` | `(timestamp >= 1704067200000000000)` |

Regular expressions, IP addresses and subnets, durations, arithmetic, other functions, bare fields such as `where flag`, the literal `null` outside a comparison, strings with control characters, and optional fields such as `x?` stay in Tenzir. A time compares only with SentinelOne’s own `timestamp`, not with a field that holds a time as text, nor with `timestamp` after a [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) that renames it or after a `query` with `|`.

## SentinelOne semantics

The operators that SentinelOne takes over run as SentinelOne runs them, which can differ from TQL:

* `x != "a"` and `not (x in […])` also match events without `x`.
* Numbers are doubles. A time compares as nanoseconds since the epoch, exact to a few hundred nanoseconds.
* SentinelOne keeps nested fields as flat fields with dotted names, such as `event.type`. A [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of a record, such as `select event`, returns `null`. Select its fields instead.
* `count(x)` counts the events where `x` has a value. `group` puts events without a group key into the group `null`.
* `sort` puts `null` first in ascending and last in descending order.
* A query that SentinelOne rejects fails the pipeline with a hint to use `pushdown=false`.

Summaries with `min`, `max`, `sum`, `mean`, or other functions stay in Tenzir, since PowerQuery computes them only for numbers and returns a timestamp’s minimum as a floating-point number.

## Time window

Without `query`, comparisons of `timestamp` with times in the filters before any summary, limit, or sort also narrow the time window of the request, rounded outward to whole milliseconds plus one more on each side, since SentinelOne compares times as floating-point numbers. An `or` of time ranges selects their enclosing range. When you omit `start` or `end`, these comparisons supply them, so a historical search needs no explicit bounds; otherwise, they narrow the bounds that you set and never widen them. The comparisons stay in the query in every case. A narrowed window that cannot contain an event completes the read without a request, unless a summary still yields a row for it. With `query`, the window stays as you set it.

## Warnings

SentinelOne’s warnings, such as the default cap of 1,000 rows, become warnings of the pipeline, as do results that SentinelOne reports as partial, with omitted events, or with discarded array items. The results still arrive.

## Verify an optimization

To see the operators that SentinelOne takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_sentinelone_data_lake "https://<tenant>.sentinelone.net", token=secret("s1"), start=2024-01-01, end=2024-01-02 | where event.type == "DNS Resolved" | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`. When SentinelOne rejects a query, the diagnostic shows its response.
