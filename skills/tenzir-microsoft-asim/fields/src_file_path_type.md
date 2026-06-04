# `SrcFilePathType`

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

#### `SrcFilePathType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Windows Local`, `Windows Share`, `Unix`, `URL`
- **Follows**: [`SrcFilePath`](../fields/src_file_path.md)

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

The type of SrcFilePath. For more information.
