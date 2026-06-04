# `SrcHostname`

- **Schema occurrences**: `6`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [Authentication](../schemas/authentication.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [Dhcp](../schemas/dhcp.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [Dns](../schemas/dns.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [User Management](../schemas/user_management.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |

## Details by schema

### AuditEvent

#### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### Authentication

#### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### Dhcp

#### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### Dns

#### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### FileEvent

#### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### User Management

#### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.
