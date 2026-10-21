# Device Config State (config_state)

Device Config State events report device configuration data, device assessments, and/or CIS Benchmark results.

> **Deprecated since v1.5.0.** Use `compliance_finding` class.

- **Class UID**: `5002`
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

### `assessments`

- **Type**: [`assessment`](../objects/assessment.md)
- **Requirement**: optional
- **Group**: context

A list of assessments associated with the device.

### `cis_benchmark_result`

- **Type**: [`cis_benchmark_result`](../objects/cis_benchmark_result.md)
- **Requirement**: recommended
- **Group**: primary

> **Deprecated since v1.5.0.** Use the `compliance.checks` attribute instead.

The CIS Benchmark Result object captures results generated from benchmark evaluations as defined by the Center for Internet Security.

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

The device that is being discovered by an inventory process.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5002`: `Device Config State` - Device Config State events report device configuration data, device assessments, and/or CIS Benchmark results.

The unique identifier of a class. A class describes the attributes available in an event. Producers and mappers must set this to the `uid` defined in the event class definition. For example, `Detection Finding` is `2004`.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `500200`: `Device Config State: Unknown`
- `500201`: `Device Config State: Log` - The discovered information is via a log.
- `500202`: `Device Config State: Collect` - The discovered information is via a collection process.
- `500299`: `Device Config State: Other`

The event/finding type ID. It identifies the event's semantics and structure. Producers and mappers must compute this as `class_uid * 100 + activity_id`. It uniquely identifies the combination of event class and activity across the entire schema. For example, `Detection Finding: Create` is `200401`.
