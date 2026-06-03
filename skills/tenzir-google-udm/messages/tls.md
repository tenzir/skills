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

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Tls.Client`](tls_client.md)
- **JSON name**: `client`

Certificate information for the client certificate.

### `server`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`Tls.Server`](tls_server.md)
- **JSON name**: `server`

Certificate information for the server certificate.

### `cipher`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `cipher`

Cipher used during the connection.

### `curve`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `curve`

Elliptical curve used for a given cipher.

### `version`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `version`

TLS version.

### `version_protocol`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `versionProtocol`

Protocol.

### `established`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `established`

Indicates whether the TLS negotiation was successful.

### `next_protocol`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `nextProtocol`

Protocol to be used for tunnel.

### `resumed`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `resumed`

Indicates whether the TLS connection was resumed from a previous TLS negotiation.
