# Remediation Activity (remediation_activity)

Remediation Activity events report on attempts at remediating a compromised device or computer network.

- **Class UID**: `7001`
- **Category**: Remediation
- **Extends**: [Base Event (base_event)](base_event.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

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
- `1`: `Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses.
- `2`: `Evict` - Removes an adversary or malicious resource from a device or computer network.
- `3`: `Restore` - Returns the system to a better state.
- `4`: `Harden` - Increases the opportunity cost of computer network exploitation.
- `5`: `Detect` - Identify adversary access to or unauthorized activity on computer networks.
- `6`: `Deceive` - Advertise, entice, and allow potential attackers access to an observed or controlled environment.
- `99`: `Other` - The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

Matches the countermeasure tactic. Note: the Model tactic is not supported by the OCSF Remediation event class.

### `command_uid`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

The unique identifier of the remediation command that pertains to this event.

### `countermeasures`

- **Type**: [`d3fend`](../objects/d3fend.md)
- **Requirement**: recommended
- **Group**: primary

The MITRE D3FEND™ Matrix Countermeasures associated with a remediation.

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
- `1`: `Success` - The activity completed successfully.
- `2`: `Failure` - The activity failed.
- `3`: `Does Not Exist` - The target of the remediation does not exist.
- `4`: `Partial` - The remediation was partially completed.
- `5`: `Unsupported` - The remediation was not supported.
- `6`: `Error` - There was an error during the remediation process.
- `99`: `Other` - The status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized status of the event outcome. Use this family of attributes to convey the outcome of the activity described by the event. Producers should map their source outcome to `1` (Success) or `2` (Failure). Use `0` (Unknown) when the outcome cannot be determined, and `99` (Other) with a populated `status` string when the source value does not map cleanly.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `7001`: `Remediation Activity` - Remediation Activity events report on attempts at remediating a compromised device or computer network.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `700100`: `Remediation Activity: Unknown`
- `700101`: `Remediation Activity: Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses.
- `700102`: `Remediation Activity: Evict` - Removes an adversary or malicious resource from a device or computer network.
- `700103`: `Remediation Activity: Restore` - Returns the system to a better state.
- `700104`: `Remediation Activity: Harden` - Increases the opportunity cost of computer network exploitation.
- `700105`: `Remediation Activity: Detect` - Identify adversary access to or unauthorized activity on computer networks.
- `700106`: `Remediation Activity: Deceive` - Advertise, entice, and allow potential attackers access to an observed or controlled environment.
- `700199`: `Remediation Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
