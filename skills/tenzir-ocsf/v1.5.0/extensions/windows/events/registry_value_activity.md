# Registry Value Activity (registry_value_activity)

Registry Value Activity events reports when a process performs an action on a Windows registry value.

- **Class UID**: `201002`
- **Category**: System Activity
- **Extends**: [System Activity (system)](../../../classes/system.md)
- **Profiles**: [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md), [Host](../../../profiles/host.md), [OSINT](../../../profiles/osint.md), [Security Control](../../../profiles/security_control.md)

## Associations

- `actor.user` ↔ `device`
- `device` ↔ `actor.user`

## Inherited attributes

**From System Activity:**
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
- `1`: `Get`
- `2`: `Set`
- `3`: `Modify`
- `4`: `Delete`
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../../../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the `reg_value` object.

### `prev_reg_value`

- **Type**: `win/reg_value`
- **Requirement**: optional

The registry value before the mutation

### `reg_value`

- **Type**: `win/reg_value`
- **Requirement**: required

The registry value.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `201002`: `Registry Value Activity` - Registry Value Activity events reports when a process performs an action on a Windows registry value.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20100200`: `Registry Value Activity: Unknown`
- `20100201`: `Registry Value Activity: Get`
- `20100202`: `Registry Value Activity: Set`
- `20100203`: `Registry Value Activity: Modify`
- `20100204`: `Registry Value Activity: Delete`
- `20100299`: `Registry Value Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
