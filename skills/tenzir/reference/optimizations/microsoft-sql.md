---
title: "Microsoft SQL Server"
canonical: https://tenzir.com/docs/v7.0.0/reference/optimizations/microsoft-sql
source: https://tenzir.com/docs/v7.0.0/reference/optimizations/microsoft-sql.md
section: "Docs"
---

# Microsoft SQL Server

> When frommicrosoftsql reads a table, it hands SQL Server the operators that follow it, so that SQL Server sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in SQL Server, with its semantics. This page describes which operators SQL Server takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The optimizations overview explains how Tenzir optimizes pipelines in general.

When [`from_microsoft_sql`](https://tenzir.com/docs/v7.0.0/reference/operators/from_microsoft_sql.md) reads a table, it hands SQL Server the operators that follow it, so that SQL Server sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in SQL Server, with its semantics. This page describes which operators SQL Server takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_microsoft_sql table="dbo.alerts"`. The operator writes the query itself and adds the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` or `query` exactly as written, and the rest of the pipeline runs in Tenzir. So does **show mode** with `show`. To have SQL Server filter, write the filter into your query.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) operators that directly follow the operator. All other operators stay in Tenzir, since a [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) counts events across polls and a live read never ends.

With `pushdown=false`, every operator stays in Tenzir and runs with TQL semantics. The operator still reads only the columns that the pipeline uses.

## Operators that SQL Server takes over

The operator takes over the longest run of operators directly after it that T-SQL can spell:

* [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), as the [filters](microsoft-sql.md#filters) section describes.
* [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of top-level fields, including renames, such as `select ip=src_ip, ts`.
* [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md) after a [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) or a [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) that SQL Server took over, which names the fields that remain. T-SQL has no way to select every column but some, so a [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md) of table columns stays in Tenzir.
* [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) with group keys on fields and `count()`, `count(x)`, `min(x)`, and `max(x)` of fields. Counts are `bigint`. The summary may follow [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) by fields.
* [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) as `TOP`, and [`top`](https://tenzir.com/docs/v7.0.0/reference/operators/top.md) or [`rare`](https://tenzir.com/docs/v7.0.0/reference/operators/rare.md) followed by [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md).

The first operator that SQL Server cannot spell ends the run. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) at `and`, so SQL Server can still take over the conjuncts that it spells. For example, SQL Server runs every step of

```tql
from_microsoft_sql table="dbo.alerts", host="db.example.com", database="soc"
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events
head 20
```

and returns at most 20 groups. The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) across them where a `TOP` decides which rows a derived table keeps.

## Filters

SQL Server takes over a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) whose predicate consists of:

* Top-level fields.
* Literals: numbers, strings, booleans, `null`, times with at most 100 nanosecond precision, and IP addresses.
* Comparisons, `in` with a list of literals, arithmetic with `+`, `-`, `*`, and `/`, and the boolean operators `and`, `or`, and `not`.
* The functions `starts_with`, `ends_with`, `length_chars`, `to_lower`, `to_upper`, `trim`, and `abs`, without named arguments such as `ignore_case`.

T-SQL has no boolean values, so a bare `bit` column is no predicate: `where flag` stays in Tenzir, while `where flag == true` compares with `1`. Other functions, including `length_bytes` and `match_regex`, nested fields, subnets, durations, other kinds of literals, strings with a NUL byte, arithmetic with a time literal such as `ts - 2024-01-01`, and optional fields such as `x?` stay in Tenzir.

## SQL Server semantics

The operators that SQL Server takes over run as SQL Server runs them, which can differ from TQL:

* Comparisons with `NULL` yield `NULL`, so `name != "alpha"` does not keep rows where `name` is `NULL`.
* Text compares, groups, and sorts under the collation of its column. The default collations ignore case and trailing spaces, so `name == "alice"` matches `Alice`, and `a`, `A`, and `a `form one group. In turn, SQL Server can use its indexes for such comparisons.
* SQL Server sorts `NULL` first in ascending order, and returns groups that tie in a sort in any order.
* SQL Server compares the stored value of a column, such as the exact value of a `decimal` or `money`, which Tenzir reads as a `double`, and computes arithmetic in the types of its operands.
* A time becomes a `datetimeoffset(7)` in UTC, such as `CAST('2024-01-01T00:00:00.0000000+00:00' AS datetimeoffset(7))`, which SQL Server compares with `date`, `datetime`, `smalldatetime`, `datetime2`, and `datetimeoffset` columns as an instant, reading the types without an offset as UTC.
* An IP address becomes its text, such as `N'10.0.0.1'`, which compares as text.
* `min` and `max` also take text, which TQL’s functions do not.
* The operator takes over operators before it knows the types of the columns, so a query that SQL Server rejects fails the pipeline: for example, a stage that reads a column that the table lacks, where Tenzir would warn and read `null`, `max` of a `bit` column, or a comparison, count, group, or sort of a legacy `text`, `ntext`, or `image` column. Use `pushdown=false` for such pipelines.

## Verify an optimization

To see the operators that SQL Server takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_microsoft_sql table="dbo.alerts", host="db.example.com" | where severity >= 3 | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`.
