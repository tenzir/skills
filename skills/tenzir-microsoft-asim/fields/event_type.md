# `EventType`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `10`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Mandatory` | `string` | `Enumerated` | `Set`, `Read`, `Create`, `Delete`, `Execute`, `Install`, `Clear`, `Enable`, `Disable`, `Other` | local override |
| [Authentication](../schemas/authentication.md) | `Mandatory` | `string` | `Enumerated` | `Logon`, `Logoff`, `Elevate` | local override |
| [Dhcp](../schemas/dhcp.md) | `Mandatory` | `string` | `Enumerated` | `Assign`, `Renew`, `Release`, `DNS Update` | local override |
| [Dns](../schemas/dns.md) | `Mandatory` | `string` | `Enumerated` | `TBD` | local override |
| [FileEvent](../schemas/file_event.md) | `Mandatory` | `string` | `Enumerated` | `FileAccessed`, `FileCreated`, `FileModified`, `FileDeleted`, `FileRenamed`, `FileCopied`, `FileMoved`, `FolderCreated`, `FolderDeleted`, `FolderMoved`, `FolderModified`, `FolderCopied`, `FileCreatedOrModified` | local override |
| [Notification](../schemas/notification.md) | `Mandatory` | `string` | `Enumerated` | `Alert`, `Other` | local override |
| [ProcessEvent](../schemas/process_event.md) | `Mandatory` | `string` | `Enumerated` | `ProcessCreated`, `ProcessTerminated` | local override |
| [RegistryEvent](../schemas/registry_event.md) | `Mandatory` | `string` | `Enumerated` | `RegistryKeyCreated`, `RegistryKeyDeleted`, `RegistryKeyRenamed`, `RegistryValueDeleted`, `RegistryValueSet` | local override |
| [User Management](../schemas/user_management.md) | `Mandatory` | `string` | `Enumerated` | `UserCreated`, `UserDeleted`, `UserModified`, `UserLocked`, `UserUnlocked`, `UserDisabled`, `UserEnabled`, `PasswordChanged`, `PasswordReset`, `GroupCreated`, `GroupDeleted`, `GroupModified`, `UserAddedToGroup`, `UserRemovedFromGroup`, `GroupEnumerated`, `UserRead`, `GroupRead` | local override |

## Raw sources

- `ASIM/schemas/ASimAuditEvent.yaml`
- `ASIM/schemas/ASimAuthentication.yaml`
- `ASIM/schemas/ASimDHCPEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/ASimNotification.yaml`
- `ASIM/schemas/ASimProcessEvent.yaml`
- `ASIM/schemas/ASimRegistryEvent.yaml`
- `ASIM/schemas/ASimUserManagement.yaml`
- `ASIM/schemas/common/ASimEventFields.yaml`

## Details by schema

### AuditEvent

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Set`, `Read`, `Create`, `Delete`, `Execute`, `Install`, `Clear`, `Enable`, `Disable`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### Authentication

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Logon`, `Logoff`, `Elevate`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuthentication.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### Dhcp

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Assign`, `Renew`, `Release`, `DNS Update`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Indicate the operation reported by the record.

### Dns

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

For DNS records, this value would be the DNS op code.

#### References

- [https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)

### FileEvent

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `FileAccessed`, `FileCreated`, `FileModified`, `FileDeleted`, `FileRenamed`, `FileCopied`, `FileMoved`, `FolderCreated`, `FolderDeleted`, `FolderMoved`, `FolderModified`, `FolderCopied`, `FileCreatedOrModified`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimFileEvent.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### Notification

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Alert`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimNotification.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### ProcessEvent

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `ProcessCreated`, `ProcessTerminated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### RegistryEvent

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `RegistryKeyCreated`, `RegistryKeyDeleted`, `RegistryKeyRenamed`, `RegistryValueDeleted`, `RegistryValueSet`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimRegistryEvent.yaml`

Describes the operation reported by the record.

### User Management

#### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `UserCreated`, `UserDeleted`, `UserModified`, `UserLocked`, `UserUnlocked`, `UserDisabled`, `UserEnabled`, `PasswordChanged`, `PasswordReset`, `GroupCreated`, `GroupDeleted`, `GroupModified`, `UserAddedToGroup`, `UserRemovedFromGroup`, `GroupEnumerated`, `UserRead`, `GroupRead`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.
