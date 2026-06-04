# Id

Identifier to identify a UDM object like a UDM event, Entity, Collection. The full identifier for persistence is created by setting the 32 most significant bits as the Id.Namespace enum This is a convenience wrapper to define the id space enum values and provide an easy interface for RPCs, most persistence use cases should use a denormalized form.

- **Full name**: `google.backstory.Id`
- **Fields**: `3`
- **Nested enums**: `1`

## Nested enums

- [Id.Namespace](../enums/id_namespace.md)

## Fields

### `namespace`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Id.Namespace`](../enums/id_namespace.md)
- **JSON name**: `namespace`

Namespace the id belongs to.

### `id`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `id`

Full raw ID.

### `string_id`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `stringId`

Some ids are stored as strings that are not able to be translated to bytes, so store these separately. Ex. detection id of the form de_aaaaaaaa-aaaa...
