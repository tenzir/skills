# `DnsResponseName`

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

#### `DnsResponseName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The content of the response, as included in the record.

#### Notes

The DNS response data is inconsistent across reporting devices, is complex to parse, and has less value for source-agnostic analytics. Therefore the information model doesn't require parsing and normalization, and Microsoft Sentinel uses an auxiliary function to provide response information. For more information, see Handling DNS response.
