# Metadata Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Metadata](../messages/metadata.md)

## Fields

### `Metadata.collected_timestamp`

- **Purpose**: Encodes the GMT timestamp when the event was collected by the vendor's local collection infrastructure.
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.
- **Example**: RFC 3339: '2019-09-10T20:32:31-08:00' Proto3 format: '2012-04-23T18:25:43.511Z'

#### Examples

- RFC 3339: '2019-09-10T20:32:31-08:00'
- Proto3 format: '2012-04-23T18:25:43.511Z'

### `Metadata.description`

- **Purpose**: Human-readable description of the event.
- **Encoding**: Alpha-numeric string, punctuation allowed, 1024 bytes maximum
- **Example**: File c:\bar\foo.exe blocked from accessing sensitive document c:\documents\earnings.docx.

#### Examples

- File c:\bar\foo.exe blocked from accessing sensitive document c:\documents\earnings.docx.

### `Metadata.event_timestamp`

- **Purpose**: Encodes the GMT timestamp when the event was generated.
- **Required**: Yes
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.
- **Example**: RFC 3339: 2019-09-10T20:32:31-08:00 Proto3 format: 2012-04-23T18:25:43.511Z

#### Examples

- RFC 3339: 2019-09-10T20:32:31-08:00
- Proto3 format: 2012-04-23T18:25:43.511Z

### `Metadata.event_type`

- **Purpose**: Specifies the type of the event. If an event has multiple possible types, this value must specify the most specific type.
- **Required**: Yes.
- **Encoding**: Must be one of the predefined UDM event_type enumerated types.
- **Possible values**: The following lists all of the possible values for event_type within the UDM.

### `Metadata.product_event_type`

- **Purpose**: Short, descriptive, human-readable, and product-specific event name or type.
- **Encoding**: Alpha-numeric string, punctuation allowed, 64 bytes maximum.
- **Examples**: Registry Creation Event ProcessRollUp Privilege Escalation Detected Malware blocked

#### Examples

- Registry Creation Event
- ProcessRollUp
- Privilege Escalation Detected
- Malware blocked

### `Metadata.product_log_id`

- **Purpose**: Encodes a vendor-specific event identifier to uniquely identify the event (a GUID). Users might use this identifier to search the vendor's proprietary console for the event in question.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum.
- **Example**: ABcd1234-98766

#### Examples

- ABcd1234-98766

### `Metadata.product_name`

- **Purpose**: Specifies the name of the product.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum.
- **Examples**: Falcon Symantec Endpoint Protection

#### Examples

- Falcon
- Symantec Endpoint Protection

### `Metadata.product_version`

- **Purpose**: Specifies the version of the product.
- **Encoding**: Alphanumeric string, periods and dashes allowed, 32 bytes maximum
- **Examples**: 1.2.3b 10.3:rev1

#### Examples

- 1.2.3b
- 10.3:rev1

### `Metadata.url_back_to_product`

- **Purpose**: URL linking to a relevant website where you can view more information about this specific event (or the general event category).
- **Encoding**: Valid RFC 3986 URL with optional parameters such as port information, etc. Must have a protocol prefix before the URL (for example, https:// or http://).
- **Example**: https://newco.altostrat.com:8080/event_info?event_id=12345

#### Examples

- https://newco.altostrat.com:8080/event_info?event_id=12345

### `Metadata.vendor_name`

- **Purpose**: Specifies the product vendor's name.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum
- **Examples**: CrowdStrike Symantec

#### Examples

- CrowdStrike
- Symantec
