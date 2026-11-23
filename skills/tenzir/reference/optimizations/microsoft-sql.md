---
title: "Microsoft SQL Server"
canonical: https://tenzir.com/docs/reference/optimizations/microsoft-sql
source: https://tenzir.com/docs/reference/optimizations/microsoft-sql.md
section: "Docs"
---

# Microsoft SQL Server

> This page documents which operators and functions frommicrosoftsql transpiles to T-SQL, and how SQL Server’s semantics differ from TQL. See our explanation of transpilation for shared planning rules and our optimizations overview for cross-target matrices.

This page documents which operators and functions [`from_microsoft_sql`](../operators/from_microsoft_sql.md) transpiles to T-SQL, and how SQL Server’s semantics differ from TQL. See our explanation of [transpilation](../../explanations/transpilation.md) for shared planning rules and our [optimizations overview](../optimizations.md) for cross-target matrices.

## When it applies

The operator reads in one of these modes:

* **Table mode** reads a table that you name with `table`, as in `from_microsoft_sql table="dbo.alerts"`. The operator writes the query itself, and SQL Server takes over the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` or `query` exactly as written, and the rest of the pipeline runs in Tenzir. So does **show mode** with `show`. Use SQL mode for what the operators cannot express, such as joins or casts.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the [`where`](../operators/where.md) operators that directly follow the operator. All other operators run in Tenzir, since a [`head`](../operators/head.md) counts events across polls and a live read never ends.

With `pushdown=false`, every operator runs in Tenzir with TQL semantics. The operator still reads only the columns that the pipeline uses.

## Operators that SQL Server takes over

SQL Server takes over the [longest run of operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after the source that T-SQL can spell:

* [`where`](../operators/where.md), as the [filters and functions](microsoft-sql.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of top-level fields, including renames, such as `select ip=src_ip, ts`.
* [`drop`](../operators/drop.md) after a [`select`](../operators/select.md) or a [`summarize`](../operators/summarize.md) that SQL Server took over, which names the fields that remain. T-SQL has no way to select every column but some, so a [`drop`](../operators/drop.md) of table columns runs in Tenzir.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](microsoft-sql.md#summaries) section lists. The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../../explanations/transpilation.md#summaries-and-computed-expressions) describes.
* [`sort`](../operators/sort.md) by fields.
* [`head`](../operators/head.md) as `TOP`, and [`top`](../operators/top.md) or [`rare`](../operators/rare.md) followed by [`head`](../operators/head.md).

For example, SQL Server runs every step of

```tql
from_microsoft_sql table="dbo.alerts", host="db.example.com", database="soc"
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events
head 20
```

and returns at most 20 groups. The operator nests derived tables where SQL’s clause order requires it, and keeps the order of a [`sort`](../operators/sort.md) across them where a `TOP` decides which rows a derived table keeps.

## Summaries

SQL Server computes these aggregation functions of a [`summarize`](../operators/summarize.md), with counts as `bigint`:

🟢 runs in SQL Server, 🟡 runs in SQL Server conditionally or approximately, and ⚪ runs in Tenzir.

| TQL                   | Status | SQL Server                          | Notes                                                                      |
| --------------------- | ------ | ----------------------------------- | -------------------------------------------------------------------------- |
| `count()`             | 🟢     | `COUNT_BIG(*)`                      |                                                                            |
| `count(x)`            | 🟢     | `COUNT_BIG(x)`                      |                                                                            |
| `min(x)`              | 🟢     | `MIN(x)`                            | Also takes text                                                            |
| `max(x)`              | 🟢     | `MAX(x)`                            | Also takes text                                                            |
| `count_if(x, v => p)` | 🟢     | `COUNT_BIG(CASE WHEN p THEN x END)` | Skips `null` values                                                        |
| `count_distinct(x)`   | 🟢     | `COUNT_BIG(DISTINCT x)`             |                                                                            |
| `sum(x)`              | 🟢     | `SUM(x)`                            |                                                                            |
| `mean(x)`             | 🟢     | `AVG(CAST(x AS float))`             | Casts first, since `AVG` truncates integers                                |
| `stddev(x)`           | 🟢     | `STDEVP(x)`                         |                                                                            |
| `variance(x)`         | 🟢     | `VARP(x)`                           |                                                                            |
| `all(x)`              | 🟢     | `MIN(CAST(x AS int))`               | Decoded as a boolean; skips `null` values and yields `null` without values |
| `any(x)`              | 🟢     | `MAX(CAST(x AS int))`               | Decoded as a boolean; skips `null` values and yields `null` without values |

For example, the pipeline

```tql
from_microsoft_sql table="events",
                   host="db",
                   user="u",
                   password=secret("p"),
                   database="d"
