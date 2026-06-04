# `DnsQuery`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Mandatory` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dns

#### `DnsQuery`

- **Class**: `Mandatory`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

The domain that the request tries to resolve.

#### Notes

- Some sources send valid FQDN queries in a different format. For example, in the DNS protocol itself, the query includes a dot (.) at the end, which must be removed.
- While the DNS protocol limits the type of value in this field to an FQDN, most DNS servers allow any value, and this field is therefore not limited to FQDN values only. Most notably, DNS tunneling attacks may use invalid FQDN values in the query field.
- While the DNS protocol allows for multiple queries in a single request, this scenario is rare, if it's found at all. If the request has multiple queries, store the first one in this field, and then and optionally keep the rest in the AdditionalFields field.

#### Examples

- `www.malicious.com`
