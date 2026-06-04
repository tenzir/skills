# `SrcDomainType`

- **Schema occurrences**: `6`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [Dhcp](../schemas/dhcp.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [Dns](../schemas/dns.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [FileEvent](../schemas/file_event.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [User Management](../schemas/user_management.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |

## Details by schema

### AuditEvent

#### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### Authentication

#### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### Dhcp

#### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### Dns

#### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### FileEvent

#### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### User Management

#### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.
