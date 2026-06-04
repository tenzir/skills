# SignerInfo

File metadata related to the signer information.

- **Full name**: `google.backstory.SignerInfo`
- **Fields**: `4`

## Fields

### `name`

- Type: `string` (optional)

Common name of the signers/certificate. The order of the signers matters. Each element is a higher level authority, the last being the root authority.

### `status`

- Type: `string` (optional)

It can say "Valid" or state the problem with the certificate if any (e.g. "This certificate or one of the certificates in the certificate chain is not time valid.").

### `validUsage`

- Type: `string` (optional)

Indicates which situations the certificate is valid for (e.g. "Code Signing").

### `certIssuer`

- Type: `string` (optional)

Company that issued the certificate.
