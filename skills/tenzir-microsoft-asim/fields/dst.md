# `Dst`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Alias` | `string` |  |  | inherited from Target system entity as Target |
| [Authentication](../schemas/authentication.md) | `Alias` | `string` |  |  | inherited from Target system entity as Target |
| [Dhcp](../schemas/dhcp.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [Dns](../schemas/dns.md) | `Alias` | `string` |  |  | inherited from Destination system entity as Dst |
| [FileEvent](../schemas/file_event.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [Notification](../schemas/notification.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [ProcessEvent](../schemas/process_event.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [RegistryEvent](../schemas/registry_event.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [User Management](../schemas/user_management.md) | `Recommended` | `string` |  |  | inherited from Event Fields |

## Raw sources

- `ASIM/schemas/common/ASimEventFields.yaml`
- `ASIM/schemas/entities/ASimSystem.yaml`

## Details by schema

### AuditEvent

#### `Dst`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetFQDN`](../fields/target_fqdn.md), [`TargetDvcId`](../fields/target_dvc_id.md), [`TargetHostname`](../fields/target_hostname.md), [`TargetIpAddr`](../fields/target_ip_addr.md), [`TargetMacAddr`](../fields/target_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Target`, `Dst`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

A unique identifier of the destination device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Authentication

#### `Dst`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetFQDN`](../fields/target_fqdn.md), [`TargetDvcId`](../fields/target_dvc_id.md), [`TargetHostname`](../fields/target_hostname.md), [`TargetIpAddr`](../fields/target_ip_addr.md), [`TargetMacAddr`](../fields/target_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Target`, `Dst`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

A unique identifier of the destination device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Dhcp

#### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### Dns

#### `Dst`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DstFQDN`](../fields/dst_fqdn.md), [`DstDvcId`](../fields/dst_dvc_id.md), [`DstHostname`](../fields/dst_hostname.md), [`DstIpAddr`](../fields/dst_ip_addr.md), [`DstMacAddr`](../fields/dst_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Target`, `Dst`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Destination system entity`; role `Dst`

A unique identifier of the destination device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### FileEvent

#### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### Notification

#### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### ProcessEvent

#### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### RegistryEvent

#### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### User Management

#### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.
