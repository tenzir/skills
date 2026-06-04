# `DnsSessionId`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `DnsSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS session identifier as reported by the reporting device. This value is different from TransactionIdHex, the DNS query unique ID as assigned by the DNS client.

#### Examples

- `EB4BFA28-2EAD-4EF7-BC8A-51DF4FDF5B55`
