# `IpAddr`

- **Schema occurrences**: `6`
- **Raw fragment/source occurrences**: `6`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Alias` | `string` | `IP Address` |  | local |
| [Authentication](../schemas/authentication.md) | `Alias` | `string` | `IP Address` |  | local |
| [Dhcp](../schemas/dhcp.md) | `Alias` | `string` | `IP Address` |  | local |
| [Dns](../schemas/dns.md) | `Alias` | `string` | `IP Address` |  | local |
| [FileEvent](../schemas/file_event.md) | `Alias` | `string` | `IP Address` |  | local |
| [Notification](../schemas/notification.md) | `Alias` | `string` | `IP Address` |  | local |

## Raw sources

- `ASIM/schemas/ASimAuditEvent.yaml`
- `ASIM/schemas/ASimAuthentication.yaml`
- `ASIM/schemas/ASimDHCPEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/ASimNotification.yaml`

## Details by schema

### AuditEvent

#### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Alias to SrcIpAddr

### Authentication

#### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuthentication.yaml`

Alias to SrcIpAddr

### Dhcp

#### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to SrcIpAddr

### Dns

#### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to SrcIpAddr

### FileEvent

#### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

Alias to SrcIpAddr

### Notification

#### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`DvcIpAddr`](../fields/dvc_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

Alias to DvcIpAddr
