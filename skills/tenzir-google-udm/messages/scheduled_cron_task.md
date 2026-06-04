# ScheduledCronTask

Information about a scheduled cron task.

## Fields

### `minute`

- Type: `string` (singular)

Crontab minute field. Value is an integer between 0 and 59 and can also be a range or list of values (e.g., "0-59", "0-59/5", "0,15,30,45") and it // can also be an asterisk (*) to indicate first-last minutes. More on crontab format can be found here: https://www.linux.org/docs/man5/crontab.html

### `hour`

- Type: `string` (singular)

Crontab hour field. Value is an integer between 0 and 23, a range or list of values (e.g., "0-6", "*/2", "1,2"), or an asterisk (*) to indicate first-last hours.

### `month_day` / `monthDay`

- Type: `string` (singular)

Crontab day of month field. Value is an integer between 1 and 31, a range or list of values (e.g., "1-7", "1-31/7", "1,15"), or an asterisk (*) to indicate first-last days of month.

### `month`

- Type: `string` (singular)

Crontab month field. Value is an integer between 1 and 12 or a 3-letter name (e.g., "Jan"), a range or list of values (e.g., "1-3", "*/2", "1,6"), or an asterisk (*) to indicate first-last months.

### `week_day` / `weekDay`

- Type: `string` (singular)

Crontab day of week field. Value is an integer between 0 and 7 (0 or 7 is Sunday) or a 3-letter name (e.g., "Fri"), a range or list of values (e.g., "1-5", "0,6"), or an asterisk (*) to indicate first-last days of week.

### `comment`

- Type: `string` (singular)

A comment or description for the task.

### `author`

- Type: `string` (singular)

The author or creator of the task.

### `event`

- Type: `string` (singular)

Crontab special string or event (e.g., "@reboot", "@daily").

### `path`

- Type: `string` (singular)

The PATH environment variable defined in the crontab file.
