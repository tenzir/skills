# MessageType

DHCP message type. See RFC2131, section 3.1.

## Values

- `UNKNOWN_MESSAGE_TYPE` (0): Default message type.
- `DISCOVER` (1): DHCPDISCOVER.
- `OFFER` (2): DHCPOFFER.
- `REQUEST` (3): DHCPREQUEST.
- `DECLINE` (4): DHCPDECLINE.
- `ACK` (5): DHCPACK.
- `NAK` (6): DHCPNAK.
- `RELEASE` (7): DHCPRELEASE.
- `INFORM` (8): DHCPINFORM.
- `WIN_DELETED` (100): Microsoft Windows DHCP "lease deleted".
- `WIN_EXPIRED` (101): Microsoft Windows DHCP "lease expired".
