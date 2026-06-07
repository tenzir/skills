# Registry.Type

Type of the registry value. These values are based on the Windows Registry value types: https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types

## Values

- `TYPE_UNSPECIFIED` (0): Default registry value type used when the type is unknown.
- `NONE` (1): The registry value is not set and only the key exists.
- `SZ` (2): A null-terminated string.
- `EXPAND_SZ` (3): A null-terminated string that contains unexpanded references to environment variables
- `BINARY` (4): Binary data in any form.
- `DWORD` (5): A 32-bit number.
- `DWORD_LITTLE_ENDIAN` (6): A 32-bit number in little-endian format.
- `DWORD_BIG_ENDIAN` (7): A 32-bit number in big-endian format.
- `LINK` (8): A null-terminated Unicode string that contains the target path of a symbolic link.
- `MULTI_SZ` (9): A sequence of null-terminated strings, terminated by an empty string
- `RESOURCE_LIST` (10): A device driver resource list.
- `QWORD` (11): A 64-bit number.
- `QWORD_LITTLE_ENDIAN` (12): A 64-bit number in little-endian format.
