# ScheduledAnacronTask

Information about a scheduled anacron task.

- **Full name**: `google.backstory.ScheduledAnacronTask`
- **Fields**: `5`

## Fields

### `period`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `period`

Anacrontab period field. Value is an integer in days, or a string like "@daily", "@weekly", or "@monthly".

### `delay_minutes`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `delayMinutes`

The delay in minutes before the job is run.

### `job_id`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `jobId`

The unique identifier of the job.

### `path`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `path`

The PATH environment variable defined in the anacrontab file.

### `source_line`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sourceLine`

The original source line from the anacrontab file.
