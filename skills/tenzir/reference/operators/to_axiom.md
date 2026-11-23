---
title: "to_axiom"
canonical: https://tenzir.com/docs/reference/operators/to_axiom
source: https://tenzir.com/docs/reference/operators/to_axiom.md
section: "Docs"
---

# to_axiom

> Sends events to an Axiom dataset through Axiom’s regional edge ingest API.

Sends events to an Axiom dataset through Axiom’s regional edge ingest API.

```tql
to_axiom dataset:string, token=secret, [endpoint=string,
  timestamp_field=string, timestamp_format=string, labels=record,
  batch_timeout=duration, parallel=int, tls=bool|record]
```

## Description

The `to_axiom` operator batches events as gzip-compressed NDJSON and uploads them to Axiom’s regional [edge ingest endpoint](https://axiom.co/docs/restapi/endpoints/ingestToDataset) (`POST /v1/ingest/{dataset}`). Each batch flushes when it reaches 10,000 events, 4 MiB uncompressed, or `batch_timeout`.

The target dataset must already exist in Axiom; the ingest API does not auto-create datasets. Use [`from_axiom`](from_axiom.md) to query events back out of Axiom.

### Timestamps and field representation

By default, Axiom reads the event timestamp from `_time` when present and assigns the ingest receive time otherwise. Set `timestamp_field` to have Axiom read `_time` from another field (such as OCSF `time` or a dotted field like `metadata.logged_time`); Axiom moves that field into `_time` on ingest. The operator never auto-detects OCSF `time` unless you pass `timestamp_field`. For non-RFC3339 timestamp strings, also set `timestamp_format` to a Go reference time layout. Events with timestamps earlier than `1970-01-01T00:00:00Z` or more than 24 hours in the future are rejected by Axiom and reported as warnings from the `failures` list in the HTTP `200` response body.

Nested records are flattened by Axiom into dotted fields (for example, `{geo: {country: "DE"}}` comes back as `this["geo.country"]` in

[`from_axiom`](from_axiom.md)). Tenzir `duration`, `ip`, and `subnet` values serialize as JSON strings.

### Errors, partial failures, and retries

Axiom returns HTTP `200` even when individual events fail validation or when dataset field limits drop excess columns. The operator parses every HTTP `200` body and emits warnings whenever `failed > 0` (including the first failure reason) or `messages` contains warnings such as `column_limit_drop`.

Transient HTTP `429` and `5xx` errors are retried with a bounded retry budget. HTTP `430` (organization monthly ingest limit reached), authorization errors (`401`/`403`), missing datasets (`404`), and region-mismatch `400` responses are not retried and fail with the Axiom error message and `X-Axiom-Trace-Id` when present.

### `dataset: string`

The name of the existing Axiom dataset to ingest events into.

### `token = secret`

An Axiom Basic or Advanced API token (`xaat-`) with `ingest:create` permission on the target dataset. Personal Access Tokens (`xapt-`) are rejected by Axiom’s edge ingest endpoint.

### `endpoint = string (optional)`

The Axiom regional edge base URL.

Defaults to `"https://us-east-1.aws.edge.axiom.co"`.

### `timestamp_field = string (optional)`

Name of the event field for Axiom to parse as `_time`, sent as the `timestamp-field` query parameter. Supports top-level fields (such as `"time"`) and dotted nested paths (such as `"metadata.logged_time"`). Must not be empty.

### `timestamp_format = string (optional)`

Date-time layout for parsing `timestamp_field` (or `_time`) when timestamps are not RFC3339, sent as the `timestamp-format` query parameter. Uses Go’s reference time (`Mon Jan 2 15:04:05 -0700 MST 2006`), for example `"2006/01/02 15:04:05"`. Must not be empty.

### `labels = record (optional)`

Additional key-value labels to attach to every event in each batch, sent as compact JSON in the `X-Axiom-Event-Labels` header. Keys must not be empty.

### `batch_timeout = duration (optional)`

Maximum time to buffer events before flushing a batch. Must be positive.

Defaults to `5s`.

### `parallel = int (optional)`

Maximum number of concurrent ingest requests per operator instance. Must be at least `1`.

Defaults to `8`.

### `tls = bool | record (optional)`

TLS configuration for the HTTPS connection, or `false` to disable TLS when connecting to a local test server.

## Examples

### Send NDJSON logs to an Axiom dataset

```tql
from_file "http-logs.ndjson"
to_axiom "http-logs", token=secret("axiom_token")
```

### Send OCSF events with an explicit timestamp field and labels

```tql
from_file "ocsf-events.ndjson"
to_axiom "security-events",
  token=secret("axiom_token"),
  timestamp_field="time",
  labels={env: "prod"}
```

### Ingest into an EU edge deployment

```tql
from_file "events.ndjson"
to_axiom "eu-logs",
  token=secret("axiom_token"),
  endpoint="https://eu-central-1.aws.edge.axiom.co"
```

## See Also

* [`from_axiom`](from_axiom.md)
* [Axiom](https://tenzir.com/product/integrations/axiom)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
