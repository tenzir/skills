# Network Remediation Activity (network_remediation_activity)

Network Remediation Activity events report on attempts at remediating computer networks. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Techniques and Sub-techniques will include Network, such as Network Isolation or Network Traffic Filtering.

- **UID**: `4`
- **Category**: Remediation
- **Extends**: `remediation_activity`

## Attributes

### `connection_info`

- **Type**: `network_connection_info`
- **Requirement**: required
- **Group**: primary

The network connection that pertains to the remediation event.
