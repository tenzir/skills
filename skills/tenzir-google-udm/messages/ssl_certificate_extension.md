# Extension

Certificate's extensions.

## Fields

### `ca`

- Type: `bool` (singular)

Whether the subject acts as a certificate authority (CA) or not.

### `subject_key_id` / `subjectKeyId`

- Type: `string` (singular)

Identifies the public key being certified.

### `authority_key_id` / `authorityKeyId`

- Type: [`AuthorityKeyId`](ssl_certificate_authority_key_id.md) (singular)

Identifies the public key to be used to verify the signature on this certificate or CRL.

### `key_usage` / `keyUsage`

- Type: `string` (singular)

The purpose for which the certified public key is used.

### `ca_info_access` / `caInfoAccess`

- Type: `string` (singular)

Authority information access locations are URLs that are added to a certificate in its authority information access extension.

### `crl_distribution_points` / `crlDistributionPoints`

- Type: `string` (singular)

CRL distribution points to which a certificate user should refer to ascertain if the certificate has been revoked.

### `extended_key_usage` / `extendedKeyUsage`

- Type: `string` (singular)

One or more purposes for which the certified public key may be used, in addition to or in place of the basic purposes indicated in the key usage extension field.

### `subject_alternative_name` / `subjectAlternativeName`

- Type: `string` (singular)

Contains one or more alternative names, using any of a variety of name forms, for the entity that is bound by the CA to the certified public key.

### `certificate_policies` / `certificatePolicies`

- Type: `string` (singular)

Different certificate policies will relate to different applications which may use the certified key.

### `netscape_cert_comment` / `netscapeCertComment`

- Type: `string` (singular)

Used to include free-form text comments inside certificates.

### `cert_template_name_dc` / `certTemplateNameDc`

- Type: `string` (singular)

BMP data value "DomainController". See MS Q291010.

### `netscape_certificate` / `netscapeCertificate`

- Type: `bool` (singular)

Identify whether the certificate subject is an SSL client, an SSL server, or a CA.

### `pe_logotype` / `peLogotype`

- Type: `bool` (singular)

Whether the certificate includes a logotype.

### `old_authority_key_id` / `oldAuthorityKeyId`

- Type: `bool` (singular)

Whether the certificate has an old authority key identifier extension.
