---
title: "DuckDB"
canonical: https://tenzir.com/docs/v7.0.0/reference/optimizations/duckdb
source: https://tenzir.com/docs/v7.0.0/reference/optimizations/duckdb.md
section: "Docs"
---

# DuckDB

> When fromduckdb reads a table, it hands DuckDB the operators that follow it, so that DuckDB returns only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in DuckDB, with DuckDB’s semantics. This page describes which operators DuckDB takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The optimizations overview explains how Tenzir optimizes pipelines in general.

When [`from_duckdb`](https://tenzir.com/docs/v7.0.0/reference/operators/from_duckdb.md) reads a table, it hands DuckDB the operators that follow it, so that DuckDB returns only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in DuckDB, with DuckDB’s semantics. This page describes which operators DuckDB takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_duckdb "events.duckdb", table="alerts"`. The operator writes the query itself and adds the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and the rest of the pipeline runs in Tenzir. To have DuckDB filter, write the filter into your query.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) operators that directly follow the operator. All other operators stay in Tenzir, since a [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) counts events across polls and a live read never ends.

With `pushdown=false`, every operator stays in Tenzir and runs with TQL semantics. The operator still reads only the columns that the pipeline uses.

## Operators that DuckDB takes over

The operator takes over the longest run of operators directly after it that DuckDB can spell:

* [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), as the [filters](duckdb.md#filters) section describes.
* [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of fields, including renames and fields of `STRUCT` columns, such as `select ip=src_ip, host=meta.host`.
* [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md) of top-level fields.
* [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) with group keys on fields and `count()`, `count(x)`, `min(x)`, and `max(x)` of fields. The summary may follow [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) by fields.
* [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), and [`top`](https://tenzir.com/docs/v7.0.0/reference/operators/top.md) or [`rare`](https://tenzir.com/docs/v7.0.0/reference/operators/rare.md) followed by [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md).

The first operator that DuckDB cannot spell ends the run. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) at `and`, so DuckDB can still take over the conjuncts that it spells. For example, DuckDB runs every step of

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events
head 20
```

and returns at most 20 groups. The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) across them.

## Filters

DuckDB takes over a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) whose predicate consists of:

* Fields, including fields of `STRUCT` columns, which DuckDB reads with `struct_extract`.
* Literals: numbers, strings, booleans, `null`, times, durations of whole microseconds, and IP addresses.
* Comparisons, `in` with a list of literals, arithmetic with `+`, `-`, `*`, and `/`, and the boolean operators `and`, `or`, and `not`.
* The functions `starts_with`, `ends_with`, `length_bytes`, `length_chars`, `to_lower`, `to_upper`, `trim`, `abs`, and `match_regex`, without named arguments such as `ignore_case`.

Other functions, subnets, other kinds of literals, strings with NUL bytes, arithmetic with a time literal such as `ts - 2024-01-01`, and optional fields such as `x?` stay in Tenzir.

## DuckDB semantics

The operators that DuckDB takes over run as DuckDB runs them, which can differ from TQL:

* Comparisons with `null` yield `null`, so `name != "alpha"` does not keep rows where `name` is `null`.
* Text compares and sorts under the collation of its column, such as `COLLATE NOCASE`.
* DuckDB sorts `null` last, and returns groups that tie in a sort in any order.
* DuckDB computes arithmetic in the types of its operands, and considers `NaN` equal to itself and greater than every other number.
* A time becomes a string in UTC, such as `'2024-01-01 00:00:00.000000000+00'`, which DuckDB casts to the type of the column. A comparison therefore never depends on the session time zone, but a `DATE` or `TIMESTAMP_S` column compares with the time truncated to its precision.
* An IP address becomes its text, such as `'10.0.0.1'`, which compares as text against a `VARCHAR` column.
* `match_regex` uses DuckDB’s `regexp_matches`.
* A [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of a column that the table lacks fails the query, where Tenzir would warn and fill in `null`.

When DuckDB computes a summary or a [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), Tenzir does not see the individual rows, so it does not warn about values that it reads as `null`, such as a field of a `NULL` struct.

## Verify an optimization

To see the operators that DuckDB takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_duckdb "events.duckdb", table="alerts" | where severity >= 3 | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`.
