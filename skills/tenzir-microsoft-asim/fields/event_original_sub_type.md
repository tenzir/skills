# `EventOriginalSubType`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [Dhcp](../schemas/dhcp.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [Dns](../schemas/dns.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [Notification](../schemas/notification.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [User Management](../schemas/user_management.md) | `Optional` | `string` |  |  | inherited from Event Fields |

## Raw sources

- `ASIM/schemas/common/ASimEventFields.yaml`

## Details by schema

### AuditEvent

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### Authentication

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### Dhcp

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### Dns

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### FileEvent

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### Notification

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### ProcessEvent

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### RegistryEvent

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### User Management

#### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.