summarize big=count_if(n, v => v > 0),
          kinds=count_distinct(n),
          total=sum(id),
          avg=mean(id)
```

computes the aggregations as:

```sql
SELECT
  COUNT_BIG(CASE WHEN (([n] IS NOT NULL) AND ([n] > 0)) THEN [n] END),
  COUNT_BIG(DISTINCT [n]),
  SUM([id]),
  AVG(CAST([id] AS float))
FROM [events]
```

Group keys and aggregate arguments can be computed values, such as `level` in

```tql
level = severity * 2
summarize src_ip, worst=max(level)
```

SQL Server computes an assignment that the summary reads with its own semantics, including calls of the functions that the [filters and functions](microsoft-sql.md#filters-and-functions) section lists. An assignment that the summary doesn’t read must be infallible, as the rules for [computed keys and arguments](../../explanations/transpilation.md#summaries-and-computed-expressions) explain.

A time bucket, such as `day = floor(ts, 1d)` before a `summarize day, rows=count()`, runs in SQL Server for these widths:

| Width                                  | Status | SQL Server                                                                                                                                         |
| -------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Whole seconds, such as `1h`            | 🟡     | Runs as `DATE_BUCKET(second, w, x, CAST('1970-01-01' AS datetime2(7)))`. Needs SQL Server 2022 or later; use `pushdown=false` with earlier servers |
| Fractions of a second, such as `250ms` | ⚪      | Runs in Tenzir                                                                                                                                     |
| Multiples of a week or a month         | ⚪      | Runs in Tenzir, since TQL aligns them to the calendar                                                                                              |

## Filters and functions

SQL Server takes over a [`where`](../operators/where.md) whose predicate consists of:

* Top-level fields.
* Literals: numbers, strings, booleans, `null`, times with at most 100 nanosecond precision, and IP addresses.
* Comparisons, `in` with a list of literals, arithmetic with `+`, `-`, `*`, and `/`, and the boolean operators `and`, `or`, and `not`.
* The functions marked 🟢 or 🟡 in the following table.

| Kind    | TQL                       | Status | SQL Server                                                   | Notes                                                                                                    |
| ------- | ------------------------- | ------ | ------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Strings | `x.starts_with(y)`        | 🟢     | `LEFT(x, LEN(CAST(y AS nvarchar(max)) + N'.') - 1) = y`      | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.ends_with(y)`          | 🟢     | `RIGHT(x, LEN(CAST(y AS nvarchar(max)) + N'.') - 1) = y`     | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.match_regex(y)`        | ⚪      | —                                                            |                                                                                                          |
| Strings | `x.length_bytes()`        | 🟢     | `DATALENGTH(x)`                                              | Returns storage byte length (UTF-16 bytes for `nvarchar`, code page bytes for `varchar`)                 |
| Strings | `x.length_chars()`        | 🟢     | `LEN(CAST(x AS nvarchar(max)) + N'.') - 1`                   | Counts trailing spaces, which `LEN` alone leaves out                                                     |
| Strings | `x.to_lower()`            | 🟢     | `LOWER(x)`                                                   |                                                                                                          |
| Strings | `x.to_upper()`            | 🟢     | `UPPER(x)`                                                   |                                                                                                          |
| Strings | `x.capitalize()`          | 🟢     | `UPPER(LEFT(x, 1)) + LOWER(SUBSTRING(x, 2, 2147483647))`     |                                                                                                          |
| Strings | `x.trim()`                | 🟢     | `LTRIM(RTRIM(x))`                                            |                                                                                                          |
| Strings | `x.trim_start()`          | 🟢     | `LTRIM(x)`                                                   |                                                                                                          |
| Strings | `x.trim_end()`            | 🟢     | `RTRIM(x)`                                                   |                                                                                                          |
| Strings | `x.replace(y, z)`         | 🟢     | `REPLACE(CAST(x AS nvarchar(max)), y, z)`                    |                                                                                                          |
| Strings | `x.is_empty()`            | 🟢     | `DATALENGTH(x) = 0`                                          | As a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`) |
| Strings | `x.slice(begin=b, end=e)` | 🟡     | `SUBSTRING(x, b + 1, CASE WHEN e > b THEN e - b ELSE 0 END)` | With constant `begin` and `end` that are not negative                                                    |
| Hashes  | `x.hash_md5()`            | 🟢     | `LOWER(CONVERT(varchar(32), HASHBYTES('MD5', x), 2))`        | Hashes the column's native byte encoding (UTF-16 for `nvarchar`, database code page for `varchar`)       |
| Hashes  | `x.hash_sha1()`           | 🟢     | `LOWER(CONVERT(varchar(40), HASHBYTES('SHA1', x), 2))`       | Hashes the column's native byte encoding (UTF-16 for `nvarchar`, database code page for `varchar`)       |
| Hashes  | `x.hash_sha256()`         | 🟢     | `LOWER(CONVERT(varchar(64), HASHBYTES('SHA2_256', x), 2))`   | Hashes the column's native byte encoding (UTF-16 for `nvarchar`, database code page for `varchar`)       |
| Numbers | `x.abs()`                 | 🟢     | `ABS(x)`                                                     |                                                                                                          |
| Numbers | `x.ceil()`                | 🟢     | `CAST(CEILING(x) AS bigint)`                                 |                                                                                                          |
| Numbers | `x.floor()`               | 🟢     | `CAST(FLOOR(x) AS bigint)`                                   |                                                                                                          |
| Numbers | `x.round()`               | 🟢     | `CAST(ROUND(x, 0) AS bigint)`                                |                                                                                                          |
| Numbers | `x.sqrt()`                | 🟢     | `SQRT(x)`                                                    | Fails the query for negative inputs                                                                      |
| Numbers | `x.exp()`                 | 🟢     | `EXP(x)`                                                     |                                                                                                          |
| Numbers | `x.log()`, `x.log(base)`  | 🟢     | `LOG(x)`, `LOG(x, base)`                                     | Fails the query for zero or negative inputs                                                              |
| Times   | `x.year()`                | 🟢     | `DATEPART(year, x)`                                          |                                                                                                          |
| Times   | `x.month()`               | 🟢     | `DATEPART(month, x)`                                         |                                                                                                          |
| Times   | `x.day()`                 | 🟢     | `DATEPART(day, x)`                                           |                                                                                                          |
| Times   | `x.hour()`                | 🟢     | `DATEPART(hour, x)`                                          |                                                                                                          |
| Times   | `x.minute()`              | 🟢     | `DATEPART(minute, x)`                                        |                                                                                                          |
| Times   | `x.second()`              | 🟢     | `DATEPART(second, x) + DATEPART(nanosecond, x) / 1e9`        |                                                                                                          |
| Times   | `x.since_epoch()`         | ⚪      | —                                                            | SQL Server has no durations                                                                              |

