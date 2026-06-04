# `EventSubType`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `5`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` | `Enumerated` | `System`, `Interactive`, `Service`, `RemoteInteractive`, `RemoteService`, `Remote`, `AssumeRole` | local override |
| [Dhcp](../schemas/dhcp.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [Dns](../schemas/dns.md) | `Mandatory` | `string` | `Enumerated` | `request`, `response` | local override |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` | `Enumerated` | `Upload`, `Extended`, `Recycle`, `Preview`, `Download`, `Versions`, `Site`, `Recycle`, `Checkin`, `Checkout`, `FolderModified` | local override |
| [Notification](../schemas/notification.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [User Management](../schemas/user_management.md) | `Optional` | `string` | `Enumerated` | `Password`, `Hash` | local override |

## Raw sources

- `ASIM/schemas/ASimAuthentication.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/ASimUserManagement.yaml`
- `ASIM/schemas/common/ASimEventFields.yaml`

## Details by schema

### AuditEvent

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### Authentication

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `System`, `Interactive`, `Service`, `RemoteInteractive`, `RemoteService`, `Remote`, `AssumeRole`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuthentication.yaml`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### Dhcp

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### Dns

#### `EventSubType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `request`, `response`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

#### Notes

For most sources, only the responses are logged, and therefore the value is often response.

### FileEvent

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Upload`, `Extended`, `Recycle`, `Preview`, `Download`, `Versions`, `Site`, `Recycle`, `Checkin`, `Checkout`, `FolderModified`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimFileEvent.yaml`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### Notification

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### ProcessEvent

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### RegistryEvent

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### User Management

#### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Password`, `Hash`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.
