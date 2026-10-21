# DHCP Activity (dhcp_activity)

DHCP Activity events report MAC to IP assignment via DHCP from a client or server.

- **Class UID**: `4004`
- **Category**: Network Activity
- **Extends**: [Network (network)](network.md)
- **Profiles**: [Network Proxy](../profiles/network_proxy.md), [Load Balancer](../profiles/load_balancer.md), [AI Operation](../profiles/ai_operation.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `dst_endpoint`, `src_endpoint`

## Inherited attributes

**From Network:**
- `connection_info` (recommended)
- `proxy` (recommended)
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
- `1`: `Discover` - DHCPDISCOVER
- `2`: `Offer` - DHCPOFFER
- `3`: `Request` - DHCPREQUEST
- `4`: `Decline` - DHCPDECLINE
- `5`: `Ack` - DHCPACK: The server accepts the request by sending the client a DHCP Acknowledgment message.
- `6`: `Nak` - DHCPNAK
- `7`: `Release` - DHCPRELEASE: A DHCP client sends a DHCPRELEASE packet to the server to release the IP address and cancel any remaining lease.
- `8`: `Inform` - DHCPINFORM
- `9`: `Expire` - DHCPEXPIRE: A DHCP lease expired.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the activity that triggered the event. Each event class defines its own set of activity values. Use `0` (Unknown) when the activity cannot be determined. Use `99` (Other) when the activity does not match any defined value, in which case `activity_name` must be populated with the source-specific label.

### `dst_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The responder (server) of the DHCP connection.

### `is_renewal`

- **Type**: `boolean_t`
- **Requirement**: recommended
- **Group**: primary

Indicates whether this is a lease/session renewal event.

### `lease_dur`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary

This represents the length of the DHCP lease in seconds. This is present in DHCP Ack events.

### `relay`

- **Type**: [`network_interface`](../objects/network_interface.md)
- **Requirement**: recommended
- **Group**: primary

The network relay that is associated with the event.

### `src_endpoint`

- **Type**: [`network_endpoint`](../objects/network_endpoint.md)
- **Requirement**: recommended
- **Group**: primary

The initiator (client) of the DHCP connection.

### `transaction_uid`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The unique identifier of the transaction. This is typically a random number generated from the client to associate a dhcp request/response pair.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `4004`: `DHCP Activity` - DHCP Activity events report MAC to IP assignment via DHCP from a client or server.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `400400`: `DHCP Activity: Unknown`
- `400401`: `DHCP Activity: Discover` - DHCPDISCOVER
- `400402`: `DHCP Activity: Offer` - DHCPOFFER
- `400403`: `DHCP Activity: Request` - DHCPREQUEST
- `400404`: `DHCP Activity: Decline` - DHCPDECLINE
- `400405`: `DHCP Activity: Ack` - DHCPACK: The server accepts the request by sending the client a DHCP Acknowledgment message.
- `400406`: `DHCP Activity: Nak` - DHCPNAK
- `400407`: `DHCP Activity: Release` - DHCPRELEASE: A DHCP client sends a DHCPRELEASE packet to the server to release the IP address and cancel any remaining lease.
- `400408`: `DHCP Activity: Inform` - DHCPINFORM
- `400409`: `DHCP Activity: Expire` - DHCPEXPIRE: A DHCP lease expired.
- `400499`: `DHCP Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
