# Account Change (account_change)

Account Change events report when specific user account management tasks are performed, such as a user/role being created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.

- **Class UID**: `3001`
- **Category**: Identity & Access Management
- **Extends**: [Identity & Access Management (iam)](iam.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Identity & Access Management:**
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
- `1`: `Create` - A user/role was created.
- `2`: `Enable` - A user/role was enabled.
- `3`: `Password Change` - An attempt was made to change an account's password.
- `4`: `Password Reset` - An attempt was made to reset an account's password.
- `5`: `Disable` - A user/role was disabled.
- `6`: `Delete` - A user/role was deleted.
- `7`: `Attach Policy` - An IAM Policy was attached to a user/role.
- `8`: `Detach Policy` - An IAM Policy was detached from a user/role.
- `9`: `Lock` - A user account was locked out.
- `10`: `MFA Factor Enable` - An authentication factor was enabled for an account.
- `11`: `MFA Factor Disable` - An authentication factor was disabled for an account.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: recommended
- **Group**: context

The actor object describes details about the user/role/process that was the source of the activity.

### `policy`

- **Type**: [`policy`](../objects/policy.md)
- **Requirement**: optional
- **Group**: context

Details about the IAM policy associated to the Attach/Detach Policy activities.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: required
- **Group**: primary

The user that was a target of an activity.

### `user_result`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: recommended
- **Group**: primary

The result of the user account change. It should contain the new values of the changed attributes.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `3001`: `Account Change` - Account Change events report when specific user account management tasks are performed, such as a user/role being created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
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
- `300107`: `Account Change: Attach Policy` - An IAM Policy was attached to a user/role.
- `300108`: `Account Change: Detach Policy` - An IAM Policy was detached from a user/role.
- `300109`: `Account Change: Lock` - A user account was locked out.
- `300110`: `Account Change: MFA Factor Enable` - An authentication factor was enabled for an account.
- `300111`: `Account Change: MFA Factor Disable` - An authentication factor was disabled for an account.
- `300199`: `Account Change: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
