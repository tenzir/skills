# `TargetDvcIdType`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Target system entity as Target |

## Details by schema

### AuditEvent

#### `TargetDvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`TargetDvcId`](../fields/target_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the DvcId.

### Authentication

#### `TargetDvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`TargetDvcId`](../fields/target_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the DvcId.
