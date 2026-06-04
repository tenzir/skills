# `EventSchema`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `10`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Mandatory` | `string` | `Enumerated` | [AuditEvent](../schemas/audit_event.md) | local override |
| [Authentication](../schemas/authentication.md) | `Mandatory` | `string` | `Enumerated` | [Authentication](../schemas/authentication.md) | local override |
| [Dhcp](../schemas/dhcp.md) | `Mandatory` | `string` | `Enumerated` | [Dhcp](../schemas/dhcp.md) | local override |
| [Dns](../schemas/dns.md) | `Mandatory` | `string` | `Enumerated` | [Dns](../schemas/dns.md) | local override |
| [FileEvent](../schemas/file_event.md) | `Mandatory` | `string` | `Enumerated` | [FileEvent](../schemas/file_event.md) | local override |
| [Notification](../schemas/notification.md) | `Mandatory` | `string` | `Enumerated` | [Notification](../schemas/notification.md) | local override |
| [ProcessEvent](../schemas/process_event.md) | `Mandatory` | `string` | `Enumerated` | [ProcessEvent](../schemas/process_event.md) | local override |
| [RegistryEvent](../schemas/registry_event.md) | `Mandatory` | `string` | `Enumerated` | [RegistryEvent](../schemas/registry_event.md) | local override |
| [User Management](../schemas/user_management.md) | `Mandatory` | `string` | `Enumerated` | `UserManagement` | local override |

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

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AuditEvent](../schemas/audit_event.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### Authentication

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Authentication](../schemas/authentication.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuthentication.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### Dhcp

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Dhcp](../schemas/dhcp.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### Dns

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Dns](../schemas/dns.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### FileEvent

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [FileEvent](../schemas/file_event.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimFileEvent.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### Notification

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Notification](../schemas/notification.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimNotification.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### ProcessEvent

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [ProcessEvent](../schemas/process_event.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimProcessEvent.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### RegistryEvent

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [RegistryEvent](../schemas/registry_event.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimRegistryEvent.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### User Management

#### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `UserManagement`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

The schema the event is normalized to. Each schema documents its schema name.
