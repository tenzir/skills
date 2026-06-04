# Id

Identifier to identify a UDM object like a UDM event, Entity, Collection. The full identifier for persistence is created by setting the 32 most significant bits as the Id.Namespace enum This is a convenience wrapper to define the id space enum values and provide an easy interface for RPCs, most persistence use cases should use a denormalized form.

## Fields

### `namespace`

- Type: [`Namespace`](../enums/id_namespace.md) (singular)

Namespace the id belongs to.

### `id`

- Type: `bytes` (singular)

Full raw ID.

### `string_id` / `stringId`

- Type: `string` (singular)

Some ids are stored as strings that are not able to be translated to bytes, so store these separately. Ex. detection id of the form de_aaaaaaaa-aaaa...
