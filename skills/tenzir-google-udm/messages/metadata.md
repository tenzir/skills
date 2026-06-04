# Metadata

General information associated with a UDM event.

- **Full name**: `google.backstory.Metadata`
- **Fields**: `22`
- **Nested enums**: `3`

## Nested enums

- [Metadata.EventTimestampAttribute](../enums/metadata_event_timestamp_attribute.md)
- [Metadata.EventType](../enums/metadata_event_type.md)
- [Metadata.EnrichmentState](../enums/metadata_enrichment_state.md)

## Fields

### `id`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `id`

ID of the UDM event. Can be used for raw and normalized event retrieval.

### `product_log_id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productLogId`

A vendor-specific event identifier to uniquely identify the event (e.g. a GUID).

### `event_timestamp`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `eventTimestamp`

The GMT timestamp when the event was generated.

### `event_timestamp_attributes`

- **Number**: `21`
- **Cardinality**: `repeated`
- **Type**: [`Metadata.EventTimestampAttribute`](../enums/metadata_event_timestamp_attribute.md)
- **JSON name**: `eventTimestampAttributes`

Attributes associated with event_timestamp. This field is used to distinguish between different types of timestamps that can be used to represent the event_timestamp.

### `collected_timestamp`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `collectedTimestamp`

The GMT timestamp when the event was collected by the vendor's local collection infrastructure.

### `ingested_timestamp`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `ingestedTimestamp`

The GMT timestamp when the event was ingested (received) by Chronicle.

### `event_type`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Metadata.EventType`](../enums/metadata_event_type.md)
- **JSON name**: `eventType`

The event type. If an event has multiple possible types, this specifies the most specific type.

### `vendor_name`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `vendorName`

The name of the product vendor.

### `product_name`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productName`

The name of the product.

### `product_version`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productVersion`

The version of the product.

### `product_event_type`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productEventType`

A short, descriptive, human-readable, product-specific event name or type (e.g. "Scanned X", "User account created", "process_start").

### `product_deployment_id`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productDeploymentId`

The deployment identifier assigned by the vendor for a product deployment.

### `description`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `description`

A human-readable unparsable description of the event.

### `url_back_to_product`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `urlBackToProduct`

A URL that takes the user to the source product console for this event.

### `ingestion_labels`

- **Number**: `12`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `ingestionLabels`

User-configured ingestion metadata labels.

### `tags`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: [`Tags`](tags.md)
- **JSON name**: `tags`

Tags added by Chronicle after an event is parsed. It is an error to populate this field from within a parser.

### `enrichment_state`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: [`Metadata.EnrichmentState`](../enums/metadata_enrichment_state.md)
- **JSON name**: `enrichmentState`

The enrichment state.

### `log_type`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `logType`

The string value of log type.

### `base_labels`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: [`DataAccessLabels`](data_access_labels.md)
- **JSON name**: `baseLabels`

Data access labels on the base event.

### `enrichment_labels`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: [`DataAccessLabels`](data_access_labels.md)
- **JSON name**: `enrichmentLabels`

Data access labels from all the contextual events used to enrich the base event.

### `structured_fields`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `structuredFields`
- **Deprecated**: `true`

Flattened fields extracted from the log.

### `parser_version`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `parserVersion`

The version of the parser that generated this UDM event.

## Guidance

Population guidance from the Google UDM usage guide.

### `Metadata.collected_timestamp`

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

### `Metadata.event_timestamp`

- **Purpose**: Encodes the GMT timestamp when the event was generated.
- **Required**: Yes
- **Encoding**: RFC 3339, as appropriate for JSON or Proto3 timestamp format.

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

#### Examples

- Falcon
- Symantec Endpoint Protection

### `Metadata.product_version`

- **Purpose**: Specifies the version of the product.
- **Encoding**: Alphanumeric string, periods and dashes allowed, 32 bytes maximum

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

#### Examples

- CrowdStrike
- Symantec
