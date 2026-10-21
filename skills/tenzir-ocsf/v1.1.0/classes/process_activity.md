# Process Activity (process_activity)

Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.

- **Class UID**: `1007`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

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
- `1`: `Launch`
- `2`: `Terminate`
- `3`: `Open`
- `4`: `Inject`
- `5`: `Set User ID`
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: required
- **Group**: primary

The actor that performed the activity on the target `process`. For example, the process that started a new process or injected code into another process.

### `actual_permissions`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary

The permissions that were granted to the in a platform-native format.

### `exit_code`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary

The exit code reported by a process when it terminates. The convention is that zero indicates success and any non-zero exit code indicates that some error occurred.

### `injection_type`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The process injection method, normalized to the caption of the injection_type_id value. In the case of 'Other', it is defined by the event source.

### `injection_type_id`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary
- **Sibling**: `injection_type`

#### Enum values

- `0`: `Unknown` - The injection type is unknown.
- `1`: `Remote Thread`
- `2`: `Load Library`
- `99`: `Other` - The injection type is not mapped. See the `injection_type` attribute, which contains a data source specific value.

The normalized identifier of the process injection method.

### `module`

- **Type**: [`module`](../objects/module.md)
- **Requirement**: optional
- **Group**: primary

The module that was injected by the actor process.

### `process`

- **Type**: [`process`](../objects/process.md)
- **Requirement**: required
- **Group**: primary

The process that was launched, injected into, opened, or terminated.

### `requested_permissions`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary

The permissions mask that were requested by the process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1007`: `Process Activity` - Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `100700`: `Process Activity: Unknown`
- `100701`: `Process Activity: Launch`
- `100702`: `Process Activity: Terminate`
- `100703`: `Process Activity: Open`
- `100704`: `Process Activity: Inject`
- `100705`: `Process Activity: Set User ID`
- `100799`: `Process Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
