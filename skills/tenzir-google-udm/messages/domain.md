# Domain

Information about a domain.

## Fields

### `name`

- Type: `string` (singular)

The domain name. This field can be used as an entity indicator for Domain entities.

### `prevalence`

- Type: [`Prevalence`](prevalence.md) (singular)

The prevalence of the domain within the customer's environment.

### `first_seen_time` / `firstSeenTime`

- Type: `timestamp` (singular)

First seen timestamp of the domain in the customer's environment.

### `last_seen_time` / `lastSeenTime`

- Type: `timestamp` (singular)

Last seen timestamp of the domain in the customer's environment.

### `registrar`

- Type: `string` (singular)

Registrar name . FOr example, "Wild West Domains, Inc. (R120-LROR)", "GoDaddy.com, LLC", or "PDR LTD. D/B/A PUBLICDOMAINREGISTRY.COM".

### `contact_email` / `contactEmail`

- Type: `string` (singular)

Contact email address.

### `whois_server` / `whoisServer`

- Type: `string` (singular)

Whois server name.

### `name_server` / `nameServer`

- Type: `string` (repeated)

Repeated list of name servers.

### `creation_time` / `creationTime`

- Type: `timestamp` (singular)

Domain creation time.

### `update_time` / `updateTime`

- Type: `timestamp` (singular)

Last updated time.

### `expiration_time` / `expirationTime`

- Type: `timestamp` (singular)

Expiration time.

### `audit_update_time` / `auditUpdateTime`

- Type: `timestamp` (singular)

Audit updated time.

### `status`

- Type: `string` (singular)

Domain status. See [https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en) for meanings of possible values

### `registrant`

- Type: [`User`](user.md) (singular)

Parsed contact information for the registrant of the domain.

### `admin`

- Type: [`User`](user.md) (singular)

Parsed contact information for the administrative contact for the domain.

### `tech`

- Type: [`User`](user.md) (singular)

Parsed contact information for the technical contact for the domain

### `billing`

- Type: [`User`](user.md) (singular)

Parsed contact information for the billing contact of the domain.

### `zone`

- Type: [`User`](user.md) (singular)

Parsed contact information for the zone.

### `whois_record_raw_text` / `whoisRecordRawText`

- Type: `bytes` (singular)

WHOIS raw text.

### `registry_data_raw_text` / `registryDataRawText`

- Type: `bytes` (singular)

Registry Data raw text.

### `iana_registrar_id` / `ianaRegistrarId`

- Type: `int32` (singular)

IANA Registrar ID. See [https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml](https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml)

### `private_registration` / `privateRegistration`

- Type: `bool` (singular)

Indicates whether the domain appears to be using a private registration service to mask the owner's contact information.

### `categories`

- Type: `string` (repeated)

Categories assign to the domain as retrieved from VirusTotal.

### `favicon`

- Type: [`Favicon`](favicon.md) (singular)

Includes difference hash and MD5 hash of the domain's favicon.

### `jarm`

- Type: `string` (singular)

Domain's JARM hash.

### `last_dns_records` / `lastDnsRecords`

- Type: [`DNSRecord`](dns_record.md) (repeated)

Domain's DNS records from the last scan.

### `last_dns_records_time` / `lastDnsRecordsTime`

- Type: `timestamp` (singular)

Date when the DNS records list was retrieved by VirusTotal.

### `last_https_certificate` / `lastHttpsCertificate`

- Type: [`SSLCertificate`](ssl_certificate.md) (singular)

SSL certificate object retrieved last time the domain was analyzed.

### `last_https_certificate_time` / `lastHttpsCertificateTime`

- Type: `timestamp` (singular)

When the certificate was retrieved by VirusTotal.

### `popularity_ranks` / `popularityRanks`

- Type: [`PopularityRank`](popularity_rank.md) (repeated)

Domain's position in popularity ranks such as Alexa, Quantcast, Statvoo, etc

### `tags`

- Type: `string` (repeated)

List of representative attributes.

### `whois_time` / `whoisTime`

- Type: `timestamp` (singular)

Date of the last update of the WHOIS record.
