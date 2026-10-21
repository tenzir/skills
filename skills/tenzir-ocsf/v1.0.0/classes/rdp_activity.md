# RDP Activity (rdp_activity)

Remote Desktop Protocol (RDP) Activity events report remote client connections to a server as seen on the network.

- **Class UID**: `4005`
- **Category**: Network Activity
- **Extends**: [Network Activity (network_activity)](network_activity.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Network Activity:**
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

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Initial Request` - The initial RDP request.
- `2`: `Initial Response` - The initial RDP response.
- `3`: `Connect Request` - An RDP connection request.
- `4`: `Connect Response` - An RDP connection response.
- `5`: `TLS Handshake` - The TLS handshake.
- `6`: `Traffic` - Network traffic report.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `capabilities`

- **Type**: `string_t`
- **Requirement**: optional

A list of RDP capabilities.

### `certificate_chain`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The list of observed certificates in an RDP TLS connection.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: optional
- **Group**: primary

The device instigating the RDP connection.

### `identifier_cookie`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The client identifier cookie during client/server exchange.

### `protocol_ver`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The Remote Desktop Protocol version.

### `remote_display`

- **Type**: [`display`](../objects/display.md)
- **Requirement**: optional

The remote display affiliated with the event

### `request`

- **Type**: [`request`](../objects/request.md)
- **Requirement**: recommended
- **Group**: primary

The client request in an RDP network connection.

### `response`

- **Type**: [`response`](../objects/response.md)
- **Requirement**: recommended
- **Group**: primary

The server response in an RDP network connection.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4005`: `RDP Activity` - Remote Desktop Protocol (RDP) Activity events report remote client connections to a server as seen on the network.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400500`: `RDP Activity: Unknown`
- `400501`: `RDP Activity: Initial Request` - The initial RDP request.
- `400502`: `RDP Activity: Initial Response` - The initial RDP response.
- `400503`: `RDP Activity: Connect Request` - An RDP connection request.
- `400504`: `RDP Activity: Connect Response` - An RDP connection response.
- `400505`: `RDP Activity: TLS Handshake` - The TLS handshake.
- `400506`: `RDP Activity: Traffic` - Network traffic report.
- `400599`: `RDP Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
