# `DhcpSessionId`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Optional` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDHCPEvent.yaml`

## Details by schema

### Dhcp

#### `DhcpSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The session identifier as reported by the reporting device. For the Windows DHCP server, set this to the TransactionID field.

#### Examples

- `2099570186`
