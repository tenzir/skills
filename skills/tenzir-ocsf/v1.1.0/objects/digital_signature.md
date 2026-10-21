# Digital Signature (digital_signature)

The Digital Signature object contains information about the cryptographic mechanism used to verify the authenticity, integrity, and origin of the file or application.

- **Extends**: [Object (object)](object.md)
- **Profiles**: [Date/Time](../profiles/datetime.md)

## Attributes

### `algorithm`

- **Type**: `string_t`
- **Requirement**: optional

The digital signature algorithm used to create the signature, normalized to the caption of 'algorithm_id'. In the case of 'Other', it is defined by the event source.

### `algorithm_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Sibling**: `algorithm`

#### Enum values

- `0`: `Unknown` - The algorithm is unknown.
- `1`: `DSA` - Digital Signature Algorithm (DSA).
- `2`: `RSA` - Rivest-Shamir-Adleman (RSA) Algorithm.
- `3`: `ECDSA` - Elliptic Curve Digital Signature Algorithm.
- `4`: `Authenticode` - Microsoft Authenticode Digital Signature Algorithm.
- `99`: `Other` - The algorithm is not mapped. See the `algorithm` attribute, which contains a data source specific value.

The identifier of the normalized digital signature algorithm.

### `certificate`

- **Type**: [`certificate`](certificate.md)
- **Requirement**: recommended

The certificate object containing information about the digital certificate.

### `created_time`

- **Type**: `timestamp_t`
- **Requirement**: optional

The time when the digital signature was created.

### `developer_uid`

- **Type**: `string_t`
- **Requirement**: optional

The developer ID on the certificate that signed the file.

### `digest`

- **Type**: [`fingerprint`](fingerprint.md)
- **Requirement**: optional

The message digest attribute contains the fixed length message hash representation and the corresponding hashing algorithm information.
