# Network

A network event.

- **Full name**: `google.backstory.Network`
- **Fields**: `29`
- **Nested enums**: `4`

## Nested enums

- [Network.Direction](../enums/network_direction.md)
- [Network.IpProtocol](../enums/network_ip_protocol.md)
- [Network.ApplicationProtocol](../enums/network_application_protocol.md)
- [Network.ConnectionState](../enums/network_connection_state.md)

## Fields

### `sent_bytes`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `sentBytes`

The number of bytes sent.

### `received_bytes`

- **Number**: `2`
- **Cardinality**: `singular`
- **Type**: `uint64`
- **JSON name**: `receivedBytes`

The number of bytes received.

### `total_bytes`

- **Number**: `27`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `totalBytes`

The number of total bytes.

### `sent_packets`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `sentPackets`

The number of packets sent.

### `received_packets`

- **Number**: `23`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `receivedPackets`

The number of packets received.

### `session_duration`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Duration`
- **JSON name**: `sessionDuration`

The duration of the session as the number of seconds and nanoseconds. For seconds, network.session_duration.seconds, the type is a 64-bit integer. For nanoseconds, network.session_duration.nanos, the type is a 32-bit integer.

### `session_id`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `sessionId`

The ID of the network session.

### `parent_session_id`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `parentSessionId`

The ID of the parent network session.

### `application_protocol_version`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `applicationProtocolVersion`

The version of the application protocol. e.g. "1.1, 2.0"

### `community_id`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `communityId`

Community ID network flow value.

### `direction`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: [`Network.Direction`](../enums/network_direction.md)
- **JSON name**: `direction`

The direction of network traffic.

### `ip_protocol`

- **Number**: `3`
- **Cardinality**: `singular`
- **Type**: [`Network.IpProtocol`](../enums/network_ip_protocol.md)
- **JSON name**: `ipProtocol`

The IP protocol.

### `ipv6`

- **Number**: `29`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `ipv6`

True if IPv6 is used.

### `application_protocol`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: [`Network.ApplicationProtocol`](../enums/network_application_protocol.md)
- **JSON name**: `applicationProtocol`

The application protocol.

### `ftp`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: [`Ftp`](ftp.md)
- **JSON name**: `ftp`

FTP info.

### `email`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: [`Email`](email.md)
- **JSON name**: `email`

Email info for the sender/recipient.

### `dns`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: [`Dns`](dns.md)
- **JSON name**: `dns`

DNS info.

### `dhcp`

- **Number**: `8`
- **Cardinality**: `singular`
- **Type**: [`Dhcp`](dhcp.md)
- **JSON name**: `dhcp`

DHCP info.

### `http`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`Http`](http.md)
- **JSON name**: `http`

HTTP info.

### `tls`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`Tls`](tls.md)
- **JSON name**: `tls`

TLS info.

### `smtp`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`Smtp`](smtp.md)
- **JSON name**: `smtp`

SMTP info. Store fields specific to SMTP not covered by Email.

### `asn`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `asn`

Autonomous system number.

### `dns_domain`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `dnsDomain`

DNS domain name.

### `carrier_name`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `carrierName`

Carrier identification.

### `organization_name`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `organizationName`

Organization name (e.g Google).

### `ip_subnet_range`

- **Number**: `24`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ipSubnetRange`

Associated human-readable IP subnet range (e.g. 10.1.2.0/24).

### `is_proxy`

- **Number**: `25`
- **Cardinality**: `singular`
- **Type**: `bool`
- **JSON name**: `isProxy`

Whether the IP address is a known proxy.

### `proxy_info`

- **Number**: `26`
- **Cardinality**: `singular`
- **Type**: [`ProxyInfo`](proxy_info.md)
- **JSON name**: `proxyInfo`

Proxy information. Only set if is_proxy is true.

### `connection_state`

- **Number**: `28`
- **Cardinality**: `singular`
- **Type**: [`Network.ConnectionState`](../enums/network_connection_state.md)
- **JSON name**: `connectionState`

The state of the network connection.

## Guidance

Population guidance from the Google UDM usage guide.

### `Network.application_protocol`

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

### `Network.ip_protocol`

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

- **Purpose**: Stores the network session duration, typically returned in a drop event for the session. To set the duration you can set either `network.session_duration.seconds` = 1, (type int64) or `network.session_duration.nanos` = 1 (type int32).

### `Network.session_id`

- **Purpose**: Stores the network session identifier.
- **Encoding**: String.
- **Example**: SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34

#### Examples

- SID:ANON:www.w3.org:j6oAOxCWZh/CD723LGeXlf-01:34
