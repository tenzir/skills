# SSLCertificate.Extension

Certificate's extensions.

- **Full name**: `google.backstory.SSLCertificate.Extension`
- **Fields**: `14`

## Fields

### `ca`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `ca`

Whether the subject acts as a certificate authority (CA) or not.

### `subject_key_id`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `subjectKeyId`

Identifies the public key being certified.

### `authority_key_id`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate.AuthorityKeyId`](ssl_certificate_authority_key_id.md)
- **JSON name**: `authorityKeyId`

Identifies the public key to be used to verify the signature on this certificate or CRL.

### `key_usage`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `keyUsage`

The purpose for which the certified public key is used.

### `ca_info_access`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `caInfoAccess`

Authority information access locations are URLs that are added to a certificate in its authority information access extension.

### `crl_distribution_points`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `crlDistributionPoints`

CRL distribution points to which a certificate user should refer to ascertain if the certificate has been revoked.

### `extended_key_usage`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `extendedKeyUsage`

One or more purposes for which the certified public key may be used, in addition to or in place of the basic purposes indicated in the key usage extension field.

### `subject_alternative_name`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `subjectAlternativeName`

Contains one or more alternative names, using any of a variety of name forms, for the entity that is bound by the CA to the certified public key.

### `certificate_policies`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `certificatePolicies`

Different certificate policies will relate to different applications which may use the certified key.

### `netscape_cert_comment`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `netscapeCertComment`

Used to include free-form text comments inside certificates.

### `cert_template_name_dc`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `certTemplateNameDc`

BMP data value "DomainController". See MS Q291010.

### `netscape_certificate`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `netscapeCertificate`

Identify whether the certificate subject is an SSL client, an SSL server, or a CA.

### `pe_logotype`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `peLogotype`

Whether the certificate includes a logotype.

### `old_authority_key_id`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `oldAuthorityKeyId`

Whether the certificate has an old authority key identifier extension.
