# Authentication

The Authentication extension captures details specific to authentication events. General guidelines for authentication events: * Details about the source of the authentication event (for example, client IP or hostname), should be captured in principal. The principal may be empty if we have no details about the source of the login. * Details about the target of the authentication event (for example, details about the machine that is being logged into or logged out of) should be captured in target. * Some authentication events may involve a third-party. For example, a user logs into a cloud service (for example, Chronicle) via their company's SSO (the event is logged by their SSO solution). In this case, the principal captures information about the user's device, the target captures details about the cloud service they logged into, and the intermediary captures details about the SSO solution.

- **Full name**: `google.backstory.Authentication`
- **Fields**: `4`
- **Nested enums**: `4`

## Nested enums

- [Authentication.AuthType](../enums/authentication_auth_type.md)
- [Authentication.Mechanism](../enums/authentication_mechanism.md)
- [Authentication.AuthenticationStatus](../enums/authentication_authentication_status.md)
- [Authentication.Outcome](../enums/authentication_outcome.md)

## Fields

### `type`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Authentication.AuthType`](../enums/authentication_auth_type.md)
- **JSON name**: `type`

The type of authentication.

### `mechanism`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: [`Authentication.Mechanism`](../enums/authentication_mechanism.md)
- **JSON name**: `mechanism`

The authentication mechanism.

### `auth_details`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `authDetails`

The vendor defined details of the authentication.

### `outcome`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Authentication.Outcome`](../enums/authentication_outcome.md)
- **JSON name**: `outcome`

The outcome of the authentication event.
