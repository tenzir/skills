---
title: "Transpilation"
description: "Understand how Tenzir compiles TQL operators after a remote source into the target's native query language, how native semantics differ from TQL, and when operators stay in Tenzir."
canonical: https://tenzir.com/docs/explanations/transpilation
source: https://tenzir.com/docs/explanations/transpilation.md
section: "Docs"
---

# Transpilation

> Understand how Tenzir compiles TQL operators after a remote source into the target's native query language, how native semantics differ from TQL, and when operators stay in Tenzir.

TQL works as a single query frontend across heterogeneous data systems. When a pipeline reads from a database, a SIEM, or an API and follows the source with operators such as [`where`](../reference/operators/where.md), [`select`](../reference/operators/select.md), [`drop`](../reference/operators/drop.md),

[`summarize`](../reference/operators/summarize.md), [`sort`](../reference/operators/sort.md), or [`head`](../reference/operators/head.md), Tenzir compiles those operators into the remote system’s native language (SQL, KQL, SPL, PowerQuery, or API query parameters) and executes them where the data lives. That mechanism is called **pushdown**, and you can disable it per source with `pushdown=false`.

The main use case is **federated search**: you write one TQL pipeline instead of learning a separate dialect for every store, and each remote system, its **target**, returns only the rows or summary groups your pipeline keeps instead of transferring everything Tenzir would discard. For example, take this pipeline:

```tql
from_mysql table="alerts", host="db.example.com", database="soc"
where severity >= 3
select id, message
head 10
```

Instead of fetching the entire `alerts` table, [`from_mysql`](../reference/operators/from_mysql.md) transpiles the three operators into SQL:

```sql
SELECT `id`, `message`
FROM `alerts`
WHERE `severity` >= 3
LIMIT 10
```

The same mechanism compiles aggregations and computed expressions into each target’s dialect. A `summarize` after [`from_clickhouse`](../reference/operators/from_clickhouse.md) becomes a `GROUP BY` query, after [`from_microsoft_defender`](../reference/operators/from_microsoft_defender.md) or [`from_axiom`](../reference/operators/from_axiom.md) becomes `extend` and `summarize` stages in KQL or APL, after [`from_splunk`](../reference/operators/from_splunk.md) becomes `eval` and `stats` stages in SPL, and after

[`from_sentinelone_data_lake`](../reference/operators/from_sentinelone_data_lake.md) becomes `let` and `group` stages in PowerQuery.

Our [optimizations reference](../reference/optimizations.md) lists every source and compares what each target computes. This page explains the execution model behind transpilation, why results can differ from local TQL, and how Tenzir plans the boundary between remote and local execution.

## Transpiled targets vs. local hints

