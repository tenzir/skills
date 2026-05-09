# Finding (finding)

The Finding event is a generic event that defines a set of attributes available in the Findings category.

- **Category**: Findings
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Incident](../profiles/incident.md), [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `class_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `type_uid` (required)
- `message` (recommended)
- `observables` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Create` - A finding was created.
- `2`: `Update` - A finding was updated.
- `3`: `Close` - A finding was closed.

The normalized identifier of the finding activity. Use `1` (Create) when a finding is first generated, `2` (Update) when an existing finding is modified (e.g., severity change, new evidence), and `3` (Close) when a finding is resolved or dismissed.

### `activity_name`

- **Type**: `string_t`

The finding activity name, as defined by the `activity_id`. When `activity_id` is `99` (Other), this must contain the source-specific activity label.

### `comment`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

A user provided comment about the finding.

### `confidence`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The confidence, normalized to the caption of the confidence_id value. In the case of 'Other', it is defined by the event source.

### `confidence_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: context
- **Sibling**: `confidence`

#### Enum values

- `0`: `Unknown` - The normalized confidence is unknown.
- `1`: `Low`
- `2`: `Medium`
- `3`: `High`
- `99`: `Other` - The confidence is not mapped to the defined enum values. See the `confidence` attribute, which contains a data source specific value.

The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

### `confidence_score`

- **Type**: `integer_t`
- **Requirement**: optional
- **Group**: context

The confidence score as reported by the event source.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: optional
- **Group**: context

Describes the affected device/host. If applicable, it can be used in conjunction with `Resource(s)`.

e.g. Specific details about an AWS EC2 instance, that is affected by the Finding.

### `end_time`

- **Type**: `timestamp_t`
- **Requirement**: optional

The time of the most recent event or finding that contributed to this finding.

### `finding_info`

- **Type**: [`finding_info`](../objects/finding_info.md)
- **Requirement**: required
- **Group**: primary

Describes the supporting information about a generated finding.

### `start_time`

- **Type**: `timestamp_t`
- **Requirement**: optional

The time of the earliest event or finding that contributed to this finding.

### `time`

- **Type**: `timestamp_t`

The finding creation time — when the finding was first generated, not when the underlying activity occurred. For the time range of contributing events, use `start_time` and `end_time`.

### `status`

- **Type**: `string_t`
- **Requirement**: optional
- **Group**: context

The finding lifecycle status label, normalized to the caption of the `status_id` value. When `status_id` is `99` (Other), this must contain the source-specific status label.

### `status_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: context
- **Sibling**: `status`

#### Enum values

- `1`: `New` - The Finding is new and yet to be reviewed.
- `2`: `In Progress` - The Finding is under review.
- `3`: `Suppressed` - The Finding was reviewed, determined to be benign or a false positive and is now suppressed.
- `4`: `Resolved` - The Finding was reviewed, remediated and is now considered resolved.
- `5`: `Archived` - The Finding was archived.
- `6`: `Deleted` - The Finding was deleted. For example, it might have been created in error.

The normalized finding lifecycle status identifier. Unlike the status of an activity event, which indicates the success or failure of the activity, finding status tracks the review and triage workflow: whether the finding is new, being investigated, suppressed, or resolved. Producers should set this to reflect the current state of the finding in their system (e.g., `1` for newly created findings, `4` when remediated).

### `vendor_attributes`

- **Type**: [`vendor_attributes`](../objects/vendor_attributes.md)
- **Requirement**: optional
- **Group**: context

The Vendor Attributes object can be used to represent values of attributes populated by the Vendor/Finding Provider. It can help distinguish between the vendor-provided values and consumer-updated values, of key attributes like `severity_id`.
The original finding producer should not populate this object. It should be populated by consuming systems that support data mutability.
