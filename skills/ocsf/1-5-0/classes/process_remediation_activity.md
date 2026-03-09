# Process Remediation Activity (process_remediation_activity)

Process Remediation Activity events report on attempts at remediating processes. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Sub-techniques will include Process, such as Process Termination or Kernel-based Process Isolation.

- **UID**: `3`
- **Category**: Remediation
- **Extends**: `remediation_activity`

## Attributes

### `process`

- **Type**: `process`
- **Requirement**: required
- **Group**: primary

The process that pertains to the remediation event.
