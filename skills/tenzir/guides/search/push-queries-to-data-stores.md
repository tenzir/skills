---
title: "Push queries to data stores"
description: "Write TQL pipelines that push filters, projections, summaries, sorts, limits, and time windows into databases, SIEMs, EDRs, and cloud APIs."
canonical: https://tenzir.com/docs/guides/search/push-queries-to-data-stores
source: https://tenzir.com/docs/guides/search/push-queries-to-data-stores.md
section: "Docs"
---

# Push queries to data stores

> Write TQL pipelines that push filters, projections, summaries, sorts, limits, and time windows into databases, SIEMs, EDRs, and cloud APIs.

Querying a remote data store should transfer only the rows or aggregates you need, not the entire table. When you follow a remote source with TQL operators such as [`where`](../../reference/operators/where.md), [`select`](../../reference/operators/select.md), [`drop`](../../reference/operators/drop.md), [`summarize`](../../reference/operators/summarize.md),

[`sort`](../../reference/operators/sort.md), or [`head`](../../reference/operators/head.md), Tenzir compiles the longest supported run of those operators into the remote system’s native query language and executes them where the data lives. The remote system, its **target**, runs those transpiled stages with its native semantics, and Tenzir runs everything that follows.

This guide shows how pushdown works across SQL, SPL, KQL, APL, PowerQuery, and CloudWatch Logs sources, how to verify what runs in the target, when to opt out with `pushdown=false`, and when to write a native target query instead.

## Push operators across target families

Every supported remote source accepts the same TQL operators and translates them into the target’s native query language or API parameters. You write TQL once, and each connector decides how much of the pipeline its target can compute.

### SQL databases

In table mode (`table=...`), [`from_clickhouse`](../../reference/operators/from_clickhouse.md), [`from_duckdb`](../../reference/operators/from_duckdb.md),

[`from_hydrolix`](../../reference/operators/from_hydrolix.md), [`from_mysql`](../../reference/operators/from_mysql.md), and [`from_microsoft_sql`](../../reference/operators/from_microsoft_sql.md) push filters, projections, summaries, time buckets built with [`floor`](../../reference/functions/floor.md), post-summary filters, sorts, and limits directly into SQL.

The following pipeline groups high-severity ClickHouse events into hourly buckets and keeps the 20 busiest hour-and-address groups:

```tql
from_clickhouse table="logs.events",
  host="clickhouse.example.com",
  password=secret("CLICKHOUSE_PASSWORD")
where severity >= 3 and source == "fw"
hour = floor(time, 1h)
summarize hour, src_ip, events=count()
where events >= 10
sort -events, src_ip
head 20
```

ClickHouse evaluates the `WHERE` predicate, computes the hourly time buckets, aggregates by `hour` and `src_ip`, filters groups with fewer than 10 events, sorts descending by `events`, and applies `LIMIT 20`. At most 20 summary rows travel over the network. The same pattern works with [`top`](../../reference/operators/top.md) or

[`rare`](../../reference/operators/rare.md) followed by `head`: `top` and `rare` compile into `summarize` and `sort`, and the following `head` supplies the limit.

### Splunk (SPL and SPL2)

With `index`, [`from_splunk`](../../reference/operators/from_splunk.md) pushes initial filters into Splunk’s base `search` command where SPL can use Splunk’s indexes, turns remaining filters into `| where` stages, maps summaries to `| stats`, sorts to `| sort`, and limits to `| head`. When both `earliest` and `latest` are absolute timestamps, comparisons on `_time` also narrow the request’s time window.

```tql
from_splunk "https://splunk.example.com:8089",
  index="main",
  earliest=2026-01-01T00:00:00Z,
  latest=2026-01-02T00:00:00Z,
  headers={Authorization: secret("splunk-rest-authorization")}
where source == "auth" and user != "root"
where _time >= 2026-01-01T06:00:00Z and _time < 2026-01-01T07:00:00Z
summarize user, attempts=count()
sort -attempts
head 20
```

