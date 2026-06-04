# `NetworkApplicationProtocol`

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

#### `NetworkApplicationProtocol`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

When the operation is initiated by a remote system, this value is the application layer protocol used in the OSI model. While this field is not enumerated, and any value is accepted, preferable values include HTTP, HTTPS, SMB,FTP, and SSH.
