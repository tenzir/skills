# RDP Activity (rdp_activity)

Remote Desktop Protocol (RDP) Activity events report post-authentication remote client connections between clients and servers over the network.

- **Class UID**: `4005`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: [Network Proxy](../profiles/network_proxy.md), [Load Balancer](../profiles/load_balancer.md), [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `dst_endpoint`, `src_endpoint`

## Inherited attributes

**From Network:**
- `dst_endpoint` (recommended)
- `proxy` (recommended)
- `src_endpoint` (recommended)
- `traffic` (recommended)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
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
- `7`: `Disconnect` - An RDP connection disconnect.
- `8`: `Reconnect` - An RDP connection reconnect.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `capabilities`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

A list of RDP capabilities.

### `certificate_chain`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The list of observed certificates in an RDP TLS connection.

### `connection_info`

- **Type**: [`network_connection_info`](../objects/network_connection_info.md)
- **Requirement**: recommended
- **Group**: primary

The remote desktop connection details, either connection-based or connectionless.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: optional
- **Group**: primary

The device instigating the RDP connection.

### `file`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: optional
- **Group**: context

The file that is the target of the RDP activity.

### `identifier_cookie`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The client identifier cookie during client/server exchange.

### `keyboard_info`

- **Type**: [`keyboard_info`](../objects/keyboard_info.md)
- **Requirement**: optional
- **Group**: context

The keyboard detailed information.

### `protocol_ver`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The Remote Desktop Protocol version.

### `remote_display`

- **Type**: [`display`](../objects/display.md)
- **Requirement**: optional
- **Group**: context

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

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: recommended
- **Group**: primary

The target user associated with the RDP activity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4005`: `RDP Activity` - Remote Desktop Protocol (RDP) Activity events report post-authentication remote client connections between clients and servers over the network.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
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
- `400507`: `RDP Activity: Disconnect` - An RDP connection disconnect.
- `400508`: `RDP Activity: Reconnect` - An RDP connection reconnect.
- `400599`: `RDP Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
