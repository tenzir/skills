# Dhcp.Option

DHCP options.

- **Full name**: `google.backstory.Dhcp.Option`
- **Fields**: `2`

## Fields

### `code`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `uint32`
- **JSON name**: `code`

Code. See RFC1533.

### `data`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `bytes`
- **JSON name**: `data`

Data.

## Guidance

Population guidance from the Google UDM usage guide.

### `Option.code`

- **Purpose**: Stores the DHCP option code. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Unsigned 32-bit integer.

### `Option.data`

- **Purpose**: Stores the DHCP option data. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.
