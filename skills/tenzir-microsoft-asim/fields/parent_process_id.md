# `ParentProcessId`

- **Schema occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Parent process entity as Parent |

## Details by schema

### ProcessEvent

#### `ParentProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### RegistryEvent

#### `ParentProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Parent process entity`; role `Parent`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`
