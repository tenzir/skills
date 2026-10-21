# Tunnel Activity (tunnel_activity)

Tunnel Activity events report secure tunnel establishment (such as VPN), teardowns, renewals, and other network tunnel specific actions.

- **Class UID**: `4014`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: [Network Proxy](../profiles/network_proxy.md), [Load Balancer](../profiles/load_balancer.md), [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `connection_info`, `session`, `src_endpoint`, `traffic`, `tunnel_interface`, `tunnel_type_id`

## Associations

- `src_endpoint` ↔ `user`
- `user` ↔ `src_endpoint`

## Inherited attributes

**From Network:**
- `proxy` (recommended)

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
- `1`: `Open` - Open a tunnel.
- `2`: `Close` - Close a tunnel.
- `3`: `Renew` - Renew a tunnel.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `connection_info`

- **Type**: [`network_connection_info`](../objects/network_connection_info.md)
- **Requirement**: recommended
- **Group**: context

The tunnel connection information.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: recommended
- **Group**: primary

The device that reported the event.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The server responding to the tunnel connection.

### `protocol_name`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The networking protocol associated with the tunnel. E.g. `IPSec`, `SSL`, `GRE`.

### `session`

- **Type**: [`session`](../objects/session.md)
- **Requirement**: recommended
- **Group**: primary

The session associated with the tunnel.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The initiator (client) of the tunnel connection.

### `traffic`

- **Type**: [`network_traffic`](../objects/network_traffic.md)
- **Requirement**: recommended
- **Group**: context

Traffic refers to the amount of data moving across the tunnel at a given point of time. Ex: `bytes_in` and `bytes_out`.

### `tunnel_interface`

- **Type**: [`network_interface`](../objects/network_interface.md)
- **Requirement**: recommended
- **Group**: primary

The information about the virtual tunnel interface, e.g. `utun0`. This is usually associated with the private (rfc-1918) ip of the tunnel.

### `tunnel_type`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The type of tunnel configuration, normalized to the caption of the `tunnel_type_id` value, indicating the scope of traffic routed through the connection. Example: `Split Tunnel` or `Full Tunnel`.

### `tunnel_type_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `tunnel_type`

#### Enum values

- `0`: `Unknown` - The type of tunnel configuration is unknown.
- `1`: `Split Tunnel` - The tunnel configuration routes only specific traffic through the tunnel.
- `2`: `Full Tunnel` - The tunnel configuration routes all traffic through the tunnel.
- `99`: `Other` - The type of tunnel configuration is not defined by the event source.

The normalized identifier for the type of tunnel configuration, indicating the scope of traffic routed through the connection. Example: `1 (Split Tunnel)` or `2 (Full Tunnel)`.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: recommended
- **Group**: primary

The user associated with the tunnel activity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4014`: `Tunnel Activity` - Tunnel Activity events report secure tunnel establishment (such as VPN), teardowns, renewals, and other network tunnel specific actions.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `401400`: `Tunnel Activity: Unknown`
- `401401`: `Tunnel Activity: Open` - Open a tunnel.
- `401402`: `Tunnel Activity: Close` - Close a tunnel.
- `401403`: `Tunnel Activity: Renew` - Renew a tunnel.
- `401499`: `Tunnel Activity: Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
