# `ActingProcessName`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |

## Details by schema

### FileEvent

#### `ActingProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### ProcessEvent

#### `ActingProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### RegistryEvent

#### `ActingProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`
