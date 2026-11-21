---
title: "Overview"
canonical: https://tenzir.com/docs/reference/optimizations
source: https://tenzir.com/docs/reference/optimizations.md
section: "Docs"
---

# Overview

> Tenzir runs part of a pipeline where the data lives. When a pipeline reads from a database, a SIEM, or an API and then filters, selects, summarizes, sorts, or limits events, the source hands those operators to the system that it reads from, its target. The target takes over the operators, runs them with its own semantics, and returns only what the pipeline keeps, instead of everything that the pipeline would discard. The operators that the target does not take over run in Tenzir, with TQL semantics. With pushdown=false, a source hands over nothing, and every operator runs in Tenzir.

Tenzir runs part of a pipeline where the data lives. When a pipeline reads from a database, a SIEM, or an API and then filters, selects, summarizes, sorts, or limits events, the source hands those operators to the system that it reads from, its **target**. The target takes over the operators, runs them with its own semantics, and returns only what the pipeline keeps, instead of everything that the pipeline would discard. The operators that the target does not take over run in Tenzir, with TQL semantics. With `pushdown=false`, a source hands over nothing, and every operator runs in Tenzir.

For example, take this pipeline:

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
where severity >= 3
select id, message
head 10
```

Instead of fetching the whole `alerts` table, MySQL takes over the three operators, and [`from_mysql`](operators/from_mysql.md) sends a query equivalent to:

```sql
SELECT `id`, `message`
FROM `alerts`
WHERE `severity` >= 3
LIMIT 10
```

Our explanation of [pipeline optimization](../explanations/pipeline.md#optimization) describes how the optimizer finds this work, and how sources that act on hints differ from sources whose target takes over operators. This reference lists what each source takes over, compares what the targets compute, and states the rules that all of them share.

## Sources and their pages

Each remote source has a page that describes when its target takes over operators, which ones, and how the target’s semantics differ from TQL’s:

| Target                     | Sources                                                                                                                                                                                                    | Page                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| ClickHouse and Hydrolix    | [`from_clickhouse`](operators/from_clickhouse.md), [`from_hydrolix`](operators/from_hydrolix.md)                                       | [ClickHouse](optimizations/clickhouse.md)           |
| DuckDB                     | [`from_duckdb`](operators/from_duckdb.md)                                                                                                                                | [DuckDB](optimizations/duckdb.md)                   |
| MySQL                      | [`from_mysql`](operators/from_mysql.md)                                                                                                                                  | [MySQL](optimizations/mysql.md)                     |
| Microsoft SQL Server       | [`from_microsoft_sql`](operators/from_microsoft_sql.md)                                                                                                                  | [SQL Server](optimizations/microsoft-sql.md)        |
| Defender and Log Analytics | [`from_microsoft_defender`](operators/from_microsoft_defender.md), [`from_azure_log_analytics`](operators/from_azure_log_analytics.md) | [KQL](optimizations/kql.md)                         |
| Splunk                     | [`from_splunk`](operators/from_splunk.md)                                                                                                                                | [SPL](optimizations/spl.md)                         |
| SentinelOne                | [`from_sentinelone_data_lake`](operators/from_sentinelone_data_lake.md)                                                                                                  | [SentinelOne](optimizations/sentinelone.md)         |
| CloudWatch Logs            | [`from_amazon_cloudwatch`](operators/from_amazon_cloudwatch.md)                                                                                                          | [CloudWatch Logs](optimizations/cloudwatch.md)      |
| Microsoft Graph            | [`from_microsoft_graph`](operators/from_microsoft_graph.md)                                                                                                              | [Microsoft Graph](optimizations/microsoft-graph.md) |

Other sources narrow what they read and keep TQL’s results, as their reference pages describe: [`read_parquet`](operators/read_parquet.md) skips row groups and fields, [`subscribe`](operators/subscribe.md) filters before it queues events, and [`from_microsoft_365_activity`](operators/from_microsoft_365_activity.md) skips blobs by their metadata. [`from_velociraptor`](operators/from_velociraptor.md) hands over nothing, since a VQL query may have effects that a filter or a limit would change.

## Results follow the target’s semantics

The operators that a target takes over leave the pipeline and run as the target runs them. Their results can therefore differ from TQL’s, for example:

* **Filters.** A comparison with `null` yields `null` in SQL, so `name != "alpha"` does not keep rows where `name` is `null`. MySQL and SQL Server compare text without regard to case by default, and so does Splunk’s base `search` command.
* **Sorts.** Text sorts under the collation of its column, the target decides where `null` sorts, and groups that tie arrive in the target’s order.
* **Functions.** The target computes functions with its own arithmetic, case mapping, and regular expressions, as the [functions](optimizations.md#functions) section describes.

The semantics section of each backend page lists the differences. To run every operator with TQL semantics, set `pushdown=false`. The source then still reads only the fields that the pipeline uses.

Sources that only act on hints, such as [`read_parquet`](operators/read_parquet.md), keep TQL’s results: the [`where`](operators/where.md), [`select`](operators/select.md), and [`head`](operators/head.md) stay in the pipeline and run on what the source produces.

## What each source takes over

These operators act on the requests of the operators after them, or take them over:

| Operator                                                                                                    | Filters                      | Projections                | Limits                 | Summaries             |
| ----------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------- | ---------------------- | --------------------- |
| [`from_amazon_cloudwatch`](operators/from_amazon_cloudwatch.md)           | Patterns, times, streams     | No                         | Taken over             | No                    |
| [`from_azure_log_analytics`](operators/from_azure_log_analytics.md)       | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_clickhouse`](operators/from_clickhouse.md)                         | Taken over                   | Including tuple fields     | Taken over             | Taken over            |
| [`from_duckdb`](operators/from_duckdb.md)                                 | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_hydrolix`](operators/from_hydrolix.md)                             | Taken over                   | Including tuple fields     | Taken over             | Taken over            |
| [`from_microsoft_defender`](operators/from_microsoft_defender.md)         | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_microsoft_365_activity`](operators/from_microsoft_365_activity.md) | Skip blobs by metadata       | No                         | Stops downloading      | No                    |
| [`from_microsoft_graph`](operators/from_microsoft_graph.md)               | `$filter` where documented   | Top-level properties       | Stops paging           | No                    |
| [`from_microsoft_sql`](operators/from_microsoft_sql.md)                   | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_mysql`](operators/from_mysql.md)                                   | Taken over                   | Top-level columns          | Taken over             | Taken over            |
| [`from_sentinelone_data_lake`](operators/from_sentinelone_data_lake.md)   | Taken over                   | Including nested fields    | Taken over             | Taken over            |
| [`from_splunk`](operators/from_splunk.md)                                 | Taken over                   | Top-level fields           | Taken over             | Taken over            |
| [`read_parquet`](operators/read_parquet.md)                               | While decoding, by row group | Including record fields    | Stops decoding         | No                    |
| [`subscribe`](operators/subscribe.md)                                     | Before queuing               | Applied on arrival         | With one topic         | No                    |
| [`sort`](operators/sort.md)                                               | Moved before the sort        | Passed on                  | Keeps the top `N`      | No                    |
| [`summarize`](operators/summarize.md) (final summary)                     | Kept after aggregation       | Group and aggregate inputs | Kept after aggregation | Taken over by sources |

## What the targets compute

The targets differ in the aggregation functions, functions, and time buckets that they compute. The following matrices compare them, and each backend page lists the target’s spelling of every function.

### Aggregation functions

A source takes over a [`summarize`](operators/summarize.md) only if its target computes every aggregation function of the summary:

| Aggregation      | [ClickHouse](optimizations/clickhouse.md) | [DuckDB](optimizations/duckdb.md) | [MySQL](optimizations/mysql.md) | [SQL Server](optimizations/microsoft-sql.md) | [KQL](optimizations/kql.md) | [SPL](optimizations/spl.md) | [SentinelOne](optimizations/sentinelone.md) |
| ---------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `count()`        | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `count(x)`       | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `min`            | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `max`            | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `count_if`       | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `count_distinct` | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Not possible                                                                  |
| `sum`            | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `mean`           | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| `stddev`         | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Not yet                                                                       |
| `variance`       | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Not yet                                                                       |
| `all`            | Yes                                                                         | Yes                                                                 | Not possible                                                      | Not possible                                                                   | Yes                                                           | Not possible                                                  | Not yet                                                                       |
| `any`            | Yes                                                                         | Yes                                                                 | Not possible                                                      | Not possible                                                                   | Yes                                                           | Not possible                                                  | Not yet                                                                       |

Yes means that the target computes it, and Partly that it computes it only under conditions or approximately. Not yet means that it runs in Tenzir, and Not possible that the target cannot express it as specified. The notes below the table name the conditions and how the targets differ.

* `count()` (SPL): SPL2 spells it `count()`.
* `count(x)` (KQL): counts empty strings.
* `count(x)` (SPL): counts each value of a multivalue field.
* `count(x)` (SentinelOne): counts the events where `x` has a value.
* `min` and `max` (ClickHouse): yields the type's default without values.
* `min` and `max` (SQL Server): also takes text.
* `min` and `max` (SPL): compares numbers numerically and other values as text.
* `min` (SentinelOne): yields `Infinity` without values.
* `max` (SentinelOne): yields `-Infinity` without values.
* `count_if` (ClickHouse, DuckDB, KQL, and SentinelOne): skips `null` values.
* `count_if` (MySQL and SQL Server): skips `NULL` values.
* `count_if` (SPL): skips events without a value; `count(if(p, 1, null))` in SPL2.
* `count_distinct` (KQL): exact; counts empty strings and fails beyond 100 million values in a group.
* `count_distinct` (SPL): exact, unlike `estdc`.
* `count_distinct` (SentinelOne): powerQuery has no exact distinct count; it runs `estimate_distinct(x)` instead.
* `sum` (DuckDB): widens integers to a `HUGEINT`, which still arrives as an `int`.
* `sum` (MySQL): sums integers as a `DECIMAL`, which still arrives as an `int`.
* `sum`, `stddev`, and `variance` (KQL): yields `0` without values.
* `sum` and `mean` (SentinelOne): yields `0.0` without values.
* `mean` (SQL Server): casts first, since `AVG` truncates integers.
* `mean` (KQL): yields `NaN` without values.
* `stddev` and `variance` (SentinelOne): powerQuery has sample `stddev`, but no population deviation or variance.
* `all` and `any` (ClickHouse and KQL): skips `null` values.
* `all` and `any` (DuckDB): skips `null` values; yields `null` without values.
* `all` and `any` (MySQL, SQL Server, and SPL): the target has no booleans.

A few rules hold for every target:

* **Counting with a predicate.** The `count_if` function counts only the events whose input is not `null`, as TQL does.
* **No values.** Without values, `sum`, `mean`, `stddev`, and `variance` yield `null`, `all` holds, and `any` does not, also where the target would yield 0 or `NaN`.
* **Wide sums.** A sum that the target widens, as DuckDB does to a `HUGEINT` and MySQL to a `DECIMAL`, still arrives as an `int`. A sum beyond 64 bits becomes `null` with a warning, as in TQL.
* **Floating-point results.** The target computes results such as those of `mean` and `stddev` with its own arithmetic, which may differ from TQL’s in the last digits.

### Functions

A target computes these functions in filters, group keys, and aggregate arguments:

| Kind    | Function       | [ClickHouse](optimizations/clickhouse.md) | [DuckDB](optimizations/duckdb.md) | [MySQL](optimizations/mysql.md) | [SQL Server](optimizations/microsoft-sql.md) | [KQL](optimizations/kql.md) | [SPL](optimizations/spl.md) | [SentinelOne](optimizations/sentinelone.md) |
| ------- | -------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Strings | `starts_with`  | Yes                                                                         | Yes                                                                 | Partly                                                            | Partly                                                                         | Yes                                                           | Partly                                                        | Partly                                                                        |
| Strings | `ends_with`    | Yes                                                                         | Yes                                                                 | Partly                                                            | Partly                                                                         | Yes                                                           | Partly                                                        | Partly                                                                        |
| Strings | `match_regex`  | Yes                                                                         | Yes                                                                 | Partly                                                            | Not yet                                                                        | Yes                                                           | Partly                                                        | Not yet                                                                       |
| Strings | `length_bytes` | Yes                                                                         | Yes                                                                 | Yes                                                               | Not yet                                                                        | Not yet                                                       | Not yet                                                       | Not yet                                                                       |
| Strings | `length_chars` | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Strings | `to_lower`     | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Strings | `to_upper`     | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Strings | `capitalize`   | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Not yet                                                                       |
| Strings | `trim`         | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Strings | `trim_start`   | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Strings | `trim_end`     | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Strings | `replace`      | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Not yet                                                                       |
| Strings | `is_empty`     | Yes                                                                         | Yes                                                                 | Partly                                                            | Partly                                                                         | Yes                                                           | Partly                                                        | Partly                                                                        |
| Strings | `slice`        | Partly                                                                      | Partly                                                              | Partly                                                            | Partly                                                                         | Partly                                                        | Not yet                                                       | Partly                                                                        |
| Hashes  | `hash_md5`     | Yes                                                                         | Yes                                                                 | Yes                                                               | Not yet                                                                        | Yes                                                           | Yes                                                           | Not possible                                                                  |
| Hashes  | `hash_sha1`    | Yes                                                                         | Yes                                                                 | Yes                                                               | Not yet                                                                        | Yes                                                           | Yes                                                           | Not possible                                                                  |
| Hashes  | `hash_sha256`  | Yes                                                                         | Yes                                                                 | Yes                                                               | Not yet                                                                        | Yes                                                           | Yes                                                           | Not possible                                                                  |
| Numbers | `abs`          | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Numbers | `ceil`         | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Numbers | `floor`        | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Numbers | `round`        | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Not yet                                                                       |
| Numbers | `sqrt`         | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Numbers | `exp`          | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Numbers | `log`          | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Yes                                                           | Yes                                                                           |
| Times   | `year`         | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Yes                                                                           |
| Times   | `month`        | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Yes                                                                           |
| Times   | `day`          | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Yes                                                                           |
| Times   | `hour`         | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Yes                                                                           |
| Times   | `minute`       | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Yes                                                                           |
| Times   | `second`       | Yes                                                                         | Yes                                                                 | Yes                                                               | Yes                                                                            | Yes                                                           | Not yet                                                       | Not yet                                                                       |
| Times   | `since_epoch`  | Not yet                                                                     | Not yet                                                             | Not possible                                                      | Not possible                                                                   | Yes                                                           | Not possible                                                  | Not possible                                                                  |

Yes means that the target computes it, and Partly that it computes it only under conditions or approximately. Not yet means that it runs in Tenzir, and Not possible that the target cannot express it as specified. The notes below the table name the conditions and how the targets differ.

* `starts_with`, `ends_with`, and `is_empty` (MySQL, SQL Server, and SPL): in filters only, since the target has no booleans.
* `starts_with` and `ends_with` (SentinelOne): as a predicate with a non-empty string; in LOG queries, `x` must be a field.
* `match_regex` (ClickHouse): clickHouse's RE2.
* `match_regex` (MySQL and SPL): in filters only, since the target has no booleans.
* `length_chars` (SQL Server): counts trailing spaces, which `LEN` alone leaves out.
* `replace` (SentinelOne): powerQuery treats the pattern as a case-insensitive regex.
* `is_empty` (SentinelOne): as a predicate only; yields `true` for `null`.
* `slice` (ClickHouse, DuckDB, MySQL, SQL Server, and KQL): with constant `begin` and `end` that are not negative.
* `slice` (SentinelOne): with constant `begin` and `end` that are not negative; use `substr(x, b)` or `substr(x, 0, e)` with one bound.
* `hash_md5`, `hash_sha1`, and `hash_sha256` (ClickHouse): rejects arguments that are no strings.
* `hash_md5`, `hash_sha1`, and `hash_sha256` (SentinelOne): the target has no hash functions.
* `round` (ClickHouse): rounds halves to even.
* `sqrt` (DuckDB and SQL Server): fails the query for negative inputs.
* `log` (DuckDB and SQL Server): fails the query for zero or negative inputs.
* `second` (ClickHouse): plus the fraction of the second, from `toUnixTimestamp64Nano`.
* `since_epoch` (MySQL, SQL Server, SPL, and SentinelOne): the target has no durations.

Every target computes a function in kind like TQL: with the same type, with `null` where TQL yields `null`, such as for the root of a negative number, and with the same result without values. Within that, the target’s own semantics hold, such as how it rounds floating-point numbers, maps case, or matches regular expressions. A function takes positional arguments only, so a call with a named argument such as `ignore_case=true` runs in Tenzir. The `slice` function is the exception: it takes constant `begin` and `end` arguments.

### Time buckets

A `floor` of a time to a constant duration, such as the group key `hour` in

```tql
from_clickhouse table="events", host="localhost"
hour = floor(time, 1h)
summarize hour, events=count()
```

runs in these targets:

| Width                                  | [ClickHouse](optimizations/clickhouse.md) | [DuckDB](optimizations/duckdb.md) | [MySQL](optimizations/mysql.md) | [SQL Server](optimizations/microsoft-sql.md) | [KQL](optimizations/kql.md) | [SPL](optimizations/spl.md) | [SentinelOne](optimizations/sentinelone.md) |
| -------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------- | ------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Whole seconds, such as `1h`            | Yes                                                                         | Yes                                                                 | Yes                                                               | Partly                                                                         | Partly                                                        | Not yet                                                       | Yes                                                                           |
| Fractions of a second, such as `250ms` | Yes                                                                         | Yes                                                                 | Partly                                                            | Not yet                                                                        | Partly                                                        | Not yet                                                       | Not yet                                                                       |
| Multiples of a week or a month         | Not yet                                                                     | Not yet                                                             | Not yet                                                           | Not yet                                                                        | Not yet                                                       | Not yet                                                       | Not yet                                                                       |

Yes means that the target computes it, and Partly that it computes it only under conditions or approximately. Not yet means that it runs in Tenzir, and Not possible that the target cannot express it as specified. The notes below the table name the conditions and how the targets differ.

* Whole seconds, such as `1h` (SQL Server): needs SQL Server 2022 or later; use `pushdown=false` with earlier servers.
* Whole seconds, such as `1h` (KQL): widths that divide the time from 0001-01-01 to the epoch, such as those that divide two days.
* Fractions of a second, such as `250ms` (MySQL): whole microseconds only.
* Fractions of a second, such as `250ms` (KQL): whole multiples of 100 nanoseconds that divide the time from 0001-01-01 to the epoch.

The buckets count from the epoch, as in TQL, also before 1970. Widths that are multiples of a week or a month run in Tenzir, since TQL aligns them to the calendar.

## Rules that all sources share

The remote sources take over operators the same way, whatever their target.

### The run of operators after the source

A source takes over the longest run of operators directly after it that its target can spell: [`where`](operators/where.md), [`select`](operators/select.md), [`drop`](operators/drop.md), [`summarize`](operators/summarize.md), [`sort`](operators/sort.md), and [`head`](operators/head.md), as well as [`top`](operators/top.md) or [`rare`](operators/rare.md) followed by [`head`](operators/head.md). The first operator that the target cannot spell ends the run. That operator and everything after it run in Tenzir, even if the target could spell a later one.

The source decides from the pipeline alone and never falls back: an operator that it takes over runs in the target, and a target that rejects the request fails the pipeline with a [diagnostic](optimizations.md#diagnostics).

Tenzir splits a [`where`](operators/where.md) at `and`, so the target can still take over the conjuncts that it spells. In

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3 and message.parse_json().level == "high"
```

