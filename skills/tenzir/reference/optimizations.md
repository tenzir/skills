---
title: "Overview"
canonical: https://tenzir.com/docs/reference/optimizations
source: https://tenzir.com/docs/reference/optimizations.md
section: "Docs"
---

# Overview

> This reference lists which operators each source pushes down, compares what the query-language targets compute, and links a page per remote target with its native spellings and semantic differences. Read our explanation of transpilation for how TQL compiles into native queries, how target semantics differ from TQL, and when to disable pushdown with pushdown=false.

This reference lists which operators each source pushes down, compares what the query-language targets compute, and links a page per remote target with its native spellings and semantic differences. Read our explanation of [transpilation](../explanations/transpilation.md) for how TQL compiles into native queries, how target semantics differ from TQL, and when to disable pushdown with `pushdown=false`.

In the matrices on this page, 🟢 runs in the target (or full hint support), 🟡 runs conditionally or with restrictions, and ⚪ runs in Tenzir.

## Sources and their pages

Each remote target links to a page describing when it takes over operators, its native query spellings, and how its semantics differ from TQL’s:

| Target                                                                                  | `where` | `select` | `drop` | `summarize` | `sort` | `head` |
| --------------------------------------------------------------------------------------- | ------- | -------- | ------ | ----------- | ------ | ------ |
| [ClickHouse / Hydrolix](optimizations/clickhouse.md)  | 🟢      | 🟢       | 🟢     | 🟢          | 🟢     | 🟢     |
| [DuckDB](optimizations/duckdb.md)                     | 🟢      | 🟢       | 🟢     | 🟢          | 🟢     | 🟢     |
| [MySQL](optimizations/mysql.md)                       | 🟢      | 🟡       | 🟡     | 🟢          | 🟢     | 🟢     |
| [SQL Server](optimizations/microsoft-sql.md)          | 🟢      | 🟡       | 🟡     | 🟢          | 🟢     | 🟢     |
| [KQL (Defender, Log Analytics)](optimizations/kql.md) | 🟢      | 🟡       | 🟢     | 🟢          | 🟢     | 🟢     |
| [Axiom (APL)](optimizations/axiom.md)                 | 🟢      | 🟡       | 🟢     | 🟢          | 🟢     | 🟡     |
| [Splunk (SPL)](optimizations/spl.md)                  | 🟢      | 🟡       | 🟢     | 🟢          | 🟢     | 🟢     |
| [SentinelOne](optimizations/sentinelone.md)           | 🟢      | 🟢       | ⚪      | 🟢          | 🟡     | 🟡     |
| [CloudWatch Logs](optimizations/cloudwatch.md)        | 🟡      | ⚪        | ⚪      | ⚪           | ⚪      | 🟡     |
| [Microsoft Graph](optimizations/microsoft-graph.md)   | 🟡      | 🟡       | ⚪      | ⚪           | ⚪      | 🟡     |

Source operators and per-target restrictions

Source operators per target:

* [ClickHouse / Hydrolix](optimizations/clickhouse.md): [`from_clickhouse`](operators/from_clickhouse.md), [`from_hydrolix`](operators/from_hydrolix.md)
* [DuckDB](optimizations/duckdb.md): [`from_duckdb`](operators/from_duckdb.md)
* [MySQL](optimizations/mysql.md): [`from_mysql`](operators/from_mysql.md)
* [SQL Server](optimizations/microsoft-sql.md): [`from_microsoft_sql`](operators/from_microsoft_sql.md)
* [KQL (Defender, Log Analytics)](optimizations/kql.md): [`from_microsoft_defender`](operators/from_microsoft_defender.md), [`from_azure_log_analytics`](operators/from_azure_log_analytics.md)
* [Axiom (APL)](optimizations/axiom.md): [`from_axiom`](operators/from_axiom.md)
* [Splunk (SPL)](optimizations/spl.md): [`from_splunk`](operators/from_splunk.md)
* [SentinelOne](optimizations/sentinelone.md): [`from_sentinelone_data_lake`](operators/from_sentinelone_data_lake.md)
* [CloudWatch Logs](optimizations/cloudwatch.md): [`from_amazon_cloudwatch`](operators/from_amazon_cloudwatch.md)
* [Microsoft Graph](optimizations/microsoft-graph.md): [`from_microsoft_graph`](operators/from_microsoft_graph.md)

