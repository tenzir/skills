---
title: "MySQL"
canonical: https://tenzir.com/docs/reference/optimizations/mysql
source: https://tenzir.com/docs/reference/optimizations/mysql.md
section: "Docs"
---

# MySQL

> This page documents which operators and functions frommysql transpiles to MySQL SQL, and how MySQL’s semantics differ from TQL. See our explanation of transpilation for shared planning rules and our optimizations overview for cross-target matrices.

This page documents which operators and functions [`from_mysql`](../operators/from_mysql.md) transpiles to MySQL SQL, and how MySQL’s semantics differ from TQL. See our explanation of [transpilation](../../explanations/transpilation.md) for shared planning rules and our [optimizations overview](../optimizations.md) for cross-target matrices.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_mysql table="alerts"`. The operator writes the query itself, and MySQL takes over the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and the rest of the pipeline runs in Tenzir. So does **show mode** with `show`. Use SQL mode for what the operators cannot express, such as joins or casts.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the [`where`](../operators/where.md) operators that directly follow the operator. All other operators run in Tenzir, since a [`head`](../operators/head.md) counts events across polls and a live read never ends.

With `pushdown=false`, every operator runs in Tenzir with TQL semantics. The operator still reads only the columns that the pipeline uses.

## Operators that MySQL takes over

MySQL takes over the [longest run of operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after the source that it can spell:

* [`where`](../operators/where.md), as the [filters and functions](mysql.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of top-level fields, including renames, such as `select ip=src_ip, ts`.
* [`drop`](../operators/drop.md) after a [`select`](../operators/select.md) or a [`summarize`](../operators/summarize.md) that MySQL took over, which names the fields that remain. MySQL has no way to select every column but some, so a [`drop`](../operators/drop.md) of table columns runs in Tenzir.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](mysql.md#summaries) section lists. The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../../explanations/transpilation.md#summaries-and-computed-expressions) describes.
* [`sort`](../operators/sort.md) by fields.
* [`head`](../operators/head.md), and [`top`](../operators/top.md) or [`rare`](../operators/rare.md) followed by [`head`](../operators/head.md).

For example, the pipeline

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
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
  SELECT `src_ip` AS `__tenzir_column_0`, COUNT(*) AS `__tenzir_column_1`
  FROM (
    SELECT `src_ip`, `severity`
    FROM `alerts`
  ) AS `__tenzir_table`
  WHERE (`severity` >= 3)
  GROUP BY `src_ip`
) AS `__tenzir_level_2`
WHERE (`__tenzir_column_1` >= 10)
ORDER BY `__tenzir_column_1` DESC
LIMIT 20
```

The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](../operators/sort.md) across them. Tenzir arranges the result columns into the fields of the pipeline, such as `src_ip` and `events`.

## Summaries

MySQL computes these aggregation functions of a [`summarize`](../operators/summarize.md):

🟢 runs in MySQL, 🟡 runs in MySQL conditionally or approximately, and ⚪ runs in Tenzir.

| TQL                   | Status | MySQL                           | Notes                                                                      |
| --------------------- | ------ | ------------------------------- | -------------------------------------------------------------------------- |
| `count()`             | 🟢     | `COUNT(*)`                      |                                                                            |
| `count(x)`            | 🟢     | `COUNT(x)`                      |                                                                            |
| `min(x)`              | 🟢     | `MIN(x)`                        |                                                                            |
| `max(x)`              | 🟢     | `MAX(x)`                        |                                                                            |
| `count_if(x, v => p)` | 🟢     | `COUNT(CASE WHEN p THEN x END)` | Skips `null` values                                                        |
| `count_distinct(x)`   | 🟢     | `COUNT(DISTINCT x)`             |                                                                            |
| `sum(x)`              | 🟢     | `SUM(x)`                        | Sums integers as a `DECIMAL`, which still arrives as an `int`              |
| `mean(x)`             | 🟢     | `AVG(x)`                        |                                                                            |
| `stddev(x)`           | 🟢     | `STDDEV_POP(x)`                 |                                                                            |
| `variance(x)`         | 🟢     | `VAR_POP(x)`                    |                                                                            |
| `all(x)`              | 🟢     | `MIN(x <> 0)`                   | Decoded as a boolean; skips `null` values and yields `null` without values |
| `any(x)`              | 🟢     | `MAX(x <> 0)`                   | Decoded as a boolean; skips `null` values and yields `null` without values |

