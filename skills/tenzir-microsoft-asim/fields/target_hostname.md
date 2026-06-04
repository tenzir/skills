# `TargetHostname`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` | `Hostname` |  | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` | `Hostname` |  | inherited from Target system entity as Target |

## Details by schema

### AuditEvent

#### `TargetHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### Authentication

#### `TargetHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.
