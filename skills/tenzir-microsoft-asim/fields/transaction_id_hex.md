# `TransactionIdHex`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Recommended` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `TransactionIdHex`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS query unique ID as assigned by the DNS client, in hexadecimal format. Note that this value is part of the DNS protocol and different from DnsSessionId, the network layer session ID, typically assigned by the reporting device.
