# Network Proxy Endpoint (network_proxy)

The network proxy endpoint object describes a proxy server, which acts as an intermediary between a client requesting a resource and the server providing that resource.

- **Extends**: [Network Endpoint (network_endpoint)](network_endpoint.md)
- **Profiles**: [Container](../profiles/container.md)
- **Observable**: `20`

## Constraints

- **At least one of**: `ip`, `uid`, `name`, `hostname`, `svc_name`, `instance_uid`, `interface_uid`, `interface_name`, `domain`

## Inherited attributes

**From Network Endpoint:**
- `port` (recommended)
- `svc_name` (recommended)
- `type_id` (recommended)
- `uid` (recommended)

**From Endpoint:**
- `hostname` (recommended)
- `instance_uid` (recommended)
- `interface_name` (recommended)
- `interface_uid` (recommended)
- `ip` (recommended)
- `name` (recommended)
- `owner` (recommended)
