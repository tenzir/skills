# to_opensearch


Sends events to an OpenSearch-compatible Bulk API.

```tql
to_opensearch url:string, action=string, [index=string, id=string, doc=record,
    user=string, passwd=string, tls=record]
```

## Description

The `to_opensearch` operator sends events to a [OpenSearch-compatible Bulk API](https://opensearch.org/docs/latest/api-reference/document-apis/bulk/) such as [ElasticSearch](https://www.elastic.co/elasticsearch).

The operator accumulates multiple events before sending them as a single request. You can control the maximum request size via the `max_content_length` and the timeout before sending all accumulated events via the `send_timeout` option.

### `url: string`

The URL of the API endpoint.

### `action = string`

An expression for the action that evaluates to a `string`.

Supported actions:

* `create`: Creates a document if it doesn’t already exist and returns an error otherwise.
* `delete`: Deletes a document if it exists.
* `index`: Creates a document if it doesn’t yet exist and replace the document if it already exists.
* `update`: Updates existing documents and returns an error if the document doesn’t exist.
* `upsert`: If a document exists, it is updated; if it does not exist, a new document is indexed.

### `index = string (optional)`

An optional expression for the index that evaluates to a `string`.

Must be provided if the `url` does not have an index.

### `id = string (optional)`

The `id` of the document to act on.

Must be provided when using the `delete` and `update` actions.

### `doc = record (optional)`

The document to serialize.

Defaults to `this`.

### `user = string (optional)`

Optional user for HTTP Basic Authentication.

### `passwd = string (optional)`

Optional password for HTTP Basic Authentication.

### `tls = record (optional)`

TLS configuration. Provide an empty record (`tls={}`) to enable TLS with defaults or set fields to customize it.

```tql
{
  skip_peer_verification: bool, // skip certificate verification.
  cacert: string,               // CA bundle to verify peers.
  certfile: string,             // client certificate to present.
  keyfile: string,              // private key for the client certificate.
  min_version: string,          // minimum TLS version (`"1.0"`, `"1.1"`, `"1.2"`, "1.3"`).
  ciphers: string,              // OpenSSL cipher list string.
  client_ca: string,            // CA to validate client certificates.
  require_client_cert,          // require clients to present a certificate.
}
```

The `client_ca` and `require_client_cert` options are only applied for operators that accept incoming client connections, and otherwise ignored.

Any value not specified in the record will either be picked up from the configuration or if not configured will not be used by the operator.

See the [Node TLS Setup guide](../../guides/node-setup/configure-tls.md) for more details.

### `include_nulls = bool (optional)`

Include fields with null values in the transmitted event data. By default, the operator drops all null values to save space.

Defaults to `false`.

### `max_content_length = int (optional)`

The maximum size of the message uncompressed body in bytes. A message may consist of multiple events. If a single event is larger than this limit, it is dropped and a warning is emitted.

Defaults to `5Mi`.

### `buffer_timeout = duration (optional)`

The maximum amount of time for which the operator accumulates messages before sending them out to the HEC endpoint as a single message.

Defaults to `5s`.

### `compress = bool (optional)`

Whether to compress the message body using standard gzip.

Defaults to `true`.

## Examples

### Send events from a JSON file

```tql
from "example.json"
to_opensearch "localhost:9200", action="create", index="main"
```

## See Also

* [`from_opensearch`](/reference/operators/from_opensearch.md)
* [OpenSearch](../../integrations/opensearch.md)
* [Elasticsearch](../../integrations/elasticsearch.md)