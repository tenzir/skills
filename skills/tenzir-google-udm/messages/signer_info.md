# SignerInfo

File metadata related to the signer information.

- **Full name**: `google.backstory.SignerInfo`
- **Fields**: `4`

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `optional`
- **Type**: `string`
- **JSON name**: `name`

Common name of the signers/certificate. The order of the signers matters. Each element is a higher level authority, the last being the root authority.

### `status`

- **Number**: `2`
- **Cardinality**: `optional`
- **Type**: `string`
- **JSON name**: `status`

It can say "Valid" or state the problem with the certificate if any (e.g. "This certificate or one of the certificates in the certificate chain is not time valid.").

### `valid_usage`

- **Number**: `3`
- **Cardinality**: `optional`
- **Type**: `string`
- **JSON name**: `validUsage`

Indicates which situations the certificate is valid for (e.g. "Code Signing").

### `cert_issuer`

- **Number**: `4`
- **Cardinality**: `optional`
- **Type**: `string`
- **JSON name**: `certIssuer`

Company that issued the certificate.
