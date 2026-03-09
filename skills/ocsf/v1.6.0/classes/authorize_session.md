# Authorize Session (authorize_session)

Authorize Session events report privileges or groups assigned to a new user session, usually at login time.

- **UID**: `3`
- **Category**: Identity & Access Management
- **Extends**: `iam`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Assign Privileges` - Assign special privileges to a new logon.
- `2`: `Assign Groups` - Assign special groups to a new logon.

The normalized identifier of the activity that triggered the event.

### `dst_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: optional
- **Group**: context

The Endpoint for which the user session was targeted.

### `group`

- **Type**: `group`
- **Requirement**: recommended
- **Group**: primary

Group that was assigned to the new user session.

### `privileges`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The list of sensitive privileges, assigned to the new user session.

### `session`

- **Type**: `session`
- **Requirement**: recommended
- **Group**: primary

The user session with the assigned privileges.

### `user`

- **Type**: `user`
- **Requirement**: required
- **Group**: primary

The user to which new privileges were assigned.
