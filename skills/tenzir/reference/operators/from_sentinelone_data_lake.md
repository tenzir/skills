---
title: "from_sentinelone_data_lake"
canonical: https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake
source: https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md
section: "Docs"
---

# from_sentinelone_data_lake

> Queries SentinelOne Singularity Data Lake with TQL.

Queries SentinelOne Singularity Data Lake with TQL.

```tql
from_sentinelone_data_lake url:string, token=string,
                           [query=string, start=time, end=time,
                            account_ids=list<string>, tenant=bool, timeout=duration, raw=bool,
                            pushdown=bool]
```

## Description

The `from_sentinelone_data_lake` operator hands SentinelOne the operators that follow it, such as [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), [`sort`](https://tenzir.com/docs/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md), which then run in SentinelOne with SentinelOne’s semantics. You don’t need to write PowerQuery or pass `query`, `start`, or `end`:

```tql
let $end = now()
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token")
where timestamp >= $end - 1h and timestamp < $end
where severity > 3 and message.starts_with("alert")
head 100
```

Bind relative times with `let` so the optimizer receives fixed timestamps. Without `query`, `start`, and `end`, SentinelOne must take over a [`where`](https://tenzir.com/docs/reference/operators/where.md), [`head`](https://tenzir.com/docs/reference/operators/head.md), or [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md). Otherwise the operator reports an error before contacting SentinelOne. For example, a bare source or a `match_regex` filter, which stays in Tenzir, cannot supply the query.

Pipelines with only [`where`](https://tenzir.com/docs/reference/operators/where.md) and [`head`](https://tenzir.com/docs/reference/operators/head.md) retrieve complete parsed events, including fields that the pipeline never names. A [`select`](https://tenzir.com/docs/reference/operators/select.md) or [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) makes SentinelOne return only the columns or groups that the pipeline keeps. The operator chooses automatically; you do not need a retrieval flag.

You can provide `query` to write the PowerQuery yourself. The operator uses SentinelOne’s Long Running Query (LRQ) API on your tenant’s console host: it launches queries at `/sdl/v2/api/queries`, polls once per second, and reads completed results. Reads of whole events use LOG search with cursor continuation, and all other reads use PowerQuery (PQ). Each completed server-side query is deleted before its events are emitted, including when a downstream operator stops after the first event.

When you omit `query`, timestamp predicates supply missing time bounds. For a request that satisfies the constraint requirement, any remaining missing bound defaults: `end` to the current time and `start` to 24 hours before `end`. The default time window does not itself satisfy that requirement: a bare source still errors before contacting SentinelOne. The operator sends both time bounds explicitly and requests low query priority.

It retries rate-limited launches and transient HTTP or connection errors during polling, up to five attempts, and honors `Retry-After`. It does not retry a launch after a connection error or an ambiguous HTTP `5xx` response because the server may already have created the query. Launch retries wait for `Retry-After` within the operator’s total `timeout` budget. During polling, if the requested delay would exceed the active query’s keep-alive budget, the operator stops instead of retrying early. Invalid `Retry-After` headers, including delays outside the supported numeric range, fail the query rather than trigger a shorter fallback delay.

Migration from the V1 API

Replace regional URLs such as `https://xdr.eu1.sentinelone.net` with your console URL, `https://<tenant>.sentinelone.net`. Replace scoped SDL Log Read keys with a console service-user API token. There is no fallback to `/api/powerQuery`, which SentinelOne retires on February 15, 2027.

### `url: string`

The base URL of your tenant’s SentinelOne console, for example `https://<tenant>.sentinelone.net`.

Use HTTPS for your console. Regional `xdr.*.sentinelone.net` URLs are no longer supported.

### `token = string`

A console service-user API token. The operator sends it with Bearer authentication, not the `ApiToken` prefix used by the management API.

Use the [`secret()`](https://tenzir.com/docs/reference/functions/secret.md) function to reference credentials securely.

### `query = string (optional)`

A native PowerQuery to use instead of constructing the query entirely from TQL. It must not be empty when provided. The operator keeps its time window and appends the operators that SentinelOne takes over as further stages, which apply to the query’s result. Without such operators, it sends the query unchanged. Omit this argument for TQL-only queries.

For native queries, refer to the [SentinelOne PowerQuery documentation](https://support.sentinelone.com/hc/en-us/articles/360004195934).

### `start = time (optional)`

The start time for the query time range.

Events at or after this time are included. When you omit `query`, a supported TQL timestamp predicate can supply this bound. Otherwise it defaults to 24 hours before `end`. An explicit value is a hard lower bound. When you omit `query`, TQL can narrow it but cannot widen it. Fractional seconds retain nanosecond precision.

### `end = time (optional)`

The end time for the query time range.

Events before this time are included. When you omit `query`, a supported TQL timestamp predicate can supply this bound. Otherwise it defaults to the current time when the operator starts. An explicit value is a hard upper bound.

### `account_ids = list<string> (optional)`

The account IDs to query. The list must not be empty.

When omitted, the operator requests tenant scope. On some multi-account tenants, that scope selects a default account that may not contain your data. If a query unexpectedly returns no rows, specify the account IDs containing the data. The operator sends `tenant: false` together with `accountIds` when you set this argument.

### `tenant = bool (optional)`

Whether to query every account that the token can access when you omit `account_ids`.

Defaults to `true`, which suits console and service-user API tokens. Set it to `false` for a SentinelOne Data Lake (SDL) API key, which scopes its queries to its own account and finds no events with tenant scope. You cannot set `tenant=true` together with `account_ids`.

### `timeout = duration (optional)`

The total time budget for launching and polling queries, including all pages and retry delays. Must be greater than zero. Defaults to `3min`.

When the budget expires, the operator attempts to delete the active server-side query and reports an error. Earlier pages may already have been emitted; that run is incomplete. Cleanup can take additional time. Increase this value for longer reads, for example `timeout=5min`, or narrow the search. Neither successful polls nor new pages reset the budget.

### `raw = bool (optional)`

Whether to skip parsing strings as typed data.

Defaults to `false`. Dotted attribute names still become nested records, `timestamp` metadata remains a time value, and counts remain integers.

### `pushdown = bool (optional)`

Whether SentinelOne takes over the operators that follow the operator. With `pushdown=false`, they stay in the pipeline and run with TQL semantics. See [Optimizations](from_sentinelone_data_lake.md#optimizations).

Defaults to `true`.

## Optimizations

The operator hands SentinelOne the operators that follow it, as far as PowerQuery can spell them: [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) with `count()` and `count(x)`, including [`top`](https://tenzir.com/docs/reference/operators/top.md) and [`rare`](https://tenzir.com/docs/reference/operators/rare.md), [`sort`](https://tenzir.com/docs/reference/operators/sort.md) after a [`select`](https://tenzir.com/docs/reference/operators/select.md) or [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md). Those operators leave the pipeline and run with SentinelOne’s semantics, which can differ from TQL. For example, `x != "a"` also matches events without `x`. Comparisons of `timestamp` also narrow the time window of the request. Use `pushdown=false` to keep every operator in the pipeline.

Our [SentinelOne optimization reference](../optimizations/sentinelone.md) describes which operators SentinelOne takes over, how they spell in PowerQuery, how the operator reads the results, and where SentinelOne’s semantics differ.

## Limitations

* A `query` without operators that SentinelOne takes over keeps the default cap of 1,000 rows for queries without `limit` or `group`, which the operator reports as a warning. Add `| limit N` to the query to request more. Other PowerQuery reads end in `| limit 1600000` and warn when they reach it.
* Output order is not guaranteed without a [`sort`](https://tenzir.com/docs/reference/operators/sort.md). LOG pages are separate queries, not a snapshot of a changing data lake.
* Results that SentinelOne reports as partial or with omitted events arrive with a warning. Unreported API-side omissions cannot be detected.
* SentinelOne expires queries 30 seconds after the last poll and kills queries after five minutes. An expired or killed query fails with HTTP `404`; the operator does not relaunch it automatically.
* Graceful shutdown deletes an active query. Forced cancellation during polling relies on the server’s 30-second expiry. Checkpointing is not supported.

## Examples

### Query historical events with TQL

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token")
where timestamp >= 2024-01-01 and timestamp < 2024-01-02
where severity > 3
select timestamp, message
head 100
```

### Use a native PowerQuery

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token"),
  query="severity > 3 | columns id",
  account_ids=["1234567890123456789"],
  start=now()-10d,
  end=now()-3d
```

## See Also

* [`to_sentinelone_data_lake`](https://tenzir.com/docs/reference/operators/to_sentinelone_data_lake.md)
* [Sentinelone data lake](../../integrations/sentinelone-data-lake.md)
