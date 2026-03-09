# User Access Management (user_access)

User Access Management events report management updates to a user's privileges.

- **UID**: `5`
- **Category**: Identity & Access Management
- **Extends**: `iam`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Assign Privileges` - Assign privileges to a user.
- `2`: `Revoke Privileges` - Revoke privileges from a user.

The normalized identifier of the activity that triggered the event.

### `privileges`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

List of privileges assigned to a user.

### `resource`

- **Type**: `resource_details`
- **Requirement**: optional
- **Group**: primary

Resource that the privileges give access to.

### `user`

- **Type**: `user`
- **Requirement**: required
- **Group**: primary

User to which privileges were assigned.
