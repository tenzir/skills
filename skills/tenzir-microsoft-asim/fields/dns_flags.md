# `DnsFlags`

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

#### `DnsFlags`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

List of strings  The flags field, as provided by the reporting device. If flag information is provided in multiple fields, concatenate them with comma as a separator.

#### Notes

Since DNS flags are complex to parse and are less often used by analytics, parsing, and normalization aren't required. Microsoft Sentinel can use an auxiliary function to provide flags information. For more information, see Handling DNS response.

#### Examples

- `DR`
