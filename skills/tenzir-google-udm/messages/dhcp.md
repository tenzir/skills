# Dhcp

DHCP information.

## Fields

### `opcode`

- Type: [`OpCode`](../enums/dhcp_op_code.md) (singular)

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

### `transaction_id` / `transactionId`

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

- Type: [`Option`](dhcp_option.md) (repeated)

List of DHCP options.

### `type`

- Type: [`MessageType`](../enums/dhcp_message_type.md) (singular)

DHCP message type.

### `lease_time_seconds` / `leaseTimeSeconds`

- Type: `uint32` (singular)

Lease time in seconds. See RFC2132, section 9.2.

### `client_hostname` / `clientHostname`

- Type: `string` (singular)

Client hostname. See RFC2132, section 3.14.

### `client_identifier` / `clientIdentifier`

- Type: `bytes` (singular)

Client identifier. See RFC2132, section 9.14. Note: Make sure to update the client_identifier_string field as well if you update this field.

### `requested_address` / `requestedAddress`

- Type: `string` (singular)

Requested IP address. See RFC2132, section 9.1.

### `client_identifier_string` / `clientIdentifierString`

- Type: `string` (singular)

Client identifier as string. See RFC2132, section 9.14. This field holds the string value of the client_identifier.

## Guidance

Population guidance from the Google UDM usage guide.

### `chaddr`

- **Purpose**: Hardware address for the client.
- **Encoding**: MAC address.

### `ciaddr`

- **Purpose**: IP address for the client.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `client_hostname` / `clientHostname`

- **Purpose**: Hostname for the client. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: String.

### `client_identifier` / `clientIdentifier`

- **Purpose**: Client identifier. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.

### `file`

- **Purpose**: Filename for the boot image.
- **Encoding**: String.

### `flags`

- **Purpose**: Value for the DHCP flags field.
- **Encoding**: 32-bit unsigned integer.

### `giaddr`

- **Purpose**: IP address for the relay agent.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `hlen`

- **Purpose**: Hardware address length.
- **Encoding**: 32-bit unsigned integer.

### `hops`

- **Purpose**: DHCP hop count.
- **Encoding**: 32-bit unsigned integer.

### `htype`

- **Purpose**: Hardware address type.
- **Encoding**: 32-bit unsigned integer.

### `lease_time_seconds` / `leaseTimeSeconds`

- **Purpose**: Client-requested lease time for an IP address in seconds. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: 32-bit unsigned integer.

### `opcode`

- **Purpose**: BOOTP op code (see section 3 of RFC 951).
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_OPCODE`
  - `BOOTREQUEST`
  - `BOOTREPLY`

### `requested_address` / `requestedAddress`

- **Purpose**: Client identifier. See RFC 2132, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `seconds`

- **Purpose**: Seconds elapsed since the client began the address acquisition/renewal process.
- **Encoding**: 32-bit unsigned integer.

### `siaddr`

- **Purpose**: IP address for the next bootstrap server.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.

### `sname`

- **Purpose**: Name of the server that the client has requested to boot from.
- **Encoding**: String.

### `transaction_id` / `transactionId`

- **Purpose**: Client transaction ID.
- **Encoding**: 32-bit unsigned integer.

### `type`

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

### `yiaddr`

- **Purpose**: Your IP address.
- **Encoding**: Valid IPv4 or IPv6 address (RFC 5942) encoded in ASCII.
