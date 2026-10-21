# Compliance Finding (compliance_finding)

Compliance Finding events describe results of evaluations performed against resources, to check compliance with various Industry Frameworks or Security Standards such as `NIST SP 800-53, CIS AWS Foundations Benchmark v1.4.0, ISO/IEC 27001` etc.

- **Class UID**: `2003`
- **Category**: Findings
- **Extends**: [Finding (finding)](finding.md)
- **Profiles**: [Host](../profiles/host.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md)

## Inherited attributes

**From Finding:**
- `activity_id` (required)
- `finding_info` (required)
- `confidence_id` (recommended)
- `status_id` (recommended)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `compliance`

- **Type**: [`compliance`](../objects/compliance.md)
- **Requirement**: required
- **Group**: primary

The compliance object provides context to compliance findings (e.g., a check against a specific regulatory or best practice framework such as CIS, NIST etc.) and contains compliance related details.

### `remediation`

- **Type**: [`remediation`](../objects/remediation.md)
- **Requirement**: recommended
- **Group**: context

Describes the recommended remediation steps to address identified issue(s).

### `resource`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

Describes details about the resource that is the subject of the compliance check.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `2003`: `Compliance Finding` - Compliance Finding events describe results of evaluations performed against resources, to check compliance with various Industry Frameworks or Security Standards such as `NIST SP 800-53, CIS AWS Foundations Benchmark v1.4.0, ISO/IEC 27001` etc.

The unique identifier of a class. A Class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `200300`: `Compliance Finding: Unknown`
- `200301`: `Compliance Finding: Create` - A finding was created.
- `200302`: `Compliance Finding: Update` - A finding was updated.
- `200303`: `Compliance Finding: Close` - A finding was closed.
- `200399`: `Compliance Finding: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
