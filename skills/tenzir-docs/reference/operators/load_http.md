# load_http


Loads a byte stream via HTTP.

```tql
load_http url:string, [data=record, params=record, headers=record,
          method=string, form=bool, chunked=bool, multipart=bool,
          parallel=int, tls=record]
```

## Description

The `load_http` operator performs a HTTP request and returns the response.

### `url: string`

The URL to request from. The `http://` scheme can be omitted.

### `method = string (optional)`

The HTTP method, such as `POST` or `GET`.

The default is `"GET"`.

### `params = record (optional)`

The query parameters for the request.

### `headers = record (optional)`

The headers for the request.

### `data = record (optional)`

The request body as a record of key-value pairs. The body is encoded as JSON unless `form=true` has been set.

### `form = bool (optional)`

Submits the HTTP request body as form-encoded data.

This automatically sets the `Content-Type` header to `application/x-www-form-urlencoded`.

Defaults to `false`.

### `chunked = bool (optional)`

Whether to enable [chunked transfer encoding](https://en.wikipedia.org/wiki/Chunked_transfer_encoding). This is equivalent to manually setting the header `Transfer-Encoding: chunked`.

Defaults to `false`.

### `multipart = bool (optional)`

Whether to encode the HTTP request body as [multipart message](https://en.wikipedia.org/wiki/MIME#Multipart_messages).

This automatically sets the `Content-Type` header to `application/form-multipart; X` where `X` contains the MIME part boundary.

Defaults to `false`.

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

### Perform an API call and get the response

```tql
load_http "example.org/api", headers={"X-API-Token": "0000-0000-0000"}
```

## See Also

* [`save_http`](/reference/operators/save_http.md)
* [HTTP(S)](../../integrations/http.md)