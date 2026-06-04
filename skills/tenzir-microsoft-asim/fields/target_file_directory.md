# `TargetFileDirectory`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Optional` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`

## Details by schema

### FileEvent

#### `TargetFileDirectory`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

The target file folder or location. This field should be similar to the TargetFilePath field, without the final element. A parser can provide this value if the value available in the log source and does not need to be extracted from the full path.
