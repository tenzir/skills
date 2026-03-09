# Account Change (account_change)

Account Change events report when specific user account management tasks are performed, such as a user/role being created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.

- **UID**: `1`
- **Category**: Identity & Access Management
- **Extends**: `iam`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Create` - A user/role was created.
- `2`: `Enable` - A user/role was enabled.
- `3`: `Password Change` - An attempt was made to change an account's password.
- `4`: `Password Reset` - An attempt was made to reset an account's password.
- `5`: `Disable` - A user/role was disabled.
- `6`: `Delete` - A user/role was deleted.
- `7`: `Attach Policy` - A user/role was changed.
- `8`: `Detach Policy` - A user/role was changed.
- `9`: `Lock` - A user account was locked out.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: `actor`
- **Requirement**: recommended
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity.

### `http_request`

- **Type**: `http_request`
- **Requirement**: optional
- **Group**: context

Details about the underlying http request.

### `src_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended
- **Group**: primary

Details about the source of the activity.

### `user`

- **Type**: `user`
- **Requirement**: required
- **Group**: primary

The user that was a target of an activity.

### `user_result`

- **Type**: `user`
- **Requirement**: optional
- **Group**: primary

The result of the user account change. It should contain the new values of the changed attributes.
