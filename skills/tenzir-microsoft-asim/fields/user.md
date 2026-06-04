# `User`

- **Schema occurrences**: `8`
- **Raw fragment/source occurrences**: `8`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Alias` | `string` | `Username` |  | local |
| [Authentication](../schemas/authentication.md) | `Alias` | `string` | `Username` |  | local |
| [Dhcp](../schemas/dhcp.md) | `Alias` | `string` | `Username` |  | local |
| [Dns](../schemas/dns.md) | `Alias` | `string` | `Username` |  | local |
| [FileEvent](../schemas/file_event.md) | `Alias` | `string` | `Username` |  | local |
| [Notification](../schemas/notification.md) | `Alias` | `string` | `Username` |  | local |
| [ProcessEvent](../schemas/process_event.md) | `Alias` | `string` | `Username` |  | local |
| [RegistryEvent](../schemas/registry_event.md) | `Alias` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimAuditEvent.yaml`
- `ASIM/schemas/ASimAuthentication.yaml`
- `ASIM/schemas/ASimDHCPEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/ASimNotification.yaml`
- `ASIM/schemas/ASimProcessEvent.yaml`
- `ASIM/schemas/ASimRegistryEvent.yaml`

## Details by schema

### AuditEvent

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

### Authentication

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`TargetUsername`](../fields/target_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuthentication.yaml`

### Dhcp

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias for SrcUsername

### Dns

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

### FileEvent

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

### Notification

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

### ProcessEvent

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`

### RegistryEvent

#### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimRegistryEvent.yaml`

Alias to the ActorUsername field.
