---
title: "KQL"
canonical: https://tenzir.com/docs/reference/optimizations/kql
source: https://tenzir.com/docs/reference/optimizations/kql.md
section: "Docs"
---

# KQL

> The KQL sources frommicrosoftdefender and fromazureloganalytics use the where, select, and head operators that follow them to append stages to your Kusto Query Language (KQL) query, so that the service returns fewer rows and columns. This page describes how the query changes, which filters reach the service, and what stays in Tenzir. Our optimizations overview explains how Tenzir optimizes pipelines in general.

The KQL sources [`from_microsoft_defender`](https://tenzir.com/docs/reference/operators/from_microsoft_defender.md) and [`from_azure_log_analytics`](https://tenzir.com/docs/reference/operators/from_azure_log_analytics.md) use the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators that follow them to append stages to your Kusto Query Language (KQL) query, so that the service returns fewer rows and columns. This page describes how the query changes, which filters reach the service, and what stays in Tenzir. Our [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## How the query changes

The operator sends your query as you wrote it and appends up to four stages, each on a new line, in this order:

1. For Defender, a `take` stage with its [result cap](kql.md#result-cap), if a `where` stage follows.
2. A `where` stage with the [prefilters](kql.md#filters-are-prefilters) of the [`where`](https://tenzir.com/docs/reference/operators/where.md) operators that follow the source.
3. A `project` stage with the top-level fields that the pipeline reads.
4. A `take` stage with the limit of a [`head`](https://tenzir.com/docs/reference/operators/head.md), if no [`where`](https://tenzir.com/docs/reference/operators/where.md) precedes it.

The stages apply to the rows that your query returns, so they work with any query that produces a single table, including joins and aggregations. For example, the pipeline

```tql
from_microsoft_defender "DeviceNetworkEvents | where ActionType == 'ConnectionSuccess'",
  azure_auth={
    tenant_id: secret("AZURE_TENANT_ID"),
    client_id: secret("AZURE_CLIENT_ID"),
    client_secret: secret("AZURE_CLIENT_SECRET"),
  }
where RemotePort >= 443
select RemoteUrl
```

sends this query:

```text
DeviceNetworkEvents | where ActionType == 'ConnectionSuccess'
| take 100000
| where (gettype(column_ifexists('RemotePort', dynamic(null))) !in ("int", "long", "real", "double") or todouble(column_ifexists('RemotePort', dynamic(null))) >= 443.0)
| project ['RemoteUrl'] = column_ifexists('RemoteUrl', dynamic(null)), ['RemotePort'] = column_ifexists('RemotePort', dynamic(null))
```

The operator doesn’t know which columns and types your query returns before it runs. It therefore reads every field with `column_ifexists`, so that a field that your query doesn’t return is `null` instead of failing the query.

In a query with several tabular statements separated by `;`, the stages apply to the last statement. Defender returns only the table of the first statement, so the stages don’t reduce what it returns, and Tenzir evaluates every operator locally as usual.

## Filters are prefilters

KQL types don’t map one-to-one to TQL types. For example, a `guid` or `decimal` column arrives as a string, and in Log Analytics, a `dynamic` string that holds JSON, such as `"443"`, arrives as the decoded value. A pushed predicate therefore only preselects candidates: it compares a value only where KQL reports the type that the literal requires, and keeps every row of another type. Tenzir then evaluates every original predicate locally, including those that the operator sent, so the result is the same as without the optimization.

A predicate splits at `and`: the parts that translate go into the query, and the rest runs only in Tenzir. An `or` goes into the query only if all of its operands translate. For example, `where (Port > 1024 or Name.match_regex("^a")) and Name == "alice"` appends a prefilter for `Name == "alice"` only.

### Filters that the service evaluates

These predicates on top-level fields go into the query:

* Comparisons with `==`, `<`, `<=`, `>`, and `>=` between a field and a number.
* Equality between a field and a string or a boolean, including a bare boolean field, as in `where Flag`.
* Membership with `in` and a list of literals of a single kind: only strings, only numbers, or only booleans.
* Case-sensitive `starts_with`, `ends_with`, and substring search with `"needle" in haystack`. KQL matches these byte for byte, without Unicode normalization, as TQL does.
* Presence checks with `!= null`.
* The boolean operators `and` and `or` of these predicates.

Numeric prefilters compare values as KQL `real` numbers. Integer literals from −2^53 through 2^53 are supported, including both endpoints. At either endpoint, a strict `<` or `>` becomes `<=` or `>=` in the prefilter so that rounding doesn’t discard a matching row. For example, `x > 9007199254740992` uses `todouble(...) >= 9007199254740992.0` remotely. Tenzir still evaluates the original strict comparison locally.

### Filters that stay in Tenzir

Everything else runs only in Tenzir, with the same result. This includes:

* Negation with `not`, inequality with `!=` against a value, and `== null`.
* Lists that mix kinds or contain `null`, such as `x in ["a", 443]`.
* Ordering comparisons with strings.
* Regular expressions, case-insensitive matching with `ignore_case=true`, IP addresses and subnets, and `time` values.
* Arithmetic, comparisons between two fields, and other function calls, such as `Name.to_lower() == "alice"` or `int(x, base=16) == 16`.
* Nested fields, such as `Process.Name`.
* String literals with invalid UTF-8, integer literals beyond ±2^53, and floating-point literals with an absolute value of 2^53 or greater.

Prefilters that would make the appended text exceed 16 KiB also stay local.

## Result cap

The Microsoft Graph v1.0 [advanced-hunting quotas](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0#quotas-and-resource-allocation) limit Defender query results to 100,000 rows. The [`huntingQueryResults` response type](https://learn.microsoft.com/en-us/graph/api/resources/security-huntingqueryresults?view=graph-rest-1.0) doesn’t document a truncation indicator, so a successful response doesn’t guarantee that you received every matching row. A prefilter after your query would see all rows, so it could return matches that your query alone would never deliver. [`from_microsoft_defender`](https://tenzir.com/docs/reference/operators/from_microsoft_defender.md) therefore appends `take 100000` before the prefilters. On a sorted result, `take` keeps the same first rows as the cap. The cap doesn’t apply to the `project` stage or the `take` stage of a limit, which keep your query’s rows or a prefix of them.

Log Analytics returns at most 500,000 rows and about 100 MiB of data, and reports a result beyond either limit as a partial failure, which [`from_azure_log_analytics`](https://tenzir.com/docs/reference/operators/from_azure_log_analytics.md) rejects with an error. Its prefilters therefore run without a cap: they yield the complete filtered result, or fail as well if the filtered result still exceeds a limit. A cap would instead turn the error into a silently incomplete result.

Size limits, such as the 50 MB limit of Defender, fail the request with an error instead of truncating it. A pushed filter or projection makes the result smaller and may thus avoid such an error, in which case you get the complete result instead.

## Projections

The `project` stage keeps the top-level fields that [`select`](https://tenzir.com/docs/reference/operators/select.md) and later operators read, plus every field that a predicate reads, since Tenzir evaluates the predicates on the projected rows. A selected nested field, such as `Process.Name`, keeps its top-level field `Process`. When the pipeline reads the whole event, such as with `this`, the operator appends no `project` stage.

## Limits

A [`head`](https://tenzir.com/docs/reference/operators/head.md) becomes a `take` stage only if no [`where`](https://tenzir.com/docs/reference/operators/where.md) precedes it and its limit is between 1 and 2,147,483,647. Since every predicate runs locally after the query, a `take` would otherwise truncate rows before Tenzir filters them. Tenzir enforces the limit locally in every case.

## Time window

The operator never narrows the `start` and `end` window based on a predicate. A time field in your query’s output, such as `Timestamp` or `TimeGenerated`, may stem from an aggregation, a rename, or a computation, so a predicate on it doesn’t reliably refer to the time that the window selects. Such predicates run in Tenzir. Use `start` and `end`, or a time predicate in your query, to bound the request.

## Queries that stay unchanged

The operator sends the query unchanged, and runs every operator in Tenzir, if an appended stage might not apply to the query’s output or might break the query. This is the case for:

* Management commands, which start with a `.`.
* Queries that use `render`, `fork`, or `facet`, since `render` must end a query and the others return several tables.
* Queries with a `set` statement, such as `set notruncation` or `set query_take_max_records`, which can change how the service limits a result.
* Queries that end in `;` or `|`.
* Queries that the operator can’t tokenize, such as one with an unterminated string literal.
* Queries that contain only whitespace and comments.

Words in string literals and comments don’t count, so `where Action == "render"` still receives stages.

## Verify an optimization

Print the optimized pipeline to see which hints the source received:

```sh
tenzir --dump-opt-ir 'from_microsoft_defender "DeviceEvents", azure_auth={tenant_id: secret("AZURE_TENANT_ID"), client_id: secret("AZURE_CLIENT_ID"), client_secret: secret("AZURE_CLIENT_SECRET")} | where DeviceName == "host-a" | head 10'
```

The source shows the predicates as `filter`, the limit as `limit`, and the fields as `projection`, and the [`where`](https://tenzir.com/docs/reference/operators/where.md) that it took over no longer appears. The [compilation output guide](../../guides/troubleshooting/inspect-compilation-output.md) explains the format. The output doesn’t show the appended KQL stages, which follow the rules on this page.
