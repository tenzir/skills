# `DstHostname`

- **Schema occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `string` | `Hostname` |  | inherited from Destination system entity as Dst |

## Details by schema

### Dns

#### `DstHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.
