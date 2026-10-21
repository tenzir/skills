# Windows Service Activity (windows_service_activity)

Windows Service Activity events report when a process interacts with the Service Control Manager.

- **Class UID**: `201004`
- **Category**: System Activity
- **Extends**: [System Activity (system)](../../../classes/system.md)
- **Profiles**: [AI Operation](../../../profiles/ai_operation.md), [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md), [Host](../../../profiles/host.md), [OSINT](../../../profiles/osint.md), [Record Integrity](../../../profiles/record_integrity.md), [Security Control](../../../profiles/security_control.md)

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
- `1`: `Create` - A service is created, for example by calling the CreateService API.
- `2`: `Reconfigure` - A service is reconfigured, for example by calling the ChangeServiceConfig or ChangeServiceConfig2 API. Refer to `prev_win_service` and `win_service` attributes for details.
- `3`: `Start` - A stopped service is started, for example by calling the StartService API.
- `4`: `Stop` - A running or paused service is stopped, for example by calling the ControlService or ControlServiceEx API.
- `5`: `Pause` - A running service is paused, for example by calling the ControlService or ControlServiceEx API.
- `6`: `Continue` - A paused service is continued, for example by calling the ControlService or ControlServiceEx API.
- `7`: `Delete` - A service is deleted, for example by calling the DeleteService API.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use 0 (Unknown) when the activity cannot be determined. Use 99 (Other) when the activity does not match any defined value, in which case activity_name must be populated with the source-specific label.
Refer to the `win_service` attribute for details, unless any other attribute is mentioned.

### `prev_win_service`

- **Type**: `win/win_service`
- **Requirement**: recommended
- **Group**: primary

The Windows service before the mutation.

### `win_service`

- **Type**: `win/win_service`
- **Requirement**: required
- **Group**: primary

The current Windows service. On failed or unknown status of `Reconfigure` action may be populated with the intended state.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `201004`: `Windows Service Activity` - Windows Service Activity events report when a process interacts with the Service Control Manager.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20100400`: `Windows Service Activity: Unknown`
- `20100401`: `Windows Service Activity: Create` - A service is created, for example by calling the CreateService API.
- `20100402`: `Windows Service Activity: Reconfigure` - A service is reconfigured, for example by calling the ChangeServiceConfig or ChangeServiceConfig2 API. Refer to `prev_win_service` and `win_service` attributes for details.
- `20100403`: `Windows Service Activity: Start` - A stopped service is started, for example by calling the StartService API.
- `20100404`: `Windows Service Activity: Stop` - A running or paused service is stopped, for example by calling the ControlService or ControlServiceEx API.
- `20100405`: `Windows Service Activity: Pause` - A running service is paused, for example by calling the ControlService or ControlServiceEx API.
- `20100406`: `Windows Service Activity: Continue` - A paused service is continued, for example by calling the ControlService or ControlServiceEx API.
- `20100407`: `Windows Service Activity: Delete` - A service is deleted, for example by calling the DeleteService API.
- `20100499`: `Windows Service Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
