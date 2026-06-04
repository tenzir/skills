# `HashType`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [FileEvent](../schemas/file_event.md) | `Conditional` | `string` | `Enumerated` | `MD5`, `SHA`, `SHA256`, `SHA512`, `IMPHASH` | local |

## Raw sources

- `ASIM/schemas/ASimFileEvent.yaml`

## Details by schema

### FileEvent

#### `HashType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `MD5`, `SHA`, `SHA256`, `SHA512`, `IMPHASH`

#### Provenance

- Local: `ASIM/schemas/ASimFileEvent.yaml`

The type of hash stored in the HASH alias field
