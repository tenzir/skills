# `Hostname`

- **Schema occurrences**: `3`
- **Raw fragment/source occurrences**: `3`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [Dhcp](../schemas/dhcp.md) | `Alias` | `string` |  |  | local |
| [Dns](../schemas/dns.md) | `Alias` | `string` |  |  | local |
| [User Management](../schemas/user_management.md) | `Alias` | `string` |  |  | local |

## Raw sources

- `ASIM/schemas/ASimDHCPEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`
- `ASIM/schemas/ASimUserManagement.yaml`

## Details by schema

### Dhcp

#### `Hostname`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcHostname`](../fields/src_hostname.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to SrcHostname

### Dns

#### `Hostname`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcHostname`](../fields/src_hostname.md)

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

Alias to SrcHostname

### User Management

#### `Hostname`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcHostname`](../fields/dvc_hostname.md)

#### Provenance

- Local: `ASIM/schemas/ASimUserManagement.yaml`

Alias to DvcHostname
