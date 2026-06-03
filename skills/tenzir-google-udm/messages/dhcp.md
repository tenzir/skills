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

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Dhcp.OpCode`](../enums/dhcp_op_code.md)
- **JSON name**: `opcode`

The BOOTP op code.

### `htype`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `htype`

Hardware address type.

### `hlen`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `hlen`

Hardware address length.

### `hops`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `hops`

Hardware ops.

### `transaction_id`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `transactionId`

Transaction ID.

### `seconds`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `seconds`

Seconds elapsed since client began address acquisition/renewal process.

### `flags`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `flags`

Flags.

### `ciaddr`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ciaddr`

Client IP address (ciaddr).

### `yiaddr`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `yiaddr`

Your IP address (yiaddr).

### `siaddr`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `siaddr`

IP address of the next bootstrap server.

### `giaddr`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `giaddr`

Relay agent IP address (giaddr).

### `chaddr`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `chaddr`

Client hardware address (chaddr).

### `sname`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sname`

Server name that the client wishes to boot from.

### `file`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `file`

Boot image filename.

### `options`

- **Number**: `15`
- **Cardinality**: `repeated`
- **Type**: [`Dhcp.Option`](dhcp_option.md)
- **JSON name**: `options`

List of DHCP options.

### `type`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: [`Dhcp.MessageType`](../enums/dhcp_message_type.md)
- **JSON name**: `type`

DHCP message type.

### `lease_time_seconds`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `leaseTimeSeconds`

Lease time in seconds. See RFC2132, section 9.2.

### `client_hostname`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `clientHostname`

Client hostname. See RFC2132, section 3.14.

### `client_identifier`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `clientIdentifier`

Client identifier. See RFC2132, section 9.14. Note: Make sure to update the client_identifier_string field as well if you update this field.

### `requested_address`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `requestedAddress`

Requested IP address. See RFC2132, section 9.1.

### `client_identifier_string`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `clientIdentifierString`

Client identifier as string. See RFC2132, section 9.14. This field holds the string value of the client_identifier.
