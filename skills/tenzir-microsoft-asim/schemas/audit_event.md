# AuditEvent

- **Version**: `0.1.0`
- **Last updated**: Dec 14, 2022
- **Source**: [`ASIM/schemas/ASimAuditEvent.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/ASimAuditEvent.yaml)
- **Fields**: `133`

## References

- [ASIM Audit Event Schema](https://aka.ms/ASimAuditEventDoc)
- [ASIM](https://aka.ms/AboutASIM)

## Includes

| Include | File | Role |
| --- | --- | --- |
| Enumerations | `ASIM/schemas/common/ASimEnumerations.yaml` |  |
| Event Fields | `ASIM/schemas/common/ASimEventFields.yaml` |  |
| Inspection fields | `ASIM/schemas/common/ASimInspectionFields.yaml` |  |
| Dvc | `ASIM/schemas/entities/ASimDvc.yaml` |  |
| Actor entity | `ASIM/schemas/entities/ASimActor.yaml` |  |
| Target application entity | `ASIM/schemas/entities/ASimApp.yaml` | `Target` |
| Acting application entity | `ASIM/schemas/entities/ASimApp.yaml` | `Acting` |
| Source system entity | `ASIM/schemas/entities/ASimSystem.yaml` | `Src` |
| Target system entity | `ASIM/schemas/entities/ASimSystem.yaml` | `Target` |

## Resolved fields

| Field | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [`ActingAppId`](../fields/acting_app_id.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`ActingAppName`](../fields/acting_app_name.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`ActingAppType`](../fields/acting_app_type.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations/app_type.md) | inherited from Acting application entity as Acting |
| [`ActingOriginalAppType`](../fields/acting_original_app_type.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`ActorOriginalUserType`](../fields/actor_original_user_type.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorScope`](../fields/actor_scope.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorScopeId`](../fields/actor_scope_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorSessionId`](../fields/actor_session_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserAadId`](../fields/actor_user_aad_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserId`](../fields/actor_user_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserIdType`](../fields/actor_user_id_type.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations/user_id_type.md) | inherited from Actor entity |
| [`ActorUsername`](../fields/actor_username.md) | `Recommended` | `string` | `Username` |  | inherited from Actor entity |
| [`ActorUsernameType`](../fields/actor_username_type.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations/username_type.md) | inherited from Actor entity |
| [`ActorUserSid`](../fields/actor_user_sid.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserType`](../fields/actor_user_type.md) | `Optional` | `string` | `Enumerated` | [UserType](../enumerations/user_type.md) | inherited from Actor entity |
| [`AdditionalFields`](../fields/additional_fields.md) | `Recommended` | `dynamic` |  |  | inherited from Event Fields |
| [`Application`](../fields/application.md) | `Alias` | `string` |  |  | local |
| [`Dst`](../fields/dst.md) | `Alias` | `string` |  |  | inherited from Target system entity as Target |
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
| [`EventSchema`](../fields/event_schema.md) | `Mandatory` | `string` | `Enumerated` | [AuditEvent](../schemas/audit_event.md) | local override |
| [`EventSchemaVersion`](../fields/event_schema_version.md) | `Mandatory` | `string` | `SchemaVersion` |  | inherited from Event Fields |
| [`EventSeverity`](../fields/event_severity.md) | `Recommended` | `string` | `Enumerated` | `Informational`, `Low`, `Medium`, `High` | inherited from Event Fields |
| [`EventStartTime`](../fields/event_start_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventSubType`](../fields/event_sub_type.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventType`](../fields/event_type.md) | `Mandatory` | `string` | `Enumerated` | `Set`, `Read`, `Create`, `Delete`, `Execute`, `Install`, `Clear`, `Enable`, `Disable`, `Other` | local override |
| [`EventVendor`](../fields/event_vendor.md) | `Mandatory` | `string` | `Enumerated` | [EventVendor](../enumerations/event_vendor.md) | inherited from Event Fields |
| [`HttpUserAgent`](../fields/http_user_agent.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`IpAddr`](../fields/ip_addr.md) | `Alias` | `string` | `IP Address` |  | local |
| [`NewValue`](../fields/new_value.md) | `Recommended` | `string` |  |  | local |
| [`Object`](../fields/object.md) | `Recommended` | `string` |  |  | local |
| [`ObjectId`](../fields/object_id.md) | `Recommended` | `string` |  |  | local |
| [`ObjectType`](../fields/object_type.md) | `Related` | `string` | `Enumerated` | `Configuration Atom`, `Policy Rule`, `Cloud Resource`, `Other` | local |
| [`OldValue`](../fields/old_value.md) | `Optional` | `string` |  |  | local |
| [`Operation`](../fields/operation.md) | `Mandatory` | `string` |  |  | local |
| [`OriginalObjectType`](../fields/original_object_type.md) | `Optional` | `string` |  |  | local |
| [`Process`](../fields/process.md) | `Alias` | `string` |  |  | local |
| [`Rule`](../fields/rule.md) | `Alias` | `string` |  |  | inherited from Inspection fields |
| [`RuleName`](../fields/rule_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`RuleNumber`](../fields/rule_number.md) | `Optional` | `int` |  |  | inherited from Inspection fields |
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
| [`SrcPortNumber`](../fields/src_port_number.md) | `Optional` | `int` |  |  | inherited from Source system entity as Src |
| [`SrcRiskLevel`](../fields/src_risk_level.md) | `Optional` | `int` |  |  | inherited from Source system entity as Src |
| [`TargetAppId`](../fields/target_app_id.md) | `Optional` | `string` |  |  | inherited from Target application entity as Target |
| [`TargetAppName`](../fields/target_app_name.md) | `Optional` | `string` |  |  | inherited from Target application entity as Target |
| [`TargetAppType`](../fields/target_app_type.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations/app_type.md) | inherited from Target application entity as Target |
| [`TargetDescription`](../fields/target_description.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetDeviceType`](../fields/target_device_type.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations/device_type.md) | inherited from Target system entity as Target |
| [`TargetDomain`](../fields/target_domain.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetDomainType`](../fields/target_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations/domain_type.md) | inherited from Target system entity as Target |
| [`TargetDvcId`](../fields/target_dvc_id.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetDvcIdType`](../fields/target_dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations/dvc_id_type.md) | inherited from Target system entity as Target |
| [`TargetDvcScope`](../fields/target_dvc_scope.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetDvcScopeId`](../fields/target_dvc_scope_id.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetFQDN`](../fields/target_fqdn.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetGeoCity`](../fields/target_geo_city.md) | `Optional` | `string` | `City` |  | inherited from Target system entity as Target |
| [`TargetGeoCountry`](../fields/target_geo_country.md) | `Optional` | `string` | `Country` |  | inherited from Target system entity as Target |
| [`TargetGeoLatitude`](../fields/target_geo_latitude.md) | `Optional` | `Double` |  |  | inherited from Target system entity as Target |
| [`TargetGeoLongitude`](../fields/target_geo_longitude.md) | `Optional` | `Double` |  |  | inherited from Target system entity as Target |
| [`TargetGeoRegion`](../fields/target_geo_region.md) | `Optional` | `string` | `Region` |  | inherited from Target system entity as Target |
| [`TargetHostname`](../fields/target_hostname.md) | `Optional` | `string` | `Hostname` |  | inherited from Target system entity as Target |
| [`TargetIpAddr`](../fields/target_ip_addr.md) | `Recommended` | `string` | `IP Address` |  | inherited from Target system entity as Target |
| [`TargetMacAddr`](../fields/target_mac_addr.md) | `Optional` | `string` | `MAC address` |  | inherited from Target system entity as Target |
| [`TargetOriginalAppType`](../fields/target_original_app_type.md) | `Optional` | `string` |  |  | inherited from Target application entity as Target |
| [`TargetOriginalRiskLevel`](../fields/target_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Target system entity as Target |
| [`TargetPortNumber`](../fields/target_port_number.md) | `Optional` | `int` |  |  | inherited from Target system entity as Target |
| [`TargetRiskLevel`](../fields/target_risk_level.md) | `Optional` | `int` |  |  | inherited from Target system entity as Target |
| [`TargetUrl`](../fields/target_url.md) | `Optional` | `string` |  |  | inherited from Target application entity as Target |
| [`ThreatCategory`](../fields/threat_category.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatConfidence`](../fields/threat_confidence.md) | `Optional` | `int` | `ConfidenceLevel` |  | inherited from Inspection fields |
| [`ThreatField`](../fields/threat_field.md) | `Conditional` | `string` | `Enumerated` | `SrcIpAddr`, `DstIpAddr` | local override |
| [`ThreatFirstReportedTime`](../fields/threat_first_reported_time.md) | `Optional` | `datetime` |  |  | inherited from Inspection fields |
| [`ThreatId`](../fields/threat_id.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatIpAddr`](../fields/threat_ip_addr.md) | `Optional` | `string` | `IP Address` |  | local |
| [`ThreatIsActive`](../fields/threat_is_active.md) | `Optional` | `bool` |  |  | inherited from Inspection fields |
| [`ThreatLastReportedTime`](../fields/threat_last_reported_time.md) | `Optional` | `datetime` |  |  | inherited from Inspection fields |
| [`ThreatName`](../fields/threat_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatOriginalConfidence`](../fields/threat_original_confidence.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatOriginalRiskLevel`](../fields/threat_original_risk_level.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`ThreatRiskLevel`](../fields/threat_risk_level.md) | `Optional` | `int` | `RiskLevel` |  | inherited from Inspection fields |
| [`TimeGenerated`](../fields/time_generated.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`Type`](../fields/type.md) | `Mandatory` | `string` |  |  | inherited from Event Fields |
| [`User`](../fields/user.md) | `Alias` | `string` | `Username` |  | local |
| [`Value`](../fields/value.md) | `Alias` | `string` |  |  | local |
| [`ValueType`](../fields/value_type.md) | `Optional` | `string` | `Enumerated` | `Other` | local |

## Fields

### `ActingAppId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The ID of the application, including a process, browser, or service.

### `ActingAppName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The name of the application, including a service, a URL, or a SaaS application.

#### Examples

- `Exchange 365`

### `ActingAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations/app_type.md)
- **Follows**: [`ActingAppName`](../fields/acting_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The type of the application.

### `ActingOriginalAppType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The application type as reported by the reporting device.

### `ActorOriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

TBD

### `ActorScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

The scope, such as Azure AD tenant, in which ActorUserId and ActorUsername are defined.

### `ActorScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

The scope ID, such as Azure AD tenant ID, in which ActorUserId and ActorUsername are defined.

### `ActorSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

The unique ID of the sign-in session of the Actor.

#### Examples

- `102pTUgC3p8RIqHvzxLCHnFlg`

### `ActorUserAadId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

The Azure Active Directory ID of the actor.

### `ActorUserId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

A machine-readable, alphanumeric, unique representation of the actor.

#### Examples

- `S-1-12-1-4141952679-1282074057-627758481-2916039507`

### `ActorUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations/user_id_type.md)
- **Follows**: [`ActorUserId`](../fields/actor_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

### `ActorUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

The Actor's username, including domain information when available.

### `ActorUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations/username_type.md)
- **Follows**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

### `ActorUserSid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

The Windows user ID (SIDs) of the actor.

### `ActorUserType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserType](../enumerations/user_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

### `AdditionalFields`

- **Class**: `Recommended`
- **Type**: `dynamic`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `Application`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetAppName`](../fields/target_app_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Alias to TargetAppName

### `Dst`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetFQDN`](../fields/target_fqdn.md), [`TargetDvcId`](../fields/target_dvc_id.md), [`TargetHostname`](../fields/target_hostname.md), [`TargetIpAddr`](../fields/target_ip_addr.md), [`TargetMacAddr`](../fields/target_mac_addr.md), `strcat(EventVendor`, `/`, `EventProduct)`
- **For roles**: `Target`, `Dst`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

A unique identifier of the destination device. This field might alias the FQDN, Id, Hostname, IpAddr or MacAddr fields fields. For cloud sources, for which there is no apparent device, use the same value as the Event Product field.

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
- **List of values**: [AuditEvent](../schemas/audit_event.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuditEvent.yaml`

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
- **List of values**: `Set`, `Read`, `Create`, `Delete`, `Execute`, `Install`, `Clear`, `Enable`, `Disable`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations/event_vendor.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Actor`, `Src`, `Acting`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The user agent header accosiated with the application, when communicating using HTTP or HTTPS.

### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`SrcIpAddr`](../fields/src_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Alias to SrcIpAddr

### `NewValue`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The new value of Object after the operation was performed, if applicable.

### `Object`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The name of the object on which the operation identified by EventType is performed.

### `ObjectId`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The id of the object on which the operation identified by EventType is performed.

### `ObjectType`

- **Class**: `Related`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Configuration Atom`, `Policy Rule`, `Cloud Resource`, `Other`
- **Related to**: `Object`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

### `OldValue`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The old value of Object prior to the operation, if applicable.

### `Operation`

- **Class**: `Mandatory`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The operation audited, as specified by the reporting device.

### `OriginalObjectType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The object type as reported by the reporting device.

### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`ActingProcessName`](../fields/acting_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Alias to ActingProcessName

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

### `TargetAppId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The ID of the application, including a process, browser, or service.

### `TargetAppName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The name of the application, including a service, a URL, or a SaaS application.

#### Examples

- `Exchange 365`

### `TargetAppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations/app_type.md)
- **Follows**: [`TargetAppName`](../fields/target_app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The type of the application.

### `TargetDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

A descriptive text associated with the device.

### `TargetDeviceType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DeviceType](../enumerations/device_type.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the device.

### `TargetDomain`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The domain of the device.

### `TargetDomainType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DomainType](../enumerations/domain_type.md)
- **Follows**: [`TargetDomain`](../fields/target_domain.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the domain.

### `TargetDvcId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The ID of the device.

### `TargetDvcIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [DvcIdType](../enumerations/dvc_id_type.md)
- **Follows**: [`TargetDvcId`](../fields/target_dvc_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The type of the DvcId.

### `TargetDvcScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The cloud platform scope the device belongs to. TargetDvcScope map to a subscription ID on Azure and to an account ID on AWS.

### `TargetDvcScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The cloud platform scope ID the device belongs to. DvcScopeId maps to a subscription ID on Azure and to an account ID on AWS.

### `TargetFQDN`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The device hostname, including domain information when available.

### `TargetGeoCity`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `City`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The city associated with the IP address.

### `TargetGeoCountry`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Country`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The country associated with the IP address.

### `TargetGeoLatitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The latitude of the geographical coordinate associated with the IP address.

### `TargetGeoLongitude`

- **Class**: `Optional`
- **Type**: `Double`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The longitude of the geographical coordinate associated with the IP address.

### `TargetGeoRegion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Region`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The region within a country associated with the IP address.

### `TargetHostname`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Hostname`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The device hostname, excluding domain information. If no device name is available, store the relevant IP address in this field.

### `TargetIpAddr`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The IP address of the device.

### `TargetMacAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `MAC address`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The MAC address of the device.

### `TargetOriginalAppType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

The application type as reported by the reporting device.

### `TargetOriginalRiskLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The risk level associated with the source. As reported by the reporting device or enriched.

### `TargetPortNumber`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The IP port on which the device communicated, if applicable.

### `TargetRiskLevel`

- **Class**: `Optional`
- **Type**: `int`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimSystem.yaml`; include `Target system entity`; role `Target`

The risk level associated with the source. The value should be adjusted to a range of 0 to 100, with 0 for benign and 100 for a high risk. User the OriginalRiskLevel field for the value as reported or enriched.

### `TargetUrl`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Target`, `Dst`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Target application entity`; role `Target`

A URL associated with the application.

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
- **List of values**: `SrcIpAddr`, `DstIpAddr`
- **Follows**: [`ThreatIpAddr`](../fields/threat_ip_addr.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimInspectionFields.yaml`; include `Inspection fields`
- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The field for which a threat was identified. The value is either SrcFilePath or DstFilePath.

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

### `ThreatIpAddr`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `IP Address`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

An IP address for which a threat was identified. The field ThreatField contains the name of the field ThreatFilePath represents.

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
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

### `Value`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`NewValue`](../fields/new_value.md)

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

Alias to NewValue.

### `ValueType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `Other`

#### Provenance

- Local: `ASIM/schemas/ASimAuditEvent.yaml`

The type of the old and new values.
