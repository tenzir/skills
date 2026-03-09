# save_tcp


Saves bytes to a TCP or TLS connection.

```tql
save_tcp endpoint:string, [retry_delay=duration, max_retry_count=int,
                           tls=record]
```

## Description

Saves bytes to the given endpoint via TCP or TLS. Attempts to reconnect automatically for `max_retry_count` in case of recoverable connection errors.

Note

Due to the nature of TCP a disconnect can still lead to lost and or incomplete events on the receiving end.

### `endpoint: string`

The endpoint to which the server will connect. Must be of the form `[tcp://]<hostname>:<port>`. You can also use an IANA service name instead of a numeric port.

### `retry_delay = duration (optional)`

The amount of time to wait before attempting to reconnect in case a connection attempt fails and the error is deemed recoverable. Defaults to `30s`.

### \`max\_retry\_count = int (optional)

The number of retries to attempt in case of connection errors before transitioning into the error state. Defaults to `10`.

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

### Transform incoming Syslog to BITZ and save over TCP

```tql
load_tcp "0.0.0.0:8090" { read_syslog }
write_bitz
save_tcp "127.0.0.1:4000"
```

### Save to localhost with TLS

```tql
subscribe "feed"
write_json
save_tcp "127.0.0.1:4000", tls=true, skip_peer_verification=true
```

## See Also

* [`load_tcp`](load_tcp.md)
* [TCP](../../integrations/tcp.md)