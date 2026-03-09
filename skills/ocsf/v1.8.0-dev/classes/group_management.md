# Group Management (group_management)

Group Management events report management updates to a group, including updates to membership and permissions.

- **UID**: `6`
- **Category**: Identity & Access Management
- **Extends**: `iam`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Assign Privileges` - Assign privileges to a group.
- `2`: `Revoke Privileges` - Revoke privileges from a group.
- `3`: `Add User` - Add user to a group.
- `4`: `Remove User` - Remove user from a group.
- `5`: `Delete` - A group was deleted.
- `6`: `Create` - A group was created.
- `7`: `Add Subgroup` - Add subgroup to a group.
- `8`: `Remove Subgroup` - Remove subgroup from a group.

The normalized identifier of the activity that triggered the event.

### `group`

- **Type**: `group`
- **Requirement**: required
- **Group**: primary

Group that was the target of the event.

### `privileges`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

A list of privileges assigned to the group.

### `resource`

- **Type**: `resource_details`
- **Requirement**: recommended
- **Group**: primary

Resource that the privileges give access to.

### `subgroup`

- **Type**: `group`
- **Requirement**: recommended
- **Group**: primary

A subgroup that was added to or removed from the group.

### `user`

- **Type**: `user`
- **Requirement**: recommended
- **Group**: primary

A user that was added to or removed from the group.
