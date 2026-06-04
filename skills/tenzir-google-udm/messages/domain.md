# Domain

Information about a domain.

- **Full name**: `google.backstory.Domain`
- **Fields**: `32`

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The domain name. This field can be used as an entity indicator for Domain entities.

### `prevalence`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`Prevalence`](prevalence.md)
- **JSON name**: `prevalence`

The prevalence of the domain within the customer's environment.

### `first_seen_time`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `firstSeenTime`

First seen timestamp of the domain in the customer's environment.

### `last_seen_time`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastSeenTime`

Last seen timestamp of the domain in the customer's environment.

### `registrar`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `registrar`

Registrar name . FOr example, "Wild West Domains, Inc. (R120-LROR)", "GoDaddy.com, LLC", or "PDR LTD. D/B/A PUBLICDOMAINREGISTRY.COM".

### `contact_email`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `contactEmail`

Contact email address.

### `whois_server`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `whoisServer`

Whois server name.

### `name_server`

- **Number**: `8`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `nameServer`

Repeated list of name servers.

### `creation_time`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `creationTime`

Domain creation time.

### `update_time`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `updateTime`

Last updated time.

### `expiration_time`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `expirationTime`

Expiration time.

### `audit_update_time`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `auditUpdateTime`

Audit updated time.

### `status`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `status`

Domain status. See [https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en) for meanings of possible values

### `registrant`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: [`User`](user.md)
- **JSON name**: `registrant`

Parsed contact information for the registrant of the domain.

### `admin`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: [`User`](user.md)
- **JSON name**: `admin`

Parsed contact information for the administrative contact for the domain.

### `tech`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: [`User`](user.md)
- **JSON name**: `tech`

Parsed contact information for the technical contact for the domain

### `billing`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: [`User`](user.md)
- **JSON name**: `billing`

Parsed contact information for the billing contact of the domain.

### `zone`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: [`User`](user.md)
- **JSON name**: `zone`

Parsed contact information for the zone.

### `whois_record_raw_text`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `whoisRecordRawText`

WHOIS raw text.

### `registry_data_raw_text`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `registryDataRawText`

Registry Data raw text.

### `iana_registrar_id`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `ianaRegistrarId`

IANA Registrar ID. See [https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml](https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml)

### `private_registration`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `privateRegistration`

Indicates whether the domain appears to be using a private registration service to mask the owner's contact information.

### `categories`

- **Number**: `23`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `categories`

Categories assign to the domain as retrieved from VirusTotal.

### `favicon`

- **Number**: `24`
- **Cardinality**: `singular`
- **Type**: [`Favicon`](favicon.md)
- **JSON name**: `favicon`

Includes difference hash and MD5 hash of the domain's favicon.

### `jarm`

- **Number**: `25`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `jarm`

Domain's JARM hash.

### `last_dns_records`

- **Number**: `26`
- **Cardinality**: `repeated`
- **Type**: [`DNSRecord`](dns_record.md)
- **JSON name**: `lastDnsRecords`

Domain's DNS records from the last scan.

### `last_dns_records_time`

- **Number**: `27`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastDnsRecordsTime`

Date when the DNS records list was retrieved by VirusTotal.

### `last_https_certificate`

- **Number**: `28`
- **Cardinality**: `singular`
- **Type**: [`SSLCertificate`](ssl_certificate.md)
- **JSON name**: `lastHttpsCertificate`

SSL certificate object retrieved last time the domain was analyzed.

### `last_https_certificate_time`

- **Number**: `29`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `lastHttpsCertificateTime`

When the certificate was retrieved by VirusTotal.

### `popularity_ranks`

- **Number**: `30`
- **Cardinality**: `repeated`
- **Type**: [`PopularityRank`](popularity_rank.md)
- **JSON name**: `popularityRanks`

Domain's position in popularity ranks such as Alexa, Quantcast, Statvoo, etc

### `tags`

- **Number**: `31`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `tags`

List of representative attributes.

### `whois_time`

- **Number**: `32`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `whoisTime`

Date of the last update of the WHOIS record.
