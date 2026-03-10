# Load Balancer

> The load balancer object describes the load balancer entity and contains additional information regarding the distribution of traffic across a network.


The load balancer object describes the load balancer entity and contains additional information regarding the distribution of traffic across a network.

* **Extends**: `_entity`

## Attributes

**`code`**

* **Type**: `integer_t`
* **Requirement**: recommended

The numeric response status code detailing the connection from the load balancer to the destination target.

**`dst_endpoint`**

* **Type**: [`network_endpoint`](network_endpoint.md)
* **Requirement**: recommended

The destination to which the load balancer is distributing traffic.

**`endpoint_connections`**

* **Type**: [`endpoint_connection`](endpoint_connection.md)
* **Requirement**: recommended

An object detailing the load balancer connection attempts and responses.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the load balancer.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier for the load balancer.

**`classification`**

* **Type**: `string_t`
* **Requirement**: optional

The request classification as defined by the load balancer.

**`error_message`**

* **Type**: `string_t`
* **Requirement**: optional

The load balancer error message.

**`ip`**

* **Type**: `ip_t`
* **Requirement**: optional

The IP address of the load balancer node that handled the client request. Note: the load balancer may have other IP addresses, and this is not an IP address of the target/distribution endpoint - see `dst_endpoint`.

**`message`**

* **Type**: `string_t`
* **Requirement**: optional

The load balancer message.

**`metrics`**

* **Type**: [`metric`](metric.md)
* **Requirement**: optional

General purpose metrics associated with the load balancer.

**`status_detail`**

* **Type**: `string_t`
* **Requirement**: optional

The status detail contains additional status information about the load balancer distribution event.

## Constraints

At least one of: `name`, `uid`

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