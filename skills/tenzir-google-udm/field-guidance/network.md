# Network Field Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **License**: Content licensed under Creative Commons Attribution 4.0; code samples licensed under Apache 2.0, as stated in the Google Developers Site Policies.

## Schema

- [Network](../messages/network.md)

## Fields

### `Network.application_protocol`

- **Purpose**: Indicates the network application protocol.
- **Encoding**: Enumerated type.
- **Possible values**: UNKNOWN_APPLICATION_PROTOCOL AFP APPC AMQP ATOM BEEP BITCOIN BIT_TORRENT CFDP CIP COAP COTP DCERPC DDS DEVICE_NET DHCP DICOM DNP3 DNS E_DONKEY ENRP FAST_TRACK FINGER FREENET FTAM GOOSE GOPHER GRPC HL7 H323 HTTP HTTPS IEC104 IRCP KADEMLIA KRB5 LDAP LPD MIME MMS MODBUS MQTT NETCONF NFS NIS NNTP NTCIP NTP OSCAR PNRP PTP QUIC RDP RELP RIP RLOGIN RPC RTMP RTP RTPS RTSP SAP SDP SIP SLP SMB SMTP SNMP SNTP SSH SSMS STYX SV TCAP TDS TOR TSP VTP WHOIS WEB_DAV X400 X500 XMPP

### `Network.direction`

- **Purpose**: Indicates the direction of network traffic.
- **Encoding**: Enumerated type.
- **Possible values**: UNKNOWN_DIRECTION INBOUND OUTBOUND BROADCAST

### `Network.email`

- **Purpose**: Specifies the email address for the sender/recipient.
- **Encoding**: String.
- **Example**: jcheng@company.example.com

#### Examples

- jcheng@company.example.com

### `Network.ip_protocol`

- **Purpose**: Indicates the IP protocol.
- **Encoding**: Enumerated type.
- **Possible values**: UNKNOWN_IP_PROTOCOL EIGRP-Enhanced Interior Gateway Routing Protocol ESP-Encapsulating Security Payload ETHERIP-Ethernet-within-IP Encapsulation GRE-Generic Routing Encapsulation ICMP-Internet Control Message Protocol IGMP-Internet Group Management Protocol IP6IN4-IPv6 Encapsulation PIM-Protocol Independent Multicast TCP-Transmission Control Protocol UDP-User Datagram Protocol VRRP-Virtual Router Redundancy Protocol

### `Network.received_bytes`

- **Purpose**: Specifies the number of bytes received.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 12,453,654,768

#### Examples

- 12,453,654,768

### `Network.sent_bytes`

- **Purpose**: Specifies the number of bytes sent.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 7,654,876

#### Examples

- 7,654,876

### `Network.session_duration`

- **Purpose**: Stores the network session duration, typically returned in a drop event for the session. To set the duration you can set either network.session_duration.seconds = 1, (type int64) or network.session_duration.nanos = 1 (type int32).
- **Encoding**: 32-bit integer-For seconds (network.session_duration.seconds). 64-bit integer-For nanoseconds (network.session_duration.nanos).

### `Network.session_id`

- **Purpose**: Stores the network session identifier.
- **Encoding**: String.
- **Example**: SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34

#### Examples

- SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34
