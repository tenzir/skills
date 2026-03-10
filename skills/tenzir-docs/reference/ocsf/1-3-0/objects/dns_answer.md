# DNS Answer

> The DNS Answer object represents a specific response provided by the Domain Name System (DNS) when querying for information about a domain or performing a DNS operation.


The DNS Answer object represents a specific response provided by the Domain Name System (DNS) when querying for information about a domain or performing a DNS operation. It encapsulates the relevant details and data returned by the DNS server in response to a query.

* **Extends**: `_dns`

## Attributes

**`rdata`**

* **Type**: `string_t`
* **Requirement**: required

The data describing the DNS resource. The meaning of this data depends on the type and class of the resource record.

**`class`**

* **Type**: `string_t`
* **Requirement**: recommended

The class of DNS data contained in this resource record. See [RFC1035](https://www.rfc-editor.org/rfc/rfc1035.txt). For example: `IN`.

**`flag_ids`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The flag is unknown.
  * `1` - `Authoritative Answer`
  * `2` - `Truncated Response`
  * `3` - `Recursion Desired`
  * `4` - `Recursion Available`
  * `5` - `Authentic Data`
  * `6` - `Checking Disabled`
  * `99` - `Other`: The flag is not mapped. See the `flags` attribute, which contains a data source specific value.

The list of DNS answer header flag IDs.

**`packet_uid`**

* **Type**: `integer_t`
* **Requirement**: recommended

The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response.

**`ttl`**

* **Type**: `integer_t`
* **Requirement**: recommended

The time interval that the resource record may be cached. Zero value means that the resource record can only be used for the transaction in progress, and should not be cached.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The type of data contained in this resource record. See [RFC1035](https://www.rfc-editor.org/rfc/rfc1035.txt). For example: `CNAME`.

**`flags`**

* **Type**: `string_t`
* **Requirement**: optional

The list of DNS answer header flags.

## Used By

* [`dns_activity`](../classes/dns_activity.md)