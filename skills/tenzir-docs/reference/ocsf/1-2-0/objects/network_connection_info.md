# Network Connection Information

> The Network Connection Information object describes characteristics of a network connection.


The Network Connection Information object describes characteristics of a network connection. Defined by D3FEND [d3f:NetworkSession](https://d3fend.mitre.org/dao/artifact/d3f:NetworkSession/).

## Attributes

**`direction_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The connection direction is unknown.
  * `1` - `Inbound`: Inbound network connection. The connection was originated from the Internet or outside network, destined for services on the inside network.
  * `2` - `Outbound`: Outbound network connection. The connection was originated from inside the network, destined for services on the Internet or outside network.
  * `3` - `Lateral`: Lateral network connection. The connection was originated from inside the network, destined for services on the inside network.
  * `99` - `Other`: The direction is not mapped. See the `direction` attribute, which contains a data source specific value.

The normalized identifier of the direction of the initiated connection, traffic, or email.

**`protocol_num`**

* **Type**: `integer_t`
* **Requirement**: recommended

The TCP/IP protocol number, as defined by the Internet Assigned Numbers Authority (IANA). Use -1 if the protocol is not defined by IANA. See [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). For example: `6` for TCP and `17` for UDP.

**`boundary`**

* **Type**: `string_t`
* **Requirement**: optional

The boundary of the connection, normalized to the caption of ‘boundary\_id’. In the case of ‘Other’, it is defined by the event source.

For cloud connections, this translates to the traffic-boundary(same VPC, through IGW, etc.). For traditional networks, this is described as Local, Internal, or External.

**`boundary_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`: The connection boundary is unknown.
  * `1` - `Localhost`: Local network traffic on the same endpoint.
  * `2` - `Internal`: Internal network traffic between two endpoints inside network.
  * `3` - `External`: External network traffic between two endpoints on the Internet or outside the network.
  * `4` - `Same VPC`: Through another resource in the same VPC
  * `5` - `Internet/VPC Gateway`: Through an Internet gateway or a gateway VPC endpoint
  * `6` - `Virtual Private Gateway`: Through a virtual private gateway
  * `7` - `Intra-region VPC`: Through an intra-region VPC peering connection
  * `8` - `Inter-region VPC`: Through an inter-region VPC peering connection
  * `9` - `Local Gateway`: Through a local gateway
  * `10` - `Gateway VPC`: Through a gateway VPC endpoint (Nitro-based instances only)
  * `11` - `Internet Gateway`: Through an Internet gateway (Nitro-based instances only)
  * `99` - `Other`: The boundary is not mapped. See the `boundary` attribute, which contains a data source specific value.

The normalized identifier of the boundary of the connection.

For cloud connections, this translates to the traffic-boundary (same VPC, through IGW, etc.). For traditional networks, this is described as Local, Internal, or External.

**`direction`**

* **Type**: `string_t`
* **Requirement**: optional

The direction of the initiated connection, traffic, or email, normalized to the caption of the direction\_id value. In the case of ‘Other’, it is defined by the event source.

**`protocol_name`**

* **Type**: `string_t`
* **Requirement**: optional

The TCP/IP protocol name in lowercase, as defined by the Internet Assigned Numbers Authority (IANA). See [Protocol Numbers](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml). For example: `tcp` or `udp`.

**`protocol_ver`**

* **Type**: `string_t`
* **Requirement**: optional

The Internet Protocol version.

**`protocol_ver_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`
  * `4` - `Internet Protocol version 4 (IPv4)`
  * `6` - `Internet Protocol version 6 (IPv6)`
  * `99` - `Other`

The Internet Protocol version identifier.

**`session`**

* **Type**: [`session`](session.md)
* **Requirement**: optional

The authenticated user or service session.

**`tcp_flags`**

* **Type**: `integer_t`
* **Requirement**: optional

The network connection TCP header flags (i.e., control bits).

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the connection.

## Used By

* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`http_activity`](../classes/http_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_connection_query`](../classes/network_connection_query.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)