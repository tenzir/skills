# Network Proxy

> The attributes that identify network proxy attributes.


The attributes that identify network proxy attributes.

## Attributes

**`proxy_connection_info`**

* **Type**: [`network_connection_info`](../objects/network_connection_info.md)
* **Requirement**: recommended

The connection information from the proxy server to the remote server.

**`proxy_tls`**

* **Type**: [`tls`](../objects/tls.md)
* **Requirement**: recommended

The TLS protocol negotiated between the proxy server and the remote server.

**`proxy_traffic`**

* **Type**: [`network_traffic`](../objects/network_traffic.md)
* **Requirement**: recommended

The network traffic refers to the amount of data moving across a network, from proxy to remote server at a given point of time.

**`proxy_endpoint`**

* **Type**: [`network_proxy`](../objects/network_proxy.md)
* **Requirement**: optional

The proxy (server) in a network connection.

**`proxy_http_request`**

* **Type**: [`http_request`](../objects/http_request.md)
* **Requirement**: optional

The HTTP Request from the proxy server to the remote server.

**`proxy_http_response`**

* **Type**: [`http_response`](../objects/http_response.md)
* **Requirement**: optional

The HTTP Response from the remote server to the proxy server.

## Available In

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
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)