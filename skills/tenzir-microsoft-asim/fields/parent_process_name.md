# `ParentProcessName`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Parent process entity as Parent |

## Details by schema

### ProcessEvent

#### `ParentProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### RegistryEvent

#### `ParentProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Parent process entity`; role `Parent`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`
