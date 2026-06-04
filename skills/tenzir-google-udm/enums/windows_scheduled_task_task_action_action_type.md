# WindowsScheduledTask.TaskAction.ActionType

Enum representing the action type of the task.

## Values

0. `ACTION_TYPE_UNSPECIFIED`: The action type is not specified.
1. `EXEC`: This action performs a command-line operation. For example, the action can run a script, launch an executable, or, if the name of a document is provided, find its associated application and launch the application with the document.
2. `COM_HANDLER`: This action fires a handler. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
3. `SEND_EMAIL`: This action sends an email message. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
4. `SHOW_MESSAGE`: This action shows a message box. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
