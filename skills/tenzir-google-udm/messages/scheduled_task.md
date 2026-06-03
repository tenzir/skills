# ScheduledTask

Deprecated: use WindowsScheduledTask for Windows scheduled tasks or ScheduledCronTask for cron jobs. Information about a scheduled task.

- **Full name**: `google.backstory.ScheduledTask`
- **Fields**: `7`

## Fields

### `minute`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `minute`

The minute of the hour (0-59).

### `hour`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `hour`

The hour of the day (0-23).

### `month_day`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `monthDay`

The day of the month (1-31).

### `month`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `month`

The month of the year (1-12).

### `week_day`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `int32`
- **JSON name**: `weekDay`

The day of the week (0-6, Sunday=0).

### `comment`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `comment`

A comment or description for the task.

### `author`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `author`

The account name that authored or last modified the scheduled task.
