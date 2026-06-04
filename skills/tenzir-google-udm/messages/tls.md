# Tls

Transport Layer Security (TLS) information.

- **Full name**: `google.backstory.Tls`
- **Fields**: `9`
- **Nested messages**: `2`

## Nested messages

- [Tls.Client](tls_client.md)
- [Tls.Server](tls_server.md)

## Fields

### `client`

- Type: [`Tls.Client`](tls_client.md) (singular)

Certificate information for the client certificate.

### `server`

- Type: [`Tls.Server`](tls_server.md) (singular)

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

### `versionProtocol`

- Type: `string` (singular)

Protocol.

### `established`

- Type: `bool` (singular)

Indicates whether the TLS negotiation was successful.

### `nextProtocol`

- Type: `string` (singular)

Protocol to be used for tunnel.

### `resumed`

- Type: `bool` (singular)

Indicates whether the TLS connection was resumed from a previous TLS negotiation.