The pipeline optimizer propagates downstream requirements (predicates, field projections, row limits, summaries, and ordering) toward the source before a pipeline runs, as our explanation of [pipeline optimization](pipeline.md#optimization) describes. Sources act on those requirements in two fundamentally different ways:

* **Transpiled remote targets** absorb eligible downstream operators, remove them from the Tenzir pipeline, and compile them into the request sent to the remote system. Because the absorbed operators no longer run in Tenzir, their results follow the target’s native semantics. Any operator the target cannot transpile stays in the pipeline and runs in Tenzir with TQL semantics.
* **Local and hint-based sources**, such as [`read_parquet`](../reference/operators/read_parquet.md), [`subscribe`](../reference/operators/subscribe.md), and [`from_microsoft_365_activity`](../reference/operators/from_microsoft_365_activity.md), treat the optimizer’s requirements as physical hints: they skip Parquet row groups or columns, filter before queuing, skip blobs by metadata, or stop decoding once a limit is met, and parsers that learn order does not matter can split work across parallel jobs. The downstream [`where`](../reference/operators/where.md), [`select`](../reference/operators/select.md), and [`head`](../reference/operators/head.md) operators remain in the pipeline and run on the emitted events, so the output always keeps exact TQL semantics.

[`from_velociraptor`](../reference/operators/from_velociraptor.md) pushes nothing down because a VQL query may have side effects that a filter or limit would alter.

## Native semantics vs. TQL semantics

Once a target takes over an operator, the target executes it according to its own type system, null rules, collation, and error handling. Results can therefore differ from running the same pipeline locally in Tenzir:

* **Null handling and filters.** In SQL, comparing any value with `NULL` yields `NULL`, so `where name != "alpha"` drops rows where `name` is `NULL`, whereas in SentinelOne PowerQuery `x != "a"` also matches events without `x`. In KQL, strings are never `null` (a missing string is `""`).
* **Case sensitivity and collations.** MySQL and SQL Server compare, group, and sort text using column collations that ignore case by default, and Splunk’s base `search` command matches text case-insensitively.
* **Sorting and ties.** Each target chooses where `null` sorts (first or last in ascending order) and returns tied rows or groups in any order.
* **Functions and empty groups.** Targets apply their own arithmetic, rounding, regex engines, and domain rules. For example, DuckDB and SQL Server fail the query on `sqrt` of a negative number or `log` of zero or less instead of returning `null`, and empty-group aggregations return target defaults (`0`, `NaN`, `Infinity`, or type defaults) rather than `null`.
* **Missing fields and strict schemas.** Databases and KQL reject references to columns that do not exist, whereas Tenzir warns and substitutes `null`.

Each target’s page in the [optimizations reference](../reference/optimizations.md) documents its exact semantic differences.

To force TQL semantics for every operator, set `pushdown=false` on the source. The source then transpiles no operators and runs everything after it in Tenzir, while still narrowing the columns it fetches to the fields the pipeline reads.

## How transpilation plans a pipeline

All remote sources share the same planning rules, regardless of their target language.

### The run of operators after the source

A remote source transpiles the longest contiguous run of operators directly after it that its target can express: [`where`](../reference/operators/where.md), [`select`](../reference/operators/select.md),

[`drop`](../reference/operators/drop.md), [`summarize`](../reference/operators/summarize.md), [`sort`](../reference/operators/sort.md), and [`head`](../reference/operators/head.md), as well as [`top`](../reference/operators/top.md) or [`rare`](../reference/operators/rare.md) followed by [`head`](../reference/operators/head.md). The first operator the target cannot express ends the run. That operator and everything after it run in Tenzir, even if the target could express a later operator.

Tenzir splits a top-level [`where`](../reference/operators/where.md) at `and`, so the target still transpiles every conjunct it understands while the rest stays local. In

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3 and message.parse_json().level == "high"
```

DuckDB transpiles `severity >= 3` into SQL, and Tenzir runs `parse_json` on the matching rows DuckDB returns.

### Plan-time decisions and diagnostics

The source decides which operators to transpile from the pipeline structure alone, before contacting the target, and never silently falls back to local execution at runtime. If the target rejects the generated query or the source cannot bind a field once it inspects the table schema, the pipeline fails with a diagnostic pointing you to `pushdown=false`:

* **The target rejects the request.** The source reports the target’s error with a note and a hint:

  ```text
  error: Conversion Error: Could not convert string 'many' to INT32


  LINE 1: SELECT * FROM "keyed" WHERE ("n" = 'many')
                                             ^^^^^^^
    = note: DuckDB computes the stages that the operator took over with its own semantics
    = hint: use `pushdown=false` to run them in Tenzir
  ```

  This note and hint appear only when the source transpiled at least one operator. With `pushdown=false`, you see the target’s error alone.

* **The source cannot plan the operators for what it reads.** Sources that inspect target metadata at runtime, such as ClickHouse table columns, fail before sending the query when a field cannot be bound:

  ```text
  error: ClickHouse cannot compute the stages that the operator took over
    = note: cannot bind `al`: `al` is an `ALIAS` column, which `SELECT *` includes only depending on the session's settings
    = hint: use `pushdown=false` to run them in Tenzir
  ```

### Summaries and computed expressions

A target that supports summaries returns one row per group instead of every matching row. This applies when the source runs a bounded read (so not with `live=true`), every filter before the summary also transpiled, and the target computes every aggregation function in the [`summarize`](../reference/operators/summarize.md).

The summary can sit directly after the source or behind operators that keep every event while selecting, dropping, renaming, copying, or computing fields:

* [`select`](../reference/operators/select.md) and [`drop`](../reference/operators/drop.md) that retain the fields the summary reads.
* Renames and copies via [`select`](../reference/operators/select.md), [`set`](../reference/operators/set.md), or assignments such as `select ip=src_ip` or `ip = src_ip`. Every right-hand side reads the original event, so `select a=b, b=a` swaps the fields and the summary reads them swapped.
* Computed group keys and aggregate arguments assigned before the summary, which SQL targets inline into the aggregate expression, [`from_splunk`](../reference/operators/from_splunk.md) computes with `eval`, KQL and APL sources compute with `extend`, and [`from_sentinelone_data_lake`](../reference/operators/from_sentinelone_data_lake.md) computes with `let` before `group`.

An assignment that the summary reads may be fallible (such as a function call) because the target evaluates it with its own semantics. An assignment that the summary does not read, including one shadowed by a later assignment, must be infallible; otherwise the target would skip it and hide a runtime error that Tenzir would report. If an unused assignment is fallible, or if a computed expression uses a function the target cannot transpile, the summary runs in Tenzir.

A target that transpiles a summary also transpiles the [`where`](../reference/operators/where.md),

[`sort`](../reference/operators/sort.md), and [`head`](../reference/operators/head.md) directly after it so the target returns only the kept groups:

```tql
from_clickhouse table="events", host="clickhouse.example.com", tls=false
where severity >= 3
summarize src_ip, events=count()
where events >= 10
sort -events, src_ip
head 20
```

Here ClickHouse runs the pre-filter, groups by `src_ip`, filters groups with `events >= 10`, sorts the groups, and returns at most 20 rows. The

[`top`](../reference/operators/top.md) and [`rare`](../reference/operators/rare.md) operators followed by [`head`](../reference/operators/head.md) transpile the same way.

### Aggregation input projections

A final [`summarize`](../reference/operators/summarize.md) also tells the source which input columns it needs, so the source fetches only those columns even when `pushdown=false` or when the target cannot compute the summary itself:

```tql
from_mysql table="events", host="db.example.com", database="soc", pushdown=false
summarize host, events=count(), bytes=sum(bytes)
head 10
```

Even with `pushdown=false`, [`from_mysql`](../reference/operators/from_mysql.md) reads only `host` and `bytes`:

```sql
SELECT `host`, `bytes`
FROM `events`
```

Tenzir then runs the summary locally and keeps at most 10 summary rows. These rules preserve aggregation behavior:

* All grouping keys and aggregate arguments stay required, even if a later selection drops them, because evaluating them can emit diagnostics.
* Output aliases (such as `events`) do not request source columns.
* A keyless `summarize events=count()` needs only the row count; a source may read one column or emit a placeholder per row to preserve it.
* Whole-event access (`collect(this)`) and dynamic field access (`sum(this[key])`) prevent column narrowing.
* Unresolved summaries inside runtime-bound subpipelines ([`group`](../reference/operators/group.md), [`window`](../reference/operators/window.md)) and order-sensitive or periodic summaries keep their barriers and do not narrow the enclosing source.

### Time windows

Sources with explicit time-range APIs ([`from_splunk`](../reference/operators/from_splunk.md) with `index`,

[`from_sentinelone_data_lake`](../reference/operators/from_sentinelone_data_lake.md) without `query`, [`from_amazon_cloudwatch`](../reference/operators/from_amazon_cloudwatch.md), and [`from_microsoft_365_activity`](../reference/operators/from_microsoft_365_activity.md)) narrow their request window from timestamp comparisons in downstream filters:

| Filter                              | Request window                                                                |
| ----------------------------------- | ----------------------------------------------------------------------------- |
| `>=`, `<=`, and `==` with a time    | Includes the bound                                                            |
| `>` and `<` with a time             | Excludes the bound (shifts by 1 ns before rounding to the target’s unit)      |
| Strict comparison beyond time range | Empty window; completes without a request unless a summary still yields a row |
| `and` of comparisons                | Intersection of windows                                                       |
| `or` of comparisons                 | Enclosing range covering both windows                                         |

Each source rounds outward to the unit its API accepts (for example, whole seconds in Splunk or milliseconds in SentinelOne and CloudWatch). The original filter comparisons remain in the query or pipeline, so narrowing the window never changes the result.

## Completeness, row limits, and truncation

Remote systems enforce their own result caps, memory ceilings, and sampling policies. Tenzir surfaces those limits instead of silently dropping data:

* **Silent server caps become warnings.** Microsoft Defender caps query results at 100,000 rows without flagging truncation, so [`from_microsoft_defender`](../reference/operators/from_microsoft_defender.md) warns when a response hits 100,000 rows without an explicit matching [`head`](../reference/operators/head.md). SentinelOne PowerQuery caps unbounded queries at 1,000 rows by default, so Tenzir appends `| limit 1600000` when no [`head`](../reference/operators/head.md) is present and warns if a result reaches 1,600,000 rows (simple `where` + `head` reads without `query` use uncapped paged LOG queries instead).
* **Explicit server limits fail or warn.** ClickHouse table reads configure the server to fail rather than return partial results when hitting profile limits such as `max_result_rows`, and Azure Log Analytics partial-failure responses (beyond 500,000 rows or \~100 MiB) fail the pipeline. CloudWatch Live Tail sampling and SentinelOne partial-result warnings propagate as pipeline warnings.
* **Transpilation helps stay under limits.** Pushing filters, projections, and summaries into the target shrinks the returned payload, often avoiding server caps that a raw table read would hit.

## Inspect a transpiled pipeline

To see exactly which operators a source transpiled and why the run stopped, print the optimized pipeline IR:

```sh
tenzir --dump-opt-ir 'from_mysql table="logins" | where user == "admin" | head 10'
```

Every remote source lists the transpiled stages under `plan` and the reason the run ended under `declined`. Absorbed [`where`](../reference/operators/where.md), [`select`](../reference/operators/select.md),

[`summarize`](../reference/operators/summarize.md), [`sort`](../reference/operators/sort.md), or [`head`](../reference/operators/head.md) operators no longer appear downstream of the source. Hint-based sources instead display their received `filter`, `limit`, and `projection` hints while keeping the downstream operators in place.

To inspect the generated native request itself, check the target’s query log (such as ClickHouse’s `system.query_log`). When Splunk reports an error or warning, or when SentinelOne rejects a query, Tenzir includes the exact request it sent in the diagnostic.

## See also

* [Push queries to data stores](../guides/search/push-queries-to-data-stores.md)
* [Search across data stores](../guides/search/search-across-data-stores.md)
* [Query open archives in place](../guides/search/query-open-archives-in-place.md)
* [Optimizations](../reference/optimizations.md)
* [Pipeline](pipeline.md)
* [Executor](executor.md)
