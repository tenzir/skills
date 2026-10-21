# Authorize Session (authorize_session)

Authorize Session events report privileges or groups assigned to a new user session, usually at login time.

- **Class UID**: `3003`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Constraints

- **Exactly one of**: `privileges`, `group`

## Associations

- `session` ↔ `user`
- `user` ↔ `session`

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
- `1`: `Assign Privileges` - Assign special privileges to a new logon.
- `2`: `Assign Groups` - Assign special groups to a new logon.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: optional
- **Group**: context

The Endpoint for which the user session was targeted.

### `group`

- **Type**: [`group`](../objects/group.md)
- **Requirement**: recommended
- **Group**: primary

Group that was assigned to the new user session.

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

- `3003`: `Authorize Session` - Authorize Session events report privileges or groups assigned to a new user session, usually at login time.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `300300`: `Authorize Session: Unknown`
- `300301`: `Authorize Session: Assign Privileges` - Assign special privileges to a new logon.
- `300302`: `Authorize Session: Assign Groups` - Assign special groups to a new logon.
- `300399`: `Authorize Session: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
