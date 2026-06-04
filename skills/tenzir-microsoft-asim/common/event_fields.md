# ASimEventFields

- **Source**: [`ASIM/schemas/common/ASimEventFields.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/common/ASimEventFields.yaml)
- **Fields**: `26`

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

### `AdditionalFields`

- **Class**: `Recommended`
- **Type**: `dynamic`

### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### `EventCount`

- **Class**: `Optional`
- **Type**: `int`

The number of events described by the record. This value is used when the source supports aggregation, and a single record might represent multiple events.

### `EventEndTime`

- **Class**: `Mandatory`
- **Type**: `datetime`

The time in which the event ended. If the source supports aggregation and the record represents multiple events, the time that the last event was generated. If not provided by the source record, this field aliases the TimeGenerated field.

### `EventMessage`

- **Class**: `Optional`
- **Type**: `string`

A general message or description, either included in or generated from the record.

### `EventOriginalResultDetails`

- **Class**: `Optional`
- **Type**: `string`

The original result details provided by the source. This value is used to derive EventResultDetails, which should have only one of the values documented for each schema.

### `EventOriginalSeverity`

- **Class**: `Optional`
- **Type**: `string`

The original severity as provided by the reporting device. This value is used to derive EventSeverity.

### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### `EventOriginalType`

- **Class**: `Optional`
- **Type**: `string`

The original event type or ID, if provided by the source. For example, this field will be used to store the original Windows event ID. This value is used to derive EventType, which should have only one of the values documented for each schema.

### `EventOriginalUid`

- **Class**: `Optional`
- **Type**: `string`

A unique ID of the original record, if provided by the source.

### `EventOwner`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

The owner of the event, which is usually the department or subsidiary in which it was generated.

### `EventProduct`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventProduct](../enumerations.md#eventproduct)

The product generating the event. The value should be one of the values listed in Vendors and Products.

### `EventProductVersion`

- **Class**: `Optional`
- **Type**: `string`

The version of the product generating the event.

### `EventReportUrl`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `URL`

A URL provided in the event for a resource that provides more information about the event.

### `EventResult`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Success`, `Failure`, `Partial`, `NA`

### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Schemas](../enumerations.md#schemas)

The schema the event is normalized to. Each schema documents its schema name.

### `EventSchemaVersion`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `SchemaVersion`

The version of the schema. Each schema documents its current version.

### `EventSeverity`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Informational`, `Low`, `Medium`, `High`

The severity of the event.

### `EventStartTime`

- **Class**: `Mandatory`
- **Type**: `datetime`

The time in which the event started. If the source supports aggregation and the record represents multiple events, the time that the first event was generated. If not provided by the source record, this field aliases the TimeGenerated field.

### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations.md#eventvendor)

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `Src`

- **Class**: `Recommended`
- **Type**: `string`

A unique identifier of the source or acting device. This field might alias the ource or acting device device FQDN, Hostname, Device Id or IP address fields.

### `TimeGenerated`

- **Class**: `Mandatory`
- **Type**: `datetime`

### `Type`

- **Class**: `Mandatory`
- **Type**: `string`
