# ProcessEvent

- **Version**: `0.1.5`
- **Last updated**: Mar 06, 2023
- **Source**: [`ASIM/schemas/ASimProcessEvent.yaml`](https://github.com/Azure/Azure-Sentinel/blob/0db4cc9a326a610d44000d6af1b7035432db74ba/ASIM/schemas/ASimProcessEvent.yaml)
- **Fields**: `146`

## References

- [ASIM Process Event Schema](https://aka.ms/ASimProcessEventDoc)
- [ASIM](https://aka.ms/AboutASIM)

## Includes

| Include | File | Role |
| --- | --- | --- |
| Enumerations | `ASIM/schemas/common/ASimEnumerations.yaml` |  |
| Event Fields | `ASIM/schemas/common/ASimEventFields.yaml` |  |
| Inspection fields | `ASIM/schemas/common/ASimInspectionFields.yaml` |  |
| Dvc | `ASIM/schemas/entities/ASimDvc.yaml` |  |
| Actor entity | `ASIM/schemas/entities/ASimActor.yaml` |  |
| Acting extended process entity | `ASIM/schemas/entities/ASimExtendedProcess.yaml` | `Acting` |
| Parent extended process entity | `ASIM/schemas/entities/ASimExtendedProcess.yaml` | `Parent` |
| Target user entity | `ASIM/schemas/entities/ASimUser.yaml` | `Target` |
| Target extended process entity | `ASIM/schemas/entities/ASimExtendedProcess.yaml` | `Target` |

## Resolved fields

| Field | Class | Type | Logical type | Values | Provenance |
| --- | --- | --- | --- | --- | --- |
| [`ActingProcessCommandLine`](../fields/acting_process_command_line.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessCreationTime`](../fields/acting_process_creation_time.md) | `Optional` | `datetime` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileCompany`](../fields/acting_process_file_company.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileDescription`](../fields/acting_process_file_description.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileInternalName`](../fields/acting_process_file_internal_name.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileOriginalName`](../fields/acting_process_file_original_name.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileProduct`](../fields/acting_process_file_product.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileSize`](../fields/acting_process_file_size.md) | `Optional` | `long` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessFileVersion`](../fields/acting_process_file_version.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessGuid`](../fields/acting_process_guid.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessId`](../fields/acting_process_id.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessIMPHASH`](../fields/acting_process_imphash.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessInjectedAddress`](../fields/acting_process_injected_address.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessIntegrityLevel`](../fields/acting_process_integrity_level.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessIsHidden`](../fields/acting_process_is_hidden.md) | `Optional` | `bool` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessMD5`](../fields/acting_process_md5.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessName`](../fields/acting_process_name.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessSHA1`](../fields/acting_process_sha1.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessSHA256`](../fields/acting_process_sha256.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessSHA512`](../fields/acting_process_sha512.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
| [`ActingProcessTokenElevation`](../fields/acting_process_token_elevation.md) | `Optional` | `string` |  |  | inherited from Acting extended process entity as Acting |
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
| [`CommandLine`](../fields/command_line.md) | `Alias` | `string` |  |  | local |
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
| [`EventResultDetails`](../fields/event_result_details.md) | `Recommended` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventSchema`](../fields/event_schema.md) | `Mandatory` | `string` | `Enumerated` | [ProcessEvent](../schemas/process_event.md) | local override |
| [`EventSchemaVersion`](../fields/event_schema_version.md) | `Mandatory` | `string` | `SchemaVersion` |  | inherited from Event Fields |
| [`EventSeverity`](../fields/event_severity.md) | `Recommended` | `string` | `Enumerated` | `Informational`, `Low`, `Medium`, `High` | inherited from Event Fields |
| [`EventStartTime`](../fields/event_start_time.md) | `Mandatory` | `datetime` |  |  | inherited from Event Fields |
| [`EventSubType`](../fields/event_sub_type.md) | `Optional` | `string` | `Enumerated` |  | inherited from Event Fields |
| [`EventType`](../fields/event_type.md) | `Mandatory` | `string` | `Enumerated` | `ProcessCreated`, `ProcessTerminated` | local override |
| [`EventVendor`](../fields/event_vendor.md) | `Mandatory` | `string` | `Enumerated` | [EventVendor](../enumerations.md#eventvendor) | inherited from Event Fields |
| [`Hash`](../fields/hash.md) | `Alias` | `string` |  |  | local |
| [`ParentProcessCommandLine`](../fields/parent_process_command_line.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessCreationTime`](../fields/parent_process_creation_time.md) | `Optional` | `datetime` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileCompany`](../fields/parent_process_file_company.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileDescription`](../fields/parent_process_file_description.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileInternalName`](../fields/parent_process_file_internal_name.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileOriginalName`](../fields/parent_process_file_original_name.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileProduct`](../fields/parent_process_file_product.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileSize`](../fields/parent_process_file_size.md) | `Optional` | `long` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessFileVersion`](../fields/parent_process_file_version.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessGuid`](../fields/parent_process_guid.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessId`](../fields/parent_process_id.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessIMPHASH`](../fields/parent_process_imphash.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessInjectedAddress`](../fields/parent_process_injected_address.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessIntegrityLevel`](../fields/parent_process_integrity_level.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessIsHidden`](../fields/parent_process_is_hidden.md) | `Optional` | `bool` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessMD5`](../fields/parent_process_md5.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessName`](../fields/parent_process_name.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessSHA1`](../fields/parent_process_sha1.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessSHA256`](../fields/parent_process_sha256.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessSHA512`](../fields/parent_process_sha512.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`ParentProcessTokenElevation`](../fields/parent_process_token_elevation.md) | `Optional` | `string` |  |  | inherited from Parent extended process entity as Parent |
| [`Process`](../fields/process.md) | `Alias` | `string` |  |  | local |
| [`Rule`](../fields/rule.md) | `Alias` | `string` |  |  | inherited from Inspection fields |
| [`RuleName`](../fields/rule_name.md) | `Optional` | `string` |  |  | inherited from Inspection fields |
| [`RuleNumber`](../fields/rule_number.md) | `Optional` | `int` |  |  | inherited from Inspection fields |
| [`Src`](../fields/src.md) | `Recommended` | `string` |  |  | inherited from Event Fields |
| [`TargetOriginalUserType`](../fields/target_original_user_type.md) | `Optional` | `string` |  |  | inherited from Target user entity as Target |
| [`TargetProcessCommandLine`](../fields/target_process_command_line.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessCreationTime`](../fields/target_process_creation_time.md) | `Optional` | `datetime` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileCompany`](../fields/target_process_file_company.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileDescription`](../fields/target_process_file_description.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileInternalName`](../fields/target_process_file_internal_name.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileOriginalName`](../fields/target_process_file_original_name.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileProduct`](../fields/target_process_file_product.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileSize`](../fields/target_process_file_size.md) | `Optional` | `long` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessFileVersion`](../fields/target_process_file_version.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessGuid`](../fields/target_process_guid.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessId`](../fields/target_process_id.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessIMPHASH`](../fields/target_process_imphash.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessInjectedAddress`](../fields/target_process_injected_address.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessIntegrityLevel`](../fields/target_process_integrity_level.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessIsHidden`](../fields/target_process_is_hidden.md) | `Optional` | `bool` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessMD5`](../fields/target_process_md5.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessName`](../fields/target_process_name.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessSHA1`](../fields/target_process_sha1.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessSHA256`](../fields/target_process_sha256.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessSHA512`](../fields/target_process_sha512.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
| [`TargetProcessTokenElevation`](../fields/target_process_token_elevation.md) | `Optional` | `string` |  |  | inherited from Target extended process entity as Target |
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
| [`User`](../fields/user.md) | `Alias` | `string` | `Username` |  | local |

## Fields

### `ActingProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### `ActingProcessCreationTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The date and time when the acting process was started.

### `ActingProcessFileCompany`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The company that created the acting process image file.

#### Examples

- `Microsoft`

### `ActingProcessFileDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The description embedded in the version information of the acting process image file.

#### Examples

- `Notepad++ - a free (GPL) source code editor`

### `ActingProcessFileInternalName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The product internal file name from the version information of the acting process image file.

#### Examples

- `extensions.dll`

### `ActingProcessFileOriginalName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The product original file name from the version information of the acting process image file.

#### Examples

- `Notepad++.exe`

### `ActingProcessFileProduct`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The product name from the version information in the acting process image file.

#### Examples

- `Notepad++`

### `ActingProcessFileSize`

- **Class**: `Optional`
- **Type**: `long`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The size of the file that ran the acting process.

### `ActingProcessFileVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The product version from the version information of the acting process image file.

#### Examples

- `7.9.5.0`

### `ActingProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### `ActingProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### `ActingProcessIMPHASH`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The Import Hash of all the library DLLs that are used by the acting process.

### `ActingProcessInjectedAddress`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The memory address in which the responsible acting process is stored.

### `ActingProcessIntegrityLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

Integrity levels determine the process level of protection or access.

#### Examples

- `High`

### `ActingProcessIsHidden`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

An indication of whether the acting process is in hidden mode.

### `ActingProcessMD5`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The MD5 hash of the acting process image file.

#### Examples

- `75a599802f1fa166cdadb360960b1dd0`

### `ActingProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### `ActingProcessSHA1`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The SHA-1 hash of the acting process image file.

#### Examples

- `d55c5a4df19b46db8c54c801c4665d3338acdab0`

### `ActingProcessSHA256`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The SHA-256 hash of the acting process image file.

#### Examples

- `e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274`

### `ActingProcessSHA512`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

The SHA-512 hash of the acting process image file.

#### Examples

- `3b7fc7cc370707c1df045c35342f3d64ea7076abd84f8a8c046a7cca2b85901689f3cf4bdc1f5fc232a60456cb9d2f48702bf8f8f1064f9bcc7d70edad9f860e`

### `ActingProcessTokenElevation`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Acting extended process entity`; role `Acting`

A token indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the acting process.

#### Examples

- `None`

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

### `CommandLine`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetProcessCommandLine`](../fields/target_process_command_line.md)

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Alias to TargetProcessCommandLine

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

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

Reason or details for the result reported in the EventResult field. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalResultDetails field.

### `EventSchema`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [ProcessEvent](../schemas/process_event.md)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimProcessEvent.yaml`

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
- **List of values**: `ProcessCreated`, `ProcessTerminated`

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`
- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Describes the operation reported by the record. Each schema documents the list of values valid for this field. The original, source specific, value is stored in the EventOriginalType field.

### `EventVendor`

- **Class**: `Mandatory`
- **Type**: `string`
- **Logical type**: `Enumerated`
- **List of values**: [EventVendor](../enumerations.md#eventvendor)

#### Provenance

- Inherited: `ASIM/schemas/common/ASimEventFields.yaml`; include `Event Fields`

The vendor of the product generating the event. The value should be one of the values listed in Vendors and Products.

### `Hash`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: `TargetProcessMD5, TargetProcessSHA1, TargetProcessSHA256, TargetProcessSHA512, TargetProcessIMPHASH`

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Alias to Target Process Hash

### `ParentProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### `ParentProcessCreationTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The date and time when the acting process was started.

### `ParentProcessFileCompany`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The company that created the acting process image file.

#### Examples

- `Microsoft`

### `ParentProcessFileDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The description embedded in the version information of the acting process image file.

#### Examples

- `Notepad++ - a free (GPL) source code editor`

### `ParentProcessFileInternalName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The product internal file name from the version information of the acting process image file.

#### Examples

- `extensions.dll`

### `ParentProcessFileOriginalName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The product original file name from the version information of the acting process image file.

#### Examples

- `Notepad++.exe`

### `ParentProcessFileProduct`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The product name from the version information in the acting process image file.

#### Examples

- `Notepad++`

### `ParentProcessFileSize`

- **Class**: `Optional`
- **Type**: `long`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The size of the file that ran the acting process.

### `ParentProcessFileVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The product version from the version information of the acting process image file.

#### Examples

- `7.9.5.0`

### `ParentProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### `ParentProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### `ParentProcessIMPHASH`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The Import Hash of all the library DLLs that are used by the acting process.

### `ParentProcessInjectedAddress`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The memory address in which the responsible acting process is stored.

### `ParentProcessIntegrityLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

Integrity levels determine the process level of protection or access.

#### Examples

- `High`

### `ParentProcessIsHidden`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

An indication of whether the acting process is in hidden mode.

### `ParentProcessMD5`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The MD5 hash of the acting process image file.

#### Examples

- `75a599802f1fa166cdadb360960b1dd0`

### `ParentProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### `ParentProcessSHA1`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The SHA-1 hash of the acting process image file.

#### Examples

- `d55c5a4df19b46db8c54c801c4665d3338acdab0`

### `ParentProcessSHA256`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The SHA-256 hash of the acting process image file.

#### Examples

- `e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274`

### `ParentProcessSHA512`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

The SHA-512 hash of the acting process image file.

#### Examples

- `3b7fc7cc370707c1df045c35342f3d64ea7076abd84f8a8c046a7cca2b85901689f3cf4bdc1f5fc232a60456cb9d2f48702bf8f8f1064f9bcc7d70edad9f860e`

### `ParentProcessTokenElevation`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Parent extended process entity`; role `Parent`

A token indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the acting process.

#### Examples

- `None`

### `Process`

- **Class**: `Alias`
- **Type**: `string`
- **Aliases**: [`TargetProcessName`](../fields/target_process_name.md)

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`

Alias to TargetProcessName

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

### `TargetOriginalUserType`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimUser.yaml`; include `Target user entity`; role `Target`

TBD

### `TargetProcessCommandLine`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The command line used to run the process.

#### Examples

- `choco.exe -v`

### `TargetProcessCreationTime`

- **Class**: `Optional`
- **Type**: `datetime`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The date and time when the acting process was started.

### `TargetProcessFileCompany`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The company that created the acting process image file.

#### Examples

- `Microsoft`

### `TargetProcessFileDescription`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The description embedded in the version information of the acting process image file.

#### Examples

- `Notepad++ - a free (GPL) source code editor`

### `TargetProcessFileInternalName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The product internal file name from the version information of the acting process image file.

#### Examples

- `extensions.dll`

### `TargetProcessFileOriginalName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The product original file name from the version information of the acting process image file.

#### Examples

- `Notepad++.exe`

### `TargetProcessFileProduct`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The product name from the version information in the acting process image file.

#### Examples

- `Notepad++`

### `TargetProcessFileSize`

- **Class**: `Optional`
- **Type**: `long`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The size of the file that ran the acting process.

### `TargetProcessFileVersion`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The product version from the version information of the acting process image file.

#### Examples

- `7.9.5.0`

### `TargetProcessGuid`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

A generated unique identifier (GUID) of the process. Enables identifying the process across systems.

#### Examples

- `EF3BD0BD-2B74-60C5-AF5C-010000001E00`

### `TargetProcessId`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The process ID (PID) of the process. The type is defined as string to support varying systems, but on Windows and Linux this value must be numeric. If you are using a Windows or Linux machine and used a different type, make sure to convert the values. For example, if you used a hexadecimal value, convert it to a decimal value.

#### Examples

- `48610176`

### `TargetProcessIMPHASH`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The Import Hash of all the library DLLs that are used by the acting process.

### `TargetProcessInjectedAddress`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The memory address in which the responsible acting process is stored.

### `TargetProcessIntegrityLevel`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

Integrity levels determine the process level of protection or access.

#### Examples

- `High`

### `TargetProcessIsHidden`

- **Class**: `Optional`
- **Type**: `bool`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

An indication of whether the acting process is in hidden mode.

### `TargetProcessMD5`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The MD5 hash of the acting process image file.

#### Examples

- `75a599802f1fa166cdadb360960b1dd0`

### `TargetProcessName`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The name of the process. This name is commonly derived from the image or executable file that's used to define the initial code and data that's mapped into the process' virtual address space.

#### Examples

- `C:\Windows\explorer.exe`

### `TargetProcessSHA1`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The SHA-1 hash of the acting process image file.

#### Examples

- `d55c5a4df19b46db8c54c801c4665d3338acdab0`

### `TargetProcessSHA256`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The SHA-256 hash of the acting process image file.

#### Examples

- `e81bb824c4a09a811af17deae22f22dd2e1ec8cbb00b22629d2899f7c68da274`

### `TargetProcessSHA512`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

The SHA-512 hash of the acting process image file.

#### Examples

- `3b7fc7cc370707c1df045c35342f3d64ea7076abd84f8a8c046a7cca2b85901689f3cf4bdc1f5fc232a60456cb9d2f48702bf8f8f1064f9bcc7d70edad9f860e`

### `TargetProcessTokenElevation`

- **Class**: `Optional`
- **Type**: `string`

#### Provenance

- Inherited: `ASIM/schemas/entities/ASimExtendedProcess.yaml`; include `Target extended process entity`; role `Target`

A token indicating the presence or absence of User Access Control (UAC) privilege elevation applied to the acting process.

#### Examples

- `None`

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

### `User`

- **Class**: `Alias`
- **Type**: `string`
- **Logical type**: `Username`
- **Aliases**: [`ActorUsername`](../fields/actor_username.md)

#### Provenance

- Local: `ASIM/schemas/ASimProcessEvent.yaml`
