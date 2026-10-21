# Scheduled Job Activity (scheduled_job_activity)

Scheduled Job Activity events report activities related to scheduled jobs or tasks.

- **Class UID**: `1006`
- **Category**: System Activity
- **Extends**: [System Activity (system)](system.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

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
- `1`: `Create`
- `2`: `Update`
- `3`: `Delete`
- `4`: `Enable`
- `5`: `Disable`
- `6`: `Start`
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

The actor that performed the activity on the `job` object.

### `job`

- **Type**: [`job`](../objects/job.md)
- **Requirement**: required
- **Group**: primary

The object provides information about a scheduled job or a task.

### `updated_job`

- **Type**: [`job`](../objects/job.md)
- **Requirement**: recommended
- **Group**: primary

The intended state of the `job` after the update. On `Success`, represents the actual post-update state.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `1006`: `Scheduled Job Activity` - Scheduled Job Activity events report activities related to scheduled jobs or tasks.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `100600`: `Scheduled Job Activity: Unknown`
- `100601`: `Scheduled Job Activity: Create`
- `100602`: `Scheduled Job Activity: Update`
- `100603`: `Scheduled Job Activity: Delete`
- `100604`: `Scheduled Job Activity: Enable`
- `100605`: `Scheduled Job Activity: Disable`
- `100606`: `Scheduled Job Activity: Start`
- `100699`: `Scheduled Job Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
