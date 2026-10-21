# SSH Activity (ssh_activity)

SSH Activity events report remote client connections to a server using the Secure Shell (SSH) Protocol.

- **Class UID**: `4007`
- **Category**: Network Activity
- **Extends**: [Network Activity (network_activity)](network_activity.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Network Activity:**
- `activity_id` (required)
- `dst_endpoint` (required)
- `src_endpoint` (required)
- `connection_info` (recommended)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `client_hassh`

- **Type**: [`hassh`](../objects/hassh.md)
- **Requirement**: recommended
- **Group**: primary

The Client HASSH fingerprinting object.

### `protocol_ver`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The Secure Shell Protocol version.

### `server_hassh`

- **Type**: [`hassh`](../objects/hassh.md)
- **Requirement**: recommended
- **Group**: primary

The Server HASSH fingerprinting object.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4007`: `SSH Activity` - SSH Activity events report remote client connections to a server using the Secure Shell (SSH) Protocol.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400700`: `SSH Activity: Unknown`
- `400701`: `SSH Activity: Open` - A new network connection was opened.
- `400702`: `SSH Activity: Close` - The network connection was closed.
- `400703`: `SSH Activity: Reset` - The network connection was abnormally terminated or closed by a middle device like firewalls.
- `400704`: `SSH Activity: Fail` - The network connection failed. For example a connection timeout or no route to host.
- `400705`: `SSH Activity: Refuse` - The network connection was refused. For example an attempt to connect to a server port which is not open.
- `400706`: `SSH Activity: Traffic` - Network traffic report.
- `400799`: `SSH Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
