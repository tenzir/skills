# ASimActor

- **Source**: [`ASIM/schemas/entities/ASimActor.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/entities/ASimActor.yaml)
- **Fields**: `11`

## Included by

- [AuditEvent](../schemas/audit_event.md)
- [Authentication](../schemas/authentication.md)
- [FileEvent](../schemas/file_event.md)
- [Notification](../schemas/notification.md)
- [ProcessEvent](../schemas/process_event.md)
- [RegistryEvent](../schemas/registry_event.md)
- [User Management](../schemas/user_management.md)

## Raw fields

### `ActorOriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

TBD

### `ActorScope`

- **Class**: `Optional`
- **Type**: `string`

The scope, such as Azure AD tenant, in which ActorUserId and ActorUsername are defined.

### `ActorScopeId`

- **Class**: `Optional`
- **Type**: `string`

The scope ID, such as Azure AD tenant ID, in which ActorUserId and ActorUsername are defined.

### `ActorSessionId`

- **Class**: `Optional`
- **Type**: `string`

The unique ID of the sign-in session of the Actor.

#### Examples

- `102pTUgC3p8RIqHvzxLCHnFlg`

### `ActorUserAadId`

- **Class**: `Optional`
- **Type**: `string`

The Azure Active Directory ID of the actor.

### `ActorUserId`

- **Class**: `Optional`
- **Type**: `string`

A machine-readable, alphanumeric, unique representation of the actor.

#### Examples

- `S-1-12-1-4141952679-1282074057-627758481-2916039507`

### `ActorUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations.md#useridtype)
- **Follows**: [`ActorUserId`](../fields/actor_user_id.md)

### `ActorUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

The Actor's username, including domain information when available.

### `ActorUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations.md#usernametype)
- **Follows**: [`ActorUsername`](../fields/actor_username.md)

### `ActorUserSid`

- **Class**: `Optional`
- **Type**: `string`

The Windows user ID (SIDs) of the actor.

### `ActorUserType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserType](../enumerations.md#usertype)
