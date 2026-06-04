# `TargetUserIdType`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Target user entity as Target |
| [ProcessEvent](../schemas/process_event.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Target user entity as Target |
| [User Management](../schemas/user_management.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Target user entity as Target |

## Details by schema

### Authentication

#### `TargetUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`TargetUserId`](../fields/target_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### ProcessEvent

#### `TargetUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`TargetUserId`](../fields/target_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### User Management

#### `TargetUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`TargetUserId`](../fields/target_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`
