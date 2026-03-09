# Tunnel Activity (tunnel_activity)

Tunnel Activity events report secure tunnel establishment (such as VPN), teardowns, renewals, and other network tunnel specific actions.

- **UID**: `14`
- **Category**: Network Activity
- **Extends**: `network`

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Open` - Open a tunnel.
- `2`: `Close` - Close a tunnel.
- `3`: `Renew` - Renew a tunnel.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event.

### `connection_info`

- **Type**: `network_connection_info`
- **Requirement**: optional
- **Group**: context

The tunnel connection information.

### `device`

- **Type**: `device`
- **Requirement**: recommended
- **Group**: primary

The device that reported the event.

### `dst_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended
- **Group**: primary

The server responding to the tunnel connection.

### `protocol_name`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The networking protocol associated with the tunnel. E.g. `IPSec`, `SSL`, `GRE`.

### `session`

- **Type**: `session`
- **Requirement**: recommended
- **Group**: primary

The session associated with the tunnel.

### `src_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended
- **Group**: primary

The initiator (client) of the tunnel connection.

### `traffic`

- **Type**: `network_traffic`
- **Requirement**: optional
- **Group**: context

Traffic refers to the amount of data moving across the tunnel at a given point of time. Ex: `bytes_in` and `bytes_out`.

### `tunnel_interface`

- **Type**: `network_interface`
- **Requirement**: recommended
- **Group**: primary

The information about the virtual tunnel interface, e.g. `utun0`. This is usually associated with the private (rfc-1918) ip of the tunnel.

### `tunnel_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The tunnel type. Example: `Split` or `Full`.

### `tunnel_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `tunnel_type`

#### Enum values

- `0`: `Unknown`
- `1`: `Split Tunnel`
- `2`: `Full Tunnel`
- `99`: `Other`

The normalized tunnel type ID.

### `user`

- **Type**: `user`
- **Requirement**: recommended
- **Group**: primary

The user associated with the tunnel activity.
