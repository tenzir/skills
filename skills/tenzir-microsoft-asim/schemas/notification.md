# Notification

- **Version**: `0.1.0`
- **Last updated**: Apr 20, 2023
- **Source**: [`ASIM/schemas/ASimNotification.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/ASimNotification.yaml)
- **Fields**: `81`

## References

- [ASIM Notification Schema](https://aka.ms/ASimAuditNotification)
- [ASIM](https://aka.ms/AboutASIM)

## Includes

| Include | File | Role |
| --- | --- | --- |
| Enumerations | `ASIM/schemas/common/ASimEnumerations.yaml` |  |
| Event Fields | `ASIM/schemas/common/ASimEventFields.yaml` |  |
| Inspection fields | `ASIM/schemas/common/ASimInspectionFields.yaml` |  |
| Dvc | `ASIM/schemas/entities/ASimDvc.yaml` |  |
| Actor entity | `ASIM/schemas/entities/ASimActor.yaml` |  |
| Application entity | `ASIM/schemas/entities/ASimApp.yaml` |  |

## Resolved fields

| Field | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
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
| [`AppId`](../fields/app_id.md) | `Optional` | `string` |  |  | inherited from Application entity |
| [`Application`](../fields/application.md) | `Alias` | `string` |  |  | local |
| [`AppName`](../fields/app_name.md) | `Optional` | `string` |  |  | inherited from Application entity |
| [`AppType`](../fields/app_type.md) | `Conditional` | `string` | `Enumerated` | [AppType](../enumerations.md#apptype) | inherited from Application entity |
| [`AttackSubTechnique`](../fields/attack_sub_technique.md) | `Optional` | `string` | `enumerated` |  | local |
| [`AttackTactic`](../fields/attack_tactic.md) | `Optional` | `string` | `enumerated` |  | local |
| [`AttackTechnique`](../fields/attack_technique.md) | `Optional` | `string` | `enumerated` |  | local |
| [`AttackVersion`](../fields/attack_version.md) | `Optional` | `string` | `enumerated` | `v1`, `v2`, `v3`, `v4`, `v5`, `v6`, `v7`, `v7-beta`, `v8`, `v9`, `v10`, `v11`, `v12`, `v13` | local |
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
| [`EventRemediationSteps`](../fields/event_remediation_steps.md) | `Optional` | `dynamic` |  |  | local |
| [`EventReportUrl`](../fields/event_report_url.md) | `Optional` | `string` | `URL` |  | inherited from Event Fields |
| [`EventResult`](../fields/event_result.md) | `Mandatory` | `string` | `Enumerated` | `Success`, `Failure`, `Partial`, `NA` | inherited from Event Fields |
| [`EventResultDetails`](../fields/event_result_details.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventSchema`](../fields/event_schema.md) | `Mandatory` | `string` | `Enumerated` | [Notification](../schemas/notification.md) | local override |
| [`EventSchemaVersion`](../fields/event_schema_version.md) | `Mandatory` | `string` | `SchemaVersion` |  | inherited from Event Fields |
| [`EventSeverity`](../fields/event_severity.md) | `Recommended` | `string` | `Enumerated` | `Informational`, `Low`, `Medium`, `High` | inherited from Event Fields |
| [`EventStartTime`](../fields/event_start_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventSubType`](../fields/event_sub_type.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventType`](../fields/event_type.md) | `Mandatory` | `string` | `Enumerated` | `Alert`, `Other` | local override |
| [`EventVendor`](../fields/event_vendor.md) | `Mandatory` | `string` | `Enumerated` | [EventVendor](../enumerations.md#eventvendor) | inherited from Event Fields |
| [`IpAddr`](../fields/ip_addr.md) | `Alias` | `string` | `IP Address` |  | local |
| [`OriginalAppType`](../fields/original_app_type.md) | `Optional` | `string` |  |  | inherited from Application entity |
| [`Rule`](../fields/rule.md) | `Alias` | `string` |  |  | inherited from Inspection fields |
| [`RuleName`](../fields/rule_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`RuleNumber`](../fields/rule_number.md) | `Optional` | `int` |  |  | inherited from Inspection fields |
| [`Src`](../fields/src.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
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

### `AppId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Application entity`

The ID of the application, including a process, browser, or service.

### `Application`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`AppName`](../fields/app_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

Alias to AppName

### `AppName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Application entity`

The name of the application, including a service, a URL, or a SaaS application.

#### Examples

- `Exchange 365`

### `AppType`

- **Class**: `Conditional`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [AppType](../enumerations.md#apptype)
- **Follows**: [`AppName`](../fields/app_name.md)

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Application entity`

The type of the application.

### `AttackSubTechnique`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `enumerated`

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

The ATT&CK sub-technique associated with the notification

### `AttackTactic`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `enumerated`

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

The ATT&CK tactic associated with the notification

### `AttackTechnique`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `enumerated`

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

The ATT&CK technique associated with the notification

### `AttackVersion`

- **Class**: `Optional`
- **Type**: `string`
- **Logical type**: `enumerated`
- **List of values**: `v1`, `v2`, `v3`, `v4`, `v5`, `v6`, `v7`, `v7-beta`, `v8`, `v9`, `v10`, `v11`, `v12`, `v13`

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

The ATT&CK framework version associated with the other att&ck fields

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

### `EventRemediationSteps`

- **Class**: `Optional`
- **Type**: `dynamic`

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

List of actions to take to address the notification.

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
- **List of values**: [Notification](../schemas/notification.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimNotification.yaml`

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
- **List of values**: `Alert`, `Other`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimNotification.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations.md#eventvendor)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `IpAddr`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `IP Address`
- **Aliases**: [`DvcIpAddr`](../fields/dvc_ip_addr.md)

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`

Alias to DvcIpAddr

### `OriginalAppType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimApp.yaml`; include `Application entity`

The application type as reported by the reporting device.

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

- **Class**: `Recommended`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

A unique identifier of the source or acting device. This field might alias the ource or acting device device FQDN, Hostname, Device Id or IP address fields.

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
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimNotification.yaml`
