# `DnsQueryClassName`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `string` | `Enumerated` | `TBD` | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `DnsQueryClassName`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS class name. In practice, only the IN class (ID 1) is used, and therefore this field is less valuable.

#### Examples

- `IN`
