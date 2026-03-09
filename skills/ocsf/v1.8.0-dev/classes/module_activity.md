# Module Activity (module_activity)

Module Activity events report when an endpoint process acts on a `module`.

- **UID**: `5`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Load` - The target module was loaded.
- `2`: `Unload` - The target module was unloaded.
- `3`: `Invoke` - A function exported from the target module was invoked.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: required

The actor that performed the activity on the target `module`. For example, the process that loaded a module into memory.

### `module`

- **Type**: `module`
- **Requirement**: required
- **Group**: primary

The module that was loaded, unloaded, or invoked.
