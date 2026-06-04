# `DnsQueryTypeName`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Recommended` | `string` | `Enumerated` | `TBD` | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `DnsQueryTypeName`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The DNS Resource Record Type names.

#### Notes

- IANA doesn't define the case for the values, so analytics must normalize the case as needed.
- The value ANY is supported for the response code 255.
- The value TYPExxxx is supported for unmapped response codes, where xxxx is the numerical value of the response code, as reported by the BIND DNS server.
- If the source provides only a numerical query type code and not a query type name, the parser must include a lookup table to enrich with this value.

#### Examples

- `AAAA`
