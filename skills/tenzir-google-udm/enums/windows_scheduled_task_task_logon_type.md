# WindowsScheduledTask.TaskLogonType

Enum representing the logon type of the task.

## Values

0. `TASK_LOGON_TYPE_UNSPECIFIED`: The logon method is not specified. Used for non-NT credentials.
1. `PASSWORD`: Use a password for logging on the user. The password must be supplied at registration time.
2. `S4U`: Use an existing interactive token to run a task. The user must log on using a service for user (S4U) logon. When an S4U logon is used, no password is stored by the system and there is no access to either the network or encrypted files.
3. `INTERACTIVE_TOKEN`: User must already be logged on. The task will be run only in an existing interactive session.
4. `GROUP`: Logon with group credentials.
5. `SERVICE_ACCOUNT`: Indicates that a Local System, Local Service, or Network Service account is being used as a security context to run the task.
6. `INTERACTIVE_TOKEN_OR_PASSWORD`: First use the interactive token. If the user is not logged on (no interactive token is available), the password is used. The password must be specified when a task is registered. This flag is not recommended for new tasks because it is less reliable than TASK_LOGON_PASSWORD.
