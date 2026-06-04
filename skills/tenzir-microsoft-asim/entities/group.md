# ASimGroup

- **Source**: [`ASIM/schemas/entities/ASimGroup.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimGroup.yaml)
- **Fields**: `6`

## Included by

- [User Management](../schemas/user_management.md) as `Target`

## Raw fields

### `GroupId`

- **Class**: `Optional`
- **Type**: `string`

A machine-readable, alphanumeric, unique representation of the group, for activities involving a group.

#### Examples

- `S-1-5-21-1377283216-344919071-3415362939-500`

### `GroupIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

The type of the ID stored in the GroupId field.

#### Examples

- `SID`

### `GroupName`

- **Class**: `Optional`
- **Type**: `string`

The group name, including domain information when available, for activities involving a group.

#### Examples

- `grp@contoso.com`

### `GroupNameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

Specifies the type of the group name stored in the GroupName field.

#### Examples

- `UPN`

### `GroupOriginalType`

- **Class**: `Optional`
- **Type**: `string`

The original group type, if provided by the source.

### `GroupType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

The type of the group, for activities involving a group.

#### Examples

- `Global Security Enabled`
