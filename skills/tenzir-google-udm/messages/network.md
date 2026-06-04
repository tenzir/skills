# Network

A network event.

## Fields

### `sentBytes`

- Type: `uint64` (singular)

The number of bytes sent.

### `receivedBytes`

- Type: `uint64` (singular)

The number of bytes received.

### `totalBytes`

- Type: `int64` (singular)

The number of total bytes.

### `sentPackets`

- Type: `int64` (singular)

The number of packets sent.

### `receivedPackets`

- Type: `int64` (singular)

The number of packets received.

### `sessionDuration`

- Type: `google.protobuf.Duration` (singular)

The duration of the session as the number of seconds and nanoseconds. For seconds, network.sessionDuration.seconds, the type is a 64-bit integer. For nanoseconds, network.sessionDuration.nanos, the type is a 32-bit integer.

### `sessionId`

- Type: `string` (singular)

The ID of the network session.

### `parentSessionId`

- Type: `string` (singular)

The ID of the parent network session.

### `applicationProtocolVersion`

- Type: `string` (singular)

The version of the application protocol. e.g. "1.1, 2.0"

### `communityId`

- Type: `string` (singular)

Community ID network flow value.

### `direction`

- Type: [`Direction`](../enums/network_direction.md) (singular)

The direction of network traffic.

### `ipProtocol`

- Type: [`IpProtocol`](../enums/network_ip_protocol.md) (singular)

The IP protocol.

### `ipv6`

- Type: `bool` (singular)

True if IPv6 is used.

### `applicationProtocol`

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

### `dnsDomain`

- Type: `string` (singular)

DNS domain name.

### `carrierName`

- Type: `string` (singular)

Carrier identification.

### `organizationName`

- Type: `string` (singular)

Organization name (e.g Google).

### `ipSubnetRange`

- Type: `string` (singular)

Associated human-readable IP subnet range (e.g. 10.1.2.0/24).

### `isProxy`

- Type: `bool` (singular)

Whether the IP address is a known proxy.

### `proxyInfo`

- Type: [`ProxyInfo`](proxy_info.md) (singular)

Proxy information. Only set if isProxy is true.

### `connectionState`

- Type: [`ConnectionState`](../enums/network_connection_state.md) (singular)

The state of the network connection.

## Guidance

Population guidance from the Google UDM usage guide.

### `Network.applicationProtocol`

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

### `Network.ipProtocol`

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

### `Network.receivedBytes`

- **Purpose**: Specifies the number of bytes received.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 12,453,654,768

#### Examples

- 12,453,654,768

### `Network.sentBytes`

- **Purpose**: Specifies the number of bytes sent.
- **Encoding**: 64-bit unsigned integer.
- **Example**: 7,654,876

#### Examples

- 7,654,876

### `Network.sessionDuration`

- **Purpose**: Stores the network session duration, typically returned in a drop event for the session. To set the duration you can set either `network.sessionDuration.seconds` = 1, (type int64) or `network.sessionDuration.nanos` = 1 (type int32).

### `Network.sessionId`

- **Purpose**: Stores the network session identifier.
- **Encoding**: String.
- **Example**: SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34

#### Examples

- SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34
