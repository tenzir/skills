# `DstRiskLevel`

- **Schema occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Optional` | `int` |  |  | inherited from Destination system entity as Dst |

## Details by schema

### Dns

#### `DstRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.
