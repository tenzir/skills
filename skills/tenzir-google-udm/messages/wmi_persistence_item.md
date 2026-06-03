# WmiPersistenceItem

Information about a WMI persistence item.

- **Full name**: `google.backstory.WmiPersistenceItem`
- **Fields**: `10`

## Fields

### `caption`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `caption`

A brief title or caption for the WMI object.

### `name`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `name`

The name of the WMI object.

### `setting_id`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `settingId`

The identifier for the setting.

### `derivation`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `derivation`

The base class from which the WMI class is derived (e.g., CIM_Setting).

### `property_count`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `propertyCount`

The number of properties in the WMI object.

### `rel_path`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `relPath`

The relative path to the WMI object (e.g., Win32_StartupCommand.Command=''').

### `dynasty`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `dynasty`

The top-level class in the WMI inheritance hierarchy (e.g., CMI_Setting).

### `wmi_super_class`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `wmiSuperClass`

The immediate parent class in the WMI inheritance hierarchy.

### `wmi_class`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `wmiClass`

The name of the WMI class.

### `genus`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `genus`

An integer representing the type or version of the WMI object.
