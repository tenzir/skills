# WindowsScheduledTask.TaskState

Enum representing the operation state of the task.

## Values

0. `TASK_STATE_UNSPECIFIED`: The state of the task is unknown or not specified.
1. `DISABLED`: The task is registered but is disabled and no instances of the task are queued or running. The task cannot be run until it is enabled.
2. `QUEUED`: Instances of the task are queued.
3. `ACTIVE`: The task is ready to be executed, but no instances are queued or running.
4. `RUNNING`: One or more instances of the task are running.