- `where` (CloudWatch Logs): message filter patterns, time ranges, and up to 100 log streams.
- `where` (Microsoft Graph): documented `v1.0` `$filter` properties only.
- `select` (ClickHouse / Hydrolix): includes named tuple elements.
- `select` (DuckDB): includes `STRUCT` fields.
- `select` (MySQL, SQL Server, KQL (Defender, Log Analytics), Axiom (APL), and Splunk (SPL)): top-level fields only.
- `select` (SentinelOne): includes nested dotted fields.
- `select` (Microsoft Graph): top-level properties only.
- `drop` (ClickHouse / Hydrolix): top-level fields via `* EXCEPT (…)`.
- `drop` (DuckDB, KQL (Defender, Log Analytics), Axiom (APL), and Splunk (SPL)): top-level fields.
- `drop` (MySQL and SQL Server): only after a `select` or `summarize` that the target took over.
- `drop` (SentinelOne): PowerQuery has no `drop` stage.
- `sort` (SentinelOne): only after `select` or `summarize`.
- `head` (Axiom (APL)): positive counts only (`head 0` runs in Tenzir).
- `head` (SentinelOne): up to 1,600,000 rows in PowerQuery.
- `head` (CloudWatch Logs): in `search` and `replay` modes; not in `live` mode.
- `head` (Microsoft Graph): stops paging and sets `$top` where documented.

Other operators narrow what they read or pass requirements upstream while keeping exact TQL results:

| Operator                                                                                                    | Filters | Projections | Limits |
| ----------------------------------------------------------------------------------------------------------- | ------- | ----------- | ------ |
| [`from_iceberg`](operators/from_iceberg.md)                               | 🟡      | 🟢          | 🟡     |
| [`from_microsoft_365_activity`](operators/from_microsoft_365_activity.md) | 🟡      | ⚪           | 🟡     |
| [`read_parquet`](operators/read_parquet.md)                               | 🟡      | 🟢          | 🟡     |
| [`subscribe`](operators/subscribe.md)                                     | 🟡      | 🟢          | 🟡     |
| [`sort`](operators/sort.md)                                               | 🟡      | 🟢          | 🟡     |
| [`summarize`](operators/summarize.md) (final summary)                     | ⚪       | 🟢          | ⚪      |

How each operator applies physical hints

* `from_iceberg` (Filters): prunes manifests and data files; exact predicates stay local.
* `from_iceberg` (Projections): reads only needed columns, with a metadata-only fast path for zero-column scans.
* `from_iceberg` (Limits): bounds unfiltered scans and stops reading early.
* `from_microsoft_365_activity` (Filters): skips blobs by metadata.
* `from_microsoft_365_activity` (Limits): stops downloading early.
* `read_parquet` (Filters): skips row groups while decoding.
* `read_parquet` (Projections): reads only needed fields, including record fields.
* `read_parquet` (Limits): stops decoding early.
* `subscribe` (Filters): filters before queuing.
* `subscribe` (Projections): applied on arrival.
* `subscribe` (Limits): with one topic.
* `sort` (Filters): moved before the sort.
* `sort` (Projections): passed upstream.
* `sort` (Limits): keeps only the top `N`.
* `summarize` (Filters and Limits): kept after aggregation unless a source takes over the summary.
* `summarize` (Projections): requests only group keys and aggregate inputs.

[`from_velociraptor`](operators/from_velociraptor.md) pushes nothing down, since a VQL query may have side effects that a filter or a limit would change.

## What the targets compute

