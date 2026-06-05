# ScheduledTask

Deprecated: use WindowsScheduledTask for Windows scheduled tasks or ScheduledCronTask for cron jobs. Information about a scheduled task.

## Fields

### `minute`

- Type: `int32` (singular)

The minute of the hour (0-59).

### `hour`

- Type: `int32` (singular)

The hour of the day (0-23).

### `month_day` / `monthDay`

- Type: `int32` (singular)

The day of the month (1-31).

### `month`

- Type: `int32` (singular)

The month of the year (1-12).

### `week_day` / `weekDay`

- Type: `int32` (singular)

The day of the week (0-6, Sunday=0).

### `comment`

- Type: `string` (singular)

A comment or description for the task.

### `author`

- Type: `string` (singular)

The account name that authored or last modified the scheduled task.
