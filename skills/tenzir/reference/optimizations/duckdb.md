---
title: "DuckDB"
canonical: https://tenzir.com/docs/reference/optimizations/duckdb
source: https://tenzir.com/docs/reference/optimizations/duckdb.md
section: "Docs"
---

# DuckDB

> This page documents which operators and functions fromduckdb transpiles to DuckDB SQL, and how DuckDB’s semantics differ from TQL. See our explanation of transpilation for shared planning rules and our optimizations overview for cross-target matrices.

This page documents which operators and functions [`from_duckdb`](../operators/from_duckdb.md) transpiles to DuckDB SQL, and how DuckDB’s semantics differ from TQL. See our explanation of [transpilation](../../explanations/transpilation.md) for shared planning rules and our [optimizations overview](../optimizations.md) for cross-target matrices.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_duckdb "events.duckdb", table="alerts"`. The operator writes the query itself, and DuckDB takes over the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and the rest of the pipeline runs in Tenzir. Use it for what the operators cannot express, such as joins.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the [`where`](../operators/where.md) operators that directly follow the operator. All other operators run in Tenzir, since a [`head`](../operators/head.md) counts events across polls and a live read never ends.

With `pushdown=false`, every operator runs in Tenzir with TQL semantics. The operator still reads only the columns that the pipeline uses.

## Operators that DuckDB takes over

DuckDB takes over the [longest run of operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after the source that it can spell:

* [`where`](../operators/where.md), as the [filters and functions](duckdb.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of fields, including renames and fields of `STRUCT` columns, such as `select ip=src_ip, host=meta.host`.
* [`drop`](../operators/drop.md) of top-level fields.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](duckdb.md#summaries) section lists. The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../../explanations/transpilation.md#summaries-and-computed-expressions) describes.
* [`sort`](../operators/sort.md) by fields.
* [`head`](../operators/head.md), and [`top`](../operators/top.md) or [`rare`](../operators/rare.md) followed by [`head`](../operators/head.md).

For example, the pipeline

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events
head 20
```

sends this query:

```sql
SELECT *
FROM (
  SELECT "src_ip" AS "__tenzir_column_0", COUNT(*) AS "__tenzir_column_1"
  FROM (
    SELECT "src_ip", "severity"
    FROM "alerts"
  ) AS "__tenzir_table"
  WHERE ("severity" >= 3)
  GROUP BY "src_ip"
) AS "__tenzir_level_2"
WHERE ("__tenzir_column_1" >= 10)
ORDER BY "__tenzir_column_1" DESC
LIMIT 20
```

The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](../operators/sort.md) across them. Tenzir arranges the result columns into the fields of the pipeline, such as `src_ip` and `events`.

## Summaries

DuckDB computes these aggregation functions of a [`summarize`](../operators/summarize.md):

🟢 runs in DuckDB, 🟡 runs in DuckDB conditionally or approximately, and ⚪ runs in Tenzir.

| TQL                   | Status | DuckDB                          | Notes                                                           |
| --------------------- | ------ | ------------------------------- | --------------------------------------------------------------- |
| `count()`             | 🟢     | `COUNT(*)`                      |                                                                 |
| `count(x)`            | 🟢     | `COUNT(x)`                      |                                                                 |
| `min(x)`              | 🟢     | `MIN(x)`                        |                                                                 |
| `max(x)`              | 🟢     | `MAX(x)`                        |                                                                 |
| `count_if(x, v => p)` | 🟢     | `COUNT(CASE WHEN p THEN x END)` | Skips `null` values                                             |
| `count_distinct(x)`   | 🟢     | `COUNT(DISTINCT x)`             |                                                                 |
| `sum(x)`              | 🟢     | `SUM(x)`                        | Widens integers to a `HUGEINT`, which still arrives as an `int` |
| `mean(x)`             | 🟢     | `AVG(x)`                        |                                                                 |
| `stddev(x)`           | 🟢     | `STDDEV_POP(x)`                 |                                                                 |
| `variance(x)`         | 🟢     | `VAR_POP(x)`                    |                                                                 |
| `all(x)`              | 🟢     | `bool_and(x)`                   | Skips `null` values; yields `null` without values               |
| `any(x)`              | 🟢     | `bool_or(x)`                    | Skips `null` values; yields `null` without values               |

Group keys and aggregate arguments can be computed values, such as `level` in

```tql
level = severity * 2
summarize src_ip, worst=max(level)
```

