# Script Activity (script_activity)

Script Activity events report when a process executes a script.

- **Class UID**: `1009`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: `cloud`, `datetime`, `host`, `osint`, `security_control`

## Associations

- `actor.user` ↔ `device`
- `device` ↔ `actor.user`

## Inherited attributes

**From System Activity:**
- `actor` (required)
- `device` (required)

**From Base Event:**
- `category_uid` (required)
- `class_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `type_uid` (required)
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
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Execute`

The normalized identifier of the activity that triggered the event.

### `script`

- **Type**: [`script`](../objects/script.md)
- **Requirement**: required
- **Group**: primary

The script that was the target of the activity.
