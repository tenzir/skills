# Network Proxy Endpoint

> The network proxy endpoint object describes a proxy server, which acts as an intermediary between a client requesting a resource and the server providing that resource.


The network proxy endpoint object describes a proxy server, which acts as an intermediary between a client requesting a resource and the server providing that resource.

* **Extends**: `network_endpoint`

## Attributes

**`container`**

* **Type**: [`container`](container.md)
* **Requirement**: recommended

The information describing an instance of a container. A container is a prepackaged, portable system image that runs isolated on an existing system using a container runtime like containerd.

**`hostname`**

* **Type**: `hostname_t`
* **Requirement**: recommended

The fully qualified name of the endpoint.

**`instance_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of a VM instance.

**`interface_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the network interface (e.g. eth2).

**`interface_uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the network interface.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: recommended

The IP address of the endpoint, in either IPv4 or IPv6 format.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The short name of the endpoint.

**`namespace_pid`**

* **Type**: `integer_t`
* **Requirement**: recommended

If running under a process namespace (such as in a container), the process identifier within that process namespace.

**`owner`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The identity of the service or user account that owns the endpoint or was last logged into it.

**`port`**

* **Type**: `port_t`
* **Requirement**: recommended

The port used for communication within the network connection.

**`svc_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The service name in service-to-service connections. For example, AWS VPC logs the pkt-src-aws-service and pkt-dst-aws-service fields identify the connection is coming from or going to an AWS service.

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Server`: A [server](https://d3fend.mitre.org/dao/artifact/d3f:Server/).
  * `2` - `Desktop`: A [desktop computer](https://d3fend.mitre.org/dao/artifact/d3f:DesktopComputer/).
  * `3` - `Laptop`: A [laptop computer](https://d3fend.mitre.org/dao/artifact/d3f:LaptopComputer/).
  * `4` - `Tablet`: A [tablet computer](https://d3fend.mitre.org/dao/artifact/d3f:TabletComputer/).
  * `5` - `Mobile`: A [mobile phone](https://d3fend.mitre.org/dao/artifact/d3f:MobilePhone/).
  * `6` - `Virtual`: A [virtual machine](https://d3fend.mitre.org/dao/artifact/d3f:VirtualizationSoftware/).
  * `7` - `IOT`: An [IOT (Internet of Things) device](https://www.techtarget.com/iotagenda/definition/IoT-device).
  * `8` - `Browser`: A [web browser](https://d3fend.mitre.org/dao/artifact/d3f:Browser/).
  * `9` - `Firewall`: A [networking firewall](https://d3fend.mitre.org/dao/artifact/d3f:Firewall/).
  * `10` - `Switch`: A [networking switch](https://d3fend.mitre.org/dao/artifact/d3f:Switch/).
  * `11` - `Hub`: A [networking hub](https://en.wikipedia.org/wiki/Ethernet_hub).
  * `12` - `Router`: A [networking router](https://d3fend.mitre.org/dao/artifact/d3f:Router/).
  * `13` - `IDS`: An [intrusion detection system](https://d3fend.mitre.org/dao/artifact/d3f:IntrusionDetectionSystem/).
  * `14` - `IPS`: An [intrusion prevention system](https://d3fend.mitre.org/dao/artifact/d3f:IntrusionPreventionSystem/).
  * `15` - `Load Balancer`: A [Load Balancer device.](https://en.wikipedia.org/wiki/Load_balancing_\(computing\))
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The network endpoint type ID.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the endpoint.

**`agent_list`**

* **Type**: [`agent`](agent.md)
* **Requirement**: optional

A list of `agent` objects associated with a device, endpoint, or resource.

**`autonomous_system`**

* **Type**: [`autonomous_system`](autonomous_system.md)
* **Requirement**: optional

The Autonomous System details associated with an IP address.

**`domain`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the domain that the endpoint belongs to or that corresponds to the endpoint.

**`hw_info`**

* **Type**: [`device_hw_info`](device_hw_info.md)
* **Requirement**: optional

The endpoint hardware information.

**`intermediate_ips`**

* **Type**: `ip_t`
* **Requirement**: optional

The intermediate IP Addresses. For example, the IP addresses in the HTTP X-Forwarded-For header.

**`isp`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the Internet Service Provider (ISP).

**`isp_org`**

* **Type**: `string_t`
* **Requirement**: optional

The organization name of the Internet Service Provider (ISP). This represents the parent organization or company that owns/operates the ISP. For example, Comcast Corporation would be the ISP org for Xfinity internet service. This attribute helps identify the ultimate provider when ISPs operate under different brand names.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: optional

The geographical location of the endpoint.

**`mac`**

* **Type**: `mac_t`
* **Requirement**: optional

The Media Access Control (MAC) address of the endpoint.

**`network_scope`**

* **Type**: `string_t`
* **Requirement**: optional

Indicates whether the endpoint resides inside the customer’s network, outside on the Internet, or if its location relative to the customer’s network cannot be determined. The value is normalized to the caption of the `network_scope_id`.

**`network_scope_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`: Unknown whether this endpoint resides within the customer’s network.
  * `1` - `Internal`: The endpoint resides inside the customer’s network.
  * `2` - `External`: The endpoint is on the Internet or otherwise external to the customer’s network.
  * `99` - `Other`: The network scope is not mapped. See the `network_scope` attribute, which contains a data source specific value.

The normalized identifier of the endpoint’s network scope. The normalized network scope identifier indicates whether the endpoint resides inside the customer’s network, outside on the Internet, or if its location relative to the customer’s network cannot be determined.

**`os`**

* **Type**: [`os`](os.md)
* **Requirement**: optional

The endpoint operating system.

**`proxy_endpoint`**

* **Type**: [`network_proxy`](network_proxy.md)
* **Requirement**: optional

The network proxy information pertaining to a specific endpoint. This can be used to describe information pertaining to network address translation (NAT).

**`subnet_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of a virtual subnet.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The network endpoint type. For example: `unknown`, `server`, `desktop`, `laptop`, `tablet`, `mobile`, `virtual`, `browser`, or `other`.

**`vlan_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The Virtual LAN identifier.

**`vpc_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the Virtual Private Cloud (VPC).

**`zone`**

* **Type**: `string_t`
* **Requirement**: optional

The network zone or LAN segment.

## Constraints

At least one of: `ip`, `uid`, `name`, `hostname`, `svc_name`, `instance_uid`, `interface_uid`, `interface_name`, `domain`

## Used By

* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`http_activity`](../classes/http_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)