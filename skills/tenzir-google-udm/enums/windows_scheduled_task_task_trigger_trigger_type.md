# WindowsScheduledTask.TaskTrigger.TriggerType

Enum representing the trigger type of the task. For more details, see https://learn.microsoft.com/en-us/windows/win32/api/taskschd/ne-taskschd-task_trigger_type2.

- **Full name**: `google.backstory.WindowsScheduledTask.TaskTrigger.TriggerType`
- **Values**: `13`

## Values

### `TRIGGER_TYPE_UNSPECIFIED`

- **Number**: `0`

The trigger frequency is not specified.

### `EVENT`

- **Number**: `1`

Triggers the task when a specific event occurs.

### `TIME`

- **Number**: `2`

Triggers the task at a specific time of day.

### `DAILY`

- **Number**: `3`

Triggers the task on a daily schedule. For example, the task starts at a specific time every day, every other day, or every third day.

### `WEEKLY`

- **Number**: `4`

Triggers the task on a weekly schedule. For example, the task starts at 8:00 AM on a specific day every week or other week.

### `MONTHLY`

- **Number**: `5`

Triggers the task on a monthly schedule. For example, the task starts on specific days of specific months.

### `MONTHLYDOW`

- **Number**: `6`

Triggers the task on a monthly day-of-week schedule. For example, the task starts on a specific days of the week, weeks of the month, and months of the year.

### `IDLE`

- **Number**: `7`

Triggers the task when the computer goes into an idle state.

### `REGISTRATION`

- **Number**: `8`

Triggers the task when the task is registered.

### `BOOT`

- **Number**: `9`

Triggers the task when the computer boots.

### `LOGON`

- **Number**: `10`

Triggers the task when a specific user logs on.

### `SESSION_STATE_CHANGE`

- **Number**: `11`

Triggers the task when a specific user session state changes.

### `CUSTOM_TRIGGER01`

- **Number**: `12`

Custom trigger 01.