Here, Splunk adds `source="auth"` to the base search, narrows the search window to the one-hour range, evaluates `user != "root"`, groups and counts events with `stats`, and returns only the top 20 users. Splunk also appends supported TQL stages after a custom `search` or `spl2` query, so you can combine native SPL with downstream TQL filtering and aggregation, and computes whole-second time buckets built with [`floor`](../../reference/functions/floor.md) on `_time` (such as `hour = floor(_time, 1h)`) alongside summaries.

### Microsoft Defender and Azure Log Analytics (KQL)

The KQL sources [`from_microsoft_defender`](../../reference/operators/from_microsoft_defender.md) and

[`from_azure_log_analytics`](../../reference/operators/from_azure_log_analytics.md) append KQL `where`, `project`, `project-away`, `extend`, `summarize`, `sort by`, and `take` stages to your query. Starting from a table name lets you write the rest of the search in TQL:

```tql
from_microsoft_defender "DeviceNetworkEvents",
  azure_auth={
    tenant_id: secret("AZURE_TENANT_ID"),
    client_id: secret("AZURE_CLIENT_ID"),
    client_secret: secret("AZURE_CLIENT_SECRET"),
  },
  start=2026-01-01T00:00:00Z,
  end=2026-01-02T00:00:00Z
where RemotePort != null and RemoteIP in 10.0.0.0/8
hour = floor(Timestamp, 1h)
summarize hour, RemoteIP, connections=count()
sort -connections
head 25
```

