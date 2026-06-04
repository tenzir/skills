# `ParentProcessCommandLine`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Parent process entity as Parent |

## Details by schema

### ProcessEvent

#### `ParentProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### RegistryEvent

#### `ParentProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Parent process entity`; role `Parent`

The command line used to run the process.

#### Examples

- `choco.exe -v`
