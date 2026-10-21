# User Access Management (user_access)

User Access Management events report management updates to a user's privileges.

- **Class UID**: `3005`
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
- `1`: `Assign Privileges` - Assign privileges to a user.
- `2`: `Revoke Privileges` - Revoke privileges from a user.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `privileges`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

List of privileges assigned to a user.

### `resource`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: optional
- **Group**: primary

Resource that the privileges give access to.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: required
- **Group**: primary

User to which privileges were assigned.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3005`: `User Access Management` - User Access Management events report management updates to a user's privileges.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300500`: `User Access Management: Unknown`
- `300501`: `User Access Management: Assign Privileges` - Assign privileges to a user.
- `300502`: `User Access Management: Revoke Privileges` - Revoke privileges from a user.
- `300599`: `User Access Management: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
