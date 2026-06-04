# WindowsScheduledTask

Information about a Windows scheduled task.

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

- Type: [`TaskState`](../enums/windows_scheduled_task_task_state.md) (singular)

The operation state of the task.

### `logonType`

- Type: [`TaskLogonType`](../enums/windows_scheduled_task_task_logon_type.md) (singular)

The logon type of the task.

### `taskActions`

- Type: [`TaskAction`](windows_scheduled_task_task_action.md) (repeated)

The actions of the scheduled task.

### `taskTriggers`

- Type: [`TaskTrigger`](windows_scheduled_task_task_trigger.md) (repeated)

The triggers of the scheduled task.
