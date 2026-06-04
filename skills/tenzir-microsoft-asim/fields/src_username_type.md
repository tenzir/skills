# `SrcUsernameType`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Source user entity as Src |
| [Dns](../schemas/dns.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Source user entity as Src |

## Details by schema

### Dhcp

#### `SrcUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### Dns

#### `SrcUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`
