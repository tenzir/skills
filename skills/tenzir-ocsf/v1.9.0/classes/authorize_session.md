# Authorize Session (authorize_session)

Authorize Session events report privileges, groups or roles assigned to a new user session, usually at login time.

- **Class UID**: `3003`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `privileges`, `groups`, `iam_roles`

## Associations

- `session` ↔ `user`
- `user` ↔ `session`

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
- `1`: `Assign Privileges` - Assign special privileges to a new logon.
- `2`: `Assign Groups` - Assign special groups to a new logon.
- `3`: `Assign Roles` - Assign special roles to a new logon.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: optional
- **Group**: context

The Endpoint for which the user session was targeted.

### `group`

- **Type**: [`group`](../objects/group.md)
- **Requirement**: recommended
- **Group**: primary

> **Deprecated since v1.9.0.** Use `groups` instead.

Group that was assigned to the new user session.

### `groups`

- **Type**: [`group`](../objects/group.md)
- **Requirement**: recommended
- **Group**: primary

The list of groups assigned to the new user session.

### `iam_roles`

- **Type**: [`iam_role`](../objects/iam_role.md)
- **Requirement**: recommended
- **Group**: primary

The list of roles assigned to the new user session.

### `privileges`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The list of sensitive privileges, assigned to the new user session.

### `session`

- **Type**: [`session`](../objects/session.md)
- **Requirement**: recommended
- **Group**: primary

The user session with the assigned privileges.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: required
- **Group**: primary

The user to which new privileges were assigned.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3003`: `Authorize Session` - Authorize Session events report privileges, groups or roles assigned to a new user session, usually at login time.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300300`: `Authorize Session: Unknown`
- `300301`: `Authorize Session: Assign Privileges` - Assign special privileges to a new logon.
- `300302`: `Authorize Session: Assign Groups` - Assign special groups to a new logon.
- `300303`: `Authorize Session: Assign Roles` - Assign special roles to a new logon.
- `300399`: `Authorize Session: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
