# FileMetadataSignatureInfo

Signature information.

- **Full name**: `google.backstory.FileMetadataSignatureInfo`
- **Fields**: `5`

## Fields

### `verification_message`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `verificationMessage`

Status of the certificate. Valid values are "Signed", "Unsigned" or a description of the certificate anomaly, if found.

### `verified`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `verified`

True if verification_message == "Signed"

### `signer`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `signer`
- **Deprecated**: `true`

Deprecated: use signers field.

### `signers`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: [`SignerInfo`](signer_info.md)
- **JSON name**: `signers`

File metadata signer information. The order of the signers matters. Each element is a higher level authority, being the last the root authority.

### `x509`

- **Number**: `5`
- **Cardinality**: `repeated`
- **Type**: [`X509`](x509.md)
- **JSON name**: `x509`

List of certificates.
