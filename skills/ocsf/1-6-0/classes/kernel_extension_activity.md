# Kernel Extension Activity (kernel_extension_activity)

Kernel Extension events report when a driver/extension is loaded or unloaded into the kernel

- **UID**: `2`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Load` - A driver/extension was loaded into the kernel
- `2`: `Unload` - A driver/extension was unloaded (removed) from the kernel

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