DuckDB takes over `severity >= 3`, and `parse_json` runs in Tenzir on the rows that DuckDB returns.

### Aggregations in the source

A target that computes a final summary returns one row per group instead of every matching row. This happens if the source writes or extends the query itself in a read that ends, so not with `live=true`, as the backend pages describe for each source, and if every filter before the summary went to the target as well. The summary can follow the source directly or behind operators that keep every event and only keep, drop, or copy fields:

* [`select`](operators/select.md) and [`drop`](operators/drop.md) that keep the fields that the summary reads.
* Renames and copies with [`select`](operators/select.md), [`set`](operators/set.md), or a plain assignment, such as `select ip=src_ip` or `ip = src_ip`. The target then groups and aggregates the original fields, and the result keeps the new names.

For example, MySQL computes the summary of

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
select ip=src_ip, ts, severity
where severity >= 3
summarize ip, alerts=count(), last=max(ts)
```

by grouping on the `src_ip` column. Every right-hand side of a [`select`](operators/select.md) or [`set`](operators/set.md) reads the original event, so `select a=b, b=a` swaps the fields, and the summary reads them swapped. A summary can also read [computed values](optimizations.md#computed-keys-and-arguments).

A target that computes the summary also takes over the [`where`](operators/where.md), [`sort`](operators/sort.md), and [`head`](operators/head.md) that directly follow it, so that it returns only the groups that the pipeline keeps:

```tql
from_clickhouse table="events", host="clickhouse.example.com", tls=false
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events, src_ip
head 20
```

The filter applies to the groups after grouping, and the limit counts groups. A [`top`](operators/top.md) or [`rare`](operators/rare.md) followed by [`head`](operators/head.md) runs in the target as well.

### Computed keys and arguments

A summary can group by or aggregate computed values, such as values that a [`set`](operators/set.md) before it assigns. The target computes them with its own semantics before the aggregation:

| Source                                                                                                                                                                                                                                                                                                                                                                                                                  | Computes with                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| [`from_clickhouse`](operators/from_clickhouse.md), [`from_duckdb`](operators/from_duckdb.md), [`from_hydrolix`](operators/from_hydrolix.md), [`from_microsoft_sql`](operators/from_microsoft_sql.md), [`from_mysql`](operators/from_mysql.md) | The expression inside the aggregate |
| [`from_splunk`](operators/from_splunk.md)                                                                                                                                                                                                                                                                                                                                             | `eval`                              |
| [`from_microsoft_defender`](operators/from_microsoft_defender.md), [`from_azure_log_analytics`](operators/from_azure_log_analytics.md)                                                                                                                                                                                                              | `extend`                            |
| [`from_sentinelone_data_lake`](operators/from_sentinelone_data_lake.md)                                                                                                                                                                                                                                                                                                               | `let` before `group`                |

For example, Splunk computes the key of

```tql
from_splunk "https://splunk:8089", index="main", earliest="-1h", latest="now"
kind = action.to_upper()
summarize kind, events=count()
```

with `| eval tenzir_column_0=upper('action')` before its `stats`, and DuckDB computes `worst` in

```tql
from_duckdb "events.duckdb", table="events"
level = severity * 2
summarize src_ip, worst=max(level)
```

as `MAX(("severity" * 2))`.

An assignment that the summary reads may be fallible, such as a function call, since the target computes it with its own semantics. An assignment that the summary doesn’t read, including one that a later assignment shadows, must be infallible, since the target skips it and so would hide a failure that the pipeline would report. Otherwise, the operators run in Tenzir. A value that the target cannot spell, such as a call of a function that the [matrix](optimizations.md#functions) doesn’t list for it, also makes the summary run in Tenzir.

### Aggregation input projections

A final [`summarize`](operators/summarize.md) also tells the source which fields it reads, so a source reads only those even if its target does not compute the summary. You do not need an explicit [`select`](operators/select.md) before aggregation:

```tql
from_mysql table="events", host="db.example.com", database="soc", pushdown=false
summarize host, events=count(), bytes=sum(bytes)
head 10
```

With `pushdown=false`, MySQL computes nothing, but the source still reads only `host` and `bytes`, with a query equivalent to:

```sql
SELECT `host`, `bytes`
FROM `events`
```

Tenzir then groups and aggregates the complete input and keeps at most ten summary rows. These rules preserve the aggregation’s inputs and behavior:

* All grouping keys remain required, even if a later selection drops them.
* All aggregate arguments remain required, even if their results are unused, because evaluating them can produce diagnostics.
* Output aliases are not input dependencies. In the example, `events` does not request a source column.
* A keyless `summarize events=count()` needs the row count but no field values. A source may still read a column or emit a placeholder per row to preserve that count.
* Whole-event access, such as `collect(this)`, and dynamic field access, such as `sum(this[key])`, prevent narrowing.
* Options must be resolved before `summarize` supplies a projection. Inside runtime-bound subpipelines, such as [`group`](operators/group.md) and [`window`](operators/window.md), an unresolved `summarize` does not narrow the enclosing source.
* Input ordering requirements remain intact for order-sensitive aggregates. Trigger output, event output, and periodic summaries retain their barriers.

The [`top`](operators/top.md) and [`rare`](operators/rare.md) operators compile into `summarize` and [`sort`](operators/sort.md), so they benefit from the same input projection. A following [`head`](operators/head.md) still limits groups, not raw input events.

### Time windows

[`from_splunk`](operators/from_splunk.md) with `index`, [`from_sentinelone_data_lake`](operators/from_sentinelone_data_lake.md) without `query`, [`from_amazon_cloudwatch`](operators/from_amazon_cloudwatch.md), and [`from_microsoft_365_activity`](operators/from_microsoft_365_activity.md) narrow the time range of their request to the comparisons of a time in the filters after them. They share one reading of these filters:

| Filter                                         | Window                                                                                     |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------ |
| `>=`, `<=`, and `==` with a time               | Includes the time                                                                          |
| `>` and `<` with a time                        | Excludes the time, so the window moves by 1 ns                                             |
| A strict comparison beyond the range of a time | Empty window, so the read completes without a request, unless a summary still yields a row |
| `and` of comparisons                           | The intersection of their windows                                                          |
| `or` of comparisons                            | The range that encloses their windows                                                      |

Each source then rounds the window to the units of its request. A strict bound now excludes its time, so `from_splunk` requests `latest_time=1735689720`, and not `1735689721`, for `where _time < 2025-01-01T00:02:00Z`. [`from_microsoft_365_activity`](operators/from_microsoft_365_activity.md) also narrows the listing to the range that encloses an `or`, such as for

```tql
where microsoft_365_activity.content_created >= 2024-01-02
   or microsoft_365_activity.content_created == 2024-01-01
