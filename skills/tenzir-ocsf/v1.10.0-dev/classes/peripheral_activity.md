# Peripheral Activity (peripheral_activity)

Peripheral Activity events log a system's interactions with external, connectable, and detachable hardware. These events provide visibility into the external devices connected to and used by a system.

- **Class UID**: `1010`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Associations

- `actor.user` ↔ `device`
- `device` ↔ `actor.user`

## Inherited attributes

**From System Activity:**
- `actor` (required)
- `device` (required)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Connect` - A peripheral device was connected to the system.
- `2`: `Disconnect` - A peripheral device was disconnected from the system.
- `3`: `Enable` - A peripheral device was enabled on the system.
- `4`: `Disable` - A peripheral device was disabled on the system.
- `5`: `Eject` - A peripheral device was ejected from the system. This is typically used for removable media devices. Note: For `Mount` and `Unmount` events, see the [File System Activity](file_activity.md) event class.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `peripheral_device`

- **Type**: [`peripheral_device`](../objects/peripheral_device.md)
- **Requirement**: required
- **Group**: primary

The peripheral device that is the subject of the activity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1010`: `Peripheral Activity` - Peripheral Activity events log a system's interactions with external, connectable, and detachable hardware. These events provide visibility into the external devices connected to and used by a system.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `101000`: `Peripheral Activity: Unknown`
- `101001`: `Peripheral Activity: Connect` - A peripheral device was connected to the system.
- `101002`: `Peripheral Activity: Disconnect` - A peripheral device was disconnected from the system.
- `101003`: `Peripheral Activity: Enable` - A peripheral device was enabled on the system.
- `101004`: `Peripheral Activity: Disable` - A peripheral device was disabled on the system.
- `101005`: `Peripheral Activity: Eject` - A peripheral device was ejected from the system. This is typically used for removable media devices. Note: For `Mount` and `Unmount` events, see the [File System Activity](file_activity.md) event class.
- `101099`: `Peripheral Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
