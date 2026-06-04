# Authentication Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Authentication](../messages/authentication.md)

## Fields

### `Authentication.auth_details`

- **Purpose**: Vendor-defined authentication details.
- **Encoding**: String.

### `Authentication.Authentication_Status`

- **Purpose**: Describes the authentication status of a user or specific credential.
- **Encoding**: Enumerated type.
- **Possible values**: UNKNOWN_AUTHENTICATION_STATUS-Default authentication status ACTIVE-Authentication method is in an active state SUSPENDED-Authentication method is in a suspended or disabled state DELETED-Authentication method has been deleted NO_ACTIVE_CREDENTIALS-Authentication method has no active credentials.

### `Authentication.AuthType`

- **Purpose**: Type of system an authentication event is associated with (Google Security Operations UDM).
- **Encoding**: Enumerated type.
- **Possible values**: AUTHTYPE_UNSPECIFIED MACHINE-Machine authentication PHYSICAL-Physical authentication (for example, a badge reader) SSO TACACS-TACACS family protocol for authentication of networked systems (for example, TACACS or TACACS+) VPN

### `Authentication.Mechanism`

- **Purpose**: Mechanism(s) used for authentication.
- **Encoding**: Enumerated type.
- **Possible values**: MECHANISM_UNSPECIFIED-Default authentication mechanism. BADGE_READER BATCH-Batch authentication. CACHED_INTERACTIVE-Interactive authentication using cached credentials. HARDWARE_KEY LOCAL MECHANISM_OTHER-Some other mechanism that is not defined here. NETWORK-Network authentication. NETWORK_CLEAR_TEXT-Network clear text authentication. NEW_CREDENTIALS-Authentication with new credentials. OTP REMOTE-Remote authentication REMOTE_INTERACTIVE-RDP, terminal services, Virtual Network Computing (VNC), etc. SERVICE-Service authentication. UNLOCK-Direct human-interactive unlock authentication. USERNAME_PASSWORD
