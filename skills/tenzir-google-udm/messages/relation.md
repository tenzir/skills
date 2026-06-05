# Relation

Defines the relationship between the entity (a) and another entity (b).

## Fields

### `entity`

- Type: [`Noun`](noun.md) (singular)

Entity (b) that the primary entity (a) is related to.

### `entity_type` / `entityType`

- Type: [`EntityType`](../enums/entity_metadata_entity_type.md) (singular)

Type of the related entity (b) in this relationship.

### `relationship`

- Type: [`Relationship`](../enums/relation_relationship.md) (singular)

Type of relationship.

### `direction`

- Type: [`Directionality`](../enums/relation_directionality.md) (singular)

Directionality of relationship between primary entity (a) and the related entity (b).

### `uid`

- Type: `bytes` (singular)

UID of the relationship.

### `entity_label` / `entityLabel`

- Type: [`EntityLabel`](../enums/relation_entity_label.md) (singular)

Label to identify the Noun of the relation.
