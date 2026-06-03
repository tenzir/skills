# Role

System role for resource access and modification.

- **Full name**: `google.backstory.Role`
- **Fields**: `3`
- **Nested enums**: `1`

## Nested enums

- [Role.Type](../enums/role_type.md)

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

System role name for user.

### `description`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `description`

System role description for user.

### `type`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Role.Type`](../enums/role_type.md)
- **JSON name**: `type`

System role type for well known roles.
