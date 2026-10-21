# File Remediation Activity (file_remediation_activity)

File Remediation Activity events report on attempts at remediating files. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Sub-techniques will include File, such as File Removal or Restore File.

- **Class UID**: `7002`
- **Category**: Remediation
- **Extends**: [Remediation Activity (remediation_activity)](remediation_activity.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

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

- `7002`: `File Remediation Activity` - File Remediation Activity events report on attempts at remediating files. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/). Sub-techniques will include File, such as File Removal or Restore File.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `700200`: `File Remediation Activity: Unknown`
- `700201`: `File Remediation Activity: Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses. Defined by D3FEND™ [d3f:Isolate](https://d3fend.mitre.org/d3f:Isolate/).
- `700202`: `File Remediation Activity: Evict` - Removes an adversary or malicious resource from a device or computer network. Defined by D3FEND™ [d3f:Evict](https://d3fend.mitre.org/d3f:Evict/).
- `700203`: `File Remediation Activity: Restore` - Returns the system to a better state. Defined by D3FEND™ [d3f:Restore](https://d3fend.mitre.org/d3f:Restore/).
- `700204`: `File Remediation Activity: Harden` - Increases the opportunity cost of computer network exploitation. Defined by D3FEND™ [d3f:Harden](https://d3fend.mitre.org/d3f:Harden/).
- `700299`: `File Remediation Activity: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
