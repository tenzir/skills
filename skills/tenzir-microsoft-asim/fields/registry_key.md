# `RegistryKey`

- **Schema occurrences**: `1`
- **Raw fragment/source occurrences**: `1`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [RegistryEvent](../schemas/registry_event.md) | `Mandatory` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimRegistryEvent.yaml`

## Details by schema

### RegistryEvent

#### `RegistryKey`

- **Class**: `Mandatory`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimRegistryEvent.yaml`

The registry key associated with the operation, normalized to standard root key naming conventions.

#### Examples

- `HKEY_LOCAL_MACHINE\SOFTWARE\MTG`
