# `ActingProcessCommandLine`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |

## Details by schema

### FileEvent

#### `ActingProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### ProcessEvent

#### `ActingProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### RegistryEvent

#### `ActingProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

The command line used to run the process.

#### Examples

- `choco.exe -v`
