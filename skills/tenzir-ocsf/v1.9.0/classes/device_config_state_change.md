# Device Config State Change (device_config_state_change)

Device Config State Change events report state changes that impact the security of the device.

- **Class UID**: `5019`
- **Category**: Discovery
- **Extends**: [Discovery (discovery)](discovery.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Record Integrity](../profiles/record_integrity.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Discovery:**
- `activity_id` (required)

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
- `status_id` (recommended)
- `timezone_offset` (recommended)

## Attributes

### `actor`

- **Type**: [`actor`](../objects/actor.md)
- **Requirement**: optional
- **Group**: context

The user, process, or service that initiated the activity on the host. For system-level events this is typically a process; for IAM events it is typically a user or role.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

The device that is impacted by the state change.

### `prev_security_level`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The previous security level of the entity

### `prev_security_level_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `prev_security_level`

#### Enum values

- `0`: `Unknown`
- `1`: `Secure`
- `2`: `At Risk`
- `3`: `Compromised`
- `99`: `Other` - The security level is not mapped. See the `prev_security_level` attribute, which contains data source specific values.

The previous security level of the entity

### `prev_security_states`

- **Type**: [`security_state`](../objects/security_state.md)
- **Requirement**: recommended
- **Group**: primary

The previous security states of the device.

### `security_level`

- **Type**: `string_t`
- **Requirement**: recommended
- **Group**: primary

The current security level of the entity

### `security_level_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Group**: primary
- **Sibling**: `security_level`

#### Enum values

- `0`: `Unknown`
- `1`: `Secure`
- `2`: `At Risk`
- `3`: `Compromised`
- `99`: `Other` - The security level is not mapped. See the `security_level` attribute, which contains data source specific values.

The current security level of the entity

### `security_states`

- **Type**: [`security_state`](../objects/security_state.md)
- **Requirement**: recommended
- **Group**: primary

The current security states of the device.

### `state`

- **Type**: `string_t`
- **Requirement**: optional

The Config Change Stat, normalized to the caption of the state_id value. In the case of 'Other', it is defined by the source.

### `state_id`

- **Type**: `integer_t`
- **Requirement**: recommended
- **Sibling**: `state`

#### Enum values

- `0`: `Unknown` - The Config Change state is unknown.
- `1`: `Disabled` - Config State Changed to Disabled.
- `2`: `Enabled` - Config State Changed to Enabled.
- `99`: `Other` - The Config Change is not mapped. See the `state` attribute, which contains data source specific values.

The Config Change State of the managed entity.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5019`: `Device Config State Change` - Device Config State Change events report state changes that impact the security of the device.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `501900`: `Device Config State Change: Unknown`
- `501901`: `Device Config State Change: Log` - The discovered information is via a log.
- `501902`: `Device Config State Change: Collect` - The discovered information is via a collection process.
- `501999`: `Device Config State Change: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
