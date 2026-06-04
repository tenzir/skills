# Relation

Defines the relationship between the entity (a) and another entity (b).

- **Full name**: `google.backstory.Relation`
- **Fields**: `6`
- **Nested enums**: `3`

## Nested enums

- [Relation.Relationship](../enums/relation_relationship.md)
- [Relation.Directionality](../enums/relation_directionality.md)
- [Relation.EntityLabel](../enums/relation_entity_label.md)

## Fields

### `entity`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `entity`

Entity (b) that the primary entity (a) is related to.

### `entity_type`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`EntityMetadata.EntityType`](../enums/entity_metadata_entity_type.md)
- **JSON name**: `entityType`

Type of the related entity (b) in this relationship.

### `relationship`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Relation.Relationship`](../enums/relation_relationship.md)
- **JSON name**: `relationship`

Type of relationship.

### `direction`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Relation.Directionality`](../enums/relation_directionality.md)
- **JSON name**: `direction`

Directionality of relationship between primary entity (a) and the related entity (b).

### `uid`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `uid`

UID of the relationship.

### `entity_label`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: [`Relation.EntityLabel`](../enums/relation_entity_label.md)
- **JSON name**: `entityLabel`

Label to identify the Noun of the relation.