The following matrices compare the eight query-language targets. Each target page lists the exact native spelling for every function.

### Aggregation functions

A source pushes down a [`summarize`](operators/summarize.md) only if its target computes every aggregation function in the summary:

| Aggregation                                                                       | ClickHouse | DuckDB | MySQL | SQL Server | KQL | Axiom | SPL | SentinelOne |
| --------------------------------------------------------------------------------- | ---------- | ------ | ----- | ---------- | --- | ----- | --- | ----------- |
| [`count()`](functions/count.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`count(x)`](functions/count.md)                | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`min`](functions/min.md)                       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`max`](functions/max.md)                       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`count_if`](functions/count_if.md)             | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`count_distinct`](functions/count_distinct.md) | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟡    | 🟢  | 🟡          |
| [`sum`](functions/sum.md)                       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`mean`](functions/mean.md)                     | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`stddev`](functions/stddev.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`variance`](functions/variance.md)             | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`all`](functions/all.md)                       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| [`any`](functions/any.md)                       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |

Empty-group behavior, approximations, and dialect notes

* `count()` (SPL): SPL2 spells it `count()`.
* `count(x)` (KQL): counts empty strings.
* `count(x)` (Axiom): counts empty strings; skips `null`.
* `count(x)` (SPL): counts each value of a multivalue field.
* `count(x)` (SentinelOne): counts the events where `x` has a value.
* `min` and `max` (ClickHouse): yields the type's default without values.
* `min` and `max` (SQL Server): also takes text.
* `min` and `max` (SPL): compares numbers numerically and other values as text.
* `min` (SentinelOne): yields `Infinity` without values.
* `max` (SentinelOne): yields `-Infinity` without values.
* `count_if` (ClickHouse, DuckDB, MySQL, SQL Server, KQL, Axiom, and SentinelOne): skips `null` values.
* `count_if` (SPL): skips events without a value; `count(if(p, 1, null))` in SPL2.
* `count_distinct` (KQL): exact; counts empty strings and fails beyond 100 million values in a group.
* `count_distinct` (Axiom): exact via two `summarize` stages when siblings recompose; runs in Tenzir alongside a second distinct field, `mean`, `stddev`, or `variance`.
* `count_distinct` (SPL): exact, unlike `estdc`.
* `count_distinct` (SentinelOne): exact via two `group` stages, excluding `null`; falls back to approximate `estimate_distinct(x)` alongside `stddev`, `variance`, or another distinct field.
* `sum` (DuckDB): widens integers to a `HUGEINT`, which still arrives as an `int`.
* `sum` (MySQL): sums integers as a `DECIMAL`, which still arrives as an `int`.
* `sum` (KQL and Axiom): yields `0` without values.
* `sum` and `mean` (SentinelOne): yields `0.0` without values.
* `mean` (SQL Server): casts first, since `AVG` truncates integers.
* `mean` (KQL): yields `NaN` without values.
* `stddev` and `variance` (KQL): yields `0` without values.
* `stddev` (Axiom): rescales sample `stdev` to population form; yields `null` for `n <= 1`.
* `stddev` (SentinelOne): rescales PowerQuery's sample `stddev` to population form.
* `variance` (Axiom): rescales sample `variance` to population form; yields `null` for `n <= 1`.
* `variance` (SentinelOne): rescales PowerQuery's sample `stddev` to population variance.
* `all` and `any` (ClickHouse, KQL, and Axiom): skips `null` values.
* `all` and `any` (DuckDB): skips `null` values; yields `null` without values.
* `all` and `any` (MySQL and SQL Server): decoded as a boolean; skips `null` values and yields `null` without values.
* `all` (SPL): decoded as a boolean; skips `null` values and yields `null` without values; `min(case(...))` in SPL2.
* `all` (SentinelOne): skips `null` values; yields `true` without values.
* `any` (SPL): decoded as a boolean; skips `null` values and yields `null` without values; `max(case(...))` in SPL2.
* `any` (SentinelOne): skips `null` values; yields `false` without values.

