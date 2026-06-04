# `TargetUsernameType`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Target user entity as Target |
| [ProcessEvent](../schemas/process_event.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Target user entity as Target |
| [User Management](../schemas/user_management.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Target user entity as Target |

## Details by schema

### Authentication

#### `TargetUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### ProcessEvent

#### `TargetUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### User Management

#### `TargetUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`
