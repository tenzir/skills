# ASimUser

- **Source**: [`ASIM/schemas/entities/ASimUser.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimUser.yaml)
- **Fields**: `10`

## Included by

- [Authentication](../schemas/authentication.md) as `Target`
- [Dhcp](../schemas/dhcp.md) as `Src`
- [Dns](../schemas/dns.md) as `Src`
- [ProcessEvent](../schemas/process_event.md) as `Target`
- [User Management](../schemas/user_management.md) as `Target`

## Raw fields

### `<<Role>>OriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

TBD

### `<<Role>>UserId`

- **Class**: `Optional`
- **Type**: `string`

A machine-readable, alphanumeric, unique representation of the user.

#### Examples

- `S-1-12-1-4141952679-1282074057-627758481-2916039507`

### `<<Role>>UserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`<<Role>>UserId`](../fields/role_user_id.md)

### `<<Role>>Username`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

The user's username, including domain information when available.

### `<<Role>>UsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

### `<<Role>>UserScope`

- **Class**: `Optional`
- **Type**: `string`

The scope, such as Azure AD tenant, in which UserId and Username are defined.

### `<<Role>>UserScopeId`

- **Class**: `Optional`
- **Type**: `string`

The scope ID, such as Azure AD tenant ID, in which UserId and Username are defined.

### `<<Role>>UserSessionId`

- **Class**: `Optional`
- **Type**: `string`

The unique ID of the sign-in session of the user.

#### Examples

- `102pTUgC3p8RIqHvzxLCHnFlg`

### `<<Role>>UserType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserType](../enumerations/user_type.md)

### `<<Role>>UserUid`

- **Class**: `Optional`
- **Type**: `string`

The Unix or Linux user ID of the user.
