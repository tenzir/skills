---
title: "ClickHouse"
canonical: https://tenzir.com/docs/v7.0.0/reference/optimizations/clickhouse
source: https://tenzir.com/docs/v7.0.0/reference/optimizations/clickhouse.md
section: "Docs"
---

# ClickHouse

> When fromclickhouse reads a table, it hands ClickHouse the operators that follow it, so that ClickHouse sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in ClickHouse, with ClickHouse’s semantics. This page describes which operators ClickHouse takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The optimizations overview explains how Tenzir optimizes pipelines in general.

When [`from_clickhouse`](https://tenzir.com/docs/v7.0.0/reference/operators/from_clickhouse.md) reads a table, it hands ClickHouse the operators that follow it, so that ClickHouse sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in ClickHouse, with ClickHouse’s semantics. This page describes which operators ClickHouse takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. The [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_clickhouse table="logs.events"`. The operator writes the query itself and adds the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and the rest of the pipeline runs in Tenzir. To have ClickHouse filter, write the filter into your query.

With `pushdown=false`, every operator stays in Tenzir and runs with TQL semantics. The operator still reads only the columns that the pipeline uses.

[`from_hydrolix`](https://tenzir.com/docs/v7.0.0/reference/operators/from_hydrolix.md) follows the same rules on Hydrolix’s ClickHouse engine. Its [reference](../operators/from_hydrolix.md#optimizations) describes what is specific to Hydrolix, such as the time range on the primary timestamp.

## Operators that ClickHouse takes over

The operator takes over the longest run of operators directly after it that ClickHouse can spell:

* [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), as the [filters](clickhouse.md#filters) section describes.
* [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of fields, including renames and elements of named tuples, such as `select ip=src_ip, meta.level`.
* [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md) of top-level fields, which becomes `* EXCEPT (…)`.
* [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) with group keys on fields and `count()`, `count(x)`, `min(x)`, and `max(x)` of fields. The summary may follow [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes. `sum` and `mean` stay in Tenzir, since ClickHouse may return `NaN` or infinity for them.
* [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) by fields.
* [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), and [`top`](https://tenzir.com/docs/v7.0.0/reference/operators/top.md) or [`rare`](https://tenzir.com/docs/v7.0.0/reference/operators/rare.md) followed by [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md).

The first operator that ClickHouse cannot spell ends the run. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) at `and`, so ClickHouse can still take over the conjuncts that it spells. For example, the pipeline

```tql
from_clickhouse table="logs.events"
where x > 0
summarize Y, n=count()
where n >= 2
sort -n
head 3
```

sends this query:

```sql
SELECT * FROM (
  SELECT `Y` AS `__tenzir_column_0`, toInt64(count()) AS `__tenzir_column_1`
  FROM logs.events WHERE (`x` > 0) GROUP BY `Y`
) AS `__tenzir_level_2`
WHERE (`__tenzir_column_1` >= 2)
ORDER BY `__tenzir_column_1` DESC LIMIT 3
```

The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) across them. Tenzir arranges the result columns into the fields of the pipeline, such as `Y` and `n`. A table read asks ClickHouse to fail rather than return a partial result when it hits one of its limits, such as a `max_result_rows` setting of your user’s profile. When the pipeline stops, the operator also stops a query that ClickHouse is still running, such as a sort or a summary that has not returned its first rows yet.

## Filters

ClickHouse takes over a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) whose predicate consists of:

* Fields, including elements of named tuples, such as `meta.level`, which becomes `tupleElement(meta, 'level')`, and columns with a dot in their name, such as `this["a.b"]`.
* Literals: numbers, strings, booleans, `null`, times, which become `fromUnixTimestamp64Nano(…, 'UTC')`, and IP addresses, which become `toIPv4(…)` or `toIPv6(…)`.
* Comparisons, `in` with a list of literals, arithmetic, and the boolean operators `and`, `or`, and `not`.
* The functions `starts_with`, `ends_with`, `length_bytes`, `length_chars`, `to_lower`, `to_upper`, `trim`, `abs`, and `match_regex`, without named arguments such as `ignore_case`.

Durations, subnets, non-finite numbers, other functions, and optional fields such as `x?` stay in Tenzir.

## Binding fields

The operator decides which operators to take over from the pipeline alone. When the pipeline runs, it reads the table’s columns and binds every field that those operators use to a column: a top-level column, an element of a named tuple, a column with a dot in its name, a key of a `Map` column with string keys, such as `labels['env']` for `labels.env`, or a path below a `JSON` column. A missing map key yields the default of the map’s value type, such as `""` or `0`, and `null` only for `Nullable` values. If a field cannot be bound, the read fails before ClickHouse runs a query, with the reason and a hint to use `pushdown=false`. This happens for a path below a column that is not a named tuple, a `Map` with string keys, or `JSON`, for a tuple element that does not exist, for a generated `ALIAS`, `MATERIALIZED`, or `EPHEMERAL` column, which `SELECT *` may leave out, and for a [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) by a path below a `JSON` column whose order a later operator needs, such as in `sort j.k | head 10 | sort id`. A top-level field that the table lacks fails the query in ClickHouse.

## Catch-all tables

A table with a [catch-all column](https://docs.tenzir.com/integrations/clickhouse#catch-all-columns) returns reconstructed events, in which the fields of the catch-all move to the top level and dotted columns become nested fields. ClickHouse takes over [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) on such a table, binding each field to the single column that holds it: a typed column, or a path of the catch-all or another `JSON` column.

The read fails before it runs a query, with a hint to use `pushdown=false`, if:

* ClickHouse takes over a [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), or [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md), which need the reconstructed events.
* A field has no single origin, such as a record that a dotted column merges into, or a field that overlaps a generated column.
* A column shadows the field, such as a column `event.category` next to the catch-all `event` for the field `category`, since ClickHouse resolves the path to that column. Our integration guide explains how to [name the catch-all column](https://docs.tenzir.com/integrations/clickhouse#name-the-catch-all-column) to avoid this.
* A field holds a whole `JSON` value, such as the catch-all column itself.

Use `pushdown=false` to compute these operators in Tenzir on the reconstructed events.

## ClickHouse semantics

The operators that ClickHouse takes over run as ClickHouse runs them, which can differ from TQL:

* ClickHouse is statically typed. Comparing an `Int64` column with a string, or a string column with an IP address, fails the query. A comparison with a path of a `JSON` column works only while every row holds the same type there, and fails otherwise. A path that holds an object matches no comparison with a value, but counts as present in `!= null`. An empty object counts as missing.
* Comparisons with `NULL` yield `NULL`, so `name != "alpha"` does not keep rows where `name` is `NULL`.
* `to_lower` and `to_upper` become `lowerUTF8` and `upperUTF8`, and `match_regex` becomes `match`, which uses ClickHouse’s RE2.
* `summarize` keeps a group for `null` keys. `min` and `max` become `minOrNull` and `maxOrNull`, which yield `null` without values.
* A time compares in UTC at nanosecond precision. A `Date32` column holds no dates before 1900.
* ClickHouse sorts `NULL` last in ascending order and returns rows that tie in a sort in any order.
* A query that ClickHouse rejects fails the pipeline with a hint to use `pushdown=false`.

## Verify an optimization

To see the operators that ClickHouse takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_clickhouse table="logs.events" | where severity >= 3 | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`. ClickHouse’s `system.query_log` table shows the query that the operator sent.
