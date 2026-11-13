---
title: "MySQL"
canonical: https://tenzir.com/docs/reference/optimizations/mysql
source: https://tenzir.com/docs/reference/optimizations/mysql.md
section: "Docs"
---

# MySQL

> When frommysql reads a table, it hands MySQL the operators that follow it, so that MySQL sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in MySQL, with MySQL’s semantics. This page describes which operators MySQL takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The optimizations overview explains how Tenzir optimizes pipelines in general.

When [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md) reads a table, it hands MySQL the operators that follow it, so that MySQL sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in MySQL, with MySQL’s semantics. This page describes which operators MySQL takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_mysql table="alerts"`. The operator writes the query itself and adds the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and the rest of the pipeline runs in Tenzir. So does **show mode** with `show`. To have MySQL filter, write the filter into your query.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the [`where`](https://tenzir.com/docs/reference/operators/where.md) operators that directly follow the operator. All other operators stay in Tenzir, since a [`head`](https://tenzir.com/docs/reference/operators/head.md) counts events across polls and a live read never ends.

With `pushdown=false`, every operator stays in Tenzir and runs with TQL semantics. The operator still reads only the columns that the pipeline uses.

## Operators that MySQL takes over

The operator takes over the longest run of operators directly after it that MySQL can spell:

* [`where`](https://tenzir.com/docs/reference/operators/where.md), as the [filters](mysql.md#filters) section describes.
* [`select`](https://tenzir.com/docs/reference/operators/select.md) of top-level fields, including renames, such as `select ip=src_ip, ts`.
* [`drop`](https://tenzir.com/docs/reference/operators/drop.md) after a [`select`](https://tenzir.com/docs/reference/operators/select.md) or a [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) that MySQL took over, which names the fields that remain. MySQL has no way to select every column but some, so a [`drop`](https://tenzir.com/docs/reference/operators/drop.md) of table columns stays in Tenzir.
* [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) with group keys on fields and `count()`, `count(x)`, `min(x)`, and `max(x)` of fields. The summary may follow [`select`](https://tenzir.com/docs/reference/operators/select.md), [`drop`](https://tenzir.com/docs/reference/operators/drop.md), and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](https://tenzir.com/docs/reference/operators/sort.md) by fields.
* [`head`](https://tenzir.com/docs/reference/operators/head.md), and [`top`](https://tenzir.com/docs/reference/operators/top.md) or [`rare`](https://tenzir.com/docs/reference/operators/rare.md) followed by [`head`](https://tenzir.com/docs/reference/operators/head.md).

The first operator that MySQL cannot spell ends the run. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](https://tenzir.com/docs/reference/operators/where.md) at `and`, so MySQL can still take over the conjuncts that it spells. For example, MySQL runs every step of

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events
head 20
```

and returns at most 20 groups. The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](https://tenzir.com/docs/reference/operators/sort.md) across them.

## Filters

MySQL takes over a [`where`](https://tenzir.com/docs/reference/operators/where.md) whose predicate consists of:

* Top-level fields.
* Literals: numbers, strings, booleans, `null`, times with at most microsecond precision, and IP addresses.
* Comparisons, `in` with a list of literals, arithmetic with `+`, `-`, `*`, and `/`, and the boolean operators `and`, `or`, and `not`.
* The functions `starts_with`, `ends_with`, `length_bytes`, `length_chars`, `to_lower`, `to_upper`, `trim`, `abs`, and `match_regex`, without named arguments such as `ignore_case`.

Other functions, nested fields, subnets, durations, other kinds of literals, strings with a backslash or a NUL byte, arithmetic with a time literal such as `ts - 2024-01-01`, and optional fields such as `x?` stay in Tenzir. Whether MySQL reads a backslash as an escape depends on the session’s SQL mode, which is why such strings stay.

## MySQL semantics

The operators that MySQL takes over run as MySQL runs them, which can differ from TQL:

* Comparisons with `NULL` yield `NULL`, so `name != "alpha"` does not keep rows where `name` is `NULL`.
* Text compares, groups, and sorts under the collation of its column. The default collation of MySQL 8, `utf8mb4_0900_ai_ci`, ignores case and accents, so `name == "alice"` matches `Alice`, and `a`, `A`, and `ä` form one group. A collation with the `PAD SPACE` attribute, such as the older `utf8mb4_general_ci`, also ignores trailing spaces. In turn, MySQL can use its indexes for such comparisons.
* MySQL sorts `NULL` first in ascending order, sorts text by a prefix of `max_sort_length` bytes, and returns groups that tie in a sort in any order.
* MySQL compares the stored value of a column, such as the exact value of a `DECIMAL` or the single-precision value of a `FLOAT`, which Tenzir reads as a `double`.
* MySQL computes arithmetic in the types of its operands: it divides integers as `DECIMAL`, and fails the query when a `BIGINT UNSIGNED` result is negative.
* A time becomes a string in UTC, such as `'2024-01-01 00:00:00.000000'`, which MySQL reads as the type of the column. A table read sets the session’s time zone to UTC, so `TIMESTAMP` columns compare in UTC and also arrive in UTC.
* An IP address becomes its text, such as `'10.0.0.1'`, which compares as text.
* `match_regex` uses MySQL’s `REGEXP_LIKE`, which matches with ICU rather than RE2.
* A [`select`](https://tenzir.com/docs/reference/operators/select.md) of a column that the table lacks fails the query, where Tenzir would warn and fill in `null`.

## Verify an optimization

To see the operators that MySQL takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_mysql table="alerts", host="db.example.com" | where severity >= 3 | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`.