Defender computes the null check (`isnotnull`), subnet match (`ipv4_is_in_range`), hourly `bin` time bucket, summary, sort, and `take 25` server-side. Reducing results in KQL also helps stay within service [response caps](../../explanations/transpilation.md#completeness-row-limits-and-truncation) (100,000 rows for Defender and 500,000 rows for Log Analytics). Neither KQL source narrows `start` and `end` from TQL `where` clauses, so always bound the request with `start` and `end` or a KQL time filter.

### Axiom (APL)

The [`from_axiom`](../../reference/operators/from_axiom.md) operator queries Axiom’s regional edge API and transpiles downstream `where`, `select`, `drop`, `summarize`, `sort`, and positive `head` stages into Axiom Processing Language (APL). Unlike KQL, APL aligns `bin` time buckets to the Unix epoch with nanosecond precision and computes exact `count_distinct` via two `summarize` stages:

```tql
from_axiom "http-logs",
  token=secret("axiom_token"),
  start=2026-11-21T00:00:00Z,
  end=2026-11-22T00:00:00Z
where status >= 400 and uri.starts_with("/api/")
bucket = _time.floor(5min)
summarize bucket, method, errors = count(), unique_ips = count_distinct(src_ip)
sort -errors, bucket, method
head 10
```

Axiom evaluates the filter, 5-minute `bin` buckets, exact two-stage summary, sort, and `take 10` server-side before returning the top 10 rows. See the [Axiom integration](https://tenzir.com/product/integrations/axiom.md) for token scopes and edge endpoints, and our [Axiom optimizations reference](../../reference/optimizations/axiom.md) for APL spellings and semantic details.

### SentinelOne Singularity Data Lake (PowerQuery)

Without `query`, [`from_sentinelone_data_lake`](../../reference/operators/from_sentinelone_data_lake.md) generates the entire request from downstream TQL operators. Comparisons on `timestamp` supply or narrow the query time window automatically, so you can omit `start` and `end` when your filters provide fixed timestamps:

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token")
where timestamp >= 2026-01-01T00:00:00Z and timestamp < 2026-01-02T00:00:00Z
where severity > 3 and message.starts_with("alert")
select timestamp, event.kind=event.type, message
sort -timestamp
head 50
```

When only `where` and `head` follow the source, SentinelOne runs a LOG query that streams complete events without PowerQuery’s row cap. Adding `select` or `summarize` (including `floor` time buckets in whole seconds) switches to PowerQuery so SentinelOne returns only the requested columns or groups. Bind relative time bounds with `let` (such as `let $end = now()`) before the source so the optimizer sees constant timestamps.

### Amazon CloudWatch Logs

The [`from_amazon_cloudwatch`](../../reference/operators/from_amazon_cloudwatch.md) operator maps downstream filters and limits directly onto CloudWatch Logs request parameters. In `mode="search"`, phrase checks on `message`, comparisons on `timestamp`, stream filters on `log_stream`, and a limit from `head` all go into the `FilterLogEvents` call:

```tql
from_amazon_cloudwatch "/aws/lambda/api", mode="search"
where "ERROR" in message and not ("healthcheck" in message)
where timestamp >= 2026-01-01T00:00:00Z and timestamp < 2026-01-02T00:00:00Z
head 100
```

CloudWatch evaluates the filter pattern, time range, and event limit before returning logs. CloudWatch does not compute column projections or summaries, so any `select` or `summarize` runs in Tenzir after the matching events arrive.

Each backend differs in which functions, aggregations, and time-bucket widths its target computes. Check our [optimizations reference](../../reference/optimizations.md) for the exact per-target matrices, and read our explanation of [transpilation](../../explanations/transpilation.md) for the shared execution model.

## Understand where pushdown stops

A remote source transpiles the [longest contiguous run of supported operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after it. The first operator or expression that the target cannot express ends that run, and everything from that point onward executes in Tenzir with TQL semantics, even if a later operator would otherwise be supported.

Tenzir splits a [`where`](../../reference/operators/where.md) predicate at top-level `and` operators from left to right and hands conjuncts to the target only up to the first one the target cannot express. Consider this DuckDB pipeline:

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3 and message.parse_json().level == "high"
```

DuckDB cannot evaluate [`parse_json`](../../reference/functions/parse_json.md) through pushdown, so Tenzir splits the filter: DuckDB runs `WHERE severity >= 3`, and Tenzir parses `message` and checks `.level == "high"` only on the rows that DuckDB returns. If you reverse the order and write `where message.parse_json().level == "high" and severity >= 3`, the unsupported call comes first and ends the run immediately, so DuckDB takes over no filter at all.

Always place target-supported selective conditions first, ahead of TQL-only functions and transformations. Even when a final [`summarize`](../../reference/operators/summarize.md) runs in Tenzir instead of the target, its [input projections](../../explanations/transpilation.md#aggregation-input-projections) still tell projection-capable sources which columns it needs, so unused columns stay out of the query.

## Verify what runs in the target

To confirm the exact query that reached a remote system, check the target’s own query log, such as ClickHouse’s `system.query_log` table or your SIEM’s search audit log. When a remote target rejects a pushed query or cannot bind a column, Tenzir fails with a [plan-time or target diagnostic](../../explanations/transpilation.md#plan-time-decisions-and-diagnostics) explaining that the target computed the taken-over stages and hinting to pass `pushdown=false`. For Splunk and SentinelOne, error and warning diagnostics also include the dispatched query directly.

Our explanation of [inspecting a transpiled pipeline](../../explanations/transpilation.md#inspect-a-transpiled-pipeline) covers how to print the optimized pipeline IR and check which stages a source hands to its target before running a pipeline against production data.

## Account for target semantics and `pushdown=false`

Because transpiled operators leave the pipeline and run inside the remote system, their results follow the target’s native semantics rather than TQL’s. Common differences include:

* **Null comparisons.** In SQL, comparisons with `NULL` yield `NULL`, so `name != "alpha"` drops rows where `name` is `NULL`. In SentinelOne, `!=` matches events that lack the field. In KQL, strings are never `null` and missing strings arrive as `""`.
* **Case sensitivity and collations.** MySQL, SQL Server, and Splunk’s base `search` command match strings case-insensitively by default, whereas TQL `==` is case-sensitive.
* **Static typing.** ClickHouse, DuckDB, and KQL reject comparisons between incompatible column types or selections of missing columns, whereas TQL warns and yields `null`.
* **Phrase vs. substring matching.** CloudWatch filter patterns match whole words and phrases rather than arbitrary substrings, so `"ERROR" in message` may skip words that merely contain `ERROR`.
* **Sort order.** Targets choose where `null` sorts and how tied rows order.

See our explanation of [native semantics vs. TQL semantics](../../explanations/transpilation.md#native-semantics-vs-tql-semantics) for the general rules and each target’s page in our [optimizations reference](../../reference/optimizations.md) for backend-specific details.

When exact TQL semantics matter, or when a target cannot bind a field (for example, a ClickHouse `ALIAS` column or a `summarize` on a ClickHouse catch-all table), pass `pushdown=false` on the source:

```tql
from_duckdb "events.duckdb", table="alerts", pushdown=false
where name != "alpha"
summarize host, alerts=count()
```

With `pushdown=false`, every operator runs in Tenzir with TQL semantics, so rows where `name` is `null` pass `name != "alpha"`. Projection-capable sources still read only the columns that the pipeline uses (`name` and `host` here), so disabling pushdown does not force a full-width table scan.

## Choose between TQL pushdown and native queries

Use TQL pushdown when your query consists of filters, projections, time buckets, summaries, sorts, and limits. Keeping those stages in TQL makes pipelines portable across targets and lets downstream filters fold into the source automatically.

Reach for a raw native query parameter when you need capabilities that TQL pushdown does not express:

| Target family                                                                               | Pushdown mode                                                            | Native query mode                                                                          | When to use native mode                                                                                                  |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| SQL (`from_clickhouse`, `from_duckdb`, `from_hydrolix`, `from_mysql`, `from_microsoft_sql`) | `table="..."`                                                            | `sql="..."` (sent verbatim, no pushdown)                                                   | SQL joins, window functions, target-specific functions like `arrayJoin`, or metadata queries (`SHOW TABLES`, `DESCRIBE`) |
| Splunk (`from_splunk`)                                                                      | `index="..."` (builds base `search` and narrows `_time` bounds)          | `search="..."` or `spl2="..."` (appends supported TQL stages when the query syntax allows) | Transforming SPL commands (`tstats`, `transaction`, `lookup`) or SPL2 pipelines                                          |
| KQL (`from_microsoft_defender`, `from_azure_log_analytics`)                                 | Bare table name in `query` (e.g., `"DeviceNetworkEvents"`)               | Full KQL in `query` (appends supported TQL stages when the query syntax allows)            | KQL joins across tables, `let` bindings, `mv-expand`, or `parse` expressions                                             |
| Axiom (`from_axiom`)                                                                        | Positional dataset name (e.g., `"http-logs"`)                            | Full APL in `query="..."` (appends supported TQL stages when the query syntax allows)      | APL joins, `let` bindings, `mv-expand`, or dataset-specific functions                                                    |
| SentinelOne (`from_sentinelone_data_lake`)                                                  | Omit `query` (writes LOG or PowerQuery from TQL and narrows `timestamp`) | `query="..."` (appends supported TQL stages when the query syntax allows)                  | Native PowerQuery joins, `parse` stages, or custom PowerQuery commands                                                   |

Not every native query accepts appended stages. For example, Splunk takes over nothing when `search` uses a macro or `fieldformat`, or when you pass `options` (see our [SPL optimizations reference](../../reference/optimizations/spl.md)), and KQL takes over nothing after queries that use `render`, `fork`, `facet`, a `set` statement, or multiple tabular statements (see our [KQL optimizations reference](../../reference/optimizations/kql.md)).

Once you can push selective work cleanly into a single store, the next step is combining several stores in one investigation pipeline. Follow our guide on [searching across data stores](search-across-data-stores.md) to run federated searches across heterogeneous targets.

## See also

* [Search across data stores](search-across-data-stores.md)
* [Query open archives in place](query-open-archives-in-place.md)
* [Read from data stores](../collect/read-from-data-stores.md)
* [Transpilation](../../explanations/transpilation.md)
* [Pipeline](../../explanations/pipeline.md)
* [Optimizations](../../reference/optimizations.md)
