# to_http


Sends events as a single HTTP request to a webhook or API endpoint.

```tql
to_http url:string, [method=string, headers=record, timeout=duration,
        tls=record, connection_timeout=duration,
        max_retry_count=int, retry_delay=duration] { … }
```

## Description

The `to_http` operator collects all input events into a single HTTP request to a webhook or API endpoint. A required printer sub-pipeline turns the events into bytes, which Tenzir streams as the request body. The request body flows from the printer sub-pipeline into the HTTP connection as chunks become available, without buffering the entire body in memory first. By default, the operator sends requests with the `POST` method.

To split events across multiple requests, wrap `to_http` in the [`every`](/reference/operators/every.md) operator. For example, `every 1m { to_http ... }` sends one request per minute with the events that arrived during that window.

The operator retries transient connection errors and HTTP `429` and `5xx` responses up to `max_retry_count` times, but only before any body data has been sent. Once the body stream has started, retries are not possible because the data cannot be replayed. For retried HTTP responses, a `Retry-After` header overrides the configured delay.

Non-2xx HTTP status codes cause pipeline errors.

### `url: string`

URL to send the request to.

The URL is resolved as a [secret](../../explanations/secrets.md), so you can pass a secret name to avoid hardcoding sensitive URLs.

### `method = string (optional)`

One of the following HTTP methods to use:

* `get`
* `head`
* `post`
* `put`
* `del`
* `connect`
* `options`
* `trace`

Defaults to `post`.

### `headers = record (optional)`

Record of headers to send with the request. Each value is resolved as a [secret](../../explanations/secrets.md), so you can pass secret names to avoid hardcoding tokens or API keys directly in the pipeline.

### `timeout = duration (optional)`

Timeout for the overall request.

Defaults to `90s`.

### `connection_timeout = duration (optional)`

Timeout for establishing the connection.

Defaults to `5s`.

### `max_retry_count = int (optional)`

Maximum number of retry attempts per request.

A request is retried on transient transport failures and HTTP `429` and `5xx` responses, but only before any request body bytes have been sent.

Defaults to `5`.

### `retry_delay = duration (optional)`

Base duration between retry attempts.

Tenzir uses exponential backoff starting at `retry_delay` and capping at `16 * retry_delay`. For retried HTTP `429` and `5xx` responses, a `Retry-After` response header overrides this delay.

Defaults to `1s`.

### `{ … }`

A required pipeline that receives events and must return bytes. The output of this pipeline becomes the HTTP request body.

Tenzir reads this pipeline incrementally and forwards the emitted chunks to the HTTP client as they are produced. Use this pipeline to choose the request format explicitly. For example, use `write_ndjson`, `write_json`, or another byte-producing pipeline.

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

### Send events to a webhook

Send all events as a single JSON POST request:

```tql
from {message: "hello", severity: "info"}
to_http "https://example.com/webhook" {
  write_ndjson
}
```

### Control the request body format

Use the printer sub-pipeline to control how the operator serializes events:

```tql
from {foo: "bar"}
to_http "https://example.com/api" {
  write_json
}
```

### Set a custom method and headers

```tql
from {foo: "bar"}
to_http "https://example.com/api",
  method="put",
  headers={"X-Custom": "value"} {
  write_ndjson
}
```

### Send events with TLS

```tql
from {data: "sensitive"}
to_http "https://secure.example.com/api",
  tls={skip_peer_verification: true} {
  write_ndjson
}
```

### Send events in periodic batches

Use `every` to group events into time-based batches, with each batch sent as a separate HTTP request:

```tql
subscribe "stream-of-events"
every 1m {
  to_http "https://example.com/ingest" {
    write_ndjson
  }
}
```

## See Also

* [`from_http`](/reference/operators/from_http.md)
* [`http`](/reference/operators/http.md)
* [`accept_http`](/reference/operators/accept_http.md)
* [`serve_http`](/reference/operators/serve_http.md)
* [`every`](/reference/operators/every.md)
* [Tenzir v6 Migration](../../guides/tenzir-v6-migration.md)
* [Fetch via HTTP and APIs](../../guides/collecting/fetch-via-http-and-apis.md)
* [HTTP(S)](../../integrations/http.md)