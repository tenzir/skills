# `TargetDvcScopeId`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |

## Details by schema

### AuditEvent

#### `TargetDvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.

### Authentication

#### `TargetDvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.