The same functions compute group keys and aggregate arguments. Predicates used as values are wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded back as booleans (`null` predicates become `false`).

T-SQL has no boolean values, so a bare `bit` column is no predicate: `where flag` runs in Tenzir, while `where flag == true` compares with `1`. Other functions, including `match_regex`, named arguments such as `ignore_case`, nested fields, subnets, durations, other kinds of literals, strings with a NUL byte, arithmetic with a time literal such as `ts - 2024-01-01`, and optional fields such as `x?` run in Tenzir.

## SQL Server semantics

The operators that SQL Server takes over run as SQL Server runs them, which can differ from TQL:

* Comparisons with `NULL` yield `NULL`, so `name != "alpha"` does not keep rows where `name` is `NULL`.
* Text compares, groups, and sorts under the collation of its column. The default collations ignore case and trailing spaces, so `name == "alice"` matches `Alice`, and `a`, `A`, and `a `form one group. In turn, SQL Server can use its indexes for such comparisons.
* SQL Server sorts `NULL` first in ascending order, and returns groups that tie in a sort in any order.
* SQL Server compares the stored value of a column, such as the exact value of a `decimal` or `money`, which Tenzir reads as a `double`, and computes arithmetic in the types of its operands.
* A time becomes a `datetimeoffset(7)` in UTC, such as `CAST('2024-01-01T00:00:00.0000000+00:00' AS datetimeoffset(7))`, which SQL Server compares with `date`, `datetime`, `smalldatetime`, `datetime2`, and `datetimeoffset` columns as an instant, reading the types without an offset as UTC.
* An IP address becomes its text, such as `N'10.0.0.1'`, which compares as text.
* The operator takes over operators before it knows the types of the columns, so a query that SQL Server rejects fails the pipeline: for example, a stage that reads a column that the table lacks, where Tenzir would warn and read `null`, `max` of a `bit` column, a comparison, count, group, or sort of a legacy `text`, `ntext`, or `image` column, or a time bucket on a server earlier than SQL Server 2022. The error carries the note and the hint that our explanation of [plan-time diagnostics](../../explanations/transpilation.md#plan-time-decisions-and-diagnostics) describes, and `pushdown=false` runs such pipelines in Tenzir.
