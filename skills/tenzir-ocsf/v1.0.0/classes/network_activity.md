# Network Activity (network_activity)

Network Activity events report network connection and traffic activity.

- **Class UID**: `4001`
- **Category**: Network Activity
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Host](../profiles/host.md), [Security Control](../profiles/security_control.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

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
- `1`: `Open` - A new network connection was opened.
- `2`: `Close` - The network connection was closed.
- `3`: `Reset` - The network connection was abnormally terminated or closed by a middle device like firewalls.
- `4`: `Fail` - The network connection failed. For example a connection timeout or no route to host.
- `5`: `Refuse` - The network connection was refused. For example an attempt to connect to a server port which is not open.
- `6`: `Traffic` - Network traffic report.
- `99`: `Other` - The event activity is not mapped.

The normalized identifier of the activity that triggered the event.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4001`: `Network Activity` - Network Activity events report network connection and traffic activity.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400100`: `Network Activity: Unknown`
- `400101`: `Network Activity: Open` - A new network connection was opened.
- `400102`: `Network Activity: Close` - The network connection was closed.
- `400103`: `Network Activity: Reset` - The network connection was abnormally terminated or closed by a middle device like firewalls.
- `400104`: `Network Activity: Fail` - The network connection failed. For example a connection timeout or no route to host.
- `400105`: `Network Activity: Refuse` - The network connection was refused. For example an attempt to connect to a server port which is not open.
- `400106`: `Network Activity: Traffic` - Network traffic report.
- `400199`: `Network Activity: Other`

The event type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

### `app_name`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The name of the application that is associated with the event or object.

### `connection_info`

- **Type**: [`network_connection_info`](../objects/network_connection_info.md)
- **Requirement**: recommended
- **Group**: primary

The network connection information.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: required
- **Group**: primary

The responder (server) in a network connection.

### `proxy`

- **Type**: [`network_proxy`](../objects/network_proxy.md)
- **Requirement**: optional
- **Group**: primary

If a proxy connection is present, the connection from the client to the proxy server.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: required
- **Group**: primary

The initiator (client) of the network connection.

### `tls`

- **Type**: [`tls`](../objects/tls.md)
- **Requirement**: optional
- **Group**: primary

The Transport Layer Security (TLS) attributes.

### `traffic`

- **Type**: [`network_traffic`](../objects/network_traffic.md)
- **Requirement**: optional
- **Group**: primary

The network traffic refers to the amount of data moving across a network at a given point of time. Intended to be used alongside Network Connection.
