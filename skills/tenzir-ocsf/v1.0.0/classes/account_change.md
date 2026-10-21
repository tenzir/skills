# Account Change (account_change)

Account Change events report when specific user account management tasks are performed, such as a user/role being created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.

- **Class UID**: `3001`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

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
- `1`: `Create` - A user/role was created.
- `2`: `Enable` - A user/role was enabled.
- `3`: `Password Change` - An attempt was made to change an account's password.
- `4`: `Password Reset` - An attempt was made to reset an account's password.
- `5`: `Disable` - A user/role was disabled.
- `6`: `Delete` - A user/role was deleted.
- `7`: `Attach Policy` - A user/role was changed.
- `8`: `Detach Policy` - A user/role was changed.
- `9`: `Lock` - A user account was locked out.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: recommended
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity.

### `http_request`

- **Type**: [`http_request`](../objects/http_request.md)
- **Requirement**: optional
- **Group**: context

Details about the underlying http request.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

Details about the source of the activity.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: required
- **Group**: primary

The user that was a target of an activity.

### `user_result`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: optional
- **Group**: primary

The result of the user account change. It should contain the new values of the changed attributes.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3001`: `Account Change` - Account Change events report when specific user account management tasks are performed, such as a user/role being created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300100`: `Account Change: Unknown`
- `300101`: `Account Change: Create` - A user/role was created.
- `300102`: `Account Change: Enable` - A user/role was enabled.
- `300103`: `Account Change: Password Change` - An attempt was made to change an account's password.
- `300104`: `Account Change: Password Reset` - An attempt was made to reset an account's password.
- `300105`: `Account Change: Disable` - A user/role was disabled.
- `300106`: `Account Change: Delete` - A user/role was deleted.
- `300107`: `Account Change: Attach Policy` - A user/role was changed.
- `300108`: `Account Change: Detach Policy` - A user/role was changed.
- `300109`: `Account Change: Lock` - A user account was locked out.
- `300199`: `Account Change: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
