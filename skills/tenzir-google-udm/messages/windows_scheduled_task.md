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

- Type: `string` (singular)

The account name that authored or last modified the scheduled task.

### `virtualPath`

- Type: `string` (singular)

The task's path in the Task Scheduler library.

### `exitCode`

- Type: `int32` (singular)

The result which was returned the last time the registered task was run.

### `state`

- Type: [`WindowsScheduledTask.TaskState`](../enums/windows_scheduled_task_task_state.md) (singular)

The operation state of the task.

### `logonType`

- Type: [`WindowsScheduledTask.TaskLogonType`](../enums/windows_scheduled_task_task_logon_type.md) (singular)

The logon type of the task.

### `taskActions`

- Type: [`WindowsScheduledTask.TaskAction`](windows_scheduled_task_task_action.md) (repeated)

The actions of the scheduled task.

### `taskTriggers`

- Type: [`WindowsScheduledTask.TaskTrigger`](windows_scheduled_task_task_trigger.md) (repeated)

The triggers of the scheduled task.
