# Registry.Type

Type of the registry value. These values are based on the Windows Registry value types: https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry-value-types

## Values

0. `TYPE_UNSPECIFIED`: Default registry value type used when the type is unknown.
1. `NONE`: The registry value is not set and only the key exists.
2. `SZ`: A null-terminated string.
3. `EXPAND_SZ`: A null-terminated string that contains unexpanded references to environment variables
4. `BINARY`: Binary data in any form.
5. `DWORD`: A 32-bit number.
6. `DWORD_LITTLE_ENDIAN`: A 32-bit number in little-endian format.
7. `DWORD_BIG_ENDIAN`: A 32-bit number in big-endian format.
8. `LINK`: A null-terminated Unicode string that contains the target path of a symbolic link.
9. `MULTI_SZ`: A sequence of null-terminated strings, terminated by an empty string
10. `RESOURCE_LIST`: A device driver resource list.
11. `QWORD`: A 64-bit number.
12. `QWORD_LITTLE_ENDIAN`: A 64-bit number in little-endian format.
