# Network Connection Query (network_connection_query)

Network Connection Query events report information about active network connections.

> **Deprecated since v1.5.0.** Use the `evidence_info` class.

- **Class UID**: `5012`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](discovery_result.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Discovery Result:**
- `activity_id` (required)
- `query_result_id` (required)
- `query_info` (recommended)
- `query_result` (recommended)

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

### `connection_info`

- **Type**: [`network_connection_info`](../objects/network_connection_info.md)
- **Requirement**: required
- **Group**: primary

The network connection information.

### `process`

- **Type**: [`process`](../objects/process.md)
- **Requirement**: required
- **Group**: primary

The process that owns the socket.

### `state`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The state of the socket, normalized to the caption of the state_id value. In the case of 'Other', it is defined by the event source.

### `state_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: primary
- **Sibling**: `state`

#### Enum values

- `0`: `Unknown` - The socket state is unknown.
- `1`: `ESTABLISHED` - The socket has an established connection between a local application and a remote peer.
- `2`: `SYN_SENT` - The socket is actively trying to establish a connection to a remote peer.
- `3`: `SYN_RECV` - The socket has passively received a connection request from a remote peer.
- `4`: `FIN_WAIT1` - The socket connection has been closed by the local application, the remote peer has not yet acknowledged the close, and the system is waiting for it to close its half of the connection.
- `5`: `FIN_WAIT2` - The socket connection has been closed by the local application, the remote peer has acknowledged the close, and the system is waiting for it to close its half of the connection.
- `6`: `TIME_WAIT` - The socket connection has been closed by the local application, the remote peer has closed its half of the connection, and the system is waiting to be sure that the remote peer received the last acknowledgement.
- `7`: `CLOSED` - The socket is not in use.
- `8`: `CLOSE_WAIT` - The socket connection has been closed by the remote peer, and the system is waiting for the local application to close its half of the connection.
- `9`: `LAST_ACK` - The socket connection has been closed by the remote peer, the local application has closed its half of the connection, and the system is waiting for the remote peer to acknowledge the close.
- `10`: `LISTEN` - The socket is listening for incoming connections.
- `11`: `CLOSING` - The socket connection has been closed by the local application and the remote peer simultaneously, and the remote peer has not yet acknowledged the close attempt of the local application.
- `99`: `Other` - The state is not mapped. See the `state` attribute, which contains a data source specific value.

The state of the socket.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5012`: `Network Connection Query` - Network Connection Query events report information about active network connections.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `501200`: `Network Connection Query: Unknown`
- `501201`: `Network Connection Query: Query` - The discovered results are via a query request.
- `501299`: `Network Connection Query: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
