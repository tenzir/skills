# `Duration`

- **Schema occurrences**: `2`
- **Raw fragment/source occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Alias` | `integer` |  |  | local |
| [Dns](../schemas/dns.md) | `Alias` | `integer` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDHCPEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### Dhcp

#### `Duration`

- **Class**: `Alias`
- **Type**: `integer`
- **Aliases**: [`DhcpSessionDuration`](../fields/dhcp_session_duration.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to DhcpSessionDuration

### Dns

#### `Duration`

- **Class**: `Alias`
- **Type**: `integer`
- **Aliases**: [`DnsNetworkDuration`](../fields/dns_network_duration.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to DnsNetworkDuration
