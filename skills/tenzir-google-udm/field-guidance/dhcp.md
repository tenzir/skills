# Dhcp Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Schema

- [Dhcp](../messages/dhcp.md)

## Fields

### `Dhcp.chaddr`

- **Purpose**: Hardware address for the client.
- **Encoding**: MAC address.

### `Dhcp.ciaddr`

- **Purpose**: IP address for the client.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `Dhcp.client_hostname`

- **Purpose**: Hostname for the client. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: String.

### `Dhcp.client_identifier`

- **Purpose**: Client identifier. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.

### `Dhcp.file`

- **Purpose**: Filename for the boot image.
- **Encoding**: String.

### `Dhcp.flags`

- **Purpose**: Value for the DHCP flags field.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.giaddr`

- **Purpose**: IP address for the relay agent.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `Dhcp.hlen`

- **Purpose**: Hardware address length.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.hops`

- **Purpose**: DHCP hop count.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.htype`

- **Purpose**: Hardware address type.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.lease_time_seconds`

- **Purpose**: Client-requested lease time for an IP address in seconds. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.opcode`

- **Purpose**: BOOTP op code (see section 3 of RFC 951).
- **Encoding**: Enumerated type.
- **Possible values**: UNKNOWN_OPCODE BOOTREQUEST BOOTREPLY

### `Dhcp.requested_address`

- **Purpose**: Client identifier. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `Dhcp.seconds`

- **Purpose**: Seconds elapsed since the client began the address acquisition/renewal process.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.siaddr`

- **Purpose**: IP address for the next bootstrap server.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `Dhcp.sname`

- **Purpose**: Name of the server that the client has requested to boot from.
- **Encoding**: String.

### `Dhcp.transaction_id`

- **Purpose**: Client transaction ID.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.type`

- **Purpose**: DHCP message type. See RFC 1533 for more information.
- **Encoding**: Enumerated type.
- **Possible values**: UNKNOWN_MESSAGE_TYPE DISCOVER OFFER REQUEST DECLINE ACK NAK RELEASE INFORM WIN_DELECTED WIN_EXPIRED

### `Dhcp.yiaddr`

- **Purpose**: Your IP address.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.
