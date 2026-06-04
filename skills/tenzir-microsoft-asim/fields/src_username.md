# `SrcUsername`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Recommended` | `string` | `Username` |  | inherited from Source user entity as Src |
| [Dns](../schemas/dns.md) | `Recommended` | `string` | `Username` |  | inherited from Source user entity as Src |

## Details by schema

### Dhcp

#### `SrcUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The user's username, including domain information when available.

### Dns

#### `SrcUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The user's username, including domain information when available.
