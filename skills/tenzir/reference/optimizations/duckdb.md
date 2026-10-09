---
title: "DuckDB"
canonical: https://tenzir.com/docs/reference/optimizations/duckdb
source: https://tenzir.com/docs/reference/optimizations/duckdb.md
section: "Docs"
---

# DuckDB

> When fromduckdb reads a table, it lets DuckDB filter the rows, pick the columns, and stop after enough rows, so that DuckDB reads and returns only what the pipeline needs instead of the whole table. This page describes when that happens, which filters DuckDB evaluates, and why the others stay in Tenzir. The optimizations overview explains how Tenzir optimizes pipelines in general and compares the databases.

When [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) reads a table, it lets DuckDB filter the rows, pick the columns, and stop after enough rows, so that DuckDB reads and returns only what the pipeline needs instead of the whole table. This page describes when that happens, which filters DuckDB evaluates, and why the others stay in Tenzir. The [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general and compares the databases.

## When it applies

The operator reads in one of these modes, and only table mode optimizes:

* **Table mode** reads a table that you name with `table`, as in `from_duckdb "events.duckdb", table="alerts"`. The operator writes the query itself and adds the work of the operators that follow it. The rest of this page describes this mode.
* **SQL mode** sends the query that you write with `sql` exactly as written, and Tenzir applies the rest of the pipeline to its result. To have DuckDB filter, write the filter into your query.
* **Live mode**, with `live=true`, polls a table for new rows. Every poll carries the filters and the columns of table mode, but not the limit, since the limit counts rows across polls.

## How the query changes

The operator turns the operators that follow it into parts of its `SELECT`:

* [`where`](https://tenzir.com/docs/reference/operators/where.md) becomes a `WHERE` clause, as far as DuckDB evaluates the filter exactly like Tenzir.
* [`select`](https://tenzir.com/docs/reference/operators/select.md) narrows the selected columns to the top-level columns that the pipeline reads.
* [`head`](https://tenzir.com/docs/reference/operators/head.md) becomes a `LIMIT`, if every filter before it went into the query.

For example, the pipeline

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3 and rule.starts_with("ET ")
select id, message
head 100
```

sends a query equivalent to

```sql
SELECT "id", "message", "severity", "rule"
FROM "alerts"
WHERE "severity" >= 3 AND starts_with("rule", 'ET ')
LIMIT 100
```

The [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators still run in Tenzir on the rows that DuckDB returns, so the result is the same whether DuckDB evaluated a filter or not.

## Aggregation input columns

With final summary output, [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) also narrows the input columns. A dependency on `meta.level` retains the whole top-level `meta` column. The [aggregation projection rules](../optimizations.md#aggregation-input-projections) apply to [`top`](https://tenzir.com/docs/reference/operators/top.md) and [`rare`](https://tenzir.com/docs/reference/operators/rare.md) as well. Aggregation still runs in Tenzir, not in a SQL `GROUP BY`; a [`head`](https://tenzir.com/docs/reference/operators/head.md) after it does not add an input `LIMIT`. Explicit `sql` queries remain unchanged.

## Filters that DuckDB evaluates

The operator puts a filter into the query only if DuckDB evaluates it exactly like Tenzir. These filters qualify:

* Comparisons of a column with a literal of matching kind: numbers against integer, `FLOAT`, and `DOUBLE` columns, strings against `VARCHAR` columns, and `time` values against `DATE`, `TIMESTAMP`, `TIMESTAMP_S`, `TIMESTAMP_MS`, `TIMESTAMP_NS`, and `TIMESTAMP WITH TIME ZONE` columns. Booleans compare for equality only.
* Null checks with `== null` and `!= null`.
* Membership tests with `in` and a list of such literals.
* Comparisons between two columns of the same kind. Temporal columns must share their exact type.
* Fields of `STRUCT` columns, such as `meta.level`, with the same rules as columns.
* The string functions `starts_with`, `ends_with`, and `length_bytes`, and substring search with `"needle" in haystack`. With `ignore_case=true`, `starts_with` and `ends_with` translate approximately, and so does `match_regex`, as [Approximate matching](duckdb.md#approximate-matching) explains.
* Arithmetic that cannot overflow: `+`, `-`, and `*` on integer columns of at most 32 bits with a literal whose magnitude is below 2^31, and any `+`, `-`, `*`, or `/` that yields a floating-point number, except division by zero.
* Expressions that consist of literals only, such as `2024-01-01 + 1d`, which are computed ahead of time.
* The boolean operators `and`, `or`, and `not`.
* Bare boolean columns.

Where DuckDB’s own semantics differ from TQL, the query spells out TQL’s:

* DuckDB considers `NaN` equal to itself and greater than every other number. A comparison of a floating-point value carries a guard that makes `NaN` compare as in TQL: `x > 1.5` becomes `x > 1.5e0 AND NOT isnan(x)`. Numbers are spelled as `DOUBLE` literals, so that DuckDB widens a `FLOAT` column to `DOUBLE` like TQL does, instead of comparing in single precision.
* DuckDB computes arithmetic in the types of its operands, so that it can overflow or lose precision where TQL does not. The query widens the column first: `n + 1 > 5` becomes `CAST(n AS BIGINT) + 1 > 5`, and `n * 0.5 > 5` computes in `DOUBLE`.
* DuckDB reads `meta.level` as the column `level` of a table `meta` if there is one. A field therefore goes into the query as `struct_extract(meta, 'level')`.
* A `VARCHAR` column with a collation, such as `COLLATE NOCASE`, compares text without regard to case, and so does every `VARCHAR` column when the database sets a `default_collation`. Such a column goes into the query with the binary collation, which compares bytes like TQL: `name == "a"` becomes `name COLLATE "binary" = 'a'`. DuckDB still skips row groups by their minimum and maximum values for such a comparison.

Literals take the column’s own type, so a comparison never depends on the session time zone. Values that Tenzir cannot represent, such as `infinity` or a `DATE` past the year 2262, compare as `null` in both places. An `ip` literal that is compared for equality with a `VARCHAR` column, or listed in an `in` test against one, becomes its canonical text, as with the [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md) operator. The predicate `src == 1.1.1.1` then matches rows whose `src` reads `1.1.1.1`.

## Approximate matching

Two kinds of predicates translate approximately. This is a deliberate exception to identical results, made so that common filters reach the database.

A predicate such as `msg.starts_with("error", ignore_case=true)` goes into the query as `starts_with(lower(msg), lower('error'))`. DuckDB lowercases one character at a time, which agrees with TQL for ASCII and most other text. TQL applies full Unicode case folding instead, which differs for a few characters: it folds `ß` to `ss`, so `"Straße".starts_with("strass", ignore_case=true)` is `true` in TQL but matches no row in DuckDB.

A predicate such as `msg.match_regex("^ERROR [0-9]+")` goes into the query as `regexp_matches(msg, '^ERROR [0-9]+')`. Both TQL and DuckDB use the RE2 library with the same options: the pattern matches anywhere in the string, `.` does not match a newline, and `^` and `$` match only at the start and end of the string. DuckDB bundles its own release of RE2, which may disagree with TQL’s on rarely used syntax.

## Filters that stay in Tenzir

Everything else runs in Tenzir, with the same result. This includes:

* Columns that arrive as strings, such as `DECIMAL`, `UUID`, `ENUM`, and `UNION` columns (see [Types](../operators/from_duckdb.md#types)), and `BLOB`, `INTERVAL`, `LIST`, `ARRAY`, and `MAP` columns, including the values nested in them.
* Arithmetic on 64-bit integer columns or between two columns.
* Subnet membership tests on `VARCHAR` columns, such as `src in 10.0.0.0/8`.
* Strings that contain NUL bytes, and all other functions.
