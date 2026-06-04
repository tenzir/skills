# `TargetProcessId`

- **Schema occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [ProcessEvent](../schemas/process_event.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |

## Details by schema

### ProcessEvent

#### `TargetProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`
