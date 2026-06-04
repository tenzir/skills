# `ThreatIpAddr`

- **Schema occurrences**: `2`
- **Raw fragment/source occurrences**: `2`

## Schema occurrences

| Schema | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [AuditEvent](../schemas/audit_event.md) | `Optional` | `string` | `IP Address` |  | local |
| [Dns](../schemas/dns.md) | `Optional` | `string` | `IP Address` |  | local |

## Raw sources

- `ASIM/schemas/ASimAuditEvent.yaml`
- `ASIM/schemas/ASimDns.yaml`

## Details by schema

### AuditEvent

#### `ThreatIpAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatFilePath represents.

### Dns

#### `ThreatIpAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Local: `ASIM/schemas/ASimDns.yaml`

An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatFilePath represents.
