# USER_LOGOUT Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `USER_LOGIN`, `USER_LOGOUT`
- Usage-guide section: `USER_LOGIN, USER_LOGOUT`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- principal: For remote user activity (for example, remote login), populate principal with information about the machine originating the user activity. For local user activity (for example, local login), don't set principal.
- target: Populate target.user with information about the user that has logged on or logged off. If principal is not set (for example, local login), target must also include at least one machine identifier identifying the target machine. For machine to machine user activity (for example, remote login, SSO, Cloud Service, VPN), target must include information on either the target application, target machine, or target VPN server.
- intermediary: For SSO logins, intermediary must include at least one machine identifier for the SSO server if available.
- network and network.http: If the login occurs over HTTP, you must place all available details in network.ip_protocol, network.application_protocol, and network.http.
- authentication extension: Must identify the type of authentication system that the event is related to (for example, machine, SSO, or VPN) and the mechanism employed (username and password, OTP, etc.).
- security_result: Add a security_result field to represent the login status if it fails. Specify security_result.category with the AUTH_VIOLATION value if authentication fails.

## Optional Fields

No entries extracted.

## Notes

No entries extracted.