```

and narrows the side of an `==` that it can represent. The comparisons always stay in the pipeline or the request, so the window never changes the result.

## Diagnostics

A source tells you when its target did not compute the operators that it took over like Tenzir would:

* **The target rejects the request.** The source reports the target’s error with a note and a hint:

  ```text
  note: <target> computes the stages that the operator took over with its own semantics
  hint: use `pushdown=false` to run them in Tenzir
  ```

* **The source cannot plan the operators for what it reads.** The source reports an error with the reason as note and the same hint:

  ```text
  error: <target> cannot compute the stages that the operator took over
  ```

The first case adds the note and the hint only if the source took over operators. A source that took over none, such as with `pushdown=false`, shows the error of the target alone. For example, DuckDB rejects the filter of

```tql
from_duckdb "events.duckdb", table="keyed"
where n == "many"
```

since it cannot cast the string to the type of the column:

```text
error: Conversion Error: Could not convert string 'many' to INT32


LINE 1: SELECT * FROM "keyed" WHERE ("n" = 'many')
                                           ^^^^^^^
  = note: DuckDB computes the stages that the operator took over with its own semantics
  = hint: use `pushdown=false` to run them in Tenzir
```

The second case arises for sources that learn about the target when the pipeline runs, such as the columns of a ClickHouse table:

```text
error: ClickHouse cannot compute the stages that the operator took over
  = note: cannot bind `al`: `al` is an `ALIAS` column, which `SELECT *` includes only depending on the session's settings
  = hint: use `pushdown=false` to run them in Tenzir
```

## Verify an optimization

To see what a source takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_mysql table="logins" | where user == "admin" | head 10'
```

Every remote source in the [table of sources](optimizations.md#sources-and-their-pages) lists the operators that its target took over as `plan`, and the reason why it took over no more as `declined`. The [`where`](operators/where.md), [`summarize`](operators/summarize.md), or other operators that the target took over no longer appear after the source. A source that acts on hints shows the predicates that it received as `filter`, the limit as `limit`, and the fields that it reads as `projection`.

To see the request itself, use the target’s own tools, such as the query log of a database or ClickHouse’s `system.query_log` table. When Splunk reports an error or a warning, and when SentinelOne rejects a query, the diagnostic shows the request as the source sent it.
