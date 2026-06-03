# WindowsScheduledTask.TaskState

Enum representing the operation state of the task.

- **Full name**: `google.backstory.WindowsScheduledTask.TaskState`
- **Values**: `5`

## Values

### `TASK_STATE_UNSPECIFIED`

- **Number**: `0`

The state of the task is unknown or not specified.

### `DISABLED`

- **Number**: `1`

The task is registered but is disabled and no instances of the task are queued or running. The task cannot be run until it is enabled.

### `QUEUED`

- **Number**: `2`

Instances of the task are queued.

### `ACTIVE`

- **Number**: `3`

The task is ready to be executed, but no instances are queued or running.

### `RUNNING`

- **Number**: `4`

One or more instances of the task are running.
