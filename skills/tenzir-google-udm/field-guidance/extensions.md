# Extensions Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Extensions](../messages/extensions.md)

## Fields

### `Extensions.auth`

- **Purpose**: Extension to the authentication metadata.
- **Encoding**: String.
- **Examples**: Sandbox metadata (all behaviors exhibited by a file, for example, FireEye). Network Access Control (NAC) data. LDAP details about a user (for example, role, organization, etc.).

#### Examples

- Sandbox metadata (all behaviors exhibited by a file, for example, FireEye).
- Network Access Control (NAC) data.
- LDAP details about a user (for example, role, organization, etc.).

### `Extensions.auth.auth_details`

- **Purpose**: Specify the vendor specific details for the authentication type or mechanism. Authentication providers often define types such as via_mfa or via_ad that provide useful information on the authentication type. These types can still be generalized in auth.type or auth.mechanism for usability and cross dataset rule compatibility.
- **Encoding**: String.
- **Examples**: via_mfa, via_ad.

#### Examples

- via_mfa, via_ad.

### `Extensions.vulns`

- **Purpose**: Extension to the vulnerability metadata.
- **Encoding**: String.
- **Example**: Host vulnerability scan data.

#### Examples

- Host vulnerability scan data.
