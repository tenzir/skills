# from_http


Sends an HTTP/1.1 request and returns the response as events.

```tql
from_http url:string, [method=string, body=record|string|blob, encode=string,
          headers=record, error_field=field, paginate=string,
          paginate_delay=duration, connection_timeout=duration,
          max_retry_count=int, retry_delay=duration, tls=record]
          { … }
```

## Description

The `from_http` operator issues an HTTP request and returns the response as events.

The `from_http` operator requires a parser sub-pipeline. The operator sends the HTTP response body to that sub-pipeline as bytes.

Use the sub-pipeline to parse the response body. The operator automatically handles HTTP `Content-Encoding`. If the downloaded file itself is compressed, add the appropriate decompressor to the sub-pipeline. For example, use `decompress_gzip` followed by `read_json` for a downloaded gzip-compressed JSON file.

### `url: string`

URL to connect to. Both `http://` and `https://` schemes are supported. If the scheme is omitted, `https://` is assumed.

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

For [`from_http`](/reference/operators/from_http.md), the default is `get`, or `post` when you set `body`. For [`to_http`](/reference/operators/to_http.md), the default is `post`.

### `headers = record (optional)`

Record of headers to send with the request. Each value is resolved as a [secret](../../explanations/secrets.md), so you can pass secret names to avoid hardcoding tokens or API keys directly in the pipeline.

### `connection_timeout = duration (optional)`

Timeout for establishing the connection.

Defaults to `5s`.

### `max_retry_count = int (optional)`

Maximum number of retry attempts per request.

A request is retried on transient transport failures and HTTP `429` and `5xx` responses.

Defaults to `5`.

### `retry_delay = duration (optional)`

Base duration between retry attempts.

Tenzir uses exponential backoff starting at `retry_delay` and capping at `16 * retry_delay`. A `Retry-After` response header overrides this delay.

Defaults to `1s`.

### `body = blob|record|string (optional)`

Body to send with the HTTP request.

If the value is a `record`, the body is encoded according to the `encode` option and Tenzir sets an appropriate `Content-Type` header.

### `encode = string (optional)`

Specifies how to encode `record` bodies. Supported values:

* `json`
* `form`

Defaults to `json`.

### `paginate = record -> string | string (optional)`

Controls automatic pagination of HTTP responses.

**Lambda mode**: A lambda expression to evaluate against the parsed result of a request. If the expression evaluates successfully and returns a non-null string, Tenzir uses that string as the URL for a new `GET` request with the same headers.

**Link mode**: The string `"link"` to automatically follow pagination links in the HTTP `Link` response header as defined in [RFC 8288](https://datatracker.ietf.org/doc/html/rfc8288). Tenzir follows the `rel=next` relation until the response no longer contains one.

**[OData](https://www.oasis-open.org/standard/odata-v4-01-os/) mode**: The string `"odata"` to follow OData collection responses such as Microsoft Graph. The response body must be a JSON object with a top-level `value` array. Tenzir emits each object from `value`, follows a top-level string `@odata.nextLink` as an opaque URL, and sends follow-up requests as `GET` requests with the same headers.

### `paginate_delay = duration (optional)`

The duration to wait between consecutive pagination requests.

Defaults to `0s`.

### `error_field = field (optional)`

Field to insert the response body for HTTP error responses (status codes not in the 2xx or 3xx range).

When set, any HTTP response with a status code outside the 200–399 range will have its body stored in this field as a `blob`. Otherwise, error responses are skipped and an error is emitted.

Retryable HTTP responses (`429` and `5xx`) are retried before the operator emits the final error response.

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

### Migration from `server=true`

The `server=true` flag is no longer supported. Use [`accept_http`](/reference/operators/accept_http.md) to listen for incoming HTTP requests.

### `{ … }`

A required pipeline that receives the response body as bytes, allowing parsing per request. This is especially useful in scenarios where the response body can be parsed into multiple events.

Inside the pipeline, the `$response` variable is available as a record with the following fields:

| Field     | Type     | Description                           |
| :-------- | :------- | :------------------------------------ |
| `code`    | `uint64` | The HTTP status code of the response. |
| `headers` | `record` | The response headers.                 |

The pipeline must return events.

## Examples

### Make a GET request

Make a request to [urlscan.io](https://urlscan.io/docs/api#search) to search for scans for `tenzir.com` and get the first result.

```tql
from_http "https://urlscan.io/api/v1/search?q=tenzir.com" {
  read_json
}
unroll results
head 1
```

```tql
{
  results: {
    submitter: { ... },
    task: { ... },
    stats: { ... },
    page: { ... },
    _id: "0196edb1-521e-761f-9d62-1ca4cfad5b30",
    _score: null,
    sort: [ "1747744570133", "\"0196edb1-521e-761f-9d62-1ca4cfad5b30\"" ],
    result: "https://urlscan.io/api/v1/result/0196edb1-521e-761f-9d62-1ca4cfad5b30/",
    screenshot: "https://urlscan.io/screenshots/0196edb1-521e-761f-9d62-1ca4cfad5b30.png",
  },
  total: 9,
  took: 296,
  has_more: false,
}
```

### Send a POST request with JSON body

```tql
from_http "https://httpbin.org/post", body={key: "value"}, encode="json" {
  read_json
}
```

### Access response metadata

Use the `$response` variable inside a parsing pipeline to access the HTTP response code and headers:

```tql
from_http "https://example.com/api", method="put" {
  read_json
  where $response.code == 200
  response = $response
}
```

### Paginate via Link Headers

Use `paginate="link"` to automatically follow RFC 8288 `Link` headers with `rel=next`:

```tql
from_http "https://api.github.com/repos/tenzir/tenzir/issues?per_page=10",
  paginate="link" {
  read_json
}
```

Many APIs (such as GitHub, GitLab, and Jira) use the `Link` header for pagination. The operator extracts the `rel=next` URL from the header and continues fetching until no more pages are available.

### Paginate [OData](https://www.oasis-open.org/standard/odata-v4-01-os/) collection responses

Use `paginate="odata"` for APIs that return an OData collection envelope, such as Microsoft Graph:

```tql
from_http "https://graph.microsoft.com/v1.0/users",
  headers={
    "Authorization": "Bearer " + secret("MICROSOFT_GRAPH_TOKEN"),
    "ConsistencyLevel": "eventual",
  },
  paginate="odata" {
  read_json
}
```

The response body must be a JSON object with a top-level `value` array. The operator emits each object from `value`, follows a top-level string `@odata.nextLink` as an opaque URL, and stops when the field is absent or not a string. Follow-up requests use `GET` with the same headers as the initial request.

### Retry Failed Requests

Configure retries for failed requests:

```tql
from_http "https://api.example.com/data", max_retry_count=3, retry_delay=2s {
  read_json
}
```

This retries transient transport failures and HTTP `429` and `5xx` responses up to 3 times. The delay starts at 2 seconds and backs off exponentially.

## See Also

* [`accept_http`](/reference/operators/accept_http.md)
* [`http`](/reference/operators/http.md)
* [`to_http`](/reference/operators/to_http.md)
* [`serve_http`](/reference/operators/serve_http.md)
* [Tenzir v6 Migration](../../guides/tenzir-v6-migration.md)
* [Fetch via HTTP and APIs](../../guides/collecting/fetch-via-http-and-apis.md)
* [Enrich with threat intel](../../guides/enrichment/enrich-with-threat-intel.md)
* [Work with lookup tables](../../guides/enrichment/work-with-lookup-tables.md)
* [HTTP(S)](../../integrations/http.md)