# User Management

- **Version**: `0.1.1`
- **Last updated**: Sept 12 2023
- **Source**: [`ASIM/schemas/ASimUserManagement.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/ASimUserManagement.yaml)
- **Fields**: `114`

## References

- [ASIM Authentication Schema](https://aka.ms/ASimUserManagementDoc)
- [ASIM](https://aka.ms/AboutASIM)

## Includes

| Include | File | Role |
| --- | --- | --- |
| Enumerations | `ASIM/schemas/common/ASimEnumerations.yaml` |  |
| Event Fields | `ASIM/schemas/common/ASimEventFields.yaml` |  |
| Inspection fields | `ASIM/schemas/common/ASimInspectionFields.yaml` |  |
| Dvc | `ASIM/schemas/entities/ASimDvc.yaml` |  |
| Actor entity | `ASIM/schemas/entities/ASimActor.yaml` |  |
| Acting application entity | `ASIM/schemas/entities/ASimApp.yaml` | `Acting` |
| Source system entity | `ASIM/schemas/entities/ASimSystem.yaml` | `Src` |
| Target user entity | `ASIM/schemas/entities/ASimUser.yaml` | `Target` |
| Target Group | `ASIM/schemas/entities/ASimGroup.yaml` | `Target` |

## Resolved fields

| Field | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [`ActingAppId`](../fields/acting_app_id.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`ActingAppName`](../fields/acting_app_name.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`ActingAppType`](../fields/acting_app_type.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations.md#apptype) | inherited from Acting application entity as Acting |
| [`ActingOriginalAppType`](../fields/acting_original_app_type.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`ActorOriginalUserType`](../fields/actor_original_user_type.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorScope`](../fields/actor_scope.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorScopeId`](../fields/actor_scope_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorSessionId`](../fields/actor_session_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserAadId`](../fields/actor_user_aad_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserId`](../fields/actor_user_id.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserIdType`](../fields/actor_user_id_type.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations.md#useridtype) | inherited from Actor entity |
| [`ActorUsername`](../fields/actor_username.md) | `Recommended` | `string` | `Username` |  | inherited from Actor entity |
| [`ActorUsernameType`](../fields/actor_username_type.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations.md#usernametype) | inherited from Actor entity |
| [`ActorUserSid`](../fields/actor_user_sid.md) | `Optional` | `string` |  |  | inherited from Actor entity |
| [`ActorUserType`](../fields/actor_user_type.md) | `Optional` | `string` | `Enumerated` | [UserType](../enumerations.md#usertype) | inherited from Actor entity |
| [`AdditionalFields`](../fields/additional_fields.md) | `Recommended` | `dynamic` |  |  | inherited from Event Fields |
| [`Dst`](../fields/dst.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [`Dvc`](../fields/dvc.md) | `Alias` | `string` |  |  | inherited from Dvc |
| [`DvcAction`](../fields/dvc_action.md) | `Recommended` | `string` |  |  | inherited from Dvc |
| [`DvcDescription`](../fields/dvc_description.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcDomain`](../fields/dvc_domain.md) | `Recommended` | `string` |  |  | inherited from Dvc |
| [`DvcDomainType`](../fields/dvc_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations.md#domaintype) | inherited from Dvc |
| [`DvcFQDN`](../fields/dvc_fqdn.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcHostname`](../fields/dvc_hostname.md) | `Recommended` | `string` | `Hostname` |  | inherited from Dvc |
| [`DvcId`](../fields/dvc_id.md) | `Optional` | `string` |  |  | inherited from Dvc |
| [`DvcIdType`](../fields/dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations.md#dvcidtype) | inherited from Dvc |
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
| [`EventProduct`](../fields/event_product.md) | `Mandatory` | `string` | `Enumerated` | [EventProduct](../enumerations.md#eventproduct) | inherited from Event Fields |
| [`EventProductVersion`](../fields/event_product_version.md) | `Optional` | `string` |  |  | inherited from Event Fields |
| [`EventReportUrl`](../fields/event_report_url.md) | `Optional` | `string` | `URL` |  | inherited from Event Fields |
| [`EventResult`](../fields/event_result.md) | `Mandatory` | `string` | `Enumerated` | `Success`, `Failure`, `Partial`, `NA` | inherited from Event Fields |
| [`EventResultDetails`](../fields/event_result_details.md) | `Recommended` | `string` | `Enumerated` | `NotAuthorized`, `Other` | local override |
| [`EventSchema`](../fields/event_schema.md) | `Mandatory` | `string` | `Enumerated` | `UserManagement` | local override |
| [`EventSchemaVersion`](../fields/event_schema_version.md) | `Mandatory` | `string` | `SchemaVersion` |  | inherited from Event Fields |
| [`EventSeverity`](../fields/event_severity.md) | `Recommended` | `string` | `Enumerated` | `Informational`, `Low`, `Medium`, `High` | inherited from Event Fields |
| [`EventStartTime`](../fields/event_start_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventSubType`](../fields/event_sub_type.md) | `Optional` | `string` | `Enumerated` | `Password`, `Hash` | local override |
| [`EventType`](../fields/event_type.md) | `Mandatory` | `string` | `Enumerated` | `UserCreated`, `UserDeleted`, `UserModified`, `UserLocked`, `UserUnlocked`, `UserDisabled`, `UserEnabled`, `PasswordChanged`, `PasswordReset`, `GroupCreated`, `GroupDeleted`, `GroupModified`, `UserAddedToGroup`, `UserRemovedFromGroup`, `GroupEnumerated`, `UserRead`, `GroupRead` | local override |
| [`EventVendor`](../fields/event_vendor.md) | `Mandatory` | `string` | `Enumerated` | [EventVendor](../enumerations.md#eventvendor) | inherited from Event Fields |
| [`GroupId`](../fields/group_id.md) | `Optional` | `string` |  |  | inherited from Target Group as Target |
| [`GroupIdType`](../fields/group_id_type.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Target Group as Target |
| [`GroupName`](../fields/group_name.md) | `Optional` | `string` |  |  | inherited from Target Group as Target |
| [`GroupNameType`](../fields/group_name_type.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Target Group as Target |
| [`GroupOriginalType`](../fields/group_original_type.md) | `Optional` | `string` |  |  | inherited from Target Group as Target |
| [`GroupType`](../fields/group_type.md) | `Conditional` | `string` | `Enumerated` |  | inherited from Target Group as Target |
| [`Hostname`](../fields/hostname.md) | `Alias` | `string` |  |  | local |
| [`HttpUserAgent`](../fields/http_user_agent.md) | `Optional` | `string` |  |  | inherited from Acting application entity as Acting |
| [`NewPropertyValue`](../fields/new_property_value.md) | `Optional` | `string` |  |  | local |
| [`PreviousPropertyValue`](../fields/previous_property_value.md) | `Optional` | `string` |  |  | local |
| [`Rule`](../fields/rule.md) | `Alias` | `string` |  |  | inherited from Inspection fields |
| [`RuleName`](../fields/rule_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`RuleNumber`](../fields/rule_number.md) | `Optional` | `int` |  |  | inherited from Inspection fields |
| [`Src`](../fields/src.md) | `Alias` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDescription`](../fields/src_description.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDeviceType`](../fields/src_device_type.md) | `Optional` | `string` | `Enumerated` | [DeviceType](../enumerations.md#devicetype) | inherited from Source system entity as Src |
| [`SrcDomain`](../fields/src_domain.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDomainType`](../fields/src_domain_type.md) | `Conditional` | `string` | `Enumerated` | [DomainType](../enumerations.md#domaintype) | inherited from Source system entity as Src |
| [`SrcDvcId`](../fields/src_dvc_id.md) | `Optional` | `string` |  |  | inherited from Source system entity as Src |
| [`SrcDvcIdType`](../fields/src_dvc_id_type.md) | `Conditional` | `string` | `Enumerated` | [DvcIdType](../enumerations.md#dvcidtype) | inherited from Source system entity as Src |
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
| [`TargetOriginalUserType`](../fields/target_original_user_type.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
| [`TargetUserId`](../fields/target_user_id.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
| [`TargetUserIdType`](../fields/target_user_id_type.md) | `Conditional` | `string` | `Enumerated` | [UserIdType](../enumerations.md#useridtype) | inherited from Target user entity as Target |
| [`TargetUsername`](../fields/target_username.md) | `Recommended` | `string` | `Username` |  | inherited from Target user entity as Target |
| [`TargetUsernameType`](../fields/target_username_type.md) | `Conditional` | `string` | `Enumerated` | [UsernameType](../enumerations.md#usernametype) | inherited from Target user entity as Target |
| [`TargetUserScope`](../fields/target_user_scope.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
| [`TargetUserScopeId`](../fields/target_user_scope_id.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
| [`TargetUserSessionId`](../fields/target_user_session_id.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
| [`TargetUserType`](../fields/target_user_type.md) | `Optional` | `string` | `Enumerated` | [UserType](../enumerations.md#usertype) | inherited from Target user entity as Target |
| [`TargetUserUid`](../fields/target_user_uid.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
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
| [`UpdatedPropertyName`](../fields/updated_property_name.md) | `Alias` | `string` |  |  | local |

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
- **List of values**: [AppType](../enumerations.md#apptype)
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
- **List of values**: [UserIdType](../enumerations.md#useridtype)
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
- **List of values**: [UsernameType](../enumerations.md#usernametype)
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
- **List of values**: [UserType](../enumerations.md#usertype)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimActor.yaml`; include `Actor entity`

### `AdditionalFields`

- **Class**: `Recommended`
- **Type**: `dynamic`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

### `Dst`

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the target or destination device. This field might alias the target or destination device FQDN, Hostname, Device Id or IP Address fields.

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
- **List of values**: [DomainType](../enumerations.md#domaintype)
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
- **List of values**: [DvcIdType](../enumerations.md#dvcidtype)
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
- **List of values**: [EventProduct](../enumerations.md#eventproduct)

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
- **List of values**: `NotAuthorized`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `UserManagement`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

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
- **List of values**: `Password`, `Hash`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

Describes a subdivision of the operation reported in the EventType field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalSubType field.

### `EventType`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: `UserCreated`, `UserDeleted`, `UserModified`, `UserLocked`, `UserUnlocked`, `UserDisabled`, `UserEnabled`, `PasswordChanged`, `PasswordReset`, `GroupCreated`, `GroupDeleted`, `GroupModified`, `UserAddedToGroup`, `UserRemovedFromGroup`, `GroupEnumerated`, `UserRead`, `GroupRead`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimUserManagement.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations.md#eventvendor)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `GroupId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimGroup.yaml`; include `Target Group`; role `Target`

A machine-readable, alphanumeric, unique representation of the group, for activities involving a group.

#### Examples

- `S-1-5-21-1377283216-344919071-3415362939-500`

### `GroupIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimGroup.yaml`; include `Target Group`; role `Target`

The type of the ID stored in the GroupId field.

#### Examples

- `SID`

### `GroupName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimGroup.yaml`; include `Target Group`; role `Target`

The group name, including domain information when available, for activities involving a group.

#### Examples

- `grp@contoso.com`

### `GroupNameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimGroup.yaml`; include `Target Group`; role `Target`

Specifies the type of the group name stored in the GroupName field.

#### Examples

- `UPN`

### `GroupOriginalType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimGroup.yaml`; include `Target Group`; role `Target`

The original group type, if provided by the source.

### `GroupType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimGroup.yaml`; include `Target Group`; role `Target`

The type of the group, for activities involving a group.

#### Examples

- `Global Security Enabled`

### `Hostname`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`DvcHostname`](../fields/dvc_hostname.md)

#### Provenance

- Local: `ASIM/schemas/ASimUserManagement.yaml`

Alias to DvcHostname

### `HttpUserAgent`

- **Class**: `Optional`
- **Type**: `string`
- **For roles**: `Actor`, `Src`, `Acting`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Acting application entity`; role `Acting`

The user agent header accosiated with the application, when communicating using HTTP or HTTPS.

### `NewPropertyValue`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimUserManagement.yaml`

The new value stored in the specified property.

### `PreviousPropertyValue`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Local: `ASIM/schemas/ASimUserManagement.yaml`

The previous value that was stored in the specified property.

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
- **List of values**: [DeviceType](../enumerations.md#devicetype)

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
- **List of values**: [DomainType](../enumerations.md#domaintype)
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
- **List of values**: [DvcIdType](../enumerations.md#dvcidtype)
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

### `TargetOriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

TBD

### `TargetUserId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

A machine-readable, alphanumeric, unique representation of the user.

#### Examples

- `S-1-12-1-4141952679-1282074057-627758481-2916039507`

### `TargetUserIdType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserIdType](../enumerations.md#useridtype)
- **Follows**: [`TargetUserId`](../fields/target_user_id.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### `TargetUsername`

- **Class**: `Recommended`
- **Type**: `string`
- **Logical type**: `Username`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

The user's username, including domain information when available.

### `TargetUsernameType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UsernameType](../enumerations.md#usernametype)
- **Follows**: [`SrcUsername`](../fields/src_username.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### `TargetUserScope`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

The scope, such as Azure AD tenant, in which UserId and Username are defined.

### `TargetUserScopeId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

The scope ID, such as Azure AD tenant ID, in which UserId and Username are defined.

### `TargetUserSessionId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

The unique ID of the sign-in session of the user.

#### Examples

- `102pTUgC3p8RIqHvzxLCHnFlg`

### `TargetUserType`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [UserType](../enumerations.md#usertype)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

### `TargetUserUid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

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

### `UpdatedPropertyName`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`EventSubType`](../fields/event_sub_type.md)

#### Provenance

- Local: `ASIM/schemas/ASimUserManagement.yaml`

Alias to EventSubType
