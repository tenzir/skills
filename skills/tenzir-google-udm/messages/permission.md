# Permission

System permission for resource access and modification.

- **Full name**: `google.backstory.Permission`
- **Fields**: `3`
- **Nested enums**: `1`

## Nested enums

- [Permission.PermissionType](../enums/permission_permission_type.md)

## Fields

### `name`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

Name of the permission (e.g. chronicle.analyst.updateRule).

### `description`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `description`

Description of the permission (e.g. 'Ability to update detect rules').

### `type`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Permission.PermissionType`](../enums/permission_permission_type.md)
- **JSON name**: `type`

Type of the permission.
