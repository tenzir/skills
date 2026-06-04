# `TargetFilePath`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Mandatory` | `String` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`

## Details by schema

### FileEvent

#### `TargetFilePath`

- **Class**: `Mandatory`
- **Type**: `String`

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

The full, normalized path of the target file, including the folder or location, the file name, and the extension. If the record does not include folder or location information, store the filename only here.

#### Examples

- `C:\Windows\System32\notepad.exe`
