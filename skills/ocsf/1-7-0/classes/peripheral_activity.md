# Peripheral Activity (peripheral_activity)

Peripheral Activity events log a system's interactions with external, connectable, and detachable hardware. These events provide visibility into the external devices connected to and used by a system.

- **UID**: `10`
- **Category**: System Activity
- **Extends**: `system`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Connect` - A peripheral device was connected to the system.
- `2`: `Disconnect` - A peripheral device was disconnected from the system.
- `3`: `Enable` - A peripheral device was enabled on the system.
- `4`: `Disable` - A peripheral device was disabled on the system.
- `5`: `Eject` - A peripheral device was ejected from the system. This is typically used for removable media devices. Note: For `Mount` and `Unmount` events, see the File System Activity event class.

The normalized identifier of the activity that triggered the event.

### `peripheral_device`

- **Type**: `peripheral_device`
- **Requirement**: required
- **Group**: primary

The peripheral device that is the subject of the activity.
