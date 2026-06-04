# `Dvc`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [Authentication](../schemas/authentication.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [Dhcp](../schemas/dhcp.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [Dns](../schemas/dns.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [FileEvent](../schemas/file_event.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [Notification](../schemas/notification.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [ProcessEvent](../schemas/process_event.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [RegistryEvent](../schemas/registry_event.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [User Management](../schemas/user_management.md) | `Alias` | `string` |  |  | inherited from Dvc |

## Raw sources

- `ASIM/schemas/entities/ASimDvc.yaml`

## Details by schema

### AuditEvent

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Authentication

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Dhcp

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Dns

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### FileEvent

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Notification

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### ProcessEvent

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### RegistryEvent

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### User Management

#### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.