Across all targets, `count_if` counts only events whose input is not `null`, wide sums widened by DuckDB (`HUGEINT`) or MySQL (`DECIMAL`) still arrive as `int` (overflowing 64 bits yields `null` with a warning), and floating-point results follow each target’s arithmetic. Results without values follow the target rather than TQL.

### Functions

Supported in filters, group keys, and aggregate arguments:

| Kind    | Function                                                                      | ClickHouse | DuckDB | MySQL | SQL Server | KQL | Axiom | SPL | SentinelOne |
| ------- | ----------------------------------------------------------------------------- | ---------- | ------ | ----- | ---------- | --- | ----- | --- | ----------- |
| Strings | [`starts_with`](functions/starts_with.md)   | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟡          |
| Strings | [`ends_with`](functions/ends_with.md)       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟡          |
| Strings | [`match_regex`](functions/match_regex.md)   | 🟢         | 🟢     | 🟢    | ⚪          | 🟢  | 🟢    | 🟢  | 🟡          |
| Strings | [`length_bytes`](functions/length_bytes.md) | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | ⚪   | ⚪           |
| Strings | [`length_chars`](functions/length_chars.md) | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`to_lower`](functions/to_lower.md)         | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`to_upper`](functions/to_upper.md)         | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`capitalize`](functions/capitalize.md)     | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`trim`](functions/trim.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`trim_start`](functions/trim_start.md)     | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`trim_end`](functions/trim_end.md)         | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Strings | [`replace`](functions/replace.md)           | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟡  | 🟡          |
| Strings | [`is_empty`](functions/is_empty.md)         | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟡          |
| Strings | [`slice`](functions/slice.md)               | 🟡         | 🟡     | 🟡    | 🟡         | 🟡  | 🟡    | 🟡  | 🟡          |
| Hashes  | [`hash_md5`](functions/hash_md5.md)         | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | ⚪           |
| Hashes  | [`hash_sha1`](functions/hash_sha1.md)       | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | ⚪           |
| Hashes  | [`hash_sha256`](functions/hash_sha256.md)   | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | ⚪           |
| Numbers | [`abs`](functions/abs.md)                   | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Numbers | [`ceil`](functions/ceil.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Numbers | [`floor`](functions/floor.md)               | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Numbers | [`round`](functions/round.md)               | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | ⚪           |
| Numbers | [`sqrt`](functions/sqrt.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Numbers | [`exp`](functions/exp.md)                   | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Numbers | [`log`](functions/log.md)                   | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`year`](functions/year.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`month`](functions/month.md)               | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`day`](functions/day.md)                   | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`hour`](functions/hour.md)                 | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`minute`](functions/minute.md)             | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`second`](functions/second.md)             | 🟢         | 🟢     | 🟢    | 🟢         | 🟢  | 🟢    | 🟢  | 🟢          |
| Times   | [`since_epoch`](functions/since_epoch.md)   | 🟢         | 🟢     | ⚪     | ⚪          | 🟢  | 🟢    | ⚪   | ⚪           |

Conditions, semantic differences, and target limitations

