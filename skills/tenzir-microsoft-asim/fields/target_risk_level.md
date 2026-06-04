# `TargetRiskLevel`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `int` |  |  | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Optional` | `int` |  |  | inherited from Target system entity as Target |

## Details by schema

### AuditEvent

#### `TargetRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.

### Authentication

#### `TargetRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.
