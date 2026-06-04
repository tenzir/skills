# Process

Information about a process.

- **Full name**: `google.backstory.Process`
- **Fields**: `23`
- **Nested enums**: `2`

## Nested enums

- [Process.TokenElevationType](../enums/process_token_elevation_type.md)
- [Process.State](../enums/process_state.md)

## Fields

### `pid`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `pid`

The process ID. This field can be used as an entity indicator for process entities.

### `parent_pid`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `parentPid`
- **Deprecated**: `true`

The ID of the parent process. Deprecated: use parent_process.pid instead.

### `parent_process`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`Process`](process.md)
- **JSON name**: `parentProcess`

Information about the parent process.

### `file`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`File`](file.md)
- **JSON name**: `file`

Information about the file in use by the process.

### `command_line`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `commandLine`

The command line command that created the process. This field can be used as an entity indicator for process entities.

### `command_line_history`

- **Number**: `9`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `commandLineHistory`

The command line history of the process.

### `product_specific_process_id`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productSpecificProcessId`

A product specific process id.

### `access_mask`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `accessMask`

A bit mask representing the level of access.

### `integrity_level_rid`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `integrityLevelRid`

The Microsoft Windows integrity level relative ID (RID) of the process.

### `euid`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `euid`

The effective user ID of the process.

### `ruid`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruid`

The real user ID of the process.

### `egid`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `egid`

The effective group ID of the process.

### `rgid`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `rgid`

The real group ID of the process.

### `pgid`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `pgid`

The identifier that points to the process group ID leader.

### `session_leader_pid`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sessionLeaderPid`

The process ID of the session leader process.

### `tty`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `tty`

The teletype terminal which the command was executed within.

### `token_elevation_type`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`Process.TokenElevationType`](../enums/process_token_elevation_type.md)
- **JSON name**: `tokenElevationType`

The elevation type of the process on Microsoft Windows. This determines if any privileges are removed when UAC is enabled.

### `product_specific_parent_process_id`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `productSpecificParentProcessId`
- **Deprecated**: `true`

A product specific id for the parent process. Please use parent_process.product_specific_process_id instead.

### `ipv6`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `ipv6`

This is used to determine if the process is an IPv6 process.

### `kernel_duration`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration`
- **JSON name**: `kernelDuration`

The kernel time spent in the process.

### `user_duration`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration`
- **JSON name**: `userDuration`

The user time spent in the process.

### `real_duration`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration`
- **JSON name**: `realDuration`

The real time spent in the process. This is the sum of the kernel and user time.

### `state`

- **Number**: `23`
- **Cardinality**: `singular`
- **Type**: [`Process.State`](../enums/process_state.md)
- **JSON name**: `state`

The state of the process.
