# Entity

An Entity provides additional context about an item in a UDM event. For example, a PROCESS_LAUNCH event describes that user 'abc@example.corp' launched process 'shady.exe'. The event does not include information that user 'abc@example.com' is a recently terminated employee who administers a server storing finance data. Information stored in one or more Entities can add this additional context.

- **Full name**: `google.backstory.Entity`
- **Fields**: `6`

## Fields

### `metadata`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`EntityMetadata`](entity_metadata.md)
- **JSON name**: `metadata`

Entity metadata such as timestamp, product, etc.

### `entity`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `entity`

Noun in the UDM event that this entity represents.

### `relations`

- **Number**: `4`
- **Cardinality**: `repeated`
- **Type**: [`Relation`](relation.md)
- **JSON name**: `relations`

One or more relationships between the entity (a) and other entities, including the relationship type and related entity.

### `additional`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Struct`
- **JSON name**: `additional`

Important entity data that cannot be adequately represented within the formal sections of the Entity.

### `risk_score`

- **Number**: `5`
- **Cardinality**: `optional`
- **Type**: [`EntityRisk`](entity_risk.md)
- **JSON name**: `riskScore`

Stores information related to the entity's risk score.

### `metric`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: [`Metric`](metric.md)
- **JSON name**: `metric`

Stores statistical metrics about the entity. Used if metadata.entity_type is METRIC.
