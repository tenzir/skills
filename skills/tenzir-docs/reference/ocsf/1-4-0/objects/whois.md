# WHOIS

> The resources of a WHOIS record for a given domain.


The resources of a WHOIS record for a given domain. This can include domain names, IP address blocks, autonomous system information, and/or contact and registration information for a domain.

## Attributes

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

When the domain was registered or WHOIS entry was created.

**`dnssec_status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The disposition is unknown.
  * `1` - `Signed`: The related domain enables the signing of DNS records using DNSSEC.
  * `2` - `Unsigned`: The related domain does not enable the signing of DNS records using DNSSEC.
  * `99` - `Other`: The DNSSEC status is not mapped. See the `dnssec_status` attribute, which contains a data source specific value.

Describes the normalized status of DNS Security Extensions (DNSSEC) for a domain.

**`domain`**

* **Type**: `string_t`
* **Requirement**: recommended

The domain name corresponding to the WHOIS record.

**`domain_contacts`**

* **Type**: [`domain_contact`](domain_contact.md)
* **Requirement**: recommended

An array of `Domain Contact` objects.

**`last_seen_time`**

* **Type**: `timestamp_t`
* **Requirement**: recommended

When the WHOIS record was last updated or seen at.

**`name_servers`**

* **Type**: `string_t`
* **Requirement**: recommended

A collection of name servers related to a domain registration or other record.

**`registrar`**

* **Type**: `string_t`
* **Requirement**: recommended

The domain registrar.

**`status`**

* **Type**: `string_t`
* **Requirement**: recommended

The status of a domain and its ability to be transferred, e.g., `clientTransferProhibited`.

**`autonomous_system`**

* **Type**: [`autonomous_system`](autonomous_system.md)
* **Requirement**: optional

The autonomous system information associated with a domain.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

When the domain was registered or WHOIS entry was created.

**`dnssec_status`**

* **Type**: `string_t`
* **Requirement**: optional

The normalized value of dnssec\_status\_id.

**`email_addr`**

* **Type**: `email_t`
* **Requirement**: optional

The email address for the registrar’s abuse contact

**`last_seen_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

When the WHOIS record was last updated or seen at.

**`phone_number`**

* **Type**: `string_t`
* **Requirement**: optional

The phone number for the registrar’s abuse contact

**`subdomains`**

* **Type**: `string_t`
* **Requirement**: optional

An array of subdomain strings. Can be used to collect several subdomains such as those from Domain Generation Algorithms (DGAs).

**`subnet`**

* **Type**: `subnet_t`
* **Requirement**: optional

The IP address block (CIDR) associated with a domain.