# Registry Key Activity (registry_key_activity)

Registry Key Activity events report when a process performs an action on a Windows registry key.

- **Class UID**: `201001`
- **Category**: System Activity
- **Extends**: [System Activity (system)](../../../classes/system.md)
- **Profiles**: [Host](../../../profiles/host.md), [Security Control](../../../profiles/security_control.md), [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md)

## Associations

- `device` ↔ `actor.user`
- `actor.user` ↔ `device`

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

### `access_mask`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The access mask in a platform-native format.

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Create`
- `2`: `Read`
- `3`: `Modify`
- `4`: `Delete`
- `5`: `Rename`
- `6`: `Set Security`
- `7`: `Restore`
- `8`: `Import`
- `9`: `Export`
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../../../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the `reg_key` object.

### `create_mask`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The original Windows mask that is required to create the object.

### `open_mask`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

The Windows options needed to open a registry key.

### `reg_key`

- **Type**: `win/reg_key`
- **Requirement**: required
- **Group**: primary

The registry key.

### `prev_reg_key`

- **Type**: `win/reg_key`
- **Requirement**: recommended
- **Group**: primary

The registry key before the mutation

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `201001`: `Registry Key Activity` - Registry Key Activity events report when a process performs an action on a Windows registry key.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20100100`: `Registry Key Activity: Unknown`
- `20100101`: `Registry Key Activity: Create`
- `20100102`: `Registry Key Activity: Read`
- `20100103`: `Registry Key Activity: Modify`
- `20100104`: `Registry Key Activity: Delete`
- `20100105`: `Registry Key Activity: Rename`
- `20100106`: `Registry Key Activity: Set Security`
- `20100107`: `Registry Key Activity: Restore`
- `20100108`: `Registry Key Activity: Import`
- `20100109`: `Registry Key Activity: Export`
- `20100199`: `Registry Key Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
