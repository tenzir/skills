# Process

Information about a process.

## Fields

### `pid`

- Type: `string` (singular)

The process ID. This field can be used as an entity indicator for process entities.

### `parent_pid` / `parentPid`

- Type: `string` (singular)
- Deprecated: `true`

The ID of the parent process. Deprecated: use parent_process.pid instead.

### `parent_process` / `parentProcess`

- Type: [`Process`](process.md) (singular)

Information about the parent process.

### `file`

- Type: [`File`](file.md) (singular)

Information about the file in use by the process.

### `command_line` / `commandLine`

- Type: `string` (singular)

The command line command that created the process. This field can be used as an entity indicator for process entities.

### `command_line_history` / `commandLineHistory`

- Type: `string` (repeated)

The command line history of the process.

### `product_specific_process_id` / `productSpecificProcessId`

- Type: `string` (singular)

A product specific process id.

### `access_mask` / `accessMask`

- Type: `uint64` (singular)

A bit mask representing the level of access.

### `integrity_level_rid` / `integrityLevelRid`

- Type: `uint64` (singular)

The Microsoft Windows integrity level relative ID (RID) of the process.

### `euid`

- Type: `string` (singular)

The effective user ID of the process.

### `ruid`

- Type: `string` (singular)

The real user ID of the process.

### `egid`

- Type: `string` (singular)

The effective group ID of the process.

### `rgid`

- Type: `string` (singular)

The real group ID of the process.

### `pgid`

- Type: `string` (singular)

The identifier that points to the process group ID leader.

### `session_leader_pid` / `sessionLeaderPid`

- Type: `string` (singular)

The process ID of the session leader process.

### `tty`

- Type: `string` (singular)

The teletype terminal which the command was executed within.

### `token_elevation_type` / `tokenElevationType`

- Type: [`TokenElevationType`](../enums/process_token_elevation_type.md) (singular)

The elevation type of the process on Microsoft Windows. This determines if any privileges are removed when UAC is enabled.

### `product_specific_parent_process_id` / `productSpecificParentProcessId`

- Type: `string` (singular)
- Deprecated: `true`

A product specific id for the parent process. Please use parent_process.product_specific_process_id instead.

### `ipv6`

- Type: `bool` (singular)

This is used to determine if the process is an IPv6 process.

### `kernel_duration` / `kernelDuration`

- Type: `duration` (singular)

The kernel time spent in the process.

### `user_duration` / `userDuration`

- Type: `duration` (singular)

The user time spent in the process.

### `real_duration` / `realDuration`

- Type: `duration` (singular)

The real time spent in the process. This is the sum of the kernel and user time.

### `state`

- Type: [`Process.State`](../enums/process_state.md) (singular)

The state of the process.

## Guidance

Population guidance from the Google UDM usage guide.

### `Process.command_line` / `Process.commandLine`

- **Purpose**: Stores the command line string for the process.
- **Encoding**: String.
- **Example**: `c:\windows\system32\net.exe` group.

#### Examples

- `c:\windows\system32\net.exe` group.

### `Process.file`

- **Purpose**: Stores the filename of the file in use by the process.
- **Encoding**: String.
- **Example**: report.xls

#### Examples

- report.xls

### `Process.parent_process` / `Process.parentProcess`

- **Purpose**: Stores the details of the parent process.
- **Encoding**: Noun (Process)

### `Process.parent_process.product_specific_process_id` / `Process.parentProcess.productSpecificProcessId`

- **Purpose**: Stores the product specific process ID for the parent process.
- **Encoding**: String.
- **Examples**: `MySQL:78778` or `CS:90512`

#### Examples

- `MySQL:78778` or `CS:90512`

### `Process.pid`

- **Purpose**: Stores the process ID.
- **Encoding**: String.

#### Examples

- 308
- 2002

### `Process.product_specific_process_id` / `Process.productSpecificProcessId`

- **Purpose**: Stores the product specific process ID.
- **Encoding**: String.
- **Examples**: `MySQL:78778` or `CS:90512`

#### Examples

- `MySQL:78778` or `CS:90512`
