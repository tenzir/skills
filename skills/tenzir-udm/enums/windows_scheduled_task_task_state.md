# TaskState

Enum representing the operation state of the task.

## Values

- `TASK_STATE_UNSPECIFIED` (0): The state of the task is unknown or not specified.
- `DISABLED` (1): The task is registered but is disabled and no instances of the task are queued or running. The task cannot be run until it is enabled.
- `QUEUED` (2): Instances of the task are queued.
- `ACTIVE` (3): The task is ready to be executed, but no instances are queued or running.
- `RUNNING` (4): One or more instances of the task are running.
