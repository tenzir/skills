# Network Proxy Endpoint (network_proxy)

The network proxy endpoint object describes a proxy server, which acts as an intermediary between a client requesting a resource and the server providing that resource. Defined by D3FEND [d3f:ProxyServer](https://d3fend.mitre.org/dao/artifact/d3f:ProxyServer/).

- **Extends**: [Network Endpoint (network_endpoint)](network_endpoint.md)

## Constraints

- **At least one of**: `ip`, `uid`, `name`, `hostname`, `svc_name`, `instance_uid`, `interface_uid`, `interface_name`
