# User Access Management (user_access)

User Access Management events report management updates to a user's privileges.

> **Deprecated since v1.9.0.** Use the `user_management` class instead.

- **Class UID**: `3005`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

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
- `1`: `Assign Privileges` - Assign privileges to a user.
- `2`: `Revoke Privileges` - Revoke privileges from a user.
- `3`: `Assign Role` - Assign a role to a user.
- `4`: `Remove Role` - Remove a role from a user.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `iam_role`

- **Type**: [`iam_role`](../objects/iam_role.md)
- **Requirement**: recommended
- **Group**: primary

The role assigned to or removed from a user.

### `privileges`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

List of privileges assigned to a user.

### `resource`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

> **Deprecated since v1.5.0.** Use the `resources` attribute instead.

Resource that the privileges give access to.

### `resources`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

Resources that the privileges give access to.

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

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300500`: `User Access Management: Unknown`
- `300501`: `User Access Management: Assign Privileges` - Assign privileges to a user.
- `300502`: `User Access Management: Revoke Privileges` - Revoke privileges from a user.
- `300503`: `User Access Management: Assign Role` - Assign a role to a user.
- `300504`: `User Access Management: Remove Role` - Remove a role from a user.
- `300599`: `User Access Management: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
