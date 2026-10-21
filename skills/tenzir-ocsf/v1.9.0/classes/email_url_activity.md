# Email URL Activity (email_url_activity)

Email URL Activity events report URLs within an email.

> **Deprecated since v1.3.0.** Use the `email_activity` class with the `email.urls[]` array instead.

- **Class UID**: `4012`
- **Category**: Network Activity
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

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
- `1`: `Send`
- `2`: `Receive`
- `3`: `Scan` - Email URL being scanned (example: security scanning).
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `email_uid`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

> **Deprecated since v1.4.0.** Use the `email.uid` attribute instead.

The unique identifier of the email, used to correlate related email alert and activity events.

### `url`

- **Type**: [`url`](../objects/url.md)
- **Requirement**: required
- **Group**: primary

The URL included in the email content.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4012`: `Email URL Activity` - Email URL Activity events report URLs within an email.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `401200`: `Email URL Activity: Unknown`
- `401201`: `Email URL Activity: Send`
- `401202`: `Email URL Activity: Receive`
- `401203`: `Email URL Activity: Scan` - Email URL being scanned (example: security scanning).
- `401299`: `Email URL Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
