# `ParentProcessGuid`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Parent process entity as Parent |

## Details by schema

### ProcessEvent

#### `ParentProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### RegistryEvent

#### `ParentProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Parent process entity`; role `Parent`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`
