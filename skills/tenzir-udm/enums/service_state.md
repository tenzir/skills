# Service.State

The current status of the service.

## Values

- `STATE_UNSPECIFIED` (0): Default service status.
- `RUNNING` (1): The service is running.
- `STOPPED` (2): The service is stopped. This is a Windows-specific service status.
- `PAUSED` (3): The service is paused. This is a Windows-specific service status.
- `COMPLETED` (4): The service is completed.
- `START_PENDING` (5): The service is starting.
- `STOP_PENDING` (6): The service is stopping.
- `PAUSE_PENDING` (7): The service is pausing.
- `CONTINUE_PENDING` (8): The service is continuing.
