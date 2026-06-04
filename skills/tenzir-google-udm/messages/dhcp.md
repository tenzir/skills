# Dhcp

DHCP information.

- **Full name**: `google.backstory.Dhcp`
- **Fields**: `21`
- **Nested messages**: `1`
- **Nested enums**: `2`

## Nested messages

- [Dhcp.Option](dhcp_option.md)

## Nested enums

- [Dhcp.OpCode](../enums/dhcp_op_code.md)
- [Dhcp.MessageType](../enums/dhcp_message_type.md)

## Fields

### `opcode`

- Type: [`Dhcp.OpCode`](../enums/dhcp_op_code.md) (singular)

The BOOTP op code.

### `htype`

- Type: `uint32` (singular)

Hardware address type.

### `hlen`

- Type: `uint32` (singular)

Hardware address length.

### `hops`

- Type: `uint32` (singular)

Hardware ops.

### `transactionId`

- Type: `uint32` (singular)

Transaction ID.

### `seconds`

- Type: `uint32` (singular)

Seconds elapsed since client began address acquisition/renewal process.

### `flags`

- Type: `uint32` (singular)

Flags.

### `ciaddr`

- Type: `string` (singular)

Client IP address (ciaddr).

### `yiaddr`

- Type: `string` (singular)

Your IP address (yiaddr).

### `siaddr`

- Type: `string` (singular)

IP address of the next bootstrap server.

### `giaddr`

- Type: `string` (singular)

Relay agent IP address (giaddr).

### `chaddr`

- Type: `string` (singular)

Client hardware address (chaddr).

### `sname`

- Type: `string` (singular)

Server name that the client wishes to boot from.

### `file`

- Type: `string` (singular)

Boot image filename.

### `options`

- Type: [`Dhcp.Option`](dhcp_option.md) (repeated)

List of DHCP options.

### `type`

- Type: [`Dhcp.MessageType`](../enums/dhcp_message_type.md) (singular)

DHCP message type.

### `leaseTimeSeconds`

- Type: `uint32` (singular)

Lease time in seconds. See RFC2132, section 9.2.

### `clientHostname`

- Type: `string` (singular)

Client hostname. See RFC2132, section 3.14.

### `clientIdentifier`

- Type: `bytes` (singular)

Client identifier. See RFC2132, section 9.14. Note: Make sure to update the clientIdentifierString field as well if you update this field.

### `requestedAddress`

- Type: `string` (singular)

Requested IP address. See RFC2132, section 9.1.

### `clientIdentifierString`

- Type: `string` (singular)

Client identifier as string. See RFC2132, section 9.14. This field holds the string value of the clientIdentifier.

## Guidance

Population guidance from the Google UDM usage guide.

### `Dhcp.chaddr`

- **Purpose**: Hardware address for the client.
- **Encoding**: MAC address.

### `Dhcp.ciaddr`

- **Purpose**: IP address for the client.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `Dhcp.clientHostname`

- **Purpose**: Hostname for the client. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: String.

### `Dhcp.clientIdentifier`

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

### `Dhcp.leaseTimeSeconds`

- **Purpose**: Client-requested lease time for an IP address in seconds. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.opcode`

- **Purpose**: BOOTP op code (see section 3 of RFC 951).
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_OPCODE`
  - `BOOTREQUEST`
  - `BOOTREPLY`

### `Dhcp.requestedAddress`

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

### `Dhcp.transactionId`

- **Purpose**: Client transaction ID.
- **Encoding**: 32-bit unsigned integer.

### `Dhcp.type`

- **Purpose**: DHCP message type. See RFC 1533 for more information.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_MESSAGE_TYPE`
  - `DISCOVER`
  - `OFFER`
  - `REQUEST`
  - `DECLINE`
  - `ACK`
  - `NAK`
  - `RELEASE`
  - `INFORM`
  - `WIN_DELECTED`
  - `WIN_EXPIRED`

### `Dhcp.yiaddr`

- **Purpose**: Your IP address.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.
