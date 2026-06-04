# `DstDomainType`

- **Schema occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dns](../schemas/dns.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations.md#domaintype) | inherited from Destination system entity as Dst |

## Details by schema

### Dns

#### `DstDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations.md#domaintype)
- **Follows**: [`DstDomain`](../fields/dst_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

The type of the domain.
