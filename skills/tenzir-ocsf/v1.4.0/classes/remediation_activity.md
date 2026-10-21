# Remediation Activity (remediation_activity)

Remediation Activity events report on attempts at remediating a compromised device or computer network. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/).

- **Class UID**: `7001`
- **Category**: Remediation
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Base Event:**
- `category_uid` (required)
- `metadata` (required)
- `severity_id` (required)
- `time` (required)
- `message` (recommended)
- `observables` (recommended)
- `status` (recommended)
- `status_code` (recommended)
- `status_detail` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `activity_id`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `activity_name`

#### Enum values

- `0`: `Unknown` - The event activity is unknown.
- `1`: `Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses. Defined by D3FEND™ [d3f:Isolate](https://d3fend.mitre.org/d3f:Isolate/).
- `2`: `Evict` - Removes an adversary or malicious resource from a device or computer network. Defined by D3FEND™ [d3f:Evict](https://d3fend.mitre.org/d3f:Evict/).
- `3`: `Restore` - Returns the system to a better state. Defined by D3FEND™ [d3f:Restore](https://d3fend.mitre.org/d3f:Restore/).
- `4`: `Harden` - Increases the opportunity cost of computer network exploitation. Defined by D3FEND™ [d3f:Harden](https://d3fend.mitre.org/d3f:Harden/).
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

Matches the MITRE D3FEND™ Tactic. Note: the Model and Detect Tactics are not supported as remediations by the OCSF Remediation event class.

### `command_uid`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

The unique identifier of the remediation command that pertains to this event.

### `countermeasures`

- **Type**: [`d3fend`](../objects/d3fend.md)
- **Requirement**: recommended
- **Group**: primary

The MITRE DEFEND™ Matrix Countermeasures associated with a remediation.

### `remediation`

- **Type**: [`remediation`](../objects/remediation.md)
- **Requirement**: optional
- **Group**: context

Describes the recommended remediation steps to address identified issue(s).

### `scan`

- **Type**: [`scan`](../objects/scan.md)
- **Requirement**: optional
- **Group**: context

The remediation scan that pertains to this event.

### `status_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `status`

#### Enum values

- `0`: `Unknown` - The status is unknown.
- `1`: `Success`
- `2`: `Failure`
- `3`: `Does Not Exist` - The target of the remediation does not exist.
- `4`: `Partial` - The remediation was partially completed.
- `5`: `Unsupported` - The remediation was not supported.
- `6`: `Error` - There was an error during the remediation process.
- `99`: `Other` - The event status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized identifier of the event status.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `7001`: `Remediation Activity` - Remediation Activity events report on attempts at remediating a compromised device or computer network. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/).

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `700100`: `Remediation Activity: Unknown`
- `700101`: `Remediation Activity: Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses. Defined by D3FEND™ [d3f:Isolate](https://d3fend.mitre.org/d3f:Isolate/).
- `700102`: `Remediation Activity: Evict` - Removes an adversary or malicious resource from a device or computer network. Defined by D3FEND™ [d3f:Evict](https://d3fend.mitre.org/d3f:Evict/).
- `700103`: `Remediation Activity: Restore` - Returns the system to a better state. Defined by D3FEND™ [d3f:Restore](https://d3fend.mitre.org/d3f:Restore/).
- `700104`: `Remediation Activity: Harden` - Increases the opportunity cost of computer network exploitation. Defined by D3FEND™ [d3f:Harden](https://d3fend.mitre.org/d3f:Harden/).
- `700199`: `Remediation Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
