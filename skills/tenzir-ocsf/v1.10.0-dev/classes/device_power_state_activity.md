# Device Power State Activity (device_power_state_activity)

Device Power State Activity events report activities related to power state changes of a system.

- **Class UID**: `1011`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Associations

- `actor.user` ↔ `device`
- `device` ↔ `actor.user`

## Inherited attributes

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
- `1`: `Power On` - A power-on activity was reported for the system.
- `2`: `Power Off` - A power-off activity was reported for the system, including graceful shutdowns and hard power-off events. For graceful or software-initiated shutdowns, the `actor` may be specified when known.
- `3`: `Sleep` - A sleep activity was reported for the system.
- `4`: `Hibernate` - A hibernate activity was reported for the system.
- `5`: `Reboot` - A reboot activity was reported for the system.
- `6`: `Wake` - A wake activity was reported for the system.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

The actor that performed the activity on the `device` object.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

The host or device that changed power state.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1011`: `Device Power State Activity` - Device Power State Activity events report activities related to power state changes of a system.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `101100`: `Device Power State Activity: Unknown`
- `101101`: `Device Power State Activity: Power On` - A power-on activity was reported for the system.
- `101102`: `Device Power State Activity: Power Off` - A power-off activity was reported for the system, including graceful shutdowns and hard power-off events. For graceful or software-initiated shutdowns, the `actor` may be specified when known.
- `101103`: `Device Power State Activity: Sleep` - A sleep activity was reported for the system.
- `101104`: `Device Power State Activity: Hibernate` - A hibernate activity was reported for the system.
- `101105`: `Device Power State Activity: Reboot` - A reboot activity was reported for the system.
- `101106`: `Device Power State Activity: Wake` - A wake activity was reported for the system.
- `101199`: `Device Power State Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
