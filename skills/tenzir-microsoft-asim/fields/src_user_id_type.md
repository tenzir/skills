# `SrcUserIdType`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Source user entity as Src |
| [Dns](../schemas/dns.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Source user entity as Src |

## Details by schema

### Dhcp

#### `SrcUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`SrcUserId`](../fields/src_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### Dns

#### `SrcUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`SrcUserId`](../fields/src_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`
