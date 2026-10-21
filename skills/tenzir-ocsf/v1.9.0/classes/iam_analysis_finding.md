# IAM Analysis Finding (iam_analysis_finding)

This finding represents an IAM analysis result, which evaluates IAM policies, access patterns, and IAM configurations for potential security risks. The analysis can focus on either an identity (user, role, service account) or a resource to assess permissions, access patterns, and security posture within the IAM domain.
Note: Use `permission_analysis_results` for identity-centric analysis (evaluating what an identity can do) and `access_analysis_result` for resource-centric analysis (evaluating who can access a resource). These complement each other for comprehensive IAM security assessment.
Note: If the Finding is an incident, i.e. requires incident workflow, also apply the `incident` profile or aggregate this finding into an `Incident Finding`.

- **Class UID**: `2008`
- **Category**: Findings
- **Extends**: [Finding (finding)](finding.md)
- **Profiles**: [Incident](../profiles/incident.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Constraints

- **At least one of**: `access_analysis_result`, `applications`, `identity_activity_metrics`, `permission_analysis_results`

## Inherited attributes

**From Finding:**
- `activity_id` (required)
- `finding_info` (required)
- `time` (required)
- `confidence_id` (recommended)
- `status_id` (recommended)

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `message` (recommended)
- `observables` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `access_analysis_result`

- **Type**: [`access_analysis_result`](../objects/access_analysis_result.md)
- **Requirement**: optional
- **Group**: context

Describes access relationships and pathways between identities, resources, focusing on who can access what and through which mechanisms. This evaluates access levels (read/write/admin), access types (direct, cross-account, public, federated), and the conditions under which access is granted. Use this for resource-centric security assessments such as external access discovery, public exposure analysis, etc.

### `applications`

- **Type**: [`application`](../objects/application.md)
- **Requirement**: recommended
- **Group**: primary

Details about applications, services, or systems that are accessible based on the IAM analysis. For identity-centric analysis, this represents applications the identity can access. For resource-centric analysis, this represents applications that can access the resource.

### `identity_activity_metrics`

- **Type**: [`identity_activity_metrics`](../objects/identity_activity_metrics.md)
- **Requirement**: recommended
- **Group**: primary

Describes usage activity and other metrics of an Identity i.e. AWS IAM User, GCP IAM Principal, etc.

### `permission_analysis_results`

- **Type**: [`permission_analysis_result`](../objects/permission_analysis_result.md)
- **Requirement**: recommended
- **Group**: primary

Describes analysis results of permissions, policies directly associated with an identity (user, role, or service account). This evaluates what permissions an identity has been granted through attached policies, which privileges are actively used versus unused, and identifies potential over-privileged access. Use this for identity-centric security assessments such as privilege audits, dormant permission discovery, and least-privilege compliance analysis.

### `remediation`

- **Type**: [`remediation`](../objects/remediation.md)
- **Requirement**: optional
- **Group**: context

Describes the recommended remediation steps to address identified issue(s).

### `resources`

- **Type**: [`resource_details`](../objects/resource_details.md)
- **Requirement**: recommended
- **Group**: primary

Details about resources involved in the IAM analysis. For identity-centric analysis, this represents resources the identity can access. For resource-centric analysis, this represents the resource being analyzed and related resources in the access chain.

### `user`

- **Type**: [`user`](../objects/user.md)
- **Requirement**: recommended
- **Group**: primary

Details about the identity (user, role, service account, or other principal) that is the subject of the IAM analysis. This provides context about the identity being evaluated for security risks and access patterns.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `2008`: `IAM Analysis Finding` - This finding represents an IAM analysis result, which evaluates IAM policies, access patterns, and IAM configurations for potential security risks. The analysis can focus on either an identity (user, role, service account) or a resource to assess permissions, access patterns, and security posture within the IAM domain. Note: Use `permission_analysis_results` for identity-centric analysis (evaluating what an identity can do) and `access_analysis_result` for resource-centric analysis (evaluating who can access a resource). These complement each other for comprehensive IAM security assessment. Note: If the Finding is an incident, i.e. requires incident workflow, also apply the `incident` profile or aggregate this finding into an `Incident Finding`.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `200800`: `IAM Analysis Finding: Unknown`
- `200801`: `IAM Analysis Finding: Create` - A finding was created.
- `200802`: `IAM Analysis Finding: Update` - A finding was updated.
- `200803`: `IAM Analysis Finding: Close` - A finding was closed.
- `200899`: `IAM Analysis Finding: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
