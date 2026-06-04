# `TargetAppType`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations.md#apptype) | inherited from Target application entity as Target |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations.md#apptype) | inherited from Target application entity as Target |
| [FileEvent](../schemas/file_event.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations.md#apptype) | inherited from Target application entity as Target |

## Details by schema

### AuditEvent

#### `TargetAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations.md#apptype)
- **Follows**: [`TargetAppName`](../fields/target_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The type of the application.

### Authentication

#### `TargetAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations.md#apptype)
- **Follows**: [`TargetAppName`](../fields/target_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The type of the application.

### FileEvent

#### `TargetAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations.md#apptype)
- **Follows**: [`TargetAppName`](../fields/target_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The type of the application.
