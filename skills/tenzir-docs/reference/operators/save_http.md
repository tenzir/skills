# save_http


Sends a byte stream via HTTP.

```tql
save_http url:string, [params=record, headers=record, method=string,
          parallel=int, tls=record]
```

## Description

The `save_http` operator performs a HTTP request with the request body being the bytes provided by the previous operator.

### `url: string`

The URL to write to. The `http://` scheme can be omitted.

### `method = string (optional)`

The HTTP method, such as `POST` or `GET`.

The default is `"POST"`.

### `params = record (optional)`

The query parameters for the request.

### `headers = record (optional)`

The headers for the request.

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

### Call a webhook with pipeline data

```tql
save_http "example.org/api", headers={"X-API-Token": "0000-0000-0000"}
```

## See Also

* [`load_http`](load_http.md)
* [HTTP(S)](../../integrations/http.md)