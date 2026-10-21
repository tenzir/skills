# Windows Resource Activity (resource_activity)

Windows Resource Activity events report when a process accesses a Windows managed resource object, successful or otherwise.

- **Class UID**: `201003`
- **Category**: System Activity
- **Extends**: [System Activity (system)](../../../classes/system.md)
- **Profiles**: [Host](../../../profiles/host.md), [Security Control](../../../profiles/security_control.md), [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md)

## Associations

- `device` ↔ `actor.user`
- `actor.user` ↔ `device`

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
- `1`: `Access`
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `win_resource`

- **Type**: `win/win_resource`
- **Requirement**: required
- **Group**: primary

The Windows resource object that was accessed, such as a mutant or timer.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `201003`: `Windows Resource Activity` - Windows Resource Activity events report when a process accesses a Windows managed resource object, successful or otherwise.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20100300`: `Windows Resource Activity: Unknown`
- `20100301`: `Windows Resource Activity: Access`
- `20100399`: `Windows Resource Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
