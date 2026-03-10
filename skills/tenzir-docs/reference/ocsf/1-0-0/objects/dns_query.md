# DNS Query

> The DNS query object represents a specific request made to the Domain Name System (DNS) to retrieve information about a domain or perform a DNS operation.


The DNS query object represents a specific request made to the Domain Name System (DNS) to retrieve information about a domain or perform a DNS operation. This object encapsulates the necessary attributes and methods to construct and send DNS queries, specify the query type (e.g., A, AAAA, MX). Defined by D3FEND [d3f:DNSLookup](https://d3fend.mitre.org/dao/artifact/d3f:DNSLookup/).

* **Extends**: `_dns`

## Attributes

**`class`**

* **Type**: `string_t`
* **Requirement**: required

The class of resource records being queried. See [RFC1035](https://www.rfc-editor.org/rfc/rfc1035.txt). For example: `IN`.

**`hostname`**

* **Type**: `hostname_t`
* **Requirement**: required

The hostname or domain being queried. For example: `www.example.com`

**`type`**

* **Type**: `string_t`
* **Requirement**: required

The type of resource records being queried. See [RFC1035](https://www.rfc-editor.org/rfc/rfc1035.txt). For example: A, AAAA, CNAME, MX, and NS.

**`opcode_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Query`: Standard query
  * `1` - `Inverse Query`: Inverse query, obsolete
  * `2` - `Status`: Server status request
  * `3` - `Reserved`: Reserved, not used
  * `4` - `Notify`: Zone change notification
  * `5` - `Update`: Dynamic DNS update
  * `6` - `DSO Message`: DNS Stateful Operations (DSO)

The DNS opcode ID specifies the normalized query message type.

**`packet_uid`**

* **Type**: `integer_t`
* **Requirement**: recommended

The DNS packet identifier assigned by the program that generated the query. The identifier is copied to the response.

**`opcode`**

* **Type**: `string_t`
* **Requirement**: optional

The DNS opcode specifies the type of the query message.

## Used By

* [`dns_activity`](../classes/dns_activity.md)