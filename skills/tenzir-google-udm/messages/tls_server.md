# Tls.Server

Transport Layer Security (TLS) information associated with the server (for example, Certificate or JA3 hash).

- **Full name**: `google.backstory.Tls.Server`
- **Fields**: `3`

## Fields

### `certificate`

- Type: [`Certificate`](certificate.md) (singular)

Server certificate.

### `ja3s`

- Type: `string` (singular)

JA3 hash from the TLS ServerHello, as a hex-encoded string.

### `ja4s`

- Type: `string` (singular)

JA4 hash from the TLS ServerHello, as a hex-encoded string.
