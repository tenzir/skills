# `ThreatField`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `4`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Conditional` | `string` | `Enumerated` | `SrcIpAddr`, `DstIpAddr` | local override |
| [Authentication](../schemas/authentication.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |
| [Dhcp](../schemas/dhcp.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |
| [Dns](../schemas/dns.md) | `Conditional` | `string` | `Enumerated` | `SrcIpAddr`, `DstIpAddr`, `Domain`, `DnsResponseName` | local override |
| [FileEvent](../schemas/file_event.md) | `Conditional` | `string` | `Enumerated` | `SrcFilePath`, `DstFilePath` | local override |
| [Notification](../schemas/notification.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |
| [ProcessEvent](../schemas/process_event.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |
| [RegistryEvent](../schemas/registry_event.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |
| [User Management](../schemas/user_management.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |

## Raw sources

- `ASIM/schemas/ASimAuditEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/common/ASimInspectionFields.yaml`

## Details by schema

### AuditEvent

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `SrcIpAddr`, `DstIpAddr`
- **Follows**: [`ThreatIpAddr`](../fields/threat_ip_addr.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`
- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The field for which a threat was identified. The value is either SrcFilePath or DstFilePath.

### Authentication

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.

### Dhcp

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.

### Dns

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `SrcIpAddr`, `DstIpAddr`, `Domain`, `DnsResponseName`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`
- Local: `ASIM/schemas/ASimDns.yaml`

The field for which a threat was identified. The value is either SrcIpAddr, DstIpAddr, Domain, or DnsResponseName..

### FileEvent

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `SrcFilePath`, `DstFilePath`
- **Follows**: [`ThreatFilePath`](../fields/threat_file_path.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`
- Local: `ASIM/schemas/ASimFileEvent.yaml`

The field for which a threat was identified. The value is either SrcFilePath or DstFilePath.

### Notification

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.

### ProcessEvent

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.

### RegistryEvent

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.

### User Management

#### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.
