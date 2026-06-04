# SSLCertificate.Extension

Certificate's extensions.

- **Full name**: `google.backstory.SSLCertificate.Extension`
- **Fields**: `14`

## Fields

### `ca`

- Type: `bool` (singular)

Whether the subject acts as a certificate authority (CA) or not.

### `subjectKeyId`

- Type: `string` (singular)

Identifies the public key being certified.

### `authorityKeyId`

- Type: [`SSLCertificate.AuthorityKeyId`](ssl_certificate_authority_key_id.md) (singular)

Identifies the public key to be used to verify the signature on this certificate or CRL.

### `keyUsage`

- Type: `string` (singular)

The purpose for which the certified public key is used.

### `caInfoAccess`

- Type: `string` (singular)

Authority information access locations are URLs that are added to a certificate in its authority information access extension.

### `crlDistributionPoints`

- Type: `string` (singular)

CRL distribution points to which a certificate user should refer to ascertain if the certificate has been revoked.

### `extendedKeyUsage`

- Type: `string` (singular)

One or more purposes for which the certified public key may be used, in addition to or in place of the basic purposes indicated in the key usage extension field.

### `subjectAlternativeName`

- Type: `string` (singular)

Contains one or more alternative names, using any of a variety of name forms, for the entity that is bound by the CA to the certified public key.

### `certificatePolicies`

- Type: `string` (singular)

Different certificate policies will relate to different applications which may use the certified key.

### `netscapeCertComment`

- Type: `string` (singular)

Used to include free-form text comments inside certificates.

### `certTemplateNameDc`

- Type: `string` (singular)

BMP data value "DomainController". See MS Q291010.

### `netscapeCertificate`

- Type: `bool` (singular)

Identify whether the certificate subject is an SSL client, an SSL server, or a CA.

### `peLogotype`

- Type: `bool` (singular)

Whether the certificate includes a logotype.

### `oldAuthorityKeyId`

- Type: `bool` (singular)

Whether the certificate has an old authority key identifier extension.
