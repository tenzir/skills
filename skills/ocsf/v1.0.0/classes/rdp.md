# RDP Activity (rdp)

Remote Desktop Protocol (RDP) Activity events report remote client connections to a server as seen on the network.

- **UID**: `5`
- **Category**: Network Activity
- **Extends**: `network_activity`

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

- **Type**: `device`
- **Requirement**: optional

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

- **Type**: `display`
- **Requirement**: optional

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
