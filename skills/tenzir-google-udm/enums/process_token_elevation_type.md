# Process.TokenElevationType

The elevation type of the process's token. See https://learn.microsoft.com/en-us/windows/win32/api/winnt/ne-winnt-token_elevation_type

- **Full name**: `google.backstory.Process.TokenElevationType`
- **Values**: `4`

## Values

### `UNKNOWN`

- **Number**: `0`

An undetermined token type.

### `TYPE_1`

- **Number**: `1`

A full token with no privileges removed or groups disabled.

### `TYPE_2`

- **Number**: `2`

An elevated token with no privileges removed or groups disabled. Used when running as administrator.

### `TYPE_3`

- **Number**: `3`

A limited token with administrative privileges removed and administrative groups disabled.
