# Network Proxy (network_proxy)

The attributes that identify network proxy attributes.

## Attributes

### `proxy_connection_info`

- **Type**: `network_connection_info`
- **Requirement**: recommended

The connection information from the proxy server to the remote server.

### `proxy_endpoint`

- **Type**: `network_proxy`
- **Requirement**: optional

The proxy (server) in a network connection.

### `proxy_http_request`

- **Type**: `http_request`
- **Requirement**: optional

The HTTP Request from the proxy server to the remote server.

### `proxy_http_response`

- **Type**: `http_response`
- **Requirement**: optional

The HTTP Response from the remote server to the proxy server.

### `proxy_tls`

- **Type**: `tls`
- **Requirement**: recommended

The TLS protocol negotiated between the proxy server and the remote server.

### `proxy_traffic`

- **Type**: `network_traffic`
- **Requirement**: recommended

The network traffic refers to the amount of data moving across a network, from proxy to remote server at a given point of time.
