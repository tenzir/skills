# File Remediation Activity (file_remediation_activity)

File Remediation Activity events report on attempts at remediating files. Sub-techniques of countermeasures will include File, such as File Removal or Restore File.

- **Class UID**: `7002`
- **Category**: Remediation
- **Extends**: [Remediation Activity (remediation_activity)](remediation_activity.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Remediation Activity:**
- `activity_id` (required)
- `command_uid` (required)
- `countermeasures` (recommended)
- `status_id` (recommended)

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

### `file`

- **Type**: [`file`](../objects/file.md)
- **Requirement**: required
- **Group**: primary

The file that pertains to the remediation event.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `7002`: `File Remediation Activity` - File Remediation Activity events report on attempts at remediating files. Sub-techniques of countermeasures will include File, such as File Removal or Restore File.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `700200`: `File Remediation Activity: Unknown`
- `700201`: `File Remediation Activity: Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses.
- `700202`: `File Remediation Activity: Evict` - Removes an adversary or malicious resource from a device or computer network.
- `700203`: `File Remediation Activity: Restore` - Returns the system to a better state.
- `700204`: `File Remediation Activity: Harden` - Increases the opportunity cost of computer network exploitation.
- `700205`: `File Remediation Activity: Detect` - Identify adversary access to or unauthorized activity on computer networks.
- `700206`: `File Remediation Activity: Deceive` - Advertise, entice, and allow potential attackers access to an observed or controlled environment.
- `700299`: `File Remediation Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
