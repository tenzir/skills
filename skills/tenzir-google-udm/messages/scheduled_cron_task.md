# ScheduledCronTask

Information about a scheduled cron task.

- **Full name**: `google.backstory.ScheduledCronTask`
- **Fields**: `9`

## Fields

### `minute`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `minute`

Crontab minute field. Value is an integer between 0 and 59 and can also be a range or list of values (e.g., "0-59", "0-59/5", "0,15,30,45") and it // can also be an asterisk (*) to indicate first-last minutes. More on crontab format can be found here: https://www.linux.org/docs/man5/crontab.html

### `hour`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `hour`

Crontab hour field. Value is an integer between 0 and 23, a range or list of values (e.g., "0-6", "*/2", "1,2"), or an asterisk (*) to indicate first-last hours.

### `month_day`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `monthDay`

Crontab day of month field. Value is an integer between 1 and 31, a range or list of values (e.g., "1-7", "1-31/7", "1,15"), or an asterisk (*) to indicate first-last days of month.

### `month`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `month`

Crontab month field. Value is an integer between 1 and 12 or a 3-letter name (e.g., "Jan"), a range or list of values (e.g., "1-3", "*/2", "1,6"), or an asterisk (*) to indicate first-last months.

### `week_day`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `weekDay`

Crontab day of week field. Value is an integer between 0 and 7 (0 or 7 is Sunday) or a 3-letter name (e.g., "Fri"), a range or list of values (e.g., "1-5", "0,6"), or an asterisk (*) to indicate first-last days of week.

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

The author or creator of the task.

### `event`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `event`

Crontab special string or event (e.g., "@reboot", "@daily").

### `path`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `path`

The PATH environment variable defined in the crontab file.
