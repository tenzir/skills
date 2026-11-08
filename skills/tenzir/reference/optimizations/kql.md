---
title: "KQL"
canonical: https://tenzir.com/docs/v7.0.0/reference/optimizations/kql
source: https://tenzir.com/docs/v7.0.0/reference/optimizations/kql.md
section: "Docs"
---

# KQL

> The KQL sources frommicrosoftdefender and fromazureloganalytics hand the service the operators that follow them by appending stages in the Kusto Query Language (KQL) to your query, so that the service returns only what the pipeline keeps. Those operators leave the pipeline and run in the service, with KQL’s semantics. This page describes which operators the service takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our optimizations overview explains how Tenzir optimizes pipelines in general.

The KQL sources [`from_microsoft_defender`](https://tenzir.com/docs/v7.0.0/reference/operators/from_microsoft_defender.md) and [`from_azure_log_analytics`](https://tenzir.com/docs/v7.0.0/reference/operators/from_azure_log_analytics.md) hand the service the operators that follow them by appending stages in the Kusto Query Language (KQL) to your query, so that the service returns only what the pipeline keeps. Those operators leave the pipeline and run in the service, with KQL’s semantics. This page describes which operators the service takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator sends your query and appends the operators that follow as further stages, each on a new line, so that they apply to the table that your query returns, also after joins and aggregations. It takes over no operator, and sends your query as you wrote it, if an appended stage might not apply to your query’s result or might change how it parses:

* Management commands, which start with a `.`.
* Queries that use `render`, `fork`, or `facet`, since `render` must end a query and the others return several tables.
* Queries with a `set` statement, such as `set notruncation`, which can change how the service limits a result.
* Queries with several tabular statements separated by `;`, since the service returns a table for each of them. Statements with `let`, `declare`, or `alias` before the final one are fine.
* Queries that end in `;` or `|`, that contain only whitespace and comments, or that the operator can’t tokenize, such as one with an unterminated string.

Words in string literals and comments don’t count, so `where Action == "render"` still receives stages. The operator also takes over nothing with `pushdown=false`, which keeps every operator in Tenzir with TQL semantics and sends your query exactly as written.

## Operators that the service takes over

The operator takes over the longest run of operators directly after it that KQL can spell:

* [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), as the [filters](kql.md#filters) section describes.
* [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) of top-level fields, including renames, which becomes `project`.
* [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md) of top-level fields, which becomes `project-away`.
* [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) with group keys on fields and `count()`, `count(x)`, `min(x)`, `max(x)`, and `sum(x)` of fields, which becomes `summarize … by`. This includes [`top`](https://tenzir.com/docs/v7.0.0/reference/operators/top.md) and [`rare`](https://tenzir.com/docs/v7.0.0/reference/operators/rare.md). The summary may follow [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), and assignments that copy fields, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md) by fields, which becomes `sort by` with an explicit direction.
* [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), which becomes `take`.

The first operator that KQL cannot spell ends the run, and so does an operator that would make the appended stages longer than 16 KiB, since both services limit the size of a query. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) at `and`, so the service can still take over the conjuncts that it spells. For example, the pipeline

```tql
from_microsoft_defender "DeviceNetworkEvents",
  azure_auth={
    tenant_id: secret("AZURE_TENANT_ID"),
    client_id: secret("AZURE_CLIENT_ID"),
    client_secret: secret("AZURE_CLIENT_SECRET"),
  }
where RemotePort != null
summarize Allowed, events=count()
sort -events
head 2
```

sends this query:

```text
DeviceNetworkEvents
| where isnotnull(['RemotePort'])
| summarize ['__tenzir_column_0'] = count() by ['Allowed']
| sort by ['__tenzir_column_0'] desc
| take 2
```

Tenzir arranges the result columns into the fields of the pipeline, such as `events`. Without an operator that enumerates the fields, the query ends with a `project` of the top-level fields that the pipeline reads, each as `column_ifexists(…)`, which keeps the type of a column that your query returns and yields `null` for one that it doesn’t. Tenzir leaves out a projection that would exceed the 16 KiB.

## Filters

Filters become `where` stages. They consist of top-level fields, literals, comparisons, `in` with a list, arithmetic, `and`, `or`, `not`, `== null` and `!= null`, and these functions, without named arguments such as `ignore_case`:

| TQL                                       | KQL                                        |
| ----------------------------------------- | ------------------------------------------ |
| `x == null`, `x != null`                  | `isnull(x)`, `isnotnull(x)`                |
| `x.starts_with("a")`, `x.ends_with("a")`  | `x startswith_cs "a"`, `x endswith_cs "a"` |
| `"a" in x`                                | `x contains_cs "a"`                        |
| `x.match_regex("a")`                      | `x matches regex "a"`                      |
| `x.to_lower()`, `x.to_upper()`            | `tolower(x)`, `toupper(x)`                 |
| `x.length_chars()`, `x.abs()`, `x.trim()` | `strlen(x)`, `abs(x)`, `trim(@"\s+", x)`   |
| `x in 10.0.0.0/8`                         | `ipv4_is_in_range(x, "10.0.0.0/8")`        |

Literals are strings, numbers, booleans, times as `datetime(…)` and durations as `timespan(…)`, both in whole multiples of 100 nanoseconds, and IP addresses as their canonical text. Ordering comparisons with a string, nested fields such as `Process.Name`, field names with `*`, the literal `null` outside a comparison, non-finite numbers, and optional fields such as `x?` stay in Tenzir.

## KQL semantics

The operators that the service takes over run as KQL runs them, which can differ from TQL:

* KQL is statically typed. A field that your query doesn’t return, `sum` of a string, and `summarize` or `sort` by a `dynamic` column fail the query with the service’s error. Comparing a string column with a number matches no rows, and comparing a number column with a string converts the string.
* Strings are never `null` in KQL: a missing string is the empty string. So `x == null` doesn’t match it, and `count(x)`, which becomes `countif(isnotempty(x))`, doesn’t count it.
* IP addresses compare as text, so `RemoteIP == 2001:db8::1` doesn’t match another spelling of the same address. Subnet membership parses addresses.
* Integer division truncates, and arithmetic follows KQL’s types.
* `summarize` keeps a group for `null` keys. `sort` puts `null` first in ascending and last in descending order, and compares strings by their characters.
* A name that a `let` statement of your query binds shadows a column of the same name in an appended stage.
* A query that the service rejects fails the pipeline with a hint to use `pushdown=false`.

Summaries with `mean` or other functions stay in Tenzir.

## Result cap

Defender returns at most 100,000 rows of a query without reporting a truncation, so [`from_microsoft_defender`](https://tenzir.com/docs/v7.0.0/reference/operators/from_microsoft_defender.md) warns when a result has exactly that many rows, unless a [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) that the service took over explains it. Narrow the query or its time range to get the complete result.

Log Analytics returns at most 500,000 rows and about 100 MiB of data, and reports a result beyond either limit as a partial failure, which [`from_azure_log_analytics`](https://tenzir.com/docs/v7.0.0/reference/operators/from_azure_log_analytics.md) rejects with an error. Operators that the service takes over make the result smaller and may thus avoid such an error.

## Time window

The operator never narrows the `start` and `end` window based on an operator. A time field in your query’s output, such as `Timestamp` or `TimeGenerated`, may stem from an aggregation, a rename, or a computation, so a filter on it doesn’t reliably refer to the time that the window selects. Such filters still run in the service. Use `start` and `end`, or a time filter in your query, to bound the request.

## Verify an optimization

To see the operators that the service takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_microsoft_defender "DeviceEvents", azure_auth={tenant_id: secret("AZURE_TENANT_ID"), client_id: secret("AZURE_CLIENT_ID"), client_secret: secret("AZURE_CLIENT_SECRET")} | where DeviceName == "host-a" | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`. The [compilation output guide](../../guides/troubleshooting/inspect-compilation-output.md) explains the format.
