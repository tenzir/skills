# Email URL Activity (email_url_activity)

Email URL Activity events report URLs within an email.

- **UID**: `12`
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
- `3`: `Scan` - Email URL being scanned (example: security scanning).

The normalized identifier of the activity that triggered the event.

### `email_uid`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

The unique identifier of the email, used to correlate related email alert and activity events.

### `url`

- **Type**: `url`
- **Requirement**: required
- **Group**: primary

The URL included in the email content.
