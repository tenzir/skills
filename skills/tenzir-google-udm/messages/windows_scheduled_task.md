# WindowsScheduledTask

Information about a Windows scheduled task.

- **Full name**: `google.backstory.WindowsScheduledTask`
- **Fields**: `7`
- **Nested messages**: `2`
- **Nested enums**: `2`

## Nested messages

- [WindowsScheduledTask.TaskAction](windows_scheduled_task_task_action.md)
- [WindowsScheduledTask.TaskTrigger](windows_scheduled_task_task_trigger.md)

## Nested enums

- [WindowsScheduledTask.TaskState](../enums/windows_scheduled_task_task_state.md)
- [WindowsScheduledTask.TaskLogonType](../enums/windows_scheduled_task_task_logon_type.md)

## Fields

### `author`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `author`

The account name that authored or last modified the scheduled task.

### `virtual_path`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `virtualPath`

The task's path in the Task Scheduler library.

### `exit_code`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `exitCode`

The result which was returned the last time the registered task was run.

### `state`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`WindowsScheduledTask.TaskState`](../enums/windows_scheduled_task_task_state.md)
- **JSON name**: `state`

The operation state of the task.

### `logon_type`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`WindowsScheduledTask.TaskLogonType`](../enums/windows_scheduled_task_task_logon_type.md)
- **JSON name**: `logonType`

The logon type of the task.

### `task_actions`

- **Number**: `6`
- **Cardinality**: `repeated`
- **Type**: [`WindowsScheduledTask.TaskAction`](windows_scheduled_task_task_action.md)
- **JSON name**: `taskActions`

The actions of the scheduled task.

### `task_triggers`

- **Number**: `7`
- **Cardinality**: `repeated`
- **Type**: [`WindowsScheduledTask.TaskTrigger`](windows_scheduled_task_task_trigger.md)
- **JSON name**: `taskTriggers`

The triggers of the scheduled task.
