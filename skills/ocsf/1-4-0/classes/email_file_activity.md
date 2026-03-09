# Email File Activity (email_file_activity)

Email File Activity events report files within emails.

- **UID**: `11`
- **Category**: Network Activity
- **Extends**: `base_event`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Send`
- `2`: `Receive`
- `3`: `Scan` - Email file being scanned (example: security scanning).

The normalized identifier of the activity that triggered the event.

### `email_uid`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

The unique identifier of the email, used to correlate related email alert and activity events.

### `file`

- **Type**: `file`
- **Requirement**: required
- **Group**: primary

The email file attachment.
