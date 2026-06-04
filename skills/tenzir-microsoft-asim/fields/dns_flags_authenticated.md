# `DnsFlagsAuthenticated`

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

#### `DnsFlagsAuthenticated`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS AD flag, which is related to DNSSEC, indicates in a response that all data included in the answer and authority sections of the response have been verified by the server according to the policies of that server. For more information, see RFC 3655 Section 6.1 for more information.
