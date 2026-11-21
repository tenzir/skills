---
title: "ClickHouse"
canonical: https://tenzir.com/docs/reference/optimizations/clickhouse
source: https://tenzir.com/docs/reference/optimizations/clickhouse.md
section: "Docs"
---

# ClickHouse

> When fromclickhouse reads a table, ClickHouse takes over the operators that follow it, so that it sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in ClickHouse, with ClickHouse’s semantics, and the rest of the pipeline runs in Tenzir. This page describes which operators ClickHouse takes over, which functions it computes, and how its results can differ from Tenzir’s. Our optimizations overview compares the targets and describes the rules that all sources share.

When [`from_clickhouse`](../operators/from_clickhouse.md) reads a table, ClickHouse takes over the operators that follow it, so that it sends only what the pipeline keeps instead of the whole table. Those operators leave the pipeline and run in ClickHouse, with ClickHouse’s semantics, and the rest of the pipeline runs in Tenzir. This page describes which operators ClickHouse takes over, which functions it computes, and how its results can differ from Tenzir’s. Our [optimizations overview](../optimizations.md) compares the targets and describes the rules that all sources share.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_clickhouse table="logs.events"`. The operator writes the query itself, and ClickHouse takes over the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and the rest of the pipeline runs in Tenzir. Use it for what the operators cannot express, such as joins or casts.

With `pushdown=false`, every operator runs in Tenzir with TQL semantics. The operator still reads only the columns that the pipeline uses.

[`from_hydrolix`](../operators/from_hydrolix.md) follows the same rules on Hydrolix’s ClickHouse engine. Its [reference](../operators/from_hydrolix.md#optimizations) describes what is specific to Hydrolix, such as the time range on the primary timestamp.

## Operators that ClickHouse takes over

ClickHouse takes over the [longest run of operators](../optimizations.md#the-run-of-operators-after-the-source) directly after the source that it can spell:

* [`where`](../operators/where.md), as the [filters and functions](clickhouse.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of fields, including renames and elements of named tuples, such as `select ip=src_ip, meta.level`.
* [`drop`](../operators/drop.md) of top-level fields, which becomes `* EXCEPT (…)`.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](clickhouse.md#summaries) section lists. The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](../operators/sort.md) by fields.
* [`head`](../operators/head.md), and [`top`](../operators/top.md) or [`rare`](../operators/rare.md) followed by [`head`](../operators/head.md).

For example, the pipeline

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
SELECT *
FROM (
  SELECT `Y` AS `__tenzir_column_0`, toInt64(count()) AS `__tenzir_column_1`
  FROM logs.events
  WHERE (`x` > 0)
  GROUP BY `Y`
) AS `__tenzir_level_2`
WHERE (`__tenzir_column_1` >= 2)
ORDER BY `__tenzir_column_1` DESC
LIMIT 3
```

The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](../operators/sort.md) across them. Tenzir arranges the result columns into the fields of the pipeline, such as `Y` and `n`.

## Summaries

ClickHouse and Hydrolix compute these aggregation functions of a [`summarize`](../operators/summarize.md):

| TQL                   | ClickHouse               | Notes                                    |
| --------------------- | ------------------------ | ---------------------------------------- |
| `count()`             | `toInt64(count())`       |                                          |
| `count(x)`            | `toInt64(count(x))`      |                                          |
| `min(x)`              | `min(x)`                 | Yields the type's default without values |
| `max(x)`              | `max(x)`                 | Yields the type's default without values |
| `count_if(x, v => p)` | `toInt64(countIf(x, p))` | Skips `null` values                      |
| `count_distinct(x)`   | `toInt64(uniqExact(x))`  |                                          |
| `sum(x)`              | `sum(x)`                 |                                          |
| `mean(x)`             | `avg(x)`                 |                                          |
| `stddev(x)`           | `stddevPop(x)`           |                                          |
| `variance(x)`         | `varPop(x)`              |                                          |
| `all(x)`              | `min(x)`                 | Skips `null` values                      |
| `any(x)`              | `max(x)`                 | Skips `null` values                      |

Without values, `min`, `max`, and `sum` can return the type’s default rather than `null`. The `all` and `any` functions skip `null` values and can return `null` without values. A summary keeps a group for `null` keys.

Group keys and aggregate arguments can be computed values, such as `level` in

