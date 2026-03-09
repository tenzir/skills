# Live Evidence Info (evidence_info)

Data collected directly from devices that represents forensic information pulled, queried, or discovered from devices that may indicate malicious activity. It contains a number of child objects, each representing a distinct evidence domain (network connections, file artifacts, registry entries, etc.). When mapping raw telemetry data users should select Query Evidence and then the appropriate child object that best matches the evidence type.

- **UID**: `40`
- **Category**: Discovery
- **Extends**: `discovery_result`

## Attributes

### `device`

- **Type**: `device`
- **Requirement**: required
- **Group**: primary

An addressable device, computer system or host from which evidence was collected.

### `query_evidence`

- **Type**: `query_evidence`
- **Requirement**: required
- **Group**: primary

The specific resulting evidence information that was queried or discovered based on the query type. Contains various child objects corresponding to the query_type_id values.
