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

## Guidance

Population guidance from the Google UDM usage guide.

### `Authentication.auth_details`

- **Purpose**: Vendor-defined authentication details.
- **Encoding**: String.

### `Authentication.Authentication_Status`

- **Purpose**: Describes the authentication status of a user or specific credential.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_AUTHENTICATION_STATUS`: Default authentication status
  - `ACTIVE`: Authentication method is in an active state
  - `SUSPENDED`: Authentication method is in a suspended or disabled state
  - `DELETED`: Authentication method has been deleted
  - `NO_ACTIVE_CREDENTIALS`: Authentication method has no active credentials.

### `Authentication.AuthType`

- **Purpose**: Type of system an authentication event is associated with (Google Security Operations UDM).
- **Encoding**: Enumerated type.
- **Possible values**:
  - `AUTHTYPE_UNSPECIFIED`
  - `MACHINE`: Machine authentication
  - `PHYSICAL`: Physical authentication (for example, a badge reader)
  - `SSO`
  - `TACACS`: TACACS family protocol for authentication of networked systems (for example, TACACS or TACACS+)
  - `VPN`

### `Authentication.Mechanism`

- **Purpose**: Mechanism(s) used for authentication.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `MECHANISM_UNSPECIFIED`: Default authentication mechanism.
  - `BADGE_READER`
  - `BATCH`: Batch authentication.
  - `CACHED_INTERACTIVE`: Interactive authentication using cached credentials.
  - `HARDWARE_KEY`
  - `LOCAL`
  - `MECHANISM_OTHER`: Some other mechanism that is not defined here.
  - `NETWORK`: Network authentication.
  - `NETWORK_CLEAR_TEXT`: Network clear text authentication.
  - `NEW_CREDENTIALS`: Authentication with new credentials.
  - `OTP`
  - `REMOTE`: Remote authentication
  - `REMOTE_INTERACTIVE`: RDP, terminal services, Virtual Network Computing (VNC), etc.
  - `SERVICE`: Service authentication.
  - `UNLOCK`: Direct human-interactive unlock authentication.
  - `USERNAME_PASSWORD`
