# Registry Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Registry](../messages/registry.md)

## Fields

### `Registry.registry_key`

- **Purpose**: Stores the registry key associated with an application or system component.
- **Encoding**: String.
- **Example**: HKEY_LOCAL_MACHINE/SYSTEM/DriverDatabase

#### Examples

- HKEY_LOCAL_MACHINE/SYSTEM/DriverDatabase

### `Registry.registry_value_data`

- **Purpose**: Stores the data associated with a registry value.
- **Encoding**: String.
- **Example**: %USERPROFILE%\Local Settings\Temp

#### Examples

- %USERPROFILE%\Local Settings\Temp

### `Registry.registry_value_name`

- **Purpose**: Stores the name of the registry value associated with an application or system component.
- **Encoding**: String.
- **Example**: TEMP

#### Examples

- TEMP
