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

### `certSignature`

- Type: [`SSLCertificate.CertSignature`](ssl_certificate_cert_signature.md) (singular)

Certificate's signature and algorithm.

### `extension`

- Type: [`SSLCertificate.Extension`](ssl_certificate_extension.md) (singular)
- Deprecated: `true`

(DEPRECATED) certificate's extension.

### `certExtensions`

- Type: `google.protobuf.Struct` (singular)

Certificate's extensions.

### `firstSeenTime`

- Type: `google.protobuf.Timestamp` (singular)

Date the certificate was first retrieved by VirusTotal.

### `issuer`

- Type: [`SSLCertificate.Subject`](ssl_certificate_subject.md) (singular)

Certificate's issuer data.

### `ec`

- Type: [`SSLCertificate.EC`](ssl_certificate_ec.md) (singular)

EC public key information.

### `serialNumber`

- Type: `string` (singular)

Certificate's serial number hexdump.

### `signatureAlgorithm`

- Type: `string` (singular)

Algorithm used for the signature (for example, "sha1RSA").

### `size`

- Type: `int64` (singular)

Certificate content length.

### `subject`

- Type: [`SSLCertificate.Subject`](ssl_certificate_subject.md) (singular)

Certificate's subject data.

### `thumbprint`

- Type: `string` (singular)

Certificate's content SHA1 hash.

### `thumbprintSha256`

- Type: `string` (singular)

Certificate's content SHA256 hash.

### `validity`

- Type: [`SSLCertificate.Validity`](ssl_certificate_validity.md) (singular)

Certificate's validity period.

### `version`

- Type: `string` (singular)

Certificate version (typically "V1", "V2" or "V3").

### `publicKey`

- Type: [`SSLCertificate.PublicKey`](ssl_certificate_public_key.md) (singular)

Public key information.
