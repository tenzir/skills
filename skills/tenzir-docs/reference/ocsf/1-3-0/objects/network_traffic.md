# Network Traffic

> The Network Traffic object describes characteristics of network traffic.


The Network Traffic object describes characteristics of network traffic. Network traffic refers to data moving across a network at a given point of time. Defined by D3FEND [d3f:NetworkTraffic](https://d3fend.mitre.org/dao/artifact/d3f:NetworkTraffic/).

## Attributes

**`bytes`**

* **Type**: `long_t`
* **Requirement**: recommended

The total number of bytes (in and out).

**`packets`**

* **Type**: `long_t`
* **Requirement**: recommended

The total number of packets (in and out).

**`bytes_in`**

* **Type**: `long_t`
* **Requirement**: optional

The number of bytes sent from the destination to the source.

**`bytes_out`**

* **Type**: `long_t`
* **Requirement**: optional

The number of bytes sent from the source to the destination.

**`chunks`**

* **Type**: `long_t`
* **Requirement**: optional

The total number of chunks (in and out).

**`chunks_in`**

* **Type**: `long_t`
* **Requirement**: optional

The number of chunks sent from the destination to the source.

**`chunks_out`**

* **Type**: `long_t`
* **Requirement**: optional

The number of chunks sent from the source to the destination.

**`packets_in`**

* **Type**: `long_t`
* **Requirement**: optional

The number of packets sent from the destination to the source.

**`packets_out`**

* **Type**: `long_t`
* **Requirement**: optional

The number of packets sent from the source to the destination.

## Used By

* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
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