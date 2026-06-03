# Certificate

Certificate information

- **Full name**: `google.backstory.Certificate`
- **Fields**: `9`

## Fields

### `version`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `version`

Certificate version.

### `serial`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `serial`

Certificate serial number.

### `subject`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `subject`

Subject of the certificate.

### `issuer`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `issuer`

Issuer of the certificate.

### `md5`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `md5`

The MD5 hash of the certificate, as a hex-encoded string.

### `sha1`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sha1`

The SHA1 hash of the certificate, as a hex-encoded string.

### `sha256`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sha256`

The SHA256 hash of the certificate, as a hex-encoded string.

### `not_before`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `notBefore`

Indicates when the certificate is first valid.

### `not_after`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `notAfter`

Indicates when the certificate is no longer valid.
