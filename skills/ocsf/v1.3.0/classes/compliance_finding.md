# Compliance Finding (compliance_finding)

Compliance Finding events describe results of evaluations performed against resources, to check compliance with various Industry Frameworks or Security Standards such as `NIST SP 800-53, CIS AWS Foundations Benchmark v1.4.0, ISO/IEC 27001` etc.

- **UID**: `3`
- **Category**: Findings
- **Extends**: `finding`

## Attributes

### `compliance`

- **Type**: `compliance`
- **Requirement**: required
- **Group**: primary

The compliance object provides context to compliance findings (e.g., a check against a specific regulatory or best practice framework such as CIS, NIST etc.) and contains compliance related details.

### `remediation`

- **Type**: `remediation`
- **Requirement**: recommended
- **Group**: context

Describes the recommended remediation steps to address identified issue(s).

### `resource`

- **Type**: `resource_details`
- **Requirement**: recommended
- **Group**: primary

Describes details about the resource that is the subject of the compliance check.

### `resources`

- **Type**: `resource_details`
- **Requirement**: recommended
- **Group**: primary

Describes details about the resource/resouces that are the subject of the compliance check.
