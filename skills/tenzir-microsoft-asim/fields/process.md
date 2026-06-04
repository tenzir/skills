# `Process`

- **Schema occurrences**: `5`
- **Raw fragment/source occurrences**: `5`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Alias` | `string` |  |  | local |
| [Dns](../schemas/dns.md) | `Alias` | `string` |  |  | local |
| [FileEvent](../schemas/file_event.md) | `Alias` | `string` |  |  | local |
| [ProcessEvent](../schemas/process_event.md) | `Alias` | `string` |  |  | local |
| [RegistryEvent](../schemas/registry_event.md) | `Alias` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimAuditEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/ASimProcessEvent.yaml`
- `ASIM/schemas/ASimRegistryEvent.yaml`

## Details by schema

### AuditEvent

#### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`ActingProcessName`](../fields/acting_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Alias to ActingProcessName

### Dns

#### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcProcessName`](../fields/src_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to SrcProcessName

### FileEvent

#### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`ActingProcessName`](../fields/acting_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

Alias to ActingProcessName

### ProcessEvent

#### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetProcessName`](../fields/target_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Alias to TargetProcessName

### RegistryEvent

#### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`ActingProcessName`](../fields/acting_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimRegistryEvent.yaml`

Alias to the ActingProcessName field.
