# Live Evidence Info (evidence_info)

Data collected directly from devices that represents forensic information pulled, queried, or discovered from devices that may indicate malicious activity. It contains a number of child objects, each representing a distinct evidence domain (network connections, file artifacts, registry entries, etc.). When mapping raw telemetry data users should select Query Evidence and then the appropriate child object that best matches the evidence type.

- **Class UID**: `5040`
- **Category**: Discovery
- **Extends**: [Discovery Result (discovery_result)](discovery_result.md)
- **Profiles**: [Cloud](../profiles/cloud.md), [Date/Time](../profiles/datetime.md), [Host](../profiles/host.md), [OSINT](../profiles/osint.md), [Security Control](../profiles/security_control.md)

## Inherited attributes

**From Discovery Result:**
- `activity_id` (required)
- `query_result_id` (required)
- `query_info` (recommended)
- `query_result` (recommended)

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

### `device`

- **Type**: [`device`](../objects/device.md)
- **Requirement**: required
- **Group**: primary

An addressable device, computer system or host from which evidence was collected.

### `query_evidence`

- **Type**: [`query_evidence`](../objects/query_evidence.md)
- **Requirement**: required
- **Group**: primary

The specific resulting evidence information that was queried or discovered based on the query type. Contains various child objects corresponding to the query_type_id values.

### `class_uid`

- **Type**: `integer_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `class_name`

#### Enum values

- `5040`: `Live Evidence Info` - Data collected directly from devices that represents forensic information pulled, queried, or discovered from devices that may indicate malicious activity. It contains a number of child objects, each representing a distinct evidence domain (network connections, file artifacts, registry entries, etc.). When mapping raw telemetry data users should select Query Evidence and then the appropriate child object that best matches the evidence type.

The unique identifier of a class. A class describes the attributes available in an event.

### `type_uid`

- **Type**: `long_t`
- **Requirement**: required
- **Group**: classification
- **Sibling**: `type_name`

#### Enum values

- `504000`: `Live Evidence Info: Unknown`
- `504001`: `Live Evidence Info: Query` - The discovered results are via a query request.
- `504099`: `Live Evidence Info: Other`

The event/finding type ID. It identifies the event's semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.
