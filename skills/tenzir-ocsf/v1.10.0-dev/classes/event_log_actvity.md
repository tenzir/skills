# Event Log Activity (event_log_actvity)

Event Log Activity events report actions pertaining to the system's event logging service(s), such as disabling logging or clearing the log data.

- **Class UID**: `1008`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `file`, `log_name`, `log_provider`, `log_type`, `log_type_id`

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
- `1`: `Clear` - Clear the event log database, file, or cache.
- `2`: `Delete` - Delete the event log database, file, or cache.
- `3`: `Export` - Export the event log database, file, or cache.
- `4`: `Archive` - Archive the event log database, file, or cache.
- `5`: `Rotate` - Rotate the event log database, file, or cache.
- `6`: `Start` - Start the event logging service.
- `7`: `Stop` - Stop the event logging service.
- `8`: `Restart` - Restart the event logging service.
- `9`: `Enable` - Enable the event logging service.
- `10`: `Disable` - Disable the event logging service.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: recommended
- **Group**: primary

The actor that performed the activity.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: recommended
- **Group**: primary

The device that reported the event.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The

targeted

endpoint for the event log activity.

### `file`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: recommended
- **Group**: primary

The file

targeted by

the activity. Example: `/var/log/audit.log`

### `log_name`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The name of the event log

targeted by

the activity. Example: Windows `Security`.

### `log_provider`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The logging provider or logging service

targeted by

the activity.
Example: `Microsoft-Windows-Security-Auditing`, `Auditd`, or `Syslog`.

### `log_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The log type, normalized to the caption of the `log_type_id` value. In the case of 'Other', it is defined by the event source.

### `log_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `log_type`

#### Enum values

- `0`: `Unknown` - The log type is unknown.
- `1`: `OS` - The log type is an Operating System log.
- `2`: `Application` - The log type is an Application log.
- `99`: `Other` - The log type is not mapped. See the `log_type` attribute, which contains a data source specific value.

The normalized log type identifier.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The source endpoint for the event log activity.

### `status_code`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The event status code, as reported by the event source.
Example: `0`, `8`, or `21` for [Windows ClearEventLog](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/eventlogprov/cleareventlog-method-in-class-win32-nteventlogfile).

### `status_detail`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The status detail contains additional information about the event outcome.
Example: `Success`, `Privilege Missing`, or `Invalid Parameter` for [Windows ClearEventLog](https://learn.microsoft.com/en-us/previous-versions/windows/desktop/eventlogprov/cleareventlog-method-in-class-win32-nteventlogfile).

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1008`: `Event Log Activity` - Event Log Activity events report actions pertaining to the system's event logging service(s), such as disabling logging or clearing the log data.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `100800`: `Event Log Activity: Unknown`
- `100801`: `Event Log Activity: Clear` - Clear the event log database, file, or cache.
- `100802`: `Event Log Activity: Delete` - Delete the event log database, file, or cache.
- `100803`: `Event Log Activity: Export` - Export the event log database, file, or cache.
- `100804`: `Event Log Activity: Archive` - Archive the event log database, file, or cache.
- `100805`: `Event Log Activity: Rotate` - Rotate the event log database, file, or cache.
- `100806`: `Event Log Activity: Start` - Start the event logging service.
- `100807`: `Event Log Activity: Stop` - Stop the event logging service.
- `100808`: `Event Log Activity: Restart` - Restart the event logging service.
- `100809`: `Event Log Activity: Enable` - Enable the event logging service.
- `100810`: `Event Log Activity: Disable` - Disable the event logging service.
- `100899`: `Event Log Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
