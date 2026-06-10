# Special Mappings

In some cases, the mappings between fields of the original device and those of the ArcSight Extension Dictionary are not obvious. In that case, refer to the example in the following tables.

## Firewall

| Original Field | Mapped to CEF Name | Mapped to Full Name |
| --- | --- | --- |
| Rule Number / ACL Number | cs1 | deviceCustomString1 |

## Anti-Virus

| Original Field | Mapped to CEF Name | Mapped to Full Name |
| --- | --- | --- |
| Virus name | cs1 | deviceCustomString1 |
| Signature / Engine Version | cs2 | deviceCustomString2 |
| Action (Quartine, Cleaned, Deleted, …) | act | deviceAction |

## Email

| Original Field | Mapped to CEF Name | Mapped to Full Name |
| --- | --- | --- |
| Recipient (for example, [user@company.com](mailto:user@company.com)) | duser | destinationUserName |
| Sender (for example, [user@company.com](mailto:user@company.com)) | suser | sourceUserName |
| Relay | cs1 | deviceCustomString1 |

## Wireless

| Original Field | Mapped to CEF Name | Mapped to Full Name |
| --- | --- | --- |
| SSID | cs2 | deviceCustomString2 |
| Channel | cn1 | deviceCustomNumber1 |

## IPv6 Format

The connector code automatically sets labels for the **IPv6 address** fields if the field is set. You can set the label to the following values: **Device IPv6 Address**, **Source IPv6 Address**, and **Destination IPv6 Address**.

If the custom extension name is in IPv6 format and used to map:

- device address, then use **c6a1**. Use **Device IPv6 Address** as the label, or let the connector code set the label for you.
- source address, then use **c6a2**. Use **SourceIPv6 Address** as the label, or let the connector code set the label for you.
- destination address, then use **c6a3**. Use **Destination IPv6 Address** as the label, or let the connector code set the label for you.
