# Actor (actor)

The Actor object contains details about the user, role, application, service, or process that initiated or performed a specific activity. Note that Actor is not the threat actor of a campaign but may be part of a campaign.

- **Extends**: `object`

## Attributes

### `app_name`

- **Type**: `string_t`
- **Requirement**: optional

The client application or service that initiated the activity. This can be in conjunction with the `user` if present. Note that `app_name` is distinct from the `process` if present.

### `app_uid`

- **Type**: `string_t`
- **Requirement**: optional

The unique identifier of the client application or service that initiated the activity. This can be in conjunction with the `user` if present. Note that `app_name` is distinct from the `process.pid` or `process.uid` if present.

### `authorizations`

- **Type**: `authorization`
- **Requirement**: optional

Provides details about an authorization, such as authorization outcome, and any associated policies related to the activity/event.

### `idp`

- **Type**: `idp`
- **Requirement**: optional

This object describes details about the Identity Provider used.

### `invoked_by`

- **Type**: `string_t`
- **Requirement**: optional

The name of the service that invoked the activity as described in the event.

### `process`

- **Type**: `process`
- **Requirement**: recommended

The process that initiated the activity.

### `session`

- **Type**: `session`
- **Requirement**: optional

The user session from which the activity was initiated.

### `user`

- **Type**: `user`
- **Requirement**: recommended

The user that initiated the activity or the user context from which the activity was initiated.
