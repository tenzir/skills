# SSLCertificate.PublicKey

Subject public key info.

- **Full name**: `google.backstory.SSLCertificate.PublicKey`
- **Fields**: `2`

## Fields

### `algorithm`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `algorithm`

Any of "RSA", "DSA" or "EC". Indicates the algorithm used to generate the certificate.

### `rsa`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.RSA`](ssl_certificate_rsa.md)
- **JSON name**: `rsa`

RSA public key information.
