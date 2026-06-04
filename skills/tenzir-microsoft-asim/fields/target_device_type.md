# `TargetDeviceType`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations.md#devicetype) | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations.md#devicetype) | inherited from Target system entity as Target |

## Details by schema

### AuditEvent

#### `TargetDeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations.md#devicetype)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the device.

### Authentication

#### `TargetDeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations.md#devicetype)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the device.
