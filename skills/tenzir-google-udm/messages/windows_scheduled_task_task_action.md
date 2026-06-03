# WindowsScheduledTask.TaskAction

The task action.

- **Full name**: `google.backstory.WindowsScheduledTask.TaskAction`
- **Fields**: `5`
- **Nested enums**: `1`

## Nested enums

- [WindowsScheduledTask.TaskAction.ActionType](../enums/windows_scheduled_task_task_action_action_type.md)

## Fields

### `action_type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`WindowsScheduledTask.TaskAction.ActionType`](../enums/windows_scheduled_task_task_action_action_type.md)
- **JSON name**: `actionType`

The action type of the task.

### `exec_arguments`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `execArguments`

The arguments of the task. This field is only populated if the task action type is EXEC.

### `exec_working_directory`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `execWorkingDirectory`

The executable working directory of the task. This field is only populated if the task action type is EXEC.

### `com_class_id`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `comClassId`

The COM class IF the action is COM handler. This field is only populated if the task action type is COM_HANDLER.

### `com_data`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `comData`

The data of the task. This field is only populated if the task action type is COM_HANDLER.
