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
- **Type**: `google.protobuf.Timestamp` (imported)
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
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `collectedTimestamp`

The GMT timestamp when the event was collected by the vendor's local collection infrastructure.

### `ingested_timestamp`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
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
- **Type**: `google.backstory.DataAccessLabels` (imported)
- **JSON name**: `baseLabels`

Data access labels on the base event.

### `enrichment_labels`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `google.backstory.DataAccessLabels` (imported)
- **JSON name**: `enrichmentLabels`

Data access labels from all the contextual events used to enrich the base event.

### `structured_fields`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct` (imported)
- **JSON name**: `structuredFields`
- **Deprecated**: `true`

Flattened fields extracted from the log.

### `parser_version`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `parserVersion`

The version of the parser that generated this UDM event.
