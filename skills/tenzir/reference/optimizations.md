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

Before a pipeline runs, Tenzir’s [optimizer](../explanations/pipeline.md#optimization) walks it from the last operator to the first and tells each operator what the operators after it will do. We call this information **hints**, and there are four kinds:

* **Filters**: the predicates of the [`where`](https://tenzir.com/docs/reference/operators/where.md) operators.
* **Projections**: the fields that downstream operators need, such as the fields that [`select`](https://tenzir.com/docs/reference/operators/select.md) keeps or a final [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) reads.
* **Limits**: the number of events that [`head`](https://tenzir.com/docs/reference/operators/head.md) keeps.
* **Aggregations**: the groups and aggregation functions of a final [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) that directly follows the operator. Unlike the other hints, the optimizer offers an aggregation only after the walk, once it knows which filters and limits the operator took over.

An operator that understands a hint acts on it, for example by turning a filter into a `WHERE` clause. The [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators stay in the pipeline and run on what the operator produces, so an operator that acts on a hint only partially, or not at all, still produces the same result. The exception is a source that [computes an aggregation](optimizations.md#aggregations-in-the-source), which takes over the [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) and the filters before it, and which can also take over the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`sort`](https://tenzir.com/docs/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) that follow the summary and then runs them with the database’s semantics.

## Results stay the same

An optimization never changes the result of a pipeline, with a few deliberate exceptions that let common filters reach a database or Splunk:

* **Case-insensitive matching.** `starts_with` and `ends_with` with `ignore_case=true` use the database’s lowercase mapping. It agrees with TQL’s case folding for ASCII and most other text, but TQL folds `ß` to `ss`, so `"Straße".starts_with("strass", ignore_case=true)` is `true` in TQL and matches no row in the database.
* **Regular expressions.** `match_regex` uses the database’s release of RE2, which may disagree with TQL’s on rarely used syntax and on text that is not valid UTF-8.
* **IP addresses in string columns.** In TQL, a string never equals an `ip` value, so the comparison is `false`. When a database source compares a text column with an address, as in `src == 1.1.1.1`, it compares the canonical text of the address, `1.1.1.1`, instead, so that the common way of storing addresses as text works.
* **Remote sources.** [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md), [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md), [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md), [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md), [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md), [`from_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md), [`from_microsoft_defender`](https://tenzir.com/docs/reference/operators/from_microsoft_defender.md), and [`from_azure_log_analytics`](https://tenzir.com/docs/reference/operators/from_azure_log_analytics.md) hand the database the operators that follow them, which then run with the database’s semantics instead of TQL’s, unless you set `pushdown=false`. Our [ClickHouse](optimizations/clickhouse.md), [DuckDB](optimizations/duckdb.md), [MySQL](optimizations/mysql.md), [SQL Server](optimizations/microsoft-sql.md), [SPL](optimizations/spl.md), [SentinelOne](optimizations/sentinelone.md), and [KQL](optimizations/kql.md) pages describe the differences.

The [database pages](optimizations.md#filters-by-database) state which databases use these exceptions. Everything else the database cannot evaluate exactly like TQL runs in Tenzir, including when it would merely differ for `null` values, `NaN`, or text that differs only in case, accents, or trailing spaces.

## Operators that optimize

These operators act on hints:

| Operator                                                                                                  | Filters                      | Projections                | Limits                 | Aggregations          |
| --------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------- | ---------------------- | --------------------- |
| [`from_azure_log_analytics`](https://tenzir.com/docs/reference/operators/from_azure_log_analytics.md)     | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md)                       | Taken over                   | Including tuple fields     | Taken over             | Taken over            |
| [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md)                               | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_microsoft_defender`](https://tenzir.com/docs/reference/operators/from_microsoft_defender.md)       | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_microsoft_graph`](https://tenzir.com/docs/reference/operators/from_microsoft_graph.md)             | While paging                 | Default `users` properties | Stops paging           | No                    |
| [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md)                 | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md)                                 | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md) | Taken over                   | Including nested fields    | Taken over             | Taken over            |
| [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md)                               | Taken over                   | Top-level fields           | Taken over             | Taken over            |
| [`read_parquet`](https://tenzir.com/docs/reference/operators/read_parquet.md)                             | While decoding, by row group | Including record fields    | Stops decoding         | No                    |
| [`subscribe`](https://tenzir.com/docs/reference/operators/subscribe.md)                                   | At the node                  | No                         | No                     | No                    |
| [`sort`](https://tenzir.com/docs/reference/operators/sort.md)                                             | Moved before the sort        | Passed on                  | Keeps the top `N`      | No                    |
| [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) (final summary)                   | Kept after aggregation       | Group and aggregate inputs | Kept after aggregation | Offered to the source |

The reference page of each operator describes the details.

## Aggregation input projections

With final summary output, [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) supplies its own projection hint. You do not need an explicit [`select`](https://tenzir.com/docs/reference/operators/select.md) before aggregation:

```tql
from_mysql table="events", host="db.example.com", database="soc"
summarize host, events=count(), bytes=sum(bytes)
head 10
```

The source can read only `host` and `bytes`. For this table, the generated query is equivalent to:

```sql
SELECT `host`, `bytes` FROM `events`
```

This source does not compute the aggregation, so this is input projection, not remote aggregation. The query has no `GROUP BY`, `COUNT`, `SUM`, or `LIMIT`. Tenzir groups and aggregates the complete input, then keeps at most ten summary rows. Filters after `summarize` also stay after aggregation; filters before it can still reach the source. Some sources go further and [compute the aggregation](optimizations.md#aggregations-in-the-source).

These rules preserve the aggregation’s inputs and behavior:

* All grouping keys remain required, even if a later selection drops them.
* All aggregate arguments remain required, even if their results are unused, because evaluating them can produce diagnostics.
* Output aliases are not input dependencies. In the example, `events` does not request a source column.
* A keyless `summarize events=count()` needs the row count but no field values. A source may still read a column or emit a placeholder per row to preserve that count. Unless the source [computes the aggregation](optimizations.md#aggregations-in-the-source), it does not replace the pipeline with a remote `COUNT(*)`.
* Whole-event access, such as `collect(this)`, and dynamic field access, such as `sum(this[key])`, prevent narrowing.
* Options must be resolved before `summarize` supplies a projection. Inside runtime-bound subpipelines, such as [`group`](https://tenzir.com/docs/reference/operators/group.md) and [`window`](https://tenzir.com/docs/reference/operators/window.md), an unresolved `summarize` does not narrow the enclosing source.
* Input ordering requirements remain intact for order-sensitive aggregates. Trigger output, event output, and periodic summaries retain their barriers.

The [`top`](https://tenzir.com/docs/reference/operators/top.md) and [`rare`](https://tenzir.com/docs/reference/operators/rare.md) operators compile into `summarize` and [`sort`](https://tenzir.com/docs/reference/operators/sort.md), so they benefit from the same input projection. A following [`head`](https://tenzir.com/docs/reference/operators/head.md) still limits groups, not raw input events. Source-specific column rules and fields required by earlier operators still apply.

## Aggregations in the source

A source that reads from a database can compute a final summary itself, so that the database returns one row per group instead of every matching row. This happens only if the source reads a table once, in [table mode](optimizations.md#database-sources) and without `live=true`, if [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) follows the source, after every filter before it went into the query, and if the summary groups by fields and aggregates fields with functions that the database computes exactly like Tenzir. A query that you write with `sql` is sent as written, and a live read never ends, so the summary of either runs in Tenzir. The `summarize` and the filters before it then disappear from the pipeline, the database returns only the group and aggregate fields, and the operators after the summary run on it as usual.

A source that computes the summary also takes over the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`sort`](https://tenzir.com/docs/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) that directly follow it, so that the database returns only the groups that the pipeline keeps:

```tql
from_clickhouse table="events", host="clickhouse.example.com", tls=false
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events, src_ip
head 20
```

The filter applies to the groups after grouping, and the limit counts groups. A [`top`](https://tenzir.com/docs/reference/operators/top.md) or [`rare`](https://tenzir.com/docs/reference/operators/rare.md) followed by [`head`](https://tenzir.com/docs/reference/operators/head.md) runs in the database. These operators leave the pipeline, and the database runs them with its own semantics:

* Text compares and sorts under the collation of its column.
* The database decides where `null` sorts. MySQL and SQL Server sort it first in ascending order, DuckDB and ClickHouse last.
* Groups that tie in a sort arrive in the order in which the database returns them.

Some steps still run in Tenzir, together with everything after them:

* A [`where`](https://tenzir.com/docs/reference/operators/where.md) with function calls, or with constants other than numbers, strings, booleans, and `null`, such as times and IP addresses. Tenzir splits a [`where`](https://tenzir.com/docs/reference/operators/where.md) at `and`, so it can still send the supported conjuncts to the database.
* A [`sort`](https://tenzir.com/docs/reference/operators/sort.md) by fields that the summary does not produce.

Two details depend on the database. SQL Server spells booleans as bits, so a bare `where flag` stays in Tenzir. MySQL keeps strings with backslashes in Tenzir.

The summary can follow the source directly or behind operators that keep every event and only keep, drop, or copy fields:

* [`select`](https://tenzir.com/docs/reference/operators/select.md) and [`drop`](https://tenzir.com/docs/reference/operators/drop.md) that keep the fields that the summary reads.
* Renames and copies with [`select`](https://tenzir.com/docs/reference/operators/select.md), [`set`](https://tenzir.com/docs/reference/operators/set.md), or a plain assignment, such as `select ip=src_ip` or `ip = src_ip`. The source then groups and aggregates the original fields, and the result keeps the new names.

For example, the source computes the summary of

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
select ip=src_ip, ts, severity
where severity >= 3
summarize ip, alerts=count(), last=max(ts)
```

by grouping on the `src_ip` column. Every right-hand side of a [`select`](https://tenzir.com/docs/reference/operators/select.md) or [`set`](https://tenzir.com/docs/reference/operators/set.md) reads the original event, so `select a=b, b=a` swaps the fields, and the summary reads them swapped. Assignments to fields that the summary does not read do not matter, unless they call a function, which could fail the pipeline. A computed value for a field that the summary reads, such as `ip = src_ip.string()`, an assignment of anything but a record literal to `this`, and every other operator, including [`head`](https://tenzir.com/docs/reference/operators/head.md) and a [`where`](https://tenzir.com/docs/reference/operators/where.md) that stays in Tenzir, keep the summary in Tenzir.

If [`from_hydrolix`](https://tenzir.com/docs/reference/operators/from_hydrolix.md) finds out only when it runs that it cannot compute the summary, for example because a column has a type that the database aggregates differently, it reads the rows and runs the operators between the source and the summary and the original `summarize` on them. The result is the same either way, except that Tenzir does not warn about values of rows that it never sees.

[`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md), [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md), [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md), and [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md) compute summaries with group keys, `count`, `min`, and `max`, and the steps after them, which the database runs with its own semantics. They decide from the pipeline alone and never fall back: a summary that the database takes over runs in the database. The pages on [ClickHouse](optimizations/clickhouse.md#operators-that-clickhouse-takes-over), [DuckDB](optimizations/duckdb.md#operators-that-duckdb-takes-over), [MySQL](optimizations/mysql.md#operators-that-mysql-takes-over), and [SQL Server](optimizations/microsoft-sql.md#operators-that-sql-server-takes-over) list the details.

[`from_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md) computes summaries with group keys, `count()`, and `count(x)` in SentinelOne with `group`, and the operators after them, with SentinelOne’s semantics. It decides from the pipeline alone and never falls back. Our [SentinelOne page](optimizations/sentinelone.md#operators-that-sentinelone-takes-over) lists the details.

[`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) computes summaries with group keys, `count()`, `count(field)`, `min`, and `max` in Splunk with `stats`, and the operators after them, with Splunk’s semantics. It decides from the pipeline alone and never falls back. Our [SPL page](optimizations/spl.md#operators-that-splunk-takes-over) lists the details.

[`from_microsoft_defender`](https://tenzir.com/docs/reference/operators/from_microsoft_defender.md) and [`from_azure_log_analytics`](https://tenzir.com/docs/reference/operators/from_azure_log_analytics.md) compute summaries with group keys, `count()`, `count(x)`, `min`, `max`, and `sum` with KQL’s `summarize`, and the operators after them, with KQL’s semantics. They decide from the pipeline alone and never fall back. Our [KQL page](optimizations/kql.md#operators-that-the-service-takes-over) lists the details.

The other sources still aggregate in Tenzir. [`from_hydrolix`](https://tenzir.com/docs/reference/operators/from_hydrolix.md) keeps the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`sort`](https://tenzir.com/docs/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) after a summary in Tenzir.

## Database sources

The database sources [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md), [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md), [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md), and [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md) read in one of two modes, and only one of them optimizes:

* In **table mode**, you name a table, as in `from_mysql table="alerts"`. The operator writes the query itself, so it can add the work of the operators that follow it.
* In **SQL mode**, you write the query, as in `from_mysql sql="SELECT …"`. The operator sends it exactly as written, and Tenzir applies the rest of the pipeline to its result. To have the database filter, write the filter into your query.

In table mode, the operator hands the database the operators that follow it, as our [ClickHouse](optimizations/clickhouse.md), [DuckDB](optimizations/duckdb.md), [MySQL](optimizations/mysql.md), and [SQL Server](optimizations/microsoft-sql.md) pages describe. [`from_hydrolix`](https://tenzir.com/docs/reference/operators/from_hydrolix.md) still sends filters that Tenzir evaluates again, and a limit only if every filter before it went into the query.

## SentinelOne

[`from_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md) reads with a PowerQuery that you write in `query`, or one that Tenzir writes. In both cases, the operator hands SentinelOne the operators that follow it as PowerQuery stages, which run with SentinelOne’s semantics:

* **Filters** become `filter` stages. Reads of whole events with only filters and a final [`head`](https://tenzir.com/docs/reference/operators/head.md) use a LOG query instead, which returns complete events and pages without a cap.
* **Projections** become a `columns` stage, and **summaries** a `group` stage.
* **Sorts and limits** become `sort` and `limit`. A PowerQuery that does not end in a limit ends in `limit 1600000`, since PowerQuery otherwise returns at most 1,000 rows.
* **The time window** narrows from comparisons of `timestamp` when you omit `query`.

Our [SentinelOne optimization reference](optimizations/sentinelone.md) lists the operators that SentinelOne takes over and how its semantics differ.

## KQL sources

[`from_microsoft_defender`](https://tenzir.com/docs/reference/operators/from_microsoft_defender.md) and [`from_azure_log_analytics`](https://tenzir.com/docs/reference/operators/from_azure_log_analytics.md) run a KQL query that you write, and hand the service the operators that follow by appending KQL stages to it, which apply to the table that your query returns and run with KQL’s semantics. Your query text stays as is:

* **Filters** become `where` stages, **projections** `project` and `project-away`, and **summaries, sorts, and limits** `summarize`, `sort`, and `take`.
* **Missing columns and types:** the operator knows neither the columns nor the types of your query’s output before it runs, so a stage that names a column that your query doesn’t return, or that KQL rejects for its type, fails the query with the service’s error.
* **The time window** never narrows, since a time field in your query’s output need not refer to the time that `start` and `end` select.

Our [KQL optimization reference](optimizations/kql.md) lists the operators that the service takes over and the queries that stay unchanged.

## SPL source

[`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) runs a Splunk search. With `search`, you write the search in SPL, and with `index`, Tenzir writes the search for the indexes. In both cases, the operator hands Splunk the operators that follow it by appending SPL stages, which run with Splunk’s semantics:

* **Filters** become `where` stages. With `index`, the filters right after the operator extend the base `search` command where it can spell them, which matches strings without regard to case and lets Splunk use its indexes.
* **Projections** become a `fields` stage. Without one, the operator appends `fields *`, since Splunk otherwise returns only the fields that the search references.
* **Summaries, sorts, and limits** become `stats`, `sort`, and `head`.
* **The time window** narrows with `index` from comparisons of `_time`, when `earliest` and `latest` are absolute.

Our [SPL optimization reference](optimizations/spl.md) lists the operators that Splunk takes over and how its semantics differ.

## Filters by database

Each database takes over the filters that it can spell, and runs them with its own semantics. The pages on [ClickHouse](optimizations/clickhouse.md#filters), [DuckDB](optimizations/duckdb.md#filters), [MySQL](optimizations/mysql.md#filters), and [SQL Server](optimizations/microsoft-sql.md#filters) list them.

## Verify an optimization

To see which hints an operator received, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_mysql table="logins" | where user == "admin" | head 10'
```

The operator shows the accepted predicates as `filter`, the limit as `limit`, the projection as `projection`, and a summary that it computes as `aggregation`, and the [`where`](https://tenzir.com/docs/reference/operators/where.md) or [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) that it took over no longer appears. [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md), [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md), [`from_microsoft_sql`](https://tenzir.com/docs/reference/operators/from_microsoft_sql.md), and [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) list the operators that they took over as `plan`, and the reason why they took over no more as `declined`. The [compilation output guide](../guides/troubleshooting/inspect-compilation-output.md) explains the format. To see the query that a database source sends, look it up in the database’s own query log.
