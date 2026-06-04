# `ActingAppType`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations/app_type.md) | inherited from Acting application entity as Acting |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations/app_type.md) | inherited from Acting application entity as Acting |
| [User Management](../schemas/user_management.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations/app_type.md) | inherited from Acting application entity as Acting |

## Details by schema

### AuditEvent

#### `ActingAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations/app_type.md)
- **Follows**: [`ActingAppName`](../fields/acting_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The type of the application.

### Authentication

#### `ActingAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations/app_type.md)
- **Follows**: [`ActingAppName`](../fields/acting_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The type of the application.

### User Management

#### `ActingAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations/app_type.md)
- **Follows**: [`ActingAppName`](../fields/acting_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The type of the application.
