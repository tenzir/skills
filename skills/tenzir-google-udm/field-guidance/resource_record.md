# ResourceRecord Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Dns.ResourceRecord](../messages/dns_resource_record.md)

## Fields

### `ResourceRecord.binary_data`

- **Purpose**: Stores the raw bytes of any non-UTF8 strings that might be included as part of a DNS response. This field must only be used if the response data returned by the DNS server contains non-UTF8 data. Otherwise, place the DNS response in the data field below. This type of information must be stored here rather than in ResourceRecord.data.
- **Encoding**: Bytes. Note: This field is not specified in RFC 1035 (unlike the other DNS resource record fields), but has been defined by Google SecOps for the UDM.

### `ResourceRecord.class`

- **Purpose**: Stores the code specifying the class of the resource record.
- **Encoding**: 32-bit integer.

### `ResourceRecord.data`

- **Purpose**: Stores the payload or response to the DNS question for all responses encoded in UTF-8 format. For example, the data field could return the IP address of the machine that the domain name refers to. If the resource record is for a different type or class, it might contain another domain name (when one domain name is redirected to another domain name). Data must be stored just as it is in the DNS response.
- **Encoding**: String.

### `ResourceRecord.name`

- **Purpose**: Stores the name of the owner of the resource record.
- **Encoding**: String.

### `ResourceRecord.ttl`

- **Purpose**: Stores the time interval for which the resource record can be cached before the source of the information should again be queried.
- **Encoding**: 32-bit integer.

### `ResourceRecord.type`

- **Purpose**: Stores the code specifying the type of the resource record.
- **Encoding**: 32-bit integer.
