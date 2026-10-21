# Windows Service Activity (win_service_activity)

Windows Service Activity events report when a process interacts with the Service Control Manager.

- **Class UID**: `201004`
- **Category**: System Activity
- **Extends**: [System Activity (system)](../../../classes/system.md)
- **Profiles**: [Host](../../../profiles/host.md), [Security Control](../../../profiles/security_control.md), [Cloud](../../../profiles/cloud.md), [Date/Time](../../../profiles/datetime.md), [OSINT](../../../profiles/osint.md)

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
- `1`: `Create` - A service is created, for example by calling `CreateService`. Refer to the `win_service` attribute for details.
- `2`: `Reconfigure` - A service is reconfigured, for example by calling `ChangeServiceConfig` or `ChangeServiceConfig2`. Refer to the `win_service` attribute for details.
- `3`: `Start` - A stopped service is started, for example by calling `StartService`. Refer to the `service` attribute for details.
- `4`: `Stop` - A running or paused service is stopped, for example by calling `ControlService` or `ControlServiceEx`. Refer to the `win_service` attribute for details.
- `5`: `Pause` - A running service is paused, for example by calling `ControlService` or `ControlServiceEx`. Refer to the `win_service` attribute for details.
- `6`: `Continue` - A paused service is continued, for example by calling `ControlService` or `ControlServiceEx`. Refer to the `win_service` attribute for details.
- `7`: `Delete` - A service is deleted, for example by calling `DeleteService`. Refer to the `win_service` attribute for details.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `win_service`

- **Type**: `win/win_service`
- **Requirement**: required

The Windows service.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `201004`: `Windows Service Activity` - Windows Service Activity events report when a process interacts with the Service Control Manager.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `20100400`: `Windows Service Activity: Unknown`
- `20100401`: `Windows Service Activity: Create` - A service is created, for example by calling `CreateService`. Refer to the `win_service` attribute for details.
- `20100402`: `Windows Service Activity: Reconfigure` - A service is reconfigured, for example by calling `ChangeServiceConfig` or `ChangeServiceConfig2`. Refer to the `win_service` attribute for details.
- `20100403`: `Windows Service Activity: Start` - A stopped service is started, for example by calling `StartService`. Refer to the `service` attribute for details.
- `20100404`: `Windows Service Activity: Stop` - A running or paused service is stopped, for example by calling `ControlService` or `ControlServiceEx`. Refer to the `win_service` attribute for details.
- `20100405`: `Windows Service Activity: Pause` - A running service is paused, for example by calling `ControlService` or `ControlServiceEx`. Refer to the `win_service` attribute for details.
- `20100406`: `Windows Service Activity: Continue` - A paused service is continued, for example by calling `ControlService` or `ControlServiceEx`. Refer to the `win_service` attribute for details.
- `20100407`: `Windows Service Activity: Delete` - A service is deleted, for example by calling `DeleteService`. Refer to the `win_service` attribute for details.
- `20100499`: `Windows Service Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