```tql
level = severity * 2
summarize src_ip, worst=max(level)
```

ClickHouse computes an assignment that the summary reads with its own semantics, including calls of the functions that the [filters and functions](clickhouse.md#filters-and-functions) section lists. An assignment that the summary doesn’t read must be infallible, as the rules for [computed keys and arguments](../optimizations.md#computed-keys-and-arguments) explain.

A time bucket, such as `hour = floor(time, 1h)` before a `summarize hour, events=count()`, runs in ClickHouse for these widths:

| Width                                  | ClickHouse                                                           |
| -------------------------------------- | -------------------------------------------------------------------- |
| Whole seconds, such as `1h`            | Runs as flooring division of `toUnixTimestamp64Nano(x)` by the width |
| Fractions of a second, such as `250ms` | Runs as flooring division of `toUnixTimestamp64Nano(x)` by the width |
| Multiples of a week or a month         | Runs in Tenzir, since TQL aligns them to the calendar                |

## Filters and functions

ClickHouse takes over a [`where`](../operators/where.md) whose predicate consists of:

* Fields, including elements of named tuples, such as `meta.level`, which becomes `tupleElement(meta, 'level')`, and columns with a dot in their name, such as `this["a.b"]`.
* Literals: numbers, strings, booleans, `null`, times, which become `fromUnixTimestamp64Nano(…, 'UTC')`, and IP addresses, which become `toIPv4(…)` or `toIPv6(…)`.
* Comparisons, `in` with a list of literals, arithmetic, and the boolean operators `and`, `or`, and `not`.
* The functions in the following table.

| TQL                       | ClickHouse                                                          | Notes                                                         |
| ------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------- |
| `x.starts_with(y)`        | `startsWith(x, y)`                                                  |                                                               |
| `x.ends_with(y)`          | `endsWith(x, y)`                                                    |                                                               |
| `x.match_regex(y)`        | `match(x, y)`                                                       | ClickHouse's RE2                                              |
| `x.length_bytes()`        | `length(x)`                                                         |                                                               |
| `x.length_chars()`        | `lengthUTF8(x)`                                                     |                                                               |
| `x.to_lower()`            | `lowerUTF8(x)`                                                      |                                                               |
| `x.to_upper()`            | `upperUTF8(x)`                                                      |                                                               |
| `x.capitalize()`          | `concat(upperUTF8(leftUTF8(x, 1)), lowerUTF8(substringUTF8(x, 2)))` |                                                               |
| `x.trim()`                | `trimBoth(x)`                                                       |                                                               |
| `x.trim_start()`          | `trimLeft(x)`                                                       |                                                               |
| `x.trim_end()`            | `trimRight(x)`                                                      |                                                               |
| `x.replace(y, z)`         | `replaceAll(x, y, z)`                                               |                                                               |
| `x.is_empty()`            | `toBool(empty(x))`                                                  |                                                               |
| `x.slice(begin=b, end=e)` | `substringUTF8(x, b + 1, greatest(e - b, 0))`                       | With constant `begin` and `end` that are not negative         |
| `x.hash_md5()`            | `lower(hex(MD5(x)))`                                                | Rejects arguments that are no strings                         |
| `x.hash_sha1()`           | `lower(hex(SHA1(x)))`                                               | Rejects arguments that are no strings                         |
| `x.hash_sha256()`         | `lower(hex(SHA256(x)))`                                             | Rejects arguments that are no strings                         |
| `x.abs()`                 | `abs(x)`                                                            |                                                               |
| `x.ceil()`                | `toInt64(ceil(x))`                                                  |                                                               |
| `x.floor()`               | `toInt64(floor(x))`                                                 |                                                               |
| `x.round()`               | `toInt64(round(x))`                                                 | Rounds halves to even                                         |
| `x.sqrt()`                | `sqrt(x)`                                                           |                                                               |
| `x.exp()`                 | `exp(x)`                                                            |                                                               |
| `x.log()`, `x.log(base)`  | `log(x)`, `(log(x) / log(base))`                                    |                                                               |
| `x.year()`                | `toYear(x, 'UTC')`                                                  |                                                               |
| `x.month()`               | `toMonth(x, 'UTC')`                                                 |                                                               |
| `x.day()`                 | `toDayOfMonth(x, 'UTC')`                                            |                                                               |
| `x.hour()`                | `toHour(x, 'UTC')`                                                  |                                                               |
| `x.minute()`              | `toMinute(x, 'UTC')`                                                |                                                               |
| `x.second()`              | `toSecond(x, 'UTC')`                                                | Plus the fraction of the second, from `toUnixTimestamp64Nano` |

The same functions compute group keys and aggregate arguments. The time functions count in UTC, whatever the time zone of the column. Durations, subnets, non-finite numbers, other functions, named arguments such as `ignore_case`, and optional fields such as `x?` run in Tenzir.

## ClickHouse semantics

The operators that ClickHouse takes over run as ClickHouse runs them, which can differ from TQL:

* ClickHouse is statically typed. Comparing an `Int64` column with a string, or a string column with an IP address, fails the query. A comparison with a path of a `JSON` column works only while every row holds the same type there, and fails otherwise. A path that holds an object matches no comparison with a value, but counts as present in `!= null`. An empty object counts as missing.
* Comparisons with `NULL` yield `NULL`, so `name != "alpha"` does not keep rows where `name` is `NULL`.
* A time compares in UTC at nanosecond precision. A `Date32` column holds no dates before 1900.
* ClickHouse sorts `NULL` last in ascending order and returns rows that tie in a sort in any order.
* A query that ClickHouse rejects fails the pipeline with the error of ClickHouse, as the overview’s [diagnostics](../optimizations.md#diagnostics) describe.

### Limits and cancellation

A table read asks ClickHouse to fail rather than return a partial result when it hits one of its limits, such as a `max_result_rows` setting of your user’s profile. When the pipeline stops, the operator also stops a query that ClickHouse is still running, such as a sort or a summary that has not returned its first rows yet.

### Binding fields

The operator decides which operators to take over from the pipeline alone. When the pipeline runs, it reads the table’s columns and binds every field that those operators use to a column: a top-level column, an element of a named tuple, a column with a dot in its name, a key of a `Map` column with string keys, such as `labels['env']` for `labels.env`, or a path below a `JSON` column. A missing map key yields the default of the map’s value type, such as `""` or `0`, and `null` only for `Nullable` values.

If a field cannot be bound, the read fails before ClickHouse runs a query, with the error `ClickHouse cannot compute the stages that the operator took over`, the reason as a note, and a hint to use `pushdown=false`. This happens for a path below a column that is not a named tuple, a `Map` with string keys, or `JSON`, for a tuple element that does not exist, for a generated `ALIAS`, `MATERIALIZED`, or `EPHEMERAL` column, which `SELECT *` may leave out, and for a [`sort`](../operators/sort.md) by a path below a `JSON` column whose order a later operator needs, such as in `sort j.k | head 10 | sort id`. A top-level field that the table lacks fails the query in ClickHouse.

### Catch-all tables

A table with a [catch-all column](https://tenzir.com/product/integrations/clickhouse#catch-all-columns) returns reconstructed events, in which the fields of the catch-all move to the top level and dotted columns become nested fields. ClickHouse takes over [`where`](../operators/where.md), [`sort`](../operators/sort.md), and [`head`](../operators/head.md) on such a table, binding each field to the single column that holds it: a typed column, or a path of the catch-all or another `JSON` column.

The read fails before it runs a query, with the error `ClickHouse cannot compute the stages that the operator took over`, the reason as a note, and a hint to use `pushdown=false`, if:

* ClickHouse takes over a [`select`](../operators/select.md), [`drop`](../operators/drop.md), or [`summarize`](../operators/summarize.md), which need the reconstructed events.
* A field has no single origin, such as a record that a dotted column merges into, or a field that overlaps a generated column.
* A column shadows the field, such as a column `event.category` next to the catch-all `event` for the field `category`, since ClickHouse resolves the path to that column. Our integration guide explains how to [name the catch-all column](https://tenzir.com/product/integrations/clickhouse#name-the-catch-all-column) to avoid this.
* A field holds a whole `JSON` value, such as the catch-all column itself.

Use `pushdown=false` to compute these operators in Tenzir on the reconstructed events.

## Verify an optimization

To see which operators ClickHouse takes over in a pipeline, print the optimized pipeline, as the overview’s section on [verifying an optimization](../optimizations.md#verify-an-optimization) shows. ClickHouse’s `system.query_log` table shows the query that the operator sent.
