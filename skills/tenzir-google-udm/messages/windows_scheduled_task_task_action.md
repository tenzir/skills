# WindowsScheduledTask.TaskAction

The task action.

- **Full name**: `google.backstory.WindowsScheduledTask.TaskAction`
- **Fields**: `5`
- **Nested enums**: `1`

## Nested enums

- [WindowsScheduledTask.TaskAction.ActionType](../enums/windows_scheduled_task_task_action_action_type.md)

## Fields

### `actionType`

- Type: [`WindowsScheduledTask.TaskAction.ActionType`](../enums/windows_scheduled_task_task_action_action_type.md) (singular)

The action type of the task.

### `execArguments`

- Type: `string` (repeated)

The arguments of the task. This field is only populated if the task action type is EXEC.

### `execWorkingDirectory`

- Type: `string` (singular)

The executable working directory of the task. This field is only populated if the task action type is EXEC.

### `comClassId`

- Type: `string` (singular)

The COM class IF the action is COM handler. This field is only populated if the task action type is COM_HANDLER.

### `comData`

- Type: `string` (singular)

The data of the task. This field is only populated if the task action type is COM_HANDLER.
