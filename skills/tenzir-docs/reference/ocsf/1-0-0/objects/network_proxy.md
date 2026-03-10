# Network Proxy Endpoint

> The Network Proxy Endpoint describes characteristics of a network proxy.


The Network Proxy Endpoint describes characteristics of a network proxy. Defined by D3FEND [d3f:ProxyServer](https://d3fend.mitre.org/dao/artifact/d3f:ProxyServer/).

* **Extends**: `network_endpoint`

## Attributes

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

**`port`**

* **Type**: `port_t`
* **Requirement**: recommended

The port used for communication within the network connection.

**`svc_name`**

* **Type**: `string_t`
* **Requirement**: recommended

The service name in service-to-service connections. For example, AWS VPC logs the pkt-src-aws-service and pkt-dst-aws-service fields identify the connection is coming from or going to an AWS service.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the endpoint.

**`domain`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the domain.

**`intermediate_ips`**

* **Type**: `ip_t`
* **Requirement**: optional

The intermediate IP Addresses. For example, the IP addresses in the HTTP X-Forwarded-For header.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: optional

The geographical location of the endpoint.

**`mac`**

* **Type**: `mac_t`
* **Requirement**: optional

The Media Access Control (MAC) address of the endpoint.

**`subnet_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of a virtual subnet.

**`vlan_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The Virtual LAN identifier.

**`vpc_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the Virtual Private Cloud (VPC).

## Constraints

At least one of: `ip`, `uid`, `name`, `hostname`, `svc_name`, `instance_uid`, `interface_uid`, `interface_name`

## Used By

* [`dns_activity`](../classes/dns_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`http_activity`](../classes/http_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)