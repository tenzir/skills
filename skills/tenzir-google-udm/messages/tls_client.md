# Client

Transport Layer Security (TLS) information associated with the client (for example, Certificate or JA3 hash).

## Fields

### `certificate`

- Type: [`Certificate`](certificate.md) (singular)

Client certificate.

### `ja3`

- Type: `string` (singular)

JA3 hash from the TLS ClientHello, as a hex-encoded string.

### `server_name` / `serverName`

- Type: `string` (singular)

Host name of the server, that the client is connecting to.

### `supported_ciphers` / `supportedCiphers`

- Type: `string` (repeated)

Ciphers supported by the client during client hello.

### `ja4`

- Type: `string` (singular)

JA4 hash from the TLS ClientHello, as a hex-encoded string.
