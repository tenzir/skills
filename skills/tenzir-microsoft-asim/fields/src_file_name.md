# `SrcFileName`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Recommended` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`

## Details by schema

### FileEvent

#### `SrcFileName`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

The name of the target file, without a path or a location, but with an extension if relevant. This field should be similar to the final element in the SrcFilePath field.
