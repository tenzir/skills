# Tls.Client

Transport Layer Security (TLS) information associated with the client (for example, Certificate or JA3 hash).

- **Full name**: `google.backstory.Tls.Client`
- **Fields**: `5`

## Fields

### `certificate`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Certificate`](certificate.md)
- **JSON name**: `certificate`

Client certificate.

### `ja3`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ja3`

JA3 hash from the TLS ClientHello, as a hex-encoded string.

### `server_name`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `serverName`

Host name of the server, that the client is connecting to.

### `supported_ciphers`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `supportedCiphers`

Ciphers supported by the client during client hello.

### `ja4`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ja4`

JA4 hash from the TLS ClientHello, as a hex-encoded string.
