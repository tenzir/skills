# Metadata

General information associated with a UDM event.

## Fields

### `id`

- Type: `bytes` (singular)

ID of the UDM event. Can be used for raw and normalized event retrieval.

### `productLogId`

- Type: `string` (singular)

A vendor-specific event identifier to uniquely identify the event (e.g. a GUID).

### `eventTimestamp`

- Type: `google.protobuf.Timestamp` (singular)

The GMT timestamp when the event was generated.

### `eventTimestampAttributes`

- Type: [`EventTimestampAttribute`](../enums/metadata_event_timestamp_attribute.md) (repeated)

Attributes associated with eventTimestamp. This field is used to distinguish between different types of timestamps that can be used to represent the eventTimestamp.

### `collectedTimestamp`

- Type: `google.protobuf.Timestamp` (singular)

The GMT timestamp when the event was collected by the vendor's local collection infrastructure.

### `ingestedTimestamp`

- Type: `google.protobuf.Timestamp` (singular)

The GMT timestamp when the event was ingested (received) by Chronicle.

### `eventType`

- Type: [`EventType`](../enums/metadata_event_type.md) (singular)

The event type. If an event has multiple possible types, this specifies the most specific type.

### `vendorName`

- Type: `string` (singular)

The name of the product vendor.

### `productName`

- Type: `string` (singular)

The name of the product.

### `productVersion`

- Type: `string` (singular)

The version of the product.

### `productEventType`

- Type: `string` (singular)

A short, descriptive, human-readable, product-specific event name or type (e.g. "Scanned X", "User account created", "process_start").

### `productDeploymentId`

- Type: `string` (singular)

The deployment identifier assigned by the vendor for a product deployment.

### `description`

- Type: `string` (singular)

A human-readable unparsable description of the event.

### `urlBackToProduct`

- Type: `string` (singular)

A URL that takes the user to the source product console for this event.

### `ingestionLabels`

- Type: [`Label`](label.md) (repeated)

User-configured ingestion metadata labels.

### `tags`

- Type: [`Tags`](tags.md) (singular)

Tags added by Chronicle after an event is parsed. It is an error to populate this field from within a parser.

### `enrichmentState`

- Type: [`EnrichmentState`](../enums/metadata_enrichment_state.md) (singular)

The enrichment state.

### `logType`

- Type: `string` (singular)

The string value of log type.

### `baseLabels`

- Type: [`DataAccessLabels`](data_access_labels.md) (singular)

Data access labels on the base event.

### `enrichmentLabels`

- Type: [`DataAccessLabels`](data_access_labels.md) (singular)

Data access labels from all the contextual events used to enrich the base event.

### `structuredFields`

- Type: `google.protobuf.Struct` (singular)
- Deprecated: `true`

Flattened fields extracted from the log.

### `parserVersion`

- Type: `string` (singular)

The version of the parser that generated this UDM event.

## Guidance

Population guidance from the Google UDM usage guide.

### `Metadata.collectedTimestamp`

- **Purpose**: Encodes the GMT timestamp when the event was collected by the vendor's local collection infrastructure.
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.

#### Examples

- RFC 3339: '2019-09-10T20:32:31-08:00'
- Proto3 format: '2012-04-23T18:25:43.511Z'

### `Metadata.description`

- **Purpose**: Human-readable description of the event.
- **Encoding**: Alpha-numeric string, punctuation allowed, 1024 bytes maximum
- **Example**: File c:\bar\foo.exe blocked from accessing sensitive document c:\documents\earnings.docx.

#### Examples

- File c:\bar\foo.exe blocked from accessing sensitive document c:\documents\earnings.docx.

### `Metadata.eventTimestamp`

- **Purpose**: Encodes the GMT timestamp when the event was generated.
- **Required**: Yes
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.

#### Examples

- RFC 3339: 2019-09-10T20:32:31-08:00
- Proto3 format: 2012-04-23T18:25:43.511Z

### `Metadata.eventType`

- **Purpose**: Specifies the type of the event. If an event has multiple possible types, this value must specify the most specific type.
- **Required**: Yes.
- **Encoding**: Must be one of the predefined UDM `eventType` enumerated types.
- **Possible values**: The following lists all of the possible values for `eventType` within the UDM.

### `Metadata.productEventType`

- **Purpose**: Short, descriptive, human-readable, and product-specific event name or type.
- **Encoding**: Alpha-numeric string, punctuation allowed, 64 bytes maximum.

#### Examples

- Registry Creation Event
- ProcessRollUp
- Privilege Escalation Detected
- Malware blocked

### `Metadata.productLogId`

- **Purpose**: Encodes a vendor-specific event identifier to uniquely identify the event (a GUID). Users might use this identifier to search the vendor's proprietary console for the event in question.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum.
- **Example**: ABcd1234-98766

#### Examples

- ABcd1234-98766

### `Metadata.productName`

- **Purpose**: Specifies the name of the product.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum.

#### Examples

- Falcon
- Symantec Endpoint Protection

### `Metadata.productVersion`

- **Purpose**: Specifies the version of the product.
- **Encoding**: Alphanumeric string, periods and dashes allowed, 32 bytes maximum

#### Examples

- 1.2.3b
- 10.3:rev1

### `Metadata.urlBackToProduct`

- **Purpose**: URL linking to a relevant website where you can view more information about this specific event (or the general event category).
- **Encoding**: Valid RFC 3986 URL with optional parameters such as port information, etc. Must have a protocol prefix before the URL (for example, https:// or http://).
- **Example**: https://newco.altostrat.com:8080/event_info?event_id=12345

#### Examples

- https://newco.altostrat.com:8080/event_info?event_id=12345

### `Metadata.vendorName`

- **Purpose**: Specifies the product vendor's name.
- **Encoding**: Case-sensitive, alphanumeric string, punctuation allowed, 256 bytes maximum

#### Examples

- CrowdStrike
- Symantec
