# Module Activity (module)

Module  Activity events report when a process loads or unloads the `module`.

- **UID**: `5`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: required

The actor that loaded or unloaded the `module`.

### `module`

- **Type**: `module`
- **Requirement**: required
- **Group**: primary

The module that was loaded or unloaded.
