# SSLCertificate

SSL certificate.

## Fields

### `cert_signature` / `certSignature`

- Type: [`CertSignature`](ssl_certificate_cert_signature.md) (singular)

Certificate's signature and algorithm.

### `extension`

- Type: [`Extension`](ssl_certificate_extension.md) (singular)
- Deprecated: `true`

(DEPRECATED) certificate's extension.

### `cert_extensions` / `certExtensions`

- Type: `object` (singular)

Certificate's extensions.

### `first_seen_time` / `firstSeenTime`

- Type: `timestamp` (singular)

Date the certificate was first retrieved by VirusTotal.

### `issuer`

- Type: [`Subject`](ssl_certificate_subject.md) (singular)

Certificate's issuer data.

### `ec`

- Type: [`EC`](ssl_certificate_ec.md) (singular)

EC public key information.

### `serial_number` / `serialNumber`

- Type: `string` (singular)

Certificate's serial number hexdump.

### `signature_algorithm` / `signatureAlgorithm`

- Type: `string` (singular)

Algorithm used for the signature (for example, "sha1RSA").

### `size`

- Type: `int64` (singular)

Certificate content length.

### `subject`

- Type: [`Subject`](ssl_certificate_subject.md) (singular)

Certificate's subject data.

### `thumbprint`

- Type: `string` (singular)

Certificate's content SHA1 hash.

### `thumbprint_sha256` / `thumbprintSha256`

- Type: `string` (singular)

Certificate's content SHA256 hash.

### `validity`

- Type: [`Validity`](ssl_certificate_validity.md) (singular)

Certificate's validity period.

### `version`

- Type: `string` (singular)

Certificate version (typically "V1", "V2" or "V3").

### `public_key` / `publicKey`

- Type: [`PublicKey`](ssl_certificate_public_key.md) (singular)

Public key information.
