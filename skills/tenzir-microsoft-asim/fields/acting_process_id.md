# `ActingProcessId`

- **Schema occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [RegistryEvent](../schemas/registry_event.md) | `Optional` | `string` |  |  | inherited from Acting process entity as Acting |

## Details by schema

### FileEvent

#### `ActingProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### ProcessEvent

#### `ActingProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### RegistryEvent

#### `ActingProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimProcess.yaml`; include `Acting process entity`; role `Acting`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`
