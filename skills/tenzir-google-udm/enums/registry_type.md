# Registry.Type

Type of the registry value. These values are based on the Windows Registry value types: https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types

- **Full name**: `google.backstory.Registry.Type`
- **Values**: `13`

## Values

### `TYPE_UNSPECIFIED`

- **Number**: `0`

Default registry value type used when the type is unknown.

### `NONE`

- **Number**: `1`

The registry value is not set and only the key exists.

### `SZ`

- **Number**: `2`

A null-terminated string.

### `EXPAND_SZ`

- **Number**: `3`

A null-terminated string that contains unexpanded references to environment variables

### `BINARY`

- **Number**: `4`

Binary data in any form.

### `DWORD`

- **Number**: `5`

A 32-bit number.

### `DWORD_LITTLE_ENDIAN`

- **Number**: `6`

A 32-bit number in little-endian format.

### `DWORD_BIG_ENDIAN`

- **Number**: `7`

A 32-bit number in big-endian format.

### `LINK`

- **Number**: `8`

A null-terminated Unicode string that contains the target path of a symbolic link.

### `MULTI_SZ`

- **Number**: `9`

A sequence of null-terminated strings, terminated by an empty string

### `RESOURCE_LIST`

- **Number**: `10`

A device driver resource list.

### `QWORD`

- **Number**: `11`

A 64-bit number.

### `QWORD_LITTLE_ENDIAN`

- **Number**: `12`

A 64-bit number in little-endian format.