Group keys and aggregate arguments can be computed values, such as `level` in

```tql
level = severity * 2
summarize src_ip, worst=max(level)
```

MySQL computes an assignment that the summary reads with its own semantics, including calls of the functions that the [filters and functions](mysql.md#filters-and-functions) section lists. An assignment that the summary doesn’t read must be infallible, as the rules for [computed keys and arguments](../../explanations/transpilation.md#summaries-and-computed-expressions) explain.

A time bucket, such as `hour = floor(ts, 1h)` before a `summarize hour, events=count()`, runs in MySQL for these widths:

| Width                                  | Status | MySQL                                                                                                 |
| -------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------- |
| Whole seconds, such as `1h`            | 🟢     | Runs as flooring of the microseconds since the epoch, which arrive as a time                          |
| Fractions of a second, such as `250ms` | 🟡     | Runs as flooring of the microseconds since the epoch, which arrive as a time. Whole microseconds only |
| Multiples of a week or a month         | ⚪      | Runs in Tenzir, since TQL aligns them to the calendar                                                 |

The buckets arrive as times, although MySQL returns `DATETIME` and `DATE` values as text otherwise, and read the values as UTC, as comparisons with time literals do.

## Filters and functions

MySQL takes over a [`where`](../operators/where.md) whose predicate consists of:

* Top-level fields.
* Literals: numbers, strings, booleans, `null`, times with at most microsecond precision, and IP addresses.
* Comparisons, `in` with a list of literals, arithmetic with `+`, `-`, `*`, and `/`, and the boolean operators `and`, `or`, and `not`.
* The functions marked 🟢 or 🟡 in the following table.

| Kind    | TQL                       | Status | MySQL                                               | Notes                                                                                                    |
| ------- | ------------------------- | ------ | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Strings | `x.starts_with(y)`        | 🟢     | `LEFT(x, CHAR_LENGTH(y)) = y`                       | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.ends_with(y)`          | 🟢     | `RIGHT(x, CHAR_LENGTH(y)) = y`                      | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.match_regex(y)`        | 🟢     | `REGEXP_LIKE(x, y, 'c')`                            | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.length_bytes()`        | 🟢     | `LENGTH(x)`                                         |                                                                                                          |
| Strings | `x.length_chars()`        | 🟢     | `CHAR_LENGTH(x)`                                    |                                                                                                          |
| Strings | `x.to_lower()`            | 🟢     | `LOWER(x)`                                          |                                                                                                          |
| Strings | `x.to_upper()`            | 🟢     | `UPPER(x)`                                          |                                                                                                          |
| Strings | `x.capitalize()`          | 🟢     | `CONCAT(UPPER(LEFT(x, 1)), LOWER(SUBSTRING(x, 2)))` |                                                                                                          |
| Strings | `x.trim()`                | 🟢     | `TRIM(x)`                                           |                                                                                                          |
| Strings | `x.trim_start()`          | 🟢     | `LTRIM(x)`                                          |                                                                                                          |
| Strings | `x.trim_end()`            | 🟢     | `RTRIM(x)`                                          |                                                                                                          |
| Strings | `x.replace(y, z)`         | 🟢     | `REPLACE(x, y, z)`                                  |                                                                                                          |
| Strings | `x.is_empty()`            | 🟢     | `CHAR_LENGTH(x) = 0`                                | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.slice(begin=b, end=e)` | 🟡     | `SUBSTRING(x, b + 1, GREATEST(e - b, 0))`           | With constant `begin` and `end` that are not negative                                                    |
| Hashes  | `x.hash_md5()`            | 🟢     | `MD5(x)`                                            |                                                                                                          |
| Hashes  | `x.hash_sha1()`           | 🟢     | `SHA1(x)`                                           |                                                                                                          |
| Hashes  | `x.hash_sha256()`         | 🟢     | `SHA2(x, 256)`                                      |                                                                                                          |
| Numbers | `x.abs()`                 | 🟢     | `ABS(x)`                                            |                                                                                                          |
| Numbers | `x.ceil()`                | 🟢     | `CAST(CEIL(x) AS SIGNED)`                           |                                                                                                          |
| Numbers | `x.floor()`               | 🟢     | `CAST(FLOOR(x) AS SIGNED)`                          |                                                                                                          |
| Numbers | `x.round()`               | 🟢     | `CAST(ROUND(x) AS SIGNED)`                          |                                                                                                          |
| Numbers | `x.sqrt()`                | 🟢     | `SQRT(x)`                                           |                                                                                                          |
| Numbers | `x.exp()`                 | 🟢     | `EXP(x)`                                            |                                                                                                          |
| Numbers | `x.log()`, `x.log(base)`  | 🟢     | `LN(x)`, `LOG(base, x)`                             |                                                                                                          |
| Times   | `x.year()`                | 🟢     | `YEAR(x)`                                           |                                                                                                          |
| Times   | `x.month()`               | 🟢     | `MONTH(x)`                                          |                                                                                                          |
| Times   | `x.day()`                 | 🟢     | `DAY(x)`                                            |                                                                                                          |
| Times   | `x.hour()`                | 🟢     | `HOUR(x)`                                           |                                                                                                          |
| Times   | `x.minute()`              | 🟢     | `MINUTE(x)`                                         |                                                                                                          |
| Times   | `x.second()`              | 🟢     | `SECOND(x) + MICROSECOND(x) / 1e6`                  |                                                                                                          |
| Times   | `x.since_epoch()`         | ⚪      | —                                                   | MySQL has no durations                                                                                   |

The same functions compute group keys and aggregate arguments. Predicates used as values are wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded back as booleans (`null` predicates become `false`). The time functions read `DATETIME` and `DATE` values as UTC.

MySQL has no booleans, so a bare `TINYINT` column is no predicate: `where flag` runs in Tenzir, while `where flag == true` compares with `TRUE`, which is 1. Other functions, named arguments such as `ignore_case`, nested fields, subnets, durations, other kinds of literals, strings with a backslash or a NUL byte, arithmetic with a time literal such as `ts - 2024-01-01`, and optional fields such as `x?` run in Tenzir. Whether MySQL reads a backslash as an escape depends on the session’s SQL mode, which is why such strings run in Tenzir.

## MySQL semantics

The operators that MySQL takes over run as MySQL runs them, which can differ from TQL:

* Comparisons with `NULL` yield `NULL`, so `name != "alpha"` does not keep rows where `name` is `NULL`.
* Text compares, groups, and sorts under the collation of its column. The default collation of MySQL 8, `utf8mb4_0900_ai_ci`, ignores case and accents, so `name == "alice"` matches `Alice`, and `a`, `A`, and `ä` form one group. A collation with the `PAD SPACE` attribute, such as the older `utf8mb4_general_ci`, also ignores trailing spaces. In turn, MySQL can use its indexes for such comparisons.
* MySQL sorts `NULL` first in ascending order, sorts text by a prefix of `max_sort_length` bytes, and returns groups that tie in a sort in any order.
* MySQL compares the stored value of a column, such as the exact value of a `DECIMAL` or the single-precision value of a `FLOAT`, which Tenzir reads as a `double`.
* MySQL computes arithmetic in the types of its operands: it divides integers as `DECIMAL`, and fails the query when a `BIGINT UNSIGNED` result is negative.
* A time becomes a string in UTC, such as `'2024-01-01 00:00:00.000000'`, which MySQL reads as the type of the column. A table read sets the session’s time zone to UTC, so `TIMESTAMP` columns compare in UTC and also arrive in UTC.
* An IP address becomes its text, such as `'10.0.0.1'`, which compares as text.
* The `match_regex` function becomes `REGEXP_LIKE`, which matches with ICU rather than RE2.
* A [`select`](../operators/select.md) of a column that the table lacks fails the query, where Tenzir would warn and fill in `null`.
* A query that MySQL rejects fails the pipeline with the error of MySQL, as our explanation of [plan-time diagnostics](../../explanations/transpilation.md#plan-time-decisions-and-diagnostics) describes.
