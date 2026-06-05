# Extensions

Extensions to a UDM event.

## Fields

### `auth`

- Type: [`Authentication`](authentication.md) (singular)

An authentication extension.

### `vulns`

- Type: [`Vulnerabilities`](vulnerabilities.md) (singular)

A vulnerability extension.

### `entity_risk` / `entityRisk`

- Type: [`EntityRisk`](entity_risk.md) (singular)

An entity risk change extension.

### `linux_utmp` / `linuxUtmp`

- Type: [`LinuxUtmp`](linux_utmp.md) (singular)

A Linux Utmp extension. This captures details specific to Linux Utmp events, which record login and logout sessions on a Linux system.

### `windows_event_log` / `windowsEventLog`

- Type: [`WindowsEventLog`](windows_event_log.md) (singular)

A Windows Event Log extension. This captures details specific to Windows Event Log events, providing structured information from various Windows logs.

### `resource_usage` / `resourceUsage`

- Type: [`ResourceUsage`](resource_usage.md) (singular)

A resource usage extension. This captures details about what entity (e.g., process, user) is using a specific resource.

### `system_event_details` / `systemEventDetails`

- Type: [`SystemEventDetails`](system_event_details.md) (singular)

A system event details extension. This captures additional details for system-level events, such as message type, sender image ID, and subsystem.

### `outlook_metadata` / `outlookMetadata`

- Type: [`OutlookMetadata`](outlook_metadata.md) (singular)

A Microsoft Outlook specific metadata extension. This includes metadata related to Outlook items, such as comments, templates, and security flags.

### `srum`

- Type: [`Srum`](srum.md) (singular)

A SRUM extension. This captures details specific to Windows System Resource Usage Monitor (SRUM) events, providing insights into application resource consumption.

### `user_assist` / `userAssist`

- Type: [`UserAssist`](user_assist.md) (singular)

A UserAssist extension. This captures details specific to Windows User Assist events, which track application usage and execution.

## Guidance

Population guidance from the Google UDM usage guide.

### `auth`

- **Purpose**: Extension to the authentication metadata.
- **Encoding**: String.

#### Examples

- Sandbox metadata (all behaviors exhibited by a file, for example, FireEye).
- Network Access Control (NAC) data.
- LDAP details about a user (for example, role, organization, etc.).

### `auth.auth_details` / `auth.authDetails`

- **Purpose**: Specify the vendor specific details for the authentication type or mechanism. Authentication providers often define types such as via_mfa or via_ad that provide useful information on the authentication type. These types can still be generalized in auth.type or auth.mechanism for usability and cross dataset rule compatibility.
- **Encoding**: String.
- **Examples**: via_mfa, via_ad.

#### Examples

- via_mfa, via_ad.

### `vulns`

- **Purpose**: Extension to the vulnerability metadata.
- **Encoding**: String.
- **Example**: Host vulnerability scan data.

#### Examples

- Host vulnerability scan data.
