# `TargetDomainType`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations.md#domaintype) | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations.md#domaintype) | inherited from Target system entity as Target |

## Details by schema

### AuditEvent

#### `TargetDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations.md#domaintype)
- **Follows**: [`TargetDomain`](../fields/target_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the domain.

### Authentication

#### `TargetDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations.md#domaintype)
- **Follows**: [`TargetDomain`](../fields/target_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the domain.
