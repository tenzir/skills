# `SrcUserScope`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [Dns](../schemas/dns.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |

## Details by schema

### Dhcp

#### `SrcUserScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The scope, such as Azure AD tenant, in which UserId and Username are defined.

### Dns

#### `SrcUserScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The scope, such as Azure AD tenant, in which UserId and Username are defined.
