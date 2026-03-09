# Remediation Activity (remediation_activity)

Remediation Activity events report on attempts at remediating a compromised device or computer network. It follows the MITRE countermeasures defined by the D3FEND™ [Matrix](https://d3fend.mitre.org/).

- **UID**: `1`
- **Category**: Remediation
- **Extends**: `base_event`

## Attributes

### `$include`

### `activity_id`

- **Type**: `integer_t`
- **Sibling**: `activity_name`

#### Enum values

- `1`: `Isolate` - Creates logical or physical barriers in a system which reduces opportunities for adversaries to create further accesses. Defined by D3FEND™ [d3f:Isolate](https://d3fend.mitre.org/d3f:Isolate/).
- `2`: `Evict` - Removes an adversary or malicious resource from a device or computer network. Defined by D3FEND™ [d3f:Evict](https://d3fend.mitre.org/d3f:Evict/).
- `3`: `Restore` - Returns the system to a better state. Defined by D3FEND™ [d3f:Restore](https://d3fend.mitre.org/d3f:Restore/).
- `4`: `Harden` - Increases the opportunity cost of computer network exploitation. Defined by D3FEND™ [d3f:Harden](https://d3fend.mitre.org/d3f:Harden/).

Matches the MITRE D3FEND™ Tactic. Note: the Model and Detect Tactics are not supported as remediations by the OCSF Remediation event class.

### `command_uid`

- **Type**: `string_t`
- **Requirement**: required
- **Group**: primary

The unique identifier of the remediation command that pertains to this event.

### `countermeasures`

- **Type**: `d3fend`
- **Requirement**: recommended
- **Group**: primary

The MITRE DEFEND™ Matrix Countermeasures associated with a remediation.

### `remediation`

- **Type**: `remediation`
- **Requirement**: optional
- **Group**: context

Describes the recommended remediation steps to address identified issue(s).

### `scan`

- **Type**: `scan`
- **Requirement**: optional
- **Group**: context

The remediation scan that pertains to this event.

### `status_id`

- **Type**: `integer_t`
- **Sibling**: `status`

#### Enum values

- `3`: `Does Not Exist` - The target of the remediation does not exist.
- `4`: `Partial` - The remediation was partially completed.
- `5`: `Unsupported` - The remediation was not supported.
- `6`: `Error` - There was an error during the remediation process.

The normalized identifier of the event status.
