# WmiPersistenceItem

Information about a WMI persistence item.

## Fields

### `caption`

- Type: `string` (singular)

A brief title or caption for the WMI object.

### `name`

- Type: `string` (singular)

The name of the WMI object.

### `settingId`

- Type: `string` (singular)

The identifier for the setting.

### `derivation`

- Type: `string` (singular)

The base class from which the WMI class is derived (e.g., CIM_Setting).

### `propertyCount`

- Type: `int64` (singular)

The number of properties in the WMI object.

### `relPath`

- Type: `string` (singular)

The relative path to the WMI object (e.g., Win32_StartupCommand.Command=''').

### `dynasty`

- Type: `string` (singular)

The top-level class in the WMI inheritance hierarchy (e.g., CMI_Setting).

### `wmiSuperClass`

- Type: `string` (singular)

The immediate parent class in the WMI inheritance hierarchy.

### `wmiClass`

- Type: `string` (singular)

The name of the WMI class.

### `genus`

- Type: `int64` (singular)

An integer representing the type or version of the WMI object.
