# Process.TokenElevationType

The elevation type of the process's token. See https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-tokenElevationType

## Values

- `UNKNOWN` (0): An undetermined token type.
- `TYPE_1` (1): A full token with no privileges removed or groups disabled.
- `TYPE_2` (2): An elevated token with no privileges removed or groups disabled. Used when running as administrator.
- `TYPE_3` (3): A limited token with administrative privileges removed and administrative groups disabled.
