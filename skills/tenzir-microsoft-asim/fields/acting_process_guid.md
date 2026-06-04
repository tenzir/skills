# `ActingProcessGuid`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |

## Details by schema

### FileEvent

#### `ActingProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### ProcessEvent

#### `ActingProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### RegistryEvent

#### `ActingProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`
