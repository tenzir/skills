# Kernel Extension Activity (kernel_extension)

Kernel Extension events report when a driver/extension is loaded or unloaded into the kernel

- **UID**: `2`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `99`: `Other` - The event activity is not mapped.
- `0`: `Unknown` - The event activity is unknown.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: required

The actor process that loaded or unloaded the driver/extension.

### `driver`

- **Type**: `kernel_driver`
- **Requirement**: required
- **Group**: primary

The driver that was loaded/unloaded into the kernel
