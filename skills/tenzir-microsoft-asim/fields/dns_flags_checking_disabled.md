# `DnsFlagsCheckingDisabled`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `bool` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `DnsFlagsCheckingDisabled`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS CD flag, which is related to DNSSEC, indicates in a query that non-verified data is acceptable to the system sending the query. For more information, see RFC 3655 Section 6.1 for more information.
