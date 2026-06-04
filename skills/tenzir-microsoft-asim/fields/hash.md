# `Hash`

- **Schema occurrences**: `2`
- **Raw fragment/source occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Alias` | `string` |  |  | local |
| [ProcessEvent](../schemas/process_event.md) | `Alias` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`
- `ASIM/schemas/ASimProcessEvent.yaml`

## Details by schema

### FileEvent

#### `Hash`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetFileMD5`](../fields/target_file_md5.md), [`TargetFileSHA1`](../fields/target_file_sha1.md), [`TargetFileSHA256`](../fields/target_file_sha256.md), [`TargetFileSHA512`](../fields/target_file_sha512.md)

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

Alias to the best available Target File hash.

### ProcessEvent

#### `Hash`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: `TargetProcessMD5, TargetProcessSHA1, TargetProcessSHA256, TargetProcessSHA512, TargetProcessIMPHASH`

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Alias to Target Process Hash
