# `NetworkProtocol`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `string` | `Enumerated` | `TCP`, `UDP` | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `NetworkProtocol`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TCP`, `UDP`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The transport protocol used by the network resolution event. The value can be UDP or TCP, and is most commonly set to UDP for DNS.

#### Examples

- `UDP`
