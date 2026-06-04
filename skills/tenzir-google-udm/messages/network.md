# Network

A network event.

## Fields

### `sent_bytes` / `sentBytes`

- Type: `uint64` (singular)

The number of bytes sent.

### `received_bytes` / `receivedBytes`

- Type: `uint64` (singular)

The number of bytes received.

### `total_bytes` / `totalBytes`

- Type: `int64` (singular)

The number of total bytes.

### `sent_packets` / `sentPackets`

- Type: `int64` (singular)

The number of packets sent.

### `received_packets` / `receivedPackets`

- Type: `int64` (singular)

The number of packets received.

### `session_duration` / `sessionDuration`

- Type: `duration` (singular)

The duration of the session as the number of seconds and nanoseconds. For seconds, network.session_duration.seconds, the type is a 64-bit integer. For nanoseconds, network.session_duration.nanos, the type is a 32-bit integer.

### `session_id` / `sessionId`

- Type: `string` (singular)

The ID of the network session.

### `parent_session_id` / `parentSessionId`

- Type: `string` (singular)

The ID of the parent network session.

### `application_protocol_version` / `applicationProtocolVersion`

- Type: `string` (singular)

The version of the application protocol. e.g. "1.1, 2.0"

### `community_id` / `communityId`

- Type: `string` (singular)

Community ID network flow value.

### `direction`

- Type: [`Direction`](../enums/network_direction.md) (singular)

The direction of network traffic.

### `ip_protocol` / `ipProtocol`

- Type: [`IpProtocol`](../enums/network_ip_protocol.md) (singular)

The IP protocol.

### `ipv6`

- Type: `bool` (singular)

True if IPv6 is used.

### `application_protocol` / `applicationProtocol`

- Type: [`ApplicationProtocol`](../enums/network_application_protocol.md) (singular)

The application protocol.

### `ftp`

- Type: [`Ftp`](ftp.md) (singular)

FTP info.

### `email`

- Type: [`Email`](email.md) (singular)

Email info for the sender/recipient.

### `dns`

- Type: [`Dns`](dns.md) (singular)

DNS info.

### `dhcp`

- Type: [`Dhcp`](dhcp.md) (singular)

DHCP info.

### `http`

- Type: [`Http`](http.md) (singular)

HTTP info.

### `tls`

- Type: [`Tls`](tls.md) (singular)

TLS info.

### `smtp`

- Type: [`Smtp`](smtp.md) (singular)

SMTP info. Store fields specific to SMTP not covered by Email.

### `asn`

- Type: `string` (singular)

Autonomous system number.

### `dns_domain` / `dnsDomain`

- Type: `string` (singular)

DNS domain name.

### `carrier_name` / `carrierName`

- Type: `string` (singular)

Carrier identification.

### `organization_name` / `organizationName`

- Type: `string` (singular)

Organization name (e.g Google).

### `ip_subnet_range` / `ipSubnetRange`

- Type: `string` (singular)

Associated human-readable IP subnet range (e.g. 10.1.2.0/24).

### `is_proxy` / `isProxy`

- Type: `bool` (singular)

Whether the IP address is a known proxy.

### `proxy_info` / `proxyInfo`

- Type: [`ProxyInfo`](proxy_info.md) (singular)

Proxy information. Only set if is_proxy is true.

### `connection_state` / `connectionState`

- Type: [`ConnectionState`](../enums/network_connection_state.md) (singular)

The state of the network connection.

## Guidance

Population guidance from the Google UDM usage guide.

### `Network.application_protocol` / `Network.applicationProtocol`

- **Purpose**: Indicates the network application protocol.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_APPLICATION_PROTOCOL`
  - `AFP`
  - `APPC`
  - `AMQP`
  - `ATOM`
  - `BEEP`
  - `BITCOIN`
  - `BIT_TORRENT`
  - `CFDP`
  - `CIP`
  - `COAP`
  - `COTP`
  - `DCERPC`
  - `DDS`
  - `DEVICE_NET`
  - `DHCP`
  - `DICOM`
  - `DNP3`
  - `DNS`
  - `E_DONKEY`
  - `ENRP`
  - `FAST_TRACK`
  - `FINGER`
  - `FREENET`
  - `FTAM`
  - `GOOSE`
  - `GOPHER`
  - `GRPC`
  - `HL7`
  - `H323`
  - `HTTP`
  - `HTTPS`
  - `IEC104`
  - `IRCP`
  - `KADEMLIA`
  - `KRB5`
  - `LDAP`
  - `LPD`
  - `MIME`
  - `MMS`
  - `MODBUS`
  - `MQTT`
  - `NETCONF`
  - `NFS`
  - `NIS`
  - `NNTP`
  - `NTCIP`
  - `NTP`
  - `OSCAR`
  - `PNRP`
  - `PTP`
  - `QUIC`
  - `RDP`
  - `RELP`
  - `RIP`
  - `RLOGIN`
  - `RPC`
  - `RTMP`
  - `RTP`
  - `RTPS`
  - `RTSP`
  - `SAP`
  - `SDP`
  - `SIP`
  - `SLP`
  - `SMB`
  - `SMTP`
  - `SNMP`
  - `SNTP`
  - `SSH`
  - `SSMS`
  - `STYX`
  - `SV`
  - `TCAP`
  - `TDS`
  - `TOR`
  - `TSP`
  - `VTP`
  - `WHOIS`
  - `WEB_DAV`
  - `X400`
  - `X500`
  - `XMPP`

### `Network.direction`

- **Purpose**: Indicates the direction of network traffic.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_DIRECTION`
  - `INBOUND`
  - `OUTBOUND`
  - `BROADCAST`

### `Network.email`

- **Purpose**: Specifies the email address for the sender/recipient.
- **Encoding**: String.
- **Example**: jcheng@company.example.com

#### Examples

- jcheng@company.example.com

### `Network.ip_protocol` / `Network.ipProtocol`

- **Purpose**: Indicates the IP protocol.
- **Encoding**: Enumerated type.
- **Possible values**:
  - `UNKNOWN_IP_PROTOCOL`
  - `EIGRP`: Enhanced Interior Gateway Routing Protocol
  - `ESP`: Encapsulating Security Payload
  - `ETHERIP`: Ethernet-within-IP Encapsulation
  - `GRE`: Generic Routing Encapsulation
  - `ICMP`: Internet Control Message Protocol
  - `IGMP`: Internet Group Management Protocol
  - `IP6IN4`: IPv6 Encapsulation
  - `PIM`: Protocol Independent Multicast
  - `TCP`: Transmission Control Protocol
  - `UDP`: User Datagram Protocol
  - `VRRP`: Virtual Router Redundancy Protocol

### `Network.received_bytes` / `Network.receivedBytes`

- **Purpose**: Specifies the number of bytes received.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 12,453,654,768

#### Examples

- 12,453,654,768

### `Network.sent_bytes` / `Network.sentBytes`

- **Purpose**: Specifies the number of bytes sent.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 7,654,876

#### Examples

- 7,654,876

### `Network.session_duration` / `Network.sessionDuration`

- **Purpose**: Stores the network session duration, typically returned in a drop event for the session. To set the duration you can set either `network.session_duration.seconds` = 1, (type int64) or `network.session_duration.nanos` = 1 (type int32).

### `Network.session_id` / `Network.sessionId`

- **Purpose**: Stores the network session identifier.
- **Encoding**: String.
- **Example**: SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34

#### Examples

- SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34
