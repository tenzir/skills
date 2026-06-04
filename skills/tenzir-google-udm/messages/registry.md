# Registry

Information about a registry key or value.

- **Full name**: `google.backstory.Registry`
- **Fields**: `5`
- **Nested enums**: `1`

## Nested enums

- [Registry.Type](../enums/registry_type.md)

## Fields

### `registry_key`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `registryKey`

Registry key associated with an application or system component (e.g., HKEY_, HKCU\Environment...).

### `registry_value_name`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `registryValueName`

Name of the registry value associated with an application or system component (e.g. TEMP).

### `registry_value_data`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `registryValueData`

Data associated with a registry value (e.g. %USERPROFILE%\Local Settings\Temp).

### `registry_value_type`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Registry.Type`](../enums/registry_type.md)
- **JSON name**: `registryValueType`

Type of the registry value.

### `registry_value_binary_data`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `registryValueBinaryData`

Binary data associated with a registry value. This field is only populated if the registry value type is BINARY. This field is not populated for other registry value types.

## Guidance

Population guidance from the Google UDM usage guide.

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
