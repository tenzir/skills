# ASimInspectionFields

- **Source**: [`ASIM/schemas/common/ASimInspectionFields.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/common/ASimInspectionFields.yaml)
- **Fields**: `14`

## Included by

- [AuditEvent](../schemas/audit_event.md)
- [Authentication](../schemas/authentication.md)
- [Dhcp](../schemas/dhcp.md)
- [Dns](../schemas/dns.md)
- [FileEvent](../schemas/file_event.md)
- [Notification](../schemas/notification.md)
- [ProcessEvent](../schemas/process_event.md)
- [RegistryEvent](../schemas/registry_event.md)
- [User Management](../schemas/user_management.md)

## Raw fields

### `Rule`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`RuleName`](../fields/rule_name.md), [`RuleNumber`](../fields/rule_number.md)

Either the value of RuleName or the value of RuleNumber. If the value of RuleNumber is used, the type should be converted to string.

### `RuleName`

- **Class**: `Optional`
- **Type**: `string`

The name or ID of the rule by associated with the inspection results.

### `RuleNumber`

- **Class**: `Optional`
- **Type**: `int`

The number of the rule associated with the inspection results.

### `ThreatCategory`

- **Class**: `Optional`
- **Type**: `string`

The category of the threat or malware identified in activity.

### `ThreatConfidence`

- **Class**: `Optional`
- **Type**: `int`
- **Logical type**: `ConfidenceLevel`

The confidence level of the threat identified, normalized to a value between 0 and a 100.

### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

The field for which a threat was identified.

### `ThreatFirstReportedTime`

- **Class**: `Optional`
- **Type**: `datetime`

The first time the relevant IoC was identified as a threat.

### `ThreatId`

- **Class**: `Optional`
- **Type**: `string`

The ID of the threat or malware identified in the activity.

### `ThreatIsActive`

- **Class**: `Optional`
- **Type**: `bool`

True ID the threat identified is considered an active threat.

### `ThreatLastReportedTime`

- **Class**: `Optional`
- **Type**: `datetime`

The last time the relevant IoC was identified as a threat.

### `ThreatName`

- **Class**: `Optional`
- **Type**: `string`

The name of the threat or malware identified in the activity.

### `ThreatOriginalConfidence`

- **Class**: `Optional`
- **Type**: `string`

The original confidence level of the threat identified, as reported by the reporting device.

### `ThreatOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

The risk level as reported by the reporting device.

### `ThreatRiskLevel`

- **Class**: `Optional`
- **Type**: `int`
- **Logical type**: `RiskLevel`

The risk level associated with the identified threat. The level should be a number between 0 and 100.
