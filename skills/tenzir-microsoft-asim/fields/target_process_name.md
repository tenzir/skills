# `TargetProcessName`

- **Schema occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |

## Details by schema

### ProcessEvent

#### `TargetProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`
