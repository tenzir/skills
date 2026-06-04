# EntityMetadata

Information about the Entity and the product where the entity was created.

- **Full name**: `google.backstory.EntityMetadata`
- **Fields**: `17`
- **Nested enums**: `2`

## Nested enums

- [EntityMetadata.EntityType](../enums/entity_metadata_entity_type.md)
- [EntityMetadata.SourceType](../enums/entity_metadata_source_type.md)

## Fields

### `product_entity_id`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productEntityId`

A vendor-specific identifier that uniquely identifies the entity (e.g. a GUID, LDAP, OID, or similar).

### `collected_timestamp`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `collectedTimestamp`

GMT timestamp when the entity information was collected by the vendor's local collection infrastructure.

### `creation_timestamp`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp`
- **JSON name**: `creationTimestamp`

GMT timestamp when the entity described by the product_entity_id was created on the system where data was collected.

### `interval`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `google.type.Interval`
- **JSON name**: `interval`

Valid existence time range for the version of the entity represented by this entity data.

### `vendor_name`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `vendorName`

Vendor name of the product that produced the entity information.

### `product_name`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productName`

Product name that produced the entity information.

### `feed`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `feed`

Vendor feed name for a threat indicator feed.

### `product_version`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productVersion`

Version of the product that produced the entity information.

### `entity_type`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: [`EntityMetadata.EntityType`](../enums/entity_metadata_entity_type.md)
- **JSON name**: `entityType`

Entity type. If an entity has multiple possible types, this specifies the most specific type.

### `description`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `description`

Human-readable description of the entity.

### `threat`

- **Number**: `10`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult`](security_result.md)
- **JSON name**: `threat`

Metadata provided by a threat intelligence feed that identified the entity as malicious.

### `source_type`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`EntityMetadata.SourceType`](../enums/entity_metadata_source_type.md)
- **JSON name**: `sourceType`

The source of the entity.

### `source_labels`

- **Number**: `12`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `sourceLabels`

Entity source metadata labels.

### `event_metadata`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: [`Metadata`](metadata.md)
- **JSON name**: `eventMetadata`

Metadata field from the event.

### `structured_fields`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `structuredFields`
- **Deprecated**: `true`

Structured fields extracted from the log.

### `extracted`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `extracted`

Flattened fields extracted from the log.

### `ati_prioritization`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: [`AtiPrioritization`](ati_prioritization.md)
- **JSON name**: `atiPrioritization`

Prioritization factors used by ATI curated rules.
