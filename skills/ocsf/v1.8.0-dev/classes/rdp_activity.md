# RDP Activity (rdp_activity)

Remote Desktop Protocol (RDP) Activity events report post-authentication remote client connections between clients and servers over the network.

- **UID**: `5`
- **Category**: Network Activity
- **Extends**: `network`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Initial Request` - The initial RDP request.
- `2`: `Initial Response` - The initial RDP response.
- `3`: `Connect Request` - An RDP connection request.
- `4`: `Connect Response` - An RDP connection response.
- `5`: `TLS Handshake` - The TLS handshake.
- `6`: `Traffic` - Network traffic report.
- `7`: `Disconnect` - An RDP connection disconnect.
- `8`: `Reconnect` - An RDP connection reconnect.

The normalized identifier of the activity that triggered the event.

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

- **Type**: `network_connection_info`
- **Requirement**: recommended
- **Group**: primary

The remote desktop connection details, either connection-based or connectionless.

### `device`

- **Type**: `device`
- **Requirement**: optional

The device instigating the RDP connection.

### `file`

- **Type**: `file`
- **Requirement**: optional
- **Group**: context

The file that is the target of the RDP activity.

### `identifier_cookie`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The client identifier cookie during client/server exchange.

### `keyboard_info`

- **Type**: `keyboard_info`
- **Requirement**: optional
- **Group**: context

The keyboard detailed information.

### `protocol_ver`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: context

The Remote Desktop Protocol version.

### `remote_display`

- **Type**: `display`
- **Requirement**: optional
- **Group**: context

The remote display affiliated with the event

### `request`

- **Type**: `request`
- **Requirement**: recommended
- **Group**: primary

The client request in an RDP network connection.

### `response`

- **Type**: `response`
- **Requirement**: recommended
- **Group**: primary

The server response in an RDP network connection.

### `user`

- **Type**: `user`
- **Requirement**: recommended
- **Group**: primary

The target user associated with the RDP activity.
