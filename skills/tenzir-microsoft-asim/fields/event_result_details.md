# `EventResultDetails`

- **Schema occurrences**: `9`
- **Raw fragment/source occurrences**: `4`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [Authentication](../schemas/authentication.md) | `Recommended` | `string` | `Enumerated` | `No such user or password`, `No such user`, `Incorrect password`, `Incorrect key`, `Account expired`, `Password expired`, `User locked`, `User disabled`, `Logon violates policy`, `Session expired`, `Other` | local override |
| [Dhcp](../schemas/dhcp.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [Dns](../schemas/dns.md) | `Mandatory` | `string` | `Enumerated` | `TBD` | local override |
| [FileEvent](../schemas/file_event.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [Notification](../schemas/notification.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [ProcessEvent](../schemas/process_event.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [RegistryEvent](../schemas/registry_event.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [User Management](../schemas/user_management.md) | `Recommended` | `string` | `Enumerated` | `NotAuthorized`, `Other` | local override |

## Raw sources

- `ASIM/schemas/ASimAuthentication.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimUserManagement.yaml`
- `ASIM/schemas/common/ASimEventFields.yaml`

## Details by schema

### AuditEvent

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### Authentication

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `No such user or password`, `No such user`, `Incorrect password`, `Incorrect key`, `Account expired`, `Password expired`, `User locked`, `User disabled`, `Logon violates policy`, `Session expired`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuthentication.yaml`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### Dhcp

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### Dns

#### `EventResultDetails`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `TBD`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDns.yaml`

For DNS events, this field provides the DNS response code.

#### References

- [https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml](https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml)

### FileEvent

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### Notification

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### ProcessEvent

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### RegistryEvent

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### User Management

#### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `NotAuthorized`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.
