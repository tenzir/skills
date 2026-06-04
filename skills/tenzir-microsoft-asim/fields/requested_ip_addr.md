# `RequestedIpAddr`

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

#### `RequestedIpAddr`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The IP address requested by the DHCP client, when available.

#### Examples

- `192.168.12.3`
