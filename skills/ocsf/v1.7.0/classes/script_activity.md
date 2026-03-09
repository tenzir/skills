# Script Activity (script_activity)

Script Activity events report when a process executes a script.

- **UID**: `9`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Execute`

The normalized identifier of the activity that triggered the event.

### `script`

- **Type**: `script`
- **Requirement**: required
- **Group**: primary

The script that was the target of the activity.
