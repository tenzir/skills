# Dhcp

- **Version**: `0.1.0`
- **Last updated**: Sept 12 2023
- **Source**: [`ASIM/schemas/ASimDHCPEvent.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/ASimDHCPEvent.yaml)
- **Fields**: `104`

## References

- [ASIM DHCP Schema](https://aka.ms/ASimDhcpDoc)
- [ASIM](https://aka.ms/AboutASIM)

## Includes

| Include | File | Role |
| --- | --- | --- |
| Enumerations | `ASIM/schemas/common/ASimEnumerations.yaml` |  |
| Event Fields | `ASIM/schemas/common/ASimEventFields.yaml` |  |
| Inspection fields | `ASIM/schemas/common/ASimInspectionFields.yaml` |  |
| Dvc | `ASIM/schemas/entities/ASimDvc.yaml` |  |
| Source user entity | `ASIM/schemas/entities/ASimUser.yaml` | `Src` |
| Source system entity | `ASIM/schemas/entities/ASimSystem.yaml` | `Src` |

## Resolved fields

| Field | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [`AdditionalFields`](../fields/additional_fields.md) | `Recommended` | `dynamic` |  |  | inherited from Event Fields |
| [`DhcpCircuitId`](../fields/dhcp_circuit_id.md) | `Recommended` | `string` |  |  | local |
| [`DhcpLeaseDuration`](../fields/dhcp_lease_duration.md) | `Optional` | `integer` |  |  | local |
| [`DhcpSessionDuration`](../fields/dhcp_session_duration.md) | `Optional` | `integer` |  |  | local |
| [`DhcpSessionId`](../fields/dhcp_session_id.md) | `Optional` | `string` |  |  | local |
| [`DhcpSrcDHCId`](../fields/dhcp_src_dhc_id.md) | `Optional` | `string` |  |  | local |
| [`DhcpSubscriberId`](../fields/dhcp_subscriber_id.md) | `Optional` | `string` |  |  | local |
| [`DhcpUserClass`](../fields/dhcp_user_class.md) | `Optional` | `string` |  |  | local |
| [`DhcpUserClassId`](../fields/dhcp_user_class_id.md) | `Optional` | `string` |  |  | local |
| [`DhcpVendorClass`](../fields/dhcp_vendor_class.md) | `Optional` | `string` |  |  | local |
| [`DhcpVendorClassId`](../fields/dhcp_vendor_class_id.md) | `Optional` | `string` |  |  | local |
| [`Dst`](../fields/dst.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [`Duration`](../fields/duration.md) | `Alias` | `integer` |  |  | local |
| [`Dvc`](../fields/dvc.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [`DvcAction`](../fields/dvc_action.md) | `Recommended` | `string` |  |  | inherited from Dvc |
| [`DvcDescription`](../fields/dvc_description.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcDomain`](../fields/dvc_domain.md) | `Recommended` | `string` |  |  | inherited from Dvc |
| [`DvcDomainType`](../fields/dvc_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Dvc |
| [`DvcFQDN`](../fields/dvc_fqdn.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcHostname`](../fields/dvc_hostname.md) | `Recommended` | `string` | `Hostname` |  | inherited from Dvc |
| [`DvcId`](../fields/dvc_id.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcIdType`](../fields/dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Dvc |
| [`DvcInterface`](../fields/dvc_interface.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcIpAddr`](../fields/dvc_ip_addr.md) | `Recommended` | `string` | `IP Address` |  | inherited from Dvc |
| [`DvcMacAddr`](../fields/dvc_mac_addr.md) | `Optional` | `string` | `MAC address` |  | inherited from Dvc |
| [`DvcOriginalAction`](../fields/dvc_original_action.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcOs`](../fields/dvc_os.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcOsVersion`](../fields/dvc_os_version.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcScope`](../fields/dvc_scope.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcScopeId`](../fields/dvc_scope_id.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcZone`](../fields/dvc_zone.md) | `Optional` | `string` | `MAC address` |  | inherited from Dvc |
| [`EventCount`](../fields/event_count.md) | `Optional` | `int` |  |  | inherited from Event Fields |
| [`EventEndTime`](../fields/event_end_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventMessage`](../fields/event_message.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalResultDetails`](../fields/event_original_result_details.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalSeverity`](../fields/event_original_severity.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalSubType`](../fields/event_original_sub_type.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalType`](../fields/event_original_type.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOriginalUid`](../fields/event_original_uid.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventOwner`](../fields/event_owner.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventProduct`](../fields/event_product.md) | `Mandatory` | `string` | `Enumerated` | [EventProduct](../enumerations/event_product.md) | inherited from Event Fields |
| [`EventProductVersion`](../fields/event_product_version.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventReportUrl`](../fields/event_report_url.md) | `Optional` | `string` | `URL` |  | inherited from Event Fields |
| [`EventResult`](../fields/event_result.md) | `Mandatory` | `string` | `Enumerated` | `Success`, `Failure`, `Partial`, `NA` | inherited from Event Fields |
| [`EventResultDetails`](../fields/event_result_details.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventSchema`](../fields/event_schema.md) | `Mandatory` | `string` | `Enumerated` | [Dhcp](../schemas/dhcp.md) | local override |
| [`EventSchemaVersion`](../fields/event_schema_version.md) | `Mandatory` | `string` | `SchemaVersion` |  | inherited from Event Fields |
| [`EventSeverity`](../fields/event_severity.md) | `Recommended` | `string` | `Enumerated` | `Informational`, `Low`, `Medium`, `High` | inherited from Event Fields |
| [`EventStartTime`](../fields/event_start_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventSubType`](../fields/event_sub_type.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventType`](../fields/event_type.md) | `Mandatory` | `string` | `Enumerated` | `Assign`, `Renew`, `Release`, `DNS Update` | local override |
| [`EventVendor`](../fields/event_vendor.md) | `Mandatory` | `string` | `Enumerated` | [EventVendor](../enumerations/event_vendor.md) | inherited from Event Fields |
| [`Hostname`](../fields/hostname.md) | `Alias` | `string` |  |  | local |
| [`IpAddr`](../fields/ip_addr.md) | `Alias` | `string` | `IP Address` |  | local |
| [`RequestedIpAddr`](../fields/requested_ip_addr.md) | `Optional` | `string` |  |  | local |
| [`Rule`](../fields/rule.md) | `Alias` | `string` |  |  | inherited from Inspection fields |
| [`RuleName`](../fields/rule_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`RuleNumber`](../fields/rule_number.md) | `Optional` | `int` |  |  | inherited from Inspection fields |
| [`SessionId`](../fields/session_id.md) | `Alias` | `string` |  |  | local |
| [`Src`](../fields/src.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDescription`](../fields/src_description.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDeviceType`](../fields/src_device_type.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations/device_type.md) | inherited from Source system entity as Src |
| [`SrcDomain`](../fields/src_domain.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDomainType`](../fields/src_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Source system entity as Src |
| [`SrcDvcId`](../fields/src_dvc_id.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDvcIdType`](../fields/src_dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Source system entity as Src |
| [`SrcDvcScope`](../fields/src_dvc_scope.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDvcScopeId`](../fields/src_dvc_scope_id.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcFQDN`](../fields/src_fqdn.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcGeoCity`](../fields/src_geo_city.md) | `Optional` | `string` | `City` |  | inherited from Source system entity as Src |
| [`SrcGeoCountry`](../fields/src_geo_country.md) | `Optional` | `string` | `Country` |  | inherited from Source system entity as Src |
| [`SrcGeoLatitude`](../fields/src_geo_latitude.md) | `Optional` | `Double` |  |  | inherited from Source system entity as Src |
| [`SrcGeoLongitude`](../fields/src_geo_longitude.md) | `Optional` | `Double` |  |  | inherited from Source system entity as Src |
| [`SrcGeoRegion`](../fields/src_geo_region.md) | `Optional` | `string` | `Region` |  | inherited from Source system entity as Src |
| [`SrcHostname`](../fields/src_hostname.md) | `Optional` | `string` | `Hostname` |  | inherited from Source system entity as Src |
| [`SrcIpAddr`](../fields/src_ip_addr.md) | `Recommended` | `string` | `IP Address` |  | inherited from Source system entity as Src |
| [`SrcMacAddr`](../fields/src_mac_addr.md) | `Optional` | `string` | `MAC address` |  | inherited from Source system entity as Src |
| [`SrcOriginalRiskLevel`](../fields/src_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcOriginalUserType`](../fields/src_original_user_type.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcPortNumber`](../fields/src_port_number.md) | `Optional` | `int` |  |  | inherited from Source system entity as Src |
| [`SrcRiskLevel`](../fields/src_risk_level.md) | `Optional` | `int` |  |  | inherited from Source system entity as Src |
| [`SrcUserId`](../fields/src_user_id.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserIdType`](../fields/src_user_id_type.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Source user entity as Src |
| [`SrcUsername`](../fields/src_username.md) | `Recommended` | `string` | `Username` |  | inherited from Source user entity as Src |
| [`SrcUsernameType`](../fields/src_username_type.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Source user entity as Src |
| [`SrcUserScope`](../fields/src_user_scope.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserScopeId`](../fields/src_user_scope_id.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserSessionId`](../fields/src_user_session_id.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`SrcUserType`](../fields/src_user_type.md) | `Optional` | `string` | `Enumerated` | [UserType](../enumerations/user_type.md) | inherited from Source user entity as Src |
| [`SrcUserUid`](../fields/src_user_uid.md) | `Optional` | `string` |  |  | inherited from Source user entity as Src |
| [`ThreatCategory`](../fields/threat_category.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatConfidence`](../fields/threat_confidence.md) | `Optional` | `int` | `ConfidenceLevel` |  | inherited from Inspection fields |
| [`ThreatField`](../fields/threat_field.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Inspection fields |
| [`ThreatFirstReportedTime`](../fields/threat_first_reported_time.md) | `Optional` | `datetime` |  |  | inherited from Inspection fields |
| [`ThreatId`](../fields/threat_id.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatIsActive`](../fields/threat_is_active.md) | `Optional` | `bool` |  |  | inherited from Inspection fields |
| [`ThreatLastReportedTime`](../fields/threat_last_reported_time.md) | `Optional` | `datetime` |  |  | inherited from Inspection fields |
| [`ThreatName`](../fields/threat_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatOriginalConfidence`](../fields/threat_original_confidence.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatOriginalRiskLevel`](../fields/threat_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatRiskLevel`](../fields/threat_risk_level.md) | `Optional` | `int` | `RiskLevel` |  | inherited from Inspection fields |
| [`TimeGenerated`](../fields/time_generated.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`Type`](../fields/type.md) | `Mandatory` | `string` |  |  | inherited from Event Fields |
| [`User`](../fields/user.md) | `Alias` | `string` | `Username` |  | local |

## Fields

### `AdditionalFields`

- **Class**: `Recommended`
- **Type**: `dynamic`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `DhcpCircuitId`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP circuit ID, as defined by RFC3046.

### `DhcpLeaseDuration`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The length of the lease granted to a client, in seconds.

### `DhcpSessionDuration`

- **Class**: `Optional`
- **Type**: `integer`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The amount of time, in milliseconds, for the completion of the DHCP session.

#### Examples

- `1500`

### `DhcpSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The session identifier as reported by the reporting device. For the Windows DHCP server, set this to the TransactionID field.

#### Examples

- `2099570186`

### `DhcpSrcDHCId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP client ID, as defined by RFC4701.

### `DhcpSubscriberId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP subscriber ID, as defined by RFC3993.

### `DhcpUserClass`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP User Class, as defined by RFC3004.

### `DhcpUserClassId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP User Class Id, as defined by RFC3004.

### `DhcpVendorClass`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP Vendor Class, as defined by RFC3925.

### `DhcpVendorClassId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The DHCP Vendor Class Id, as defined by RFC3925.

### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

### `Duration`

- **Class**: `Alias`
- **Type**: `integer`
- **Aliases**: [`DhcpSessionDuration`](../fields/dhcp_session_duration.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to DhcpSessionDuration

### `Dvc`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcFQDN`](../fields/dvc_fqdn.md), [`DvcId`](../fields/dvc_id.md), [`DvcHostname`](../fields/dvc_hostname.md), [`DvcIpAddr`](../fields/dvc_ip_addr.md), [`DvcMacAddr`](../fields/dvc_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A unique identifier of the device on which the event occurred or which reported the event, depending on the schema. This field might alias the DvcFQDN, DvcId, DvcHostname, or DvcIpAddr fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### `DvcAction`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

For reporting security systems, the action taken by the system, if applicable.

### `DvcDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

A descriptive text associated with the device.

### `DvcDomain`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The domain of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`DvcDomain`](../fields/dvc_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

TThe type of DvcDomain.

### `DvcFQDN`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The hostname of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcHostname`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The hostname of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The unique ID of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`SrcDvcId`](../fields/src_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The type of DvcId.

### `DvcInterface`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The network interface on which data was captured. This field is typically relevant to network related activity which is captured by an intermediate or tap device.

### `DvcIpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The IP address of the device on which the event occurred or which reported the event, depending on the schema.

### `DvcMacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The MAC address of the device on which the event occurred or which reported the event.

### `DvcOriginalAction`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The original DvcAction as provided by the reporting device.

### `DvcOs`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The operating system running on the device on which the event occurred or which reported the event.

### `DvcOsVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The version of the operating system on the device on which the event occurred or which reported the event.

### `DvcScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The cloud platform scope the device belongs to. DvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `DvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The cloud platform scope ID the device belongs to. DvcScopeId map to a subscription ID on Azure and to an account ID on AWS.

### `DvcZone`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimDvc.yaml`; include `Dvc`

The network on which the event occurred or which reported the event, depending on the schema. The zone is defined by the reporting device.

### `EventCount`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The number of events described by the record. This value is used when the source supports aggregation, and a single record might represent multiple events.

### `EventEndTime`

- **Class**: `Mandatory`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The time in which the event ended. If the source supports aggregation and the record represents multiple events, the time that the last event was generated. If not provided by the source record, this field aliases the TimeGenerated field.

### `EventMessage`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A general message or description, either included in or generated from the record.

### `EventOriginalResultDetails`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original result details provided by the source. This value is used to derive EventResultDetails, which should have only one of the values documented for each schema.

### `EventOriginalSeverity`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original severity as provided by the reporting device. This value is used to derive EventSeverity.

### `EventOriginalSubType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event subtype or ID, if provided by the source. For example, this field will be used to store the original Windows logon type. This value is used to derive EventSubType, which should have only one of the values documented for each schema.

### `EventOriginalType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The original event type or ID, if provided by the source. For example, this field will be used to store the original Windows event ID. This value is used to derive EventType, which should have only one of the values documented for each schema.

### `EventOriginalUid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique ID of the original record, if provided by the source.

### `EventOwner`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The owner of the event, which is usually the department or subsidiary in which it was generated.

### `EventProduct`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventProduct](../enumerations/event_product.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The product generating the event. The value should be one of the values listed in Vendors and Products.

### `EventProductVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The version of the product generating the event.

### `EventReportUrl`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `URL`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A URL provided in the event for a resource that provides more information about the event.

### `EventResult`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Success`, `Failure`, `Partial`, `NA`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `EventResultDetails`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [Dhcp](../schemas/dhcp.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The schema the event is normalized to. Each schema documents its schema name.

### `EventSchemaVersion`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `SchemaVersion`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The version of the schema. Each schema documents its current version.

### `EventSeverity`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Informational`, `Low`, `Medium`, `High`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The severity of the event.

### `EventStartTime`

- **Class**: `Mandatory`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The time in which the event started. If the source supports aggregation and the record represents multiple events, the time that the first event was generated. If not provided by the source record, this field aliases the TimeGenerated field.

### `EventSubType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Assign`, `Renew`, `Release`, `DNS Update`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Indicate the operation reported by the record.

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations/event_vendor.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `Hostname`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcHostname`](../fields/src_hostname.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to SrcHostname

### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to SrcIpAddr

### `RequestedIpAddr`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

The IP address requested by the DHCP client, when available.

#### Examples

- `192.168.12.3`

### `Rule`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`RuleName`](../fields/rule_name.md), [`RuleNumber`](../fields/rule_number.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

Either the value of RuleName or the value of RuleNumber. If the value of RuleNumber is used, the type should be converted to string.

### `RuleName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The name or ID of the rule by associated with the inspection results.

### `RuleNumber`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The number of the rule associated with the inspection results.

### `SessionId`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DhcpSessionId`](../fields/dhcp_session_id.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias to DhcpSessionId.

### `Src`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`SrcFQDN`](../fields/src_fqdn.md), [`SrcDvcId`](../fields/src_dvc_id.md), [`SrcHostname`](../fields/src_hostname.md), [`SrcIpAddr`](../fields/src_ip_addr.md), [`SrcMacAddr`](../fields/src_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Acting`, `Src`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A unique identifier of the source device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

### `SrcDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

A descriptive text associated with the device.

### `SrcDeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations/device_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the device.

### `SrcDomain`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The domain of the device.

### `SrcDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`SrcDomain`](../fields/src_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the domain.

### `SrcDvcId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The ID of the device.

### `SrcDvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`SrcDvcId`](../fields/src_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The type of the DvcId.

### `SrcDvcScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `SrcDvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.

### `SrcFQDN`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, including domain information when available.

### `SrcGeoCity`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `City`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The city associated with the IP address.

### `SrcGeoCountry`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Country`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The country associated with the IP address.

### `SrcGeoLatitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The latitude of the geographical coordinate associated with the IP address.

### `SrcGeoLongitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The longitude of the geographical coordinate associated with the IP address.

### `SrcGeoRegion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Region`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The region within a country associated with the IP address.

### `SrcHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### `SrcIpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The IP address of the device.

### `SrcMacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The MAC address of the device.

### `SrcOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The risk level associated with the source. As reported by the reporting device or enriched.

### `SrcOriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

TBD

### `SrcPortNumber`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The IP port on which the device communicated, if applicable.

### `SrcRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Source system entity`; role `Src`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.

### `SrcUserId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

A machine-readable, alphanumeric, unique representation of the user.

#### Examples

- `S-1-12-1-4141952679-1282074057-627758481-2916039507`

### `SrcUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`SrcUserId`](../fields/src_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### `SrcUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The user's username, including domain information when available.

### `SrcUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### `SrcUserScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The scope, such as Azure AD tenant, in which UserId and Username are defined.

### `SrcUserScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The scope ID, such as Azure AD tenant ID, in which UserId and Username are defined.

### `SrcUserSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The unique ID of the sign-in session of the user.

#### Examples

- `102pTUgC3p8RIqHvzxLCHnFlg`

### `SrcUserType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserType](../enumerations/user_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

### `SrcUserUid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Source user entity`; role `Src`

The Unix or Linux user ID of the user.

### `ThreatCategory`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The category of the threat or malware identified in activity.

### `ThreatConfidence`

- **Class**: `Optional`
- **Type**: `int`
- **Logical type**: `ConfidenceLevel`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The confidence level of the threat identified, normalized to a value between 0 and a 100.

### `ThreatField`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The field for which a threat was identified.

### `ThreatFirstReportedTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The first time the relevant IoC was identified as a threat.

### `ThreatId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The ID of the threat or malware identified in the activity.

### `ThreatIsActive`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

True ID the threat identified is considered an active threat.

### `ThreatLastReportedTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The last time the relevant IoC was identified as a threat.

### `ThreatName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The name of the threat or malware identified in the activity.

### `ThreatOriginalConfidence`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The original confidence level of the threat identified, as reported by the reporting device.

### `ThreatOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The risk level as reported by the reporting device.

### `ThreatRiskLevel`

- **Class**: `Optional`
- **Type**: `int`
- **Logical type**: `RiskLevel`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`

The risk level associated with the identified threat. The level should be a number between 0 and 100.

### `TimeGenerated`

- **Class**: `Mandatory`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `Type`

- **Class**: `Mandatory`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimDHCPEvent.yaml`

Alias for SrcUsername
