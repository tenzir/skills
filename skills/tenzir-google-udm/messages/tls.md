# Tls

Transport Layer Security (TLS) information.

## Fields

### `client`

- Type: [`Client`](tls_client.md) (singular)

Certificate information for the client certificate.

### `server`

- Type: [`Server`](tls_server.md) (singular)

Certificate information for the server certificate.

### `cipher`

- Type: `string` (singular)

Cipher used during the connection.

### `curve`

- Type: `string` (singular)

Elliptical curve used for a given cipher.

### `version`

- Type: `string` (singular)

TLS version.

### `version_protocol` / `versionProtocol`

- Type: `string` (singular)

Protocol.

### `established`

- Type: `bool` (singular)

Indicates whether the TLS negotiation was successful.

### `next_protocol` / `nextProtocol`

- Type: `string` (singular)

Protocol to be used for tunnel.

### `resumed`

- Type: `bool` (singular)

Indicates whether the TLS connection was resumed from a previous TLS negotiation.
