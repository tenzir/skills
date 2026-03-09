# DHCP Activity (dhcp)

DHCP Activity events report MAC to IP assignment via DHCP from a client or server.

- **UID**: `4`
- **Category**: Network Activity
- **Extends**: `base_event`

## Attributes

### `$include`

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Discover` - DHCPDISCOVER
- `2`: `Offer` - DHCPOFFER
- `3`: `Request` - DHCPREQUEST
- `4`: `Decline` - DHCPDECLINE
- `5`: `Ack` - DHCPACK: The server accepts the request by sending the client a DHCP Acknowledgment message.
- `6`: `Nak` - DHCPNAK
- `7`: `Release` - DHCPRELEASE: A DHCP client sends a DHCPRELEASE packet to the server to release the IP address and cancel any remaining lease.
- `8`: `Inform` - DHCPINFORM
- `9`: `Expire` - DHCPEXPIRE: A DHCP lease expired.

The normalized identifier of the activity that triggered the event.

### `dst_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended
- **Group**: primary

The responder (server) of the DHCP connection.

### `is_renewal`

- **Type**: `boolean_t`
- **Requirement**: optional
- **Group**: primary

The indication of whether this is a lease/session renewal event.

### `lease_dur`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: primary

This represents the length of the DHCP lease in seconds. This is present in DHCP Ack events. (activity_id = 1)

### `src_endpoint`

- **Type**: `network_endpoint`
- **Requirement**: recommended
- **Group**: primary

The initiator (client) of the DHCP connection.

### `relay`

- **Type**: `network_interface`
- **Requirement**: optional
- **Group**: primary

The network relay that is associated with the event.

### `transaction_uid`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: primary

The unique identifier of the transaction. This is typically a random number generated from the client to associate a dhcp request/response pair.
