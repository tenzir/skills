# EntityMetadata

Information about the Entity and the product where the entity was created.

## Fields

### `productEntityId`

- Type: `string` (singular)

A vendor-specific identifier that uniquely identifies the entity (e.g. a GUID, LDAP, OID, or similar).

### `collectedTimestamp`

- Type: `timestamp` (singular)

GMT timestamp when the entity information was collected by the vendor's local collection infrastructure.

### `creationTimestamp`

- Type: `timestamp` (singular)

GMT timestamp when the entity described by the productEntityId was created on the system where data was collected.

### `interval`

- Type: `interval` (singular)

Valid existence time range for the version of the entity represented by this entity data.

### `vendorName`

- Type: `string` (singular)

Vendor name of the product that produced the entity information.

### `productName`

- Type: `string` (singular)

Product name that produced the entity information.

### `feed`

- Type: `string` (singular)

Vendor feed name for a threat indicator feed.

### `productVersion`

- Type: `string` (singular)

Version of the product that produced the entity information.

### `entityType`

- Type: [`EntityType`](../enums/entity_metadata_entity_type.md) (singular)

Entity type. If an entity has multiple possible types, this specifies the most specific type.

### `description`

- Type: `string` (singular)

Human-readable description of the entity.

### `threat`

- Type: [`SecurityResult`](security_result.md) (repeated)

Metadata provided by a threat intelligence feed that identified the entity as malicious.

### `sourceType`

- Type: [`SourceType`](../enums/entity_metadata_source_type.md) (singular)

The source of the entity.

### `sourceLabels`

- Type: [`Label`](label.md) (repeated)

Entity source metadata labels.

### `eventMetadata`

- Type: [`Metadata`](metadata.md) (singular)

Metadata field from the event.

### `structuredFields`

- Type: `object` (singular)
- Deprecated: `true`

Structured fields extracted from the log.

### `extracted`

- Type: `object` (singular)

Flattened fields extracted from the log.

### `atiPrioritization`

- Type: [`AtiPrioritization`](ati_prioritization.md) (singular)

Prioritization factors used by ATI curated rules.
