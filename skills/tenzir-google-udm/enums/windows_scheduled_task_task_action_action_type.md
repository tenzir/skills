# ActionType

Enum representing the action type of the task.

## Values

- `ACTION_TYPE_UNSPECIFIED` (0): The action type is not specified.
- `EXEC` (1): This action performs a command-line operation. For example, the action can run a script, launch an executable, or, if the name of a document is provided, find its associated application and launch the application with the document.
- `COM_HANDLER` (2): This action fires a handler. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
- `SEND_EMAIL` (3): This action sends an email message. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
- `SHOW_MESSAGE` (4): This action shows a message box. This action can only be used if the task Compatibility property is set to TASK_COMPATIBILITY_V2.
