# ScheduledAnacronTask

Information about a scheduled anacron task.

## Fields

### `period`

- Type: `string` (singular)

Anacrontab period field. Value is an integer in days, or a string like "@daily", "@weekly", or "@monthly".

### `delay_minutes` / `delayMinutes`

- Type: `int64` (singular)

The delay in minutes before the job is run.

### `job_id` / `jobId`

- Type: `string` (singular)

The unique identifier of the job.

### `path`

- Type: `string` (singular)

The PATH environment variable defined in the anacrontab file.

### `source_line` / `sourceLine`

- Type: `string` (singular)

The original source line from the anacrontab file.
