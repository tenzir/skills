---
title: "from_sentinelone_data_lake"
canonical: https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake
source: https://tenzir.com/docs/reference/operators/from_sentinelone_data_lake.md
section: "Docs"
---

# from_sentinelone_data_lake

> Retrieves PowerQuery results from SentinelOne Singularity Data Lake.

Retrieves PowerQuery results from SentinelOne Singularity Data Lake.

```tql
from_sentinelone_data_lake url:string, token=string, query=string,
                           [start=time, end=time, account_ids=list<string>,
                            timeout=duration, raw=bool]
```

## Description

The `from_sentinelone_data_lake` operator runs a PowerQuery through SentinelOne’s Long Running Query (LRQ) API on your tenant’s console host. It launches the query at `/sdl/v2/api/queries`, polls once per second, and reads the final tabular result. It deletes the server-side query before emitting events, including when a downstream operator stops after the first event.

By default, the query covers the past 24 hours. The operator sends both time bounds explicitly and requests low query priority. It retries rate-limited launches and transient HTTP or connection errors during polling, up to five attempts, and honors `Retry-After`. It does not retry a launch after a connection error or HTTP `5xx` response because the server may already have created the query. Launch retries wait for `Retry-After` within the operator’s total `timeout` budget. During polling, if the requested delay would exceed the active query’s keep-alive budget, the operator stops instead of retrying early. Invalid `Retry-After` headers, including delays outside the supported numeric range, fail the query rather than trigger a shorter fallback delay.

Migration from the V1 API

Replace regional URLs such as `https://xdr.eu1.sentinelone.net` with your console URL, `https://<tenant>.sentinelone.net`. Replace scoped SDL Log Read keys with a console service-user API token. There is no fallback to `/api/powerQuery`, which SentinelOne retires on February 15, 2027.

### `url: string`

The base URL of your tenant’s SentinelOne console, for example `https://<tenant>.sentinelone.net`.

Use HTTPS for your console. Regional `xdr.*.sentinelone.net` URLs are no longer supported.

### `token = string`

A console service-user API token. The operator sends it with Bearer authentication, not the `ApiToken` prefix used by the management API.

Use the [`secret()`](https://tenzir.com/docs/reference/functions/secret.md) function to reference credentials securely.

### `query = string`

The PowerQuery query string to execute against the Data Lake.

PowerQuery is SentinelOne’s query language for searching and analyzing data in the Data Lake. Refer to the [SentinelOne PowerQuery documentation](https://support.sentinelone.com/hc/en-us/articles/360004195934) for query syntax details.

### `start = time (optional)`

The start time for the query time range.

Events at or after this time are included. Defaults to 24 hours before `end`. Fractional seconds retain nanosecond precision.

### `end = time (optional)`

The end time for the query time range.

Events before this time are included. Defaults to the current time when the operator starts.

### `account_ids = list<string> (optional)`

The account IDs to query. The list must not be empty.

When omitted, the operator requests tenant scope. On some multi-account tenants, that scope selects a default account that may not contain your data. If a query unexpectedly returns no rows, specify the account IDs containing the data. The operator sends `tenant: false` together with `accountIds` when you set this argument.

### `timeout = duration (optional)`

The time budget for launching and polling the query, including retry delays. Must be greater than zero. Defaults to `3min`.

When the budget expires, the operator attempts to delete the server-side query and reports an error without emitting results. Cleanup can take additional time. Increase this value for longer queries, for example `timeout=5min`, or narrow the query to finish sooner. Successful polls do not reset the budget.

### `raw = bool (optional)`

Whether to skip parsing strings as typed data.

Defaults to `false`.

## Limitations

* PowerQuery returns at most 1,000 rows by default for queries without `limit` or `group`. Add `| limit N` to the PowerQuery string to request a larger result. A TQL `head` after this operator does not change the remote limit.
* The operator reads the final result without paging. Memory limits can omit events; the operator does not currently report those omissions.
* SentinelOne expires queries 30 seconds after the last poll and kills queries after five minutes. An expired or killed query fails with HTTP `404`; the operator does not relaunch it automatically.
* Graceful shutdown deletes an active query. Forced cancellation during polling relies on the server’s 30-second expiry. Checkpointing is not supported.

## Examples

### Query threat events from the last 24 hours

```tql
from_sentinelone_data_lake "https://<tenant>.sentinelone.net",
  token=secret("sentinelone-console-token"),
  query="severity > 3 | columns id | limit 5000"
```

### Query specific fields with time range filters

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
* [SentinelOne Data Lake](../../integrations/sentinelone-data-lake.md)
