# FileMetadataSignatureInfo

Signature information.

## Fields

### `verificationMessage`

- Type: `string` (singular)

Status of the certificate. Valid values are "Signed", "Unsigned" or a description of the certificate anomaly, if found.

### `verified`

- Type: `bool` (singular)

True if verification_message == "Signed"

### `signer`

- Type: `string` (repeated)
- Deprecated: `true`

Deprecated: use signers field.

### `signers`

- Type: [`SignerInfo`](signer_info.md) (repeated)

File metadata signer information. The order of the signers matters. Each element is a higher level authority, being the last the root authority.

### `x509`

- Type: [`X509`](x509.md) (repeated)

List of certificates.
