# File Remediation Activity (file_remediation_activity)

File Remediation Activity events report on attempts at remediating files. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Sub-techniques will include File, such as File Removal or Restore File.

- **UID**: `2`
- **Category**: Remediation
- **Extends**: `remediation_activity`

## Attributes

### `file`

- **Type**: `file`
- **Requirement**: required
- **Group**: primary

The file that pertains to the remediation event.
