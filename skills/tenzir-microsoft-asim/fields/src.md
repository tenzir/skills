# `Src`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [Authentication](../schemas/authentication.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [Dhcp](../schemas/dhcp.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [Dns](../schemas/dns.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [FileEvent](../schemas/file_event.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [Notification](../schemas/notification.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [ProcessEvent](../schemas/process_event.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [RegistryEvent](../schemas/registry_event.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [User Management](../schemas/user_management.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |

## Raw sources

- `ASIM/schemas/common/ASimEventFields.yaml`
- `ASIM/schemas/entities/ASimSystem.yaml`

## Details by schema

### AuditEvent

#### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Authentication

#### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Dhcp

#### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Dns

#### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### FileEvent

#### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### Notification

#### `Src`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the source or acting device. This field might alias the ource or acting device device FQDN, Hostname, Device Id or IP address fields.

### ProcessEvent

#### `Src`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the source or acting device. This field might alias the ource or acting device device FQDN, Hostname, Device Id or IP address fields.

### RegistryEvent

#### `Src`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the source or acting device. This field might alias the ource or acting device device FQDN, Hostname, Device Id or IP address fields.

### User Management

#### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.
