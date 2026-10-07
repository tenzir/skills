---
title: "Overview"
canonical: https://tenzir.com/docs/reference/optimizations
source: https://tenzir.com/docs/reference/optimizations.md
section: "Docs"
---

# Overview

> Tenzir runs part of a pipeline where the data lives. When a pipeline reads from a database or a file and then filters events, selects fields, or keeps only the first few, the source can often do that work itself: it skips the rows and columns that the rest of the pipeline would discard, instead of reading everything and throwing most of it away. You write the pipeline as usual, and Tenzir applies these optimizations automatically, without changing the result.

Tenzir runs part of a pipeline where the data lives. When a pipeline reads from a database or a file and then filters events, selects fields, or keeps only the first few, the source can often do that work itself: it skips the rows and columns that the rest of the pipeline would discard, instead of reading everything and throwing most of it away. You write the pipeline as usual, and Tenzir applies these optimizations automatically, without changing the result.

For example, take this pipeline:

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
where severity >= 3
select id, message
head 10
```

Instead of fetching the whole `alerts` table, [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md) sends a query that returns only the ten rows and the columns that the pipeline needs:

```sql
SELECT `id`, `message`, `severity` FROM `alerts` WHERE `severity` >= 3 LIMIT 10
```

This reference explains how such optimizations come about, what they promise about results, which operators apply them, and, for each database, which filters it evaluates.

## How it works

Before a pipeline runs, Tenzir’s [optimizer](../explanations/pipeline.md#optimization) walks it from the last operator to the first and tells each operator what the operators after it will do. We call this information **hints**, and there are three kinds:

* **Filters**: the predicates of the [`where`](https://tenzir.com/docs/reference/operators/where.md) operators.
* **Projections**: the fields that [`select`](https://tenzir.com/docs/reference/operators/select.md) keeps.
* **Limits**: the number of events that [`head`](https://tenzir.com/docs/reference/operators/head.md) keeps.

An operator that understands a hint acts on it, for example by turning a filter into a `WHERE` clause. The [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators stay in the pipeline regardless and run on what the operator produces, so an operator that acts on a hint only partially, or not at all, still produces the same result.

## Results stay the same

An optimization never changes the result of a pipeline, with three deliberate exceptions that let common filters reach a database:

* **Case-insensitive matching.** `starts_with` and `ends_with` with `ignore_case=true` use the database’s lowercase mapping. It agrees with TQL’s case folding for ASCII and most other text, but TQL folds `ß` to `ss`, so `"Straße".starts_with("strass", ignore_case=true)` is `true` in TQL and matches no row in the database.
* **Regular expressions.** `match_regex` uses the database’s release of RE2, which may disagree with TQL’s on rarely used syntax and on text that is not valid UTF-8.
* **IP addresses in string columns.** In TQL, comparing a string with an `ip` value is a type mismatch that yields `null`. When a database source compares a text column with an address, as in `src == 1.1.1.1`, it compares the canonical text of the address, `1.1.1.1`, instead, so that the common way of storing addresses as text works.

The [database pages](optimizations.md#filters-by-database) state which databases use these exceptions. Everything else the database cannot evaluate exactly like TQL runs in Tenzir, including when it would merely differ for `null` values, `NaN`, or text that differs only in case, accents, or trailing spaces.

## Operators that optimize

These operators act on hints:

| Operator                                                                                                  | Filters                      | Projections             | Limits            |
| --------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------------- | ----------------- |
| [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md)                       | In the query                 | Including tuple fields  | In the query      |
| [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md)                               | In the query                 | Top-level columns       | In the query      |
| [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md)                 | In the query                 | Top-level columns       | In the query      |
| [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md)                                 | In the query                 | Top-level columns       | In the query      |
| [`from_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md) | As prefilters in the query   | Including nested fields | Without filters   |
| [`read_parquet`](https://tenzir.com/docs/reference/operators/read_parquet.md)                             | While decoding, by row group | Including record fields | Stops decoding    |
| [`subscribe`](https://tenzir.com/docs/reference/operators/subscribe.md)                                   | At the node                  | No                      | No                |
| [`sort`](https://tenzir.com/docs/reference/operators/sort.md)                                             | Moved before the sort        | Passed on               | Keeps the top `N` |

The reference page of each operator describes the details.

## Database sources

The database sources [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md), [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md), [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md), and [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md) read in one of two modes, and only one of them optimizes:

* In **table mode**, you name a table, as in `from_mysql table="alerts"`. The operator writes the query itself, so it can add the work of the operators that follow it.
* In **SQL mode**, you write the query, as in `from_mysql sql="SELECT …"`. The operator sends it exactly as written, and Tenzir applies the rest of the pipeline to its result. To have the database filter, write the filter into your query.

In table mode, these rules hold for every database:

* **Filters** become a `WHERE` clause. A predicate is split along its `and`s: each part that the database evaluates exactly like Tenzir goes into the query, and the other parts run in Tenzir. An `or` or `not` goes into the query only if all of its operands do. For example, `where (severity > 3 or msg.to_upper() == "X") and source == "fw"` sends `WHERE source = 'fw'` and evaluates the rest in Tenzir.
* **Limits** go into the query only if every predicate before the [`head`](https://tenzir.com/docs/reference/operators/head.md) did, since the database cannot count rows that Tenzir has yet to filter. Otherwise, the operator enforces the limit itself.
* **Projections** narrow the selected columns to those that the pipeline reads, including columns that only a predicate running in Tenzir needs. Fields that the table does not have are left to [`select`](https://tenzir.com/docs/reference/operators/select.md), which fills them with `null`.
* **Live mode**, which polls a table for new rows, carries the `WHERE` clause and the narrowed columns into every poll, but never a limit, since the limit counts events across polls. The operator plans each poll anew, so that columns added to the table while the pipeline runs take part in later polls.

## SentinelOne

[`from_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md) optimizes only when you omit `query`, and it differs from the database sources in two ways:

* **Filters are prefilters.** PowerQuery coerces types and compares values differently from TQL, so a pushed filter may let extra events through. Tenzir therefore evaluates every original predicate as well, including those that the operator sent.
* **Projections are required.** SentinelOne returns only `timestamp` and `message` by default, so the operator requests the fields that the filters and the rest of the pipeline read.

Generated TQL reads handle PQ’s 1,000-row cap transparently: a capped response is discarded before emission and retried through paginated LOG queries, unless an unfiltered pushed `head` intentionally requested no more than the cap. Explicit native `query` requests retain capped-result semantics. Our [SentinelOne optimization reference](optimizations/sentinelone.md#limits-and-the-result-cap) explains the fallback and continuation behavior.

## Filters by database

Which filters go into the query depends on how each database compares values:

| Predicate                                | ClickHouse  | DuckDB      | MySQL       | SQL Server  |
| ---------------------------------------- | ----------- | ----------- | ----------- | ----------- |
| Comparisons of integers up to 64 bits    | Yes         | Yes         | Yes         | Yes         |
| Comparisons of floating-point numbers    | Yes         | Yes         | Partly      | Yes         |
| Comparisons of decimals                  | No          | No          | No          | No          |
| Comparisons of strings                   | Yes         | Yes         | Partly      | Partly      |
| Comparisons of `time` values             | Yes         | Yes         | No          | Partly      |
| Comparisons of `ip` values               | Yes         | No          | No          | No          |
| Comparisons of booleans                  | Equality    | Equality    | No          | Equality    |
| `== null` and `!= null`                  | Yes         | Yes         | Yes         | Yes         |
| `in` with a list                         | Yes         | Yes         | Yes         | Yes         |
| `in` with a subnet                       | Yes         | No          | No          | No          |
| Comparisons between two columns          | Yes         | Yes         | Yes         | Yes         |
| Nested fields                            | Yes         | Yes         | No          | No          |
| String functions                         | Yes         | Yes         | Yes         | Yes         |
| String functions with `ignore_case=true` | Approximate | Approximate | Approximate | No          |
| `match_regex`                            | Approximate | Approximate | No          | No          |
| Arithmetic that cannot overflow          | Yes         | Yes         | No          | Yes         |
| `ip` literals against text columns       | Approximate | Approximate | Approximate | Approximate |

String functions are `starts_with`, `ends_with`, `length_bytes`, and substring search with `"needle" in haystack`. *Partly* means that some column types of that kind stay in Tenzir, because the database compares a different value than the one Tenzir reads. The page of each database lists its column types:

* [ClickHouse](optimizations/clickhouse.md)
* [DuckDB](optimizations/duckdb.md)
* [MySQL](optimizations/mysql.md)
* [Microsoft SQL Server](optimizations/microsoft-sql.md)

## Verify an optimization

To see which hints an operator received, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_mysql table="logins" | where user == "admin" | head 10'
```

The operator shows the accepted predicates as `filter`, the limit as `limit`, and the projection as `projection`, and the [`where`](https://tenzir.com/docs/reference/operators/where.md) that it took over no longer appears. The [compilation output guide](../guides/troubleshooting/inspect-compilation-output.md) explains the format. To see the query that a database source sends, look it up in the database’s own query log.
