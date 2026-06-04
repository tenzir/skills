# SSLCertificate

SSL certificate.

- **Full name**: `google.backstory.SSLCertificate`
- **Fields**: `15`
- **Nested messages**: `8`

## Nested messages

- [SSLCertificate.CertSignature](ssl_certificate_cert_signature.md)
- [SSLCertificate.AuthorityKeyId](ssl_certificate_authority_key_id.md)
- [SSLCertificate.Extension](ssl_certificate_extension.md)
- [SSLCertificate.Subject](ssl_certificate_subject.md)
- [SSLCertificate.RSA](ssl_certificate_rsa.md)
- [SSLCertificate.EC](ssl_certificate_ec.md)
- [SSLCertificate.PublicKey](ssl_certificate_public_key.md)
- [SSLCertificate.Validity](ssl_certificate_validity.md)

## Fields

### `cert_signature`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.CertSignature`](ssl_certificate_cert_signature.md)
- **JSON name**: `certSignature`

Certificate's signature and algorithm.

### `extension`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.Extension`](ssl_certificate_extension.md)
- **JSON name**: `extension`
- **Deprecated**: `true`

(DEPRECATED) certificate's extension.

### `cert_extensions`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `certExtensions`

Certificate's extensions.

### `first_seen_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstSeenTime`

Date the certificate was first retrieved by VirusTotal.

### `issuer`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.Subject`](ssl_certificate_subject.md)
- **JSON name**: `issuer`

Certificate's issuer data.

### `ec`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.EC`](ssl_certificate_ec.md)
- **JSON name**: `ec`

EC public key information.

### `serial_number`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `serialNumber`

Certificate's serial number hexdump.

### `signature_algorithm`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `signatureAlgorithm`

Algorithm used for the signature (for example, "sha1RSA").

### `size`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `size`

Certificate content length.

### `subject`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.Subject`](ssl_certificate_subject.md)
- **JSON name**: `subject`

Certificate's subject data.

### `thumbprint`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `thumbprint`

Certificate's content SHA1 hash.

### `thumbprint_sha256`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `thumbprintSha256`

Certificate's content SHA256 hash.

### `validity`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.Validity`](ssl_certificate_validity.md)
- **JSON name**: `validity`

Certificate's validity period.

### `version`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `version`

Certificate version (typically "V1", "V2" or "V3").

### `public_key`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.PublicKey`](ssl_certificate_public_key.md)
- **JSON name**: `publicKey`

Public key information.
