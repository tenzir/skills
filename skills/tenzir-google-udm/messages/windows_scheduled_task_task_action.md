# TaskAction

The task action.

## Fields

### `action_type` / `actionType`

- Type: [`ActionType`](../enums/windows_scheduled_task_task_action_action_type.md) (singular)

The action type of the task.

### `exec_arguments` / `execArguments`

- Type: `string` (repeated)

The arguments of the task. This field is only populated if the task action type is EXEC.

### `exec_working_directory` / `execWorkingDirectory`

- Type: `string` (singular)

The executable working directory of the task. This field is only populated if the task action type is EXEC.

### `com_class_id` / `comClassId`

- Type: `string` (singular)

The COM class IF the action is COM handler. This field is only populated if the task action type is COM_HANDLER.

### `com_data` / `comData`

- Type: `string` (singular)

The data of the task. This field is only populated if the task action type is COM_HANDLER.
