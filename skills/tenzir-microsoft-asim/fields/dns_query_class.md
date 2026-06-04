# `DnsQueryClass`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `integer` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `DnsQueryClass`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS class ID. In practice, only the IN class (ID 1) is used, and therefore this field is less valuable.
