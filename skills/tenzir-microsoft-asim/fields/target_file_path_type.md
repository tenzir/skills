# `TargetFilePathType`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Conditional` | `string` | `Enumerated` | `Windows Local`, `Windows Share`, `Unix`, `URL` | local |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`

## Details by schema

### FileEvent

#### `TargetFilePathType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Windows Local`, `Windows Share`, `Unix`, `URL`
- **Follows**: [`TargetFilePath`](../fields/target_file_path.md)

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

The type of TargetFilePath. For more information.
