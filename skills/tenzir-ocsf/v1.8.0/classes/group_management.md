# Group Management (group_management)

Group Management events report management updates to a group, including updates to membership and permissions.

- **Class UID**: `3006`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Identity & Access Management:**
- `actor` (recommended)
- `src_endpoint` (recommended)

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
- `1`: `Assign Privileges` - Assign privileges to a group.
- `2`: `Revoke Privileges` - Revoke privileges from a group.
- `3`: `Add User` - Add user to a group.
- `4`: `Remove User` - Remove user from a group.
- `5`: `Delete` - A group was deleted.
- `6`: `Create` - A group was created.
- `7`: `Add Subgroup` - Add subgroup to a group.
- `8`: `Remove Subgroup` - Remove subgroup from a group.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `group`

- **Type**: [`group`](../objects/group.md)
- **Requirement**: required
- **Group**: primary

Group that was the target of the event.

### `privileges`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

A list of privileges assigned to the group.

### `resource`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

Resource that the privileges give access to.

### `subgroup`

- **Type**: [`group`](../objects/group.md)
- **Requirement**: recommended
- **Group**: primary

A subgroup that was added to or removed from the group.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: recommended
- **Group**: primary

A user that was added to or removed from the group.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3006`: `Group Management` - Group Management events report management updates to a group, including updates to membership and permissions.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300600`: `Group Management: Unknown`
- `300601`: `Group Management: Assign Privileges` - Assign privileges to a group.
- `300602`: `Group Management: Revoke Privileges` - Revoke privileges from a group.
- `300603`: `Group Management: Add User` - Add user to a group.
- `300604`: `Group Management: Remove User` - Remove user from a group.
- `300605`: `Group Management: Delete` - A group was deleted.
- `300606`: `Group Management: Create` - A group was created.
- `300607`: `Group Management: Add Subgroup` - Add subgroup to a group.
- `300608`: `Group Management: Remove Subgroup` - Remove subgroup from a group.
- `300699`: `Group Management: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
