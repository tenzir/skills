# Extensions

Extensions to a UDM event.

- **Full name**: `google.backstory.Extensions`
- **Fields**: `10`

## Fields

### `auth`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Authentication`](authentication.md)
- **JSON name**: `auth`

An authentication extension.

### `vulns`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: [`Vulnerabilities`](vulnerabilities.md)
- **JSON name**: `vulns`

A vulnerability extension.

### `entity_risk`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`EntityRisk`](entity_risk.md)
- **JSON name**: `entityRisk`

An entity risk change extension.

### `linux_utmp`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`LinuxUtmp`](linux_utmp.md)
- **JSON name**: `linuxUtmp`

A Linux Utmp extension. This captures details specific to Linux Utmp events, which record login and logout sessions on a Linux system.

### `windows_event_log`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`WindowsEventLog`](windows_event_log.md)
- **JSON name**: `windowsEventLog`

A Windows Event Log extension. This captures details specific to Windows Event Log events, providing structured information from various Windows logs.

### `resource_usage`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: [`ResourceUsage`](resource_usage.md)
- **JSON name**: `resourceUsage`

A resource usage extension. This captures details about what entity (e.g., process, user) is using a specific resource.

### `system_event_details`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`SystemEventDetails`](system_event_details.md)
- **JSON name**: `systemEventDetails`

A system event details extension. This captures additional details for system-level events, such as message type, sender image ID, and subsystem.

### `outlook_metadata`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: [`OutlookMetadata`](outlook_metadata.md)
- **JSON name**: `outlookMetadata`

A Microsoft Outlook specific metadata extension. This includes metadata related to Outlook items, such as comments, templates, and security flags.

### `srum`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`Srum`](srum.md)
- **JSON name**: `srum`

A SRUM extension. This captures details specific to Windows System Resource Usage Monitor (SRUM) events, providing insights into application resource consumption.

### `user_assist`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`UserAssist`](user_assist.md)
- **JSON name**: `userAssist`

A UserAssist extension. This captures details specific to Windows User Assist events, which track application usage and execution.

## Guidance

Population guidance from the Google UDM usage guide.

### `Extensions.auth`

- **Purpose**: Extension to the authentication metadata.
- **Encoding**: String.

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
