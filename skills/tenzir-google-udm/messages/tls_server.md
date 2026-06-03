# Tls.Server

Transport Layer Security (TLS) information associated with the server (for example, Certificate or JA3 hash).

- **Full name**: `google.backstory.Tls.Server`
- **Fields**: `3`

## Fields

### `certificate`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Certificate`](certificate.md)
- **JSON name**: `certificate`

Server certificate.

### `ja3s`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ja3s`

JA3 hash from the TLS ServerHello, as a hex-encoded string.

### `ja4s`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ja4s`

JA4 hash from the TLS ServerHello, as a hex-encoded string.
