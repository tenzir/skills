# Scheduled Job Activity (scheduled_job)

Scheduled Job Activity events report activities related to scheduled jobs or tasks.

- **UID**: `6`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Create`
- `2`: `Update`
- `3`: `Delete`
- `4`: `Enable`
- `5`: `Disable`
- `6`: `Start`

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: optional
- **Group**: context

The actor that performed the activity on the `job` object.

### `job`

- **Type**: `job`
- **Requirement**: required
- **Group**: primary

The job object that pertains to the event.
