# Process.TokenElevationType

The elevation type of the process's token. See https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_elevation_type

## Values

0. `UNKNOWN`: An undetermined token type.
1. `TYPE_1`: A full token with no privileges removed or groups disabled.
2. `TYPE_2`: An elevated token with no privileges removed or groups disabled. Used when running as administrator.
3. `TYPE_3`: A limited token with administrative privileges removed and administrative groups disabled.
