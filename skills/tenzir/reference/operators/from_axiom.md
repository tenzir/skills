---
title: "from_axiom"
canonical: https://tenzir.com/docs/reference/operators/from_axiom
source: https://tenzir.com/docs/reference/operators/from_axiom.md
section: "Docs"
---

# from_axiom

> Queries an Axiom dataset or runs an APL query through Axiom’s regional edge query API.

Queries an Axiom dataset or runs an APL query through Axiom’s regional edge query API.

```tql
from_axiom [dataset:string], [query=string], token=secret,
  [endpoint=string, start=time, end=time, timeout=duration, nocache=bool,
  variables=record, tls=bool|record, pushdown=bool]
```

## Description

The `from_axiom` operator is a finite source that queries Axiom’s regional [edge query endpoint](https://axiom.co/docs/restapi/endpoints/queryEdge) (`POST /v1/query/_apl?format=tabular`). It reads either from a named dataset or from a raw Axiom Processing Language (APL) query, appends [pushed-down stages](from_axiom.md#optimizations) for downstream operators, and emits the first result table (`tables[0]`) as events with schema name `axiom`.

Use [`to_axiom`](to_axiom.md) to ingest events into Axiom datasets.

### Authentication and edge endpoints

Axiom’s edge query API authenticates with an Advanced API token (`xaat-`) that has `query:read` permission on the target dataset.

By default, the operator connects to Axiom’s US East 1 edge deployment (`https://us-east-1.aws.edge.axiom.co`). Set `endpoint` to another regional edge URL such as `https://eu-central-1.aws.edge.axiom.co` when querying datasets hosted in another region. If the endpoint region does not match the dataset’s region, Axiom returns HTTP `400` and the operator suggests setting `endpoint=`.

### Result types and flattened fields

Axiom returns tabular columns with declared types. The operator converts `datetime` columns to `time`, `timespan` columns (Go duration strings) to `duration`, and `float` columns to `double`. All other columns, including `integer`, `string`, `boolean`, `array`, `map`, and any unrecognized future types, decode directly from their JSON values.

Axiom flattens nested JSON objects on ingest into dotted field names. Nested records written by [`to_axiom`](to_axiom.md) therefore come back as top-level dotted fields such as `this["geo.country"]` rather than nested records, and `from_axiom` keeps them flat without unflattening.

### Result limits and completeness warnings

Every query request sends `defaultLimit: 50000` (Axiom’s base single-query row cap). The operator does not paginate across multiple requests yet; narrow the `_time` window or aggregate rows with [`summarize`](summarize.md) when working with larger datasets.

The operator surfaces Axiom’s completeness signals as warnings:

* `status.isPartial`: the result is partial.
* `status.isEstimate`: the result is estimated.
* `default_limit_warning`: the result hit Axiom’s default row limit.
* `license_limit_for_query_warning`: Axiom restricted the query time range due to plan limits.
* `max_limit_warning`: the result hit Axiom’s maximum row limit (suppressed when a pushed-down [`head`](head.md) matches the returned row count).

Transient HTTP `429` and `5xx` responses are retried with a bounded retry budget. Permanent query, authorization, and quota errors (`400`, `401`, `403`, `404`, `430`) fail the pipeline with the Axiom error message and `X-Axiom-Trace-Id` when present.

### `dataset: string (optional)`

The Axiom dataset to query. Mutually exclusive with `query`.

### `query = string (optional)`

A raw APL query to execute instead of reading a single dataset. Mutually exclusive with `dataset`.

### `token = secret`

An Axiom Advanced API token (`xaat-`) with `query:read` permission.

### `endpoint = string (optional)`

The Axiom regional edge base URL.

Defaults to `"https://us-east-1.aws.edge.axiom.co"`.

### `start = time (optional)`

Start of the query time window, sent as `startTime` in the request body. Must be specified together with `end` and earlier than `end`.

### `end = time (optional)`

End of the query time window, sent as `endTime` in the request body. Must be specified together with `start`.

### `timeout = duration (optional)`

Maximum time to wait for the query response. Must be positive and at most `10min`.

Defaults to `60s`.

### `nocache = bool (optional)`

Set to `true` to pass `nocache=true` and bypass Axiom’s query result cache.

Defaults to `false`.

### `variables = record (optional)`

Typed variables inserted into the APL query via the request body’s `variables` object. Requires `query=`. Keys must not be empty.

### `tls = bool | record (optional)`

TLS configuration for the HTTPS connection, or `false` to disable TLS when connecting to a local test server.

### `pushdown = bool (optional)`

Controls whether downstream operators run in Axiom as APL stages. Set `pushdown=false` to run every operator in Tenzir with TQL semantics.

Defaults to `true`.

## Optimizations

The `from_axiom` operator hands downstream [`where`](where.md), [`select`](select.md),

[`drop`](drop.md), [`summarize`](summarize.md), [`sort`](sort.md), and [`head`](head.md) stages to Axiom as APL stages, and appends a `project` with `column_ifexists` for implicit downstream field projections. Pushed stages run with APL’s native semantics; see our [Axiom optimization reference](../optimizations/axiom.md) for the complete function table, two-stage exact `count_distinct` behavior, and semantic differences from TQL.

## Examples

### Filter, bucket by time, summarize, sort, and take the top 10

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

Tenzir pushes all stages into Axiom as a single APL query:

```kusto
['http-logs']
| where (['status'] >= 400)
| where (['uri'] startswith_cs "/api/")
| extend ['__tenzir_column_0'] = bin(['_time'], timespan(300000000000ns))
| summarize ['__tenzir_part_0'] = count() by ['__tenzir_column_0'], ['method'], ['src_ip']
| summarize ['__tenzir_column_1'] = sum(['__tenzir_part_0']), ['__tenzir_column_2'] = countif(isnotnull(['src_ip'])) by ['__tenzir_column_0'], ['method']
| sort by ['__tenzir_column_1'] desc, ['__tenzir_column_0'] asc, ['method'] asc
| take 10
```

### Filter on a flattened dotted field

```tql
from_axiom "http-logs", token=secret("axiom_token")
where this["geo.country"] == "DE"
select _time, method, status, this["geo.country"]
head 25
```

### Run a parameterized raw APL query without caching

```tql
from_axiom query="['http-logs'] | where status >= min_status",
  token=secret("axiom_token"),
  variables={min_status: 500},
  nocache=true
head 20
```

## See Also

* [`to_axiom`](to_axiom.md)
* [Axiom](https://tenzir.com/product/integrations/axiom.md)
* [Axiom](../optimizations/axiom.md)
