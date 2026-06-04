# Option

DHCP options.

## Fields

### `code`

- Type: `uint32` (singular)

Code. See RFC1533.

### `data`

- Type: `bytes` (singular)

Data.

## Guidance

Population guidance from the Google UDM usage guide.

### `Option.code`

- **Purpose**: Stores the DHCP option code. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Unsigned 32-bit integer.

### `Option.data`

- **Purpose**: Stores the DHCP option data. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.
