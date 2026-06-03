# WindowsScheduledTask.TaskAction.ActionType

Enum representing the action type of the task.

- **Full name**: `google.backstory.WindowsScheduledTask.TaskAction.ActionType`
- **Values**: `5`

## Values

### `ACTION_TYPE_UNSPECIFIED`

- **Number**: `0`

The action type is not specified.

### `EXEC`

- **Number**: `1`

This action performs a command-line operation. For example, the action can run a script, launch an executable, or, if the name of a document is provided, find its associated application and launch the application with the document.

### `COM_HANDLER`

- **Number**: `2`

This action fires a handler. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.

### `SEND_EMAIL`

- **Number**: `3`

This action sends an email message. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.

### `SHOW_MESSAGE`

- **Number**: `4`

This action shows a message box. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
