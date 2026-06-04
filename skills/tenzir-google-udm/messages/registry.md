# Registry

Information about a registry key or value.

## Fields

### `registry_key` / `registryKey`

- Type: `string` (singular)

Registry key associated with an application or system component (e.g., HKEY_, HKCU\Environment...).

### `registry_value_name` / `registryValueName`

- Type: `string` (singular)

Name of the registry value associated with an application or system component (e.g. TEMP).

### `registry_value_data` / `registryValueData`

- Type: `string` (singular)

Data associated with a registry value (e.g. %USERPROFILE%\Local Settings\Temp).

### `registry_value_type` / `registryValueType`

- Type: [`Registry.Type`](../enums/registry_type.md) (singular)

Type of the registry value.

### `registry_value_binary_data` / `registryValueBinaryData`

- Type: `bytes` (singular)

Binary data associated with a registry value. This field is only populated if the registry value type is BINARY. This field is not populated for other registry value types.

## Guidance

Population guidance from the Google UDM usage guide.

### `registry_key` / `registryKey`

- **Purpose**: Stores the registry key associated with an application or system component.
- **Encoding**: String.
- **Example**: HKEY_LOCAL_MACHINE/SYSTEM/DriverDatabase

#### Examples

- HKEY_LOCAL_MACHINE/SYSTEM/DriverDatabase

### `registry_value_data` / `registryValueData`

- **Purpose**: Stores the data associated with a registry value.
- **Encoding**: String.
- **Example**: %USERPROFILE%\Local Settings\Temp

#### Examples

- %USERPROFILE%\Local Settings\Temp

### `registry_value_name` / `registryValueName`

- **Purpose**: Stores the name of the registry value associated with an application or system component.
- **Encoding**: String.
- **Example**: TEMP

#### Examples

- TEMP