* `starts_with`, `ends_with`, and `is_empty` (MySQL and SQL Server): as a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`).
* `starts_with`, `ends_with`, `match_regex`, and `is_empty` (SPL): as a value, wrapped in `if(p, "true", "false")` and decoded as a boolean (`null` becomes `false`).
* `starts_with`, `ends_with`, and `match_regex` (SentinelOne): with a non-empty string literal; in LOG queries, `x` must be a field and only in predicates.
* `match_regex` (ClickHouse): ClickHouse's RE2.
* `match_regex` (MySQL): as a value, wrapped in `CASE WHEN p THEN 1 ELSE 0 END` and decoded as a boolean (`null` becomes `false`).
* `match_regex` (Axiom): go RE2.
* `length_bytes` (SQL Server): returns storage byte length (UTF-16 bytes for `nvarchar`, code page bytes for `varchar`).
* `length_chars` (SQL Server): counts trailing spaces, which `LEN` alone leaves out.
* `capitalize` (SPL): yields `null` for an empty string.
* `replace` (SPL): with a constant string `y`, regex-escaped for Splunk's PCRE matcher.
* `replace` (SentinelOne): with a non-empty constant string `y` (regex-escaped, matched case-insensitively) and constant string `z` (interprets `$n` group references).
* `is_empty` (Axiom): yields `true` for `null`.
* `is_empty` (SentinelOne): yields `true` for `null`; in PowerQuery only.
* `slice` (ClickHouse, DuckDB, MySQL, SQL Server, KQL, and Axiom): with constant `begin` and `end` that are not negative.
* `slice` (SPL): with constant `begin` and `end` that are not negative; uses `substr(x, b + 1)` or `substr(x, 1, e)` with one bound.
* `slice` (SentinelOne): with constant `begin` and `end` that are not negative; uses `substr(x, b)` or `substr(x, 0, e)` with one bound.
* `hash_md5`, `hash_sha1`, and `hash_sha256` (ClickHouse): rejects non-string arguments.
* `hash_md5`, `hash_sha1`, and `hash_sha256` (SQL Server): hashes the column's native byte encoding (UTF-16 for `nvarchar`, database code page for `varchar`).
* `hash_md5`, `hash_sha1`, and `hash_sha256` (SentinelOne): the target has no hash functions.
* `round` (ClickHouse): rounds halves to even.
* `sqrt` (DuckDB and SQL Server): fails the query for negative inputs.
* `log` (DuckDB and SQL Server): fails the query for zero or negative inputs.
* `year`, `month`, `day`, `hour`, and `minute` (SPL): uses Splunk's configured time zone.
* `second` (ClickHouse): plus the fraction of the second, from `toUnixTimestamp64Nano`.
* `second` (SPL): microsecond precision.
* `second` (SentinelOne): millisecond precision.
* `since_epoch` (ClickHouse): decoded from nanoseconds as a duration.
* `since_epoch` (DuckDB): microsecond precision (`INTERVAL`).
* `since_epoch` (MySQL, SQL Server, SPL, and SentinelOne): the target has no durations.

Functions take positional arguments only (calls with named arguments such as `ignore_case=true` run in Tenzir), except `slice`, which takes constant non-negative `begin` and `end` arguments. Error handling, return types, rounding, case mapping, and regex engines follow each target’s native semantics.

### Time buckets

Support for `floor(time, width)` with a constant duration:

| Width                                  | ClickHouse | DuckDB | MySQL | SQL Server | KQL | Axiom | SPL | SentinelOne |
| -------------------------------------- | ---------- | ------ | ----- | ---------- | --- | ----- | --- | ----------- |
| Whole seconds, such as `1h`            | 🟢         | 🟢     | 🟢    | 🟡         | 🟡  | 🟢    | 🟢  | 🟢          |
| Fractions of a second, such as `250ms` | 🟢         | 🟢     | 🟡    | ⚪          | 🟡  | 🟢    | ⚪   | ⚪           |
| Multiples of a week or a month         | ⚪          | ⚪      | ⚪     | ⚪          | ⚪   | ⚪     | ⚪   | ⚪           |

Supported bucket widths and server version requirements

* Whole seconds, such as `1h` (SQL Server): needs SQL Server 2022 or later; use `pushdown=false` with earlier servers.
* Whole seconds, such as `1h` (KQL): widths that divide the time from 0001-01-01 to the epoch, such as those that divide two days.
* Fractions of a second, such as `250ms` (MySQL): whole microseconds only.
* Fractions of a second, such as `250ms` (KQL): whole multiples of 100 nanoseconds that divide the time from 0001-01-01 to the epoch.

Time buckets align to the epoch in UTC, including before 1970. Calendar widths (multiples of a week or a month) always run in Tenzir.
