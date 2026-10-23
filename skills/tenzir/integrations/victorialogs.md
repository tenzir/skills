---
title: "VictoriaLogs integration"
description: "Store logs in a fast, resource-efficient database and search them with LogsQL."
canonical: https://tenzir.com/integrations/victorialogs
source: https://tenzir.com/integrations/victorialogs.md
section: "Integrations"
---

# VictoriaLogs integration

> Store logs in a fast, resource-efficient database and search them with LogsQL.

[VictoriaLogs](https://docs.victoriametrics.com/victorialogs/) is an open-source log database from the VictoriaMetrics team that runs as a single binary. It indexes every field, so field lookups and full-text searches work without index configuration. Tenzir sends events to its Elasticsearch-compatible bulk endpoint with [`to_opensearch`](https://tenzir.com/docs/reference/operators/to_opensearch.md) and queries them through its LogsQL HTTP API with [`from_http`](https://tenzir.com/docs/reference/operators/from_http.md).

VictoriaLogs

## How events map to VictoriaLogs

VictoriaLogs stores each event as a flat set of fields. Three of them have a special role, and the bulk endpoint selects them through URL query parameters:

| Field     | Query parameter  | Purpose                                                                           |
| --------- | ---------------- | --------------------------------------------------------------------------------- |
| `_time`   | `_time_field`    | The event timestamp. VictoriaLogs partitions data by day.                         |
| `_msg`    | `_msg_field`     | The log message, the default target of full-text filters.                         |
| `_stream` | `_stream_fields` | Fields that group events into streams, stored together and cheapest to filter on. |

Everything else follows from the shape of the event:

* Nested records become dotted field names, so `{src_endpoint: {ip: …}}` becomes the field `src_endpoint.ip`.
* Lists become JSON strings.
* VictoriaLogs stores values as strings. It detects numbers, IP addresses, and timestamps per block for compression, and LogsQL has range filters such as `range()` and `ipv4_range()` for them.
* The `preserve_json_keys` parameter keeps a record as one JSON string instead of flattening it.

VictoriaLogs rejects events older than its `-retentionPeriod` flag, which defaults to 7 days. Raise it before you replay or backfill historical data.

## Examples

These examples assume VictoriaLogs listens on `victorialogs:9428`.

### Send events

Point [`to_opensearch`](https://tenzir.com/docs/reference/operators/to_opensearch.md) at the bulk endpoint and name the time, message, and stream fields in the URL:

```tql
subscribe "logs"
to_opensearch "http://victorialogs:9428/insert/elasticsearch/_bulk?_time_field=timestamp&_msg_field=message&_stream_fields=host,app",
  action="create",
  index="logs"
```

VictoriaLogs ignores the index name, but [`to_opensearch`](https://tenzir.com/docs/reference/operators/to_opensearch.md) needs one when the URL does not contain it.

### Store OCSF events

For [OCSF](https://schema.ocsf.io) events, use the event time as `_time`, keep the original log line as the message, and group streams by event class and product:

```tql
subscribe "ocsf"
to_opensearch "http://victorialogs:9428/insert/elasticsearch/_bulk?_time_field=time&_msg_field=raw_data&_stream_fields=class_uid,metadata.product.name",
  action="create",
  index="ocsf"
```

VictoriaLogs flattens the `unmapped` record into searchable `unmapped.*` fields. To store it as a single JSON string instead, add `&preserve_json_keys=unmapped` to the URL.

Keep the stream fields to a few low-cardinality fields. In our benchmark with 100M OCSF events, `class_uid` and the product name produced about 1,400 streams.

### Query with LogsQL

Send a [LogsQL](https://docs.victoriametrics.com/victorialogs/logsql/) query to the `/select/logsql/query` endpoint. It returns one JSON object per line:

```tql
from_http "http://victorialogs:9428/select/logsql/query",
  body={query: "_time:24h src_endpoint.ip:=10.20.61.25 | limit 1000"},
  encode="form" {
  read_ndjson
}
```

Results contain the flattened fields plus `_time`, `_msg`, and `_stream`. The [`unflatten`](https://tenzir.com/docs/reference/functions/unflatten.md) function turns dotted field names back into nested records, as in `this = this.unflatten()`.

Run aggregations inside VictoriaLogs with `stats` pipes, so only the result travels to Tenzir:

```tql
from_http "http://victorialogs:9428/select/logsql/query",
  body={query: "_time:7d {class_uid=\"3002\"} status_id:=2 | stats by (user.name) count() as logons | sort by (logons desc) | limit 10"},
  encode="form" {
  read_ndjson
}
```

### Search messages by word

A word or phrase filter such as `"82da-435a"` uses the token index. A substring filter such as `*82da-435a*` cannot use it and scans every message. In our benchmark with 100M events, the substring filter took 7.1 s and 9.8 GB of memory, the phrase filter 0.36 s. Prefer word and phrase filters, and bound every query with a `_time` filter.

## Authentication and TLS

VictoriaLogs has no user management of its own. Its documentation recommends running it in a trusted network and putting [vmauth](https://docs.victoriametrics.com/victoriametrics/vmauth/) in front of it for anything else:

| Setup               | VictoriaLogs side                                                               | What it gives you                                                             |
| ------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Built-in Basic Auth | `-httpAuth.username`, `-httpAuth.password` (read it from a file with `file://`) | One credential for all endpoints                                              |
| Built-in TLS        | `-tls`, `-tlsCertFile`, `-tlsKeyFile`                                           | HTTPS on the VictoriaLogs port                                                |
| vmauth as a proxy   | Users with access to `/insert/` or `/select/` only, per tenant if needed        | Separate credentials for writers and readers, TLS termination, load balancing |

Always combine Basic Auth with TLS, since Basic Auth sends the credentials in plain text.

On the Tenzir side, [`to_opensearch`](https://tenzir.com/docs/reference/operators/to_opensearch.md) takes `user`, `passwd`, and `tls`. Store the password as a [secret](../explanations/secrets.md) instead of writing it into the pipeline:

```tql
subscribe "logs"
to_opensearch "https://victorialogs:9428/insert/elasticsearch/_bulk?_time_field=timestamp&_msg_field=message&_stream_fields=host,app",
  action="create",
  index="logs",
  user="tenzir-writer",
  passwd=secret("victorialogs-writer-password"),
  tls={}
```

For queries, [`from_http`](https://tenzir.com/docs/reference/operators/from_http.md) sends the `Authorization` header. Encoding a secret keeps the result a secret:

```tql
from_http "https://victorialogs:9428/select/logsql/query",
  headers={Authorization: "Basic " + encode_base64(secret("victorialogs-reader-credentials"))},
  body={query: "_time:1h error | limit 100"},
  encode="form" {
  read_ndjson
}
```

The `victorialogs-reader-credentials` secret holds `user:password`.

## See Also

* [Send to destinations](../guides/route/send-to-destinations.md)
* [Fetch via HTTP and APIs](../guides/collect/fetch-via-http-and-apis.md)
* [OpenSearch](opensearch.md)
* [Elasticsearch](elasticsearch.md)
