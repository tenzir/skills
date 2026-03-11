# from_opensearch


Receives events via Opensearch Bulk API.

```tql
from_opensearch [url:string, keep_actions=bool, max_request_size=int, tls=record]
```

## Description

The `from_opensearch` operator emulates simple situations for the [Opensearch Bulk API](https://opensearch.org/docs/latest/api-reference/document-apis/bulk/).

### `url: string (optional)`

URL to listen on.

Must have the form `host[:port]`.

Defaults to `"0.0.0.0:9200"`.

### `keep_actions = bool (optional)`

Whether to keep the command objects such as `{"create": ...}`.

Defaults to `false`.

### `max_request_size = int (optional)`

The maximum size of an incoming request to accept.

Defaults to `10Mib`.

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

## Examples

### Listen on port 8080 on an interface with IP 1.2.3.4

```tql
from_opensearch "1.2.3.4:8080"
```

### Listen with TLS

```tql
from_opensearch tls=true, certfile="server.crt", keyfile="private.key"
```

## See Also

* [`to_opensearch`](/reference/operators/to_opensearch.md)
* [OpenSearch](../../integrations/opensearch.md)
* [Elasticsearch](../../integrations/elasticsearch.md)