DuckDB computes an assignment that the summary reads with its own semantics, including calls of the functions that the [filters and functions](duckdb.md#filters-and-functions) section lists. An assignment that the summary doesn’t read must be infallible, as the rules for [computed keys and arguments](../../explanations/transpilation.md#summaries-and-computed-expressions) explain.

A time bucket, such as `hour = floor(ts, 1h)` before a `summarize hour, events=count()`, runs in DuckDB for these widths:

| Width                                  | Status | DuckDB                                                  |
| -------------------------------------- | ------ | ------------------------------------------------------- |
| Whole seconds, such as `1h`            | 🟢     | Runs as flooring division of `epoch_ns(x)` by the width |
| Fractions of a second, such as `250ms` | 🟢     | Runs as flooring division of `epoch_ns(x)` by the width |
| Multiples of a week or a month         | ⚪      | Runs in Tenzir, since TQL aligns them to the calendar   |

## Filters and functions

DuckDB takes over a [`where`](../operators/where.md) whose predicate consists of:

* Fields, including fields of `STRUCT` columns, which DuckDB reads with `struct_extract`.
* Literals: numbers, strings, booleans, `null`, times, durations of whole microseconds, and IP addresses.
* Comparisons, `in` with a list of literals, arithmetic with `+`, `-`, `*`, and `/`, and the boolean operators `and`, `or`, and `not`.
* The functions in the following table.

| Kind    | TQL                       | Status | DuckDB                                       | Notes                                                 |
| ------- | ------------------------- | ------ | -------------------------------------------- | ----------------------------------------------------- |
| Strings | `x.starts_with(y)`        | 🟢     | `starts_with(x, y)`                          |                                                       |
| Strings | `x.ends_with(y)`          | 🟢     | `ends_with(x, y)`                            |                                                       |
| Strings | `x.match_regex(y)`        | 🟢     | `regexp_matches(x, y)`                       |                                                       |
| Strings | `x.length_bytes()`        | 🟢     | `strlen(x)`                                  |                                                       |
| Strings | `x.length_chars()`        | 🟢     | `length(x)`                                  |                                                       |
| Strings | `x.to_lower()`            | 🟢     | `lower(x)`                                   |                                                       |
| Strings | `x.to_upper()`            | 🟢     | `upper(x)`                                   |                                                       |
| Strings | `x.capitalize()`          | 🟢     | `upper(left(x, 1)) \|\| lower(substr(x, 2))` |                                                       |
| Strings | `x.trim()`                | 🟢     | `trim(x)`                                    |                                                       |
| Strings | `x.trim_start()`          | 🟢     | `ltrim(x)`                                   |                                                       |
| Strings | `x.trim_end()`            | 🟢     | `rtrim(x)`                                   |                                                       |
| Strings | `x.replace(y, z)`         | 🟢     | `replace(x, y, z)`                           |                                                       |
| Strings | `x.is_empty()`            | 🟢     | `length(x) = 0`                              |                                                       |
| Strings | `x.slice(begin=b, end=e)` | 🟡     | `substr(x, b + 1, greatest(e - b, 0))`       | With constant `begin` and `end` that are not negative |
| Hashes  | `x.hash_md5()`            | 🟢     | `md5(x)`                                     |                                                       |
| Hashes  | `x.hash_sha1()`           | 🟢     | `sha1(x)`                                    |                                                       |
| Hashes  | `x.hash_sha256()`         | 🟢     | `sha256(x)`                                  |                                                       |
| Numbers | `x.abs()`                 | 🟢     | `abs(x)`                                     |                                                       |
| Numbers | `x.ceil()`                | 🟢     | `CAST(ceil(x) AS BIGINT)`                    |                                                       |
| Numbers | `x.floor()`               | 🟢     | `CAST(floor(x) AS BIGINT)`                   |                                                       |
| Numbers | `x.round()`               | 🟢     | `CAST(round(x) AS BIGINT)`                   |                                                       |
| Numbers | `x.sqrt()`                | 🟢     | `sqrt(x)`                                    | Fails the query for negative inputs                   |
| Numbers | `x.exp()`                 | 🟢     | `exp(x)`                                     |                                                       |
| Numbers | `x.log()`, `x.log(base)`  | 🟢     | `ln(x)`, `(ln(x) / ln(base))`                | Fails the query for zero or negative inputs           |
| Times   | `x.year()`                | 🟢     | `year(x)`                                    |                                                       |
| Times   | `x.month()`               | 🟢     | `month(x)`                                   |                                                       |
| Times   | `x.day()`                 | 🟢     | `day(x)`                                     |                                                       |
| Times   | `x.hour()`                | 🟢     | `hour(x)`                                    |                                                       |
| Times   | `x.minute()`              | 🟢     | `minute(x)`                                  |                                                       |
| Times   | `x.second()`              | 🟢     | `microsecond(x) / 1e6`                       |                                                       |
| Times   | `x.since_epoch()`         | 🟢     | `to_microseconds(epoch_us(x))`               | Microsecond precision (`INTERVAL`)                    |

The same functions compute group keys and aggregate arguments. Other functions, named arguments such as `ignore_case`, subnets, other kinds of literals, strings with NUL bytes, arithmetic with a time literal such as `ts - 2024-01-01`, and optional fields such as `x?` run in Tenzir.

## DuckDB semantics

The operators that DuckDB takes over run as DuckDB runs them, which can differ from TQL:

* Comparisons with `null` yield `null`, so `name != "alpha"` does not keep rows where `name` is `null`.
* Text compares and sorts under the collation of its column, such as `COLLATE NOCASE`.
* DuckDB sorts `null` last, and returns groups that tie in a sort in any order.
* DuckDB computes arithmetic in the types of its operands, and considers `NaN` equal to itself and greater than every other number. Functions such as `round`, `exp`, and `to_upper` follow DuckDB, which may round floating-point numbers or map case differently from TQL.
* A time becomes a string in UTC, such as `'2024-01-01 00:00:00.000000000+00'`, which DuckDB casts to the type of the column. A comparison therefore never depends on the session time zone, but a `DATE` or `TIMESTAMP_S` column compares with the time truncated to its precision.
* An IP address becomes its text, such as `'10.0.0.1'`, which compares as text against a `VARCHAR` column.
* A [`select`](../operators/select.md) of a column that the table lacks fails the query, where Tenzir would warn and fill in `null`.
* A query that DuckDB rejects fails the pipeline with the error of DuckDB, as our explanation of [plan-time diagnostics](../../explanations/transpilation.md#plan-time-decisions-and-diagnostics) describes.

When DuckDB computes a summary or a [`select`](../operators/select.md), Tenzir does not see the individual rows, so it does not warn about values that it reads as `null`, such as a field of a `NULL` struct.
