# WindowsScheduledTask.TaskLogonType

Enum representing the logon type of the task.

## Values

- `TASK_LOGON_TYPE_UNSPECIFIED` (0): The logon method is not specified. Used for non-NT credentials.
- `PASSWORD` (1): Use a password for logging on the user. The password must be supplied at registration time.
- `S4U` (2): Use an existing interactive token to run a task. The user must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or encrypted files.
- `INTERACTIVE_TOKEN` (3): User must already be logged on. The task will be run only in an existing interactive session.
- `GROUP` (4): Logon with group credentials.
- `SERVICE_ACCOUNT` (5): Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task.
- `INTERACTIVE_TOKEN_OR_PASSWORD` (6): First use the interactive token. If the user is not logged on (no interactive token is available), the password is used. The password must be specified when a task is registered. This flag is not recommended for new tasks because it is less reliable than TASK_LOGON_PASSWORD.
