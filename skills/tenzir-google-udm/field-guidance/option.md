# Option Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Dhcp.Option](../messages/dhcp_option.md)

## Fields

### `Option.code`

- **Purpose**: Stores the DHCP option code. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Unsigned 32-bit integer.

### `Option.data`

- **Purpose**: Stores the DHCP option data. See RFC 1533, DHCP Options and BOOTP Vendor Extensions, for more information.
- **Encoding**: Bytes.
