# Records

Record detail files are YAML leaves because UDM records have fixed
fields, type shapes, unions, maps, deprecation, and dual field-name
forms.

## Type Syntax

Each record YAML field key is the field-path name. The `type` value
uses a compact shape language:

- `T`: one scalar, enum, or record value of type `T`, for example
  `string`, `EventType`, or `SecurityResult`.
- `list<T>`: repeated values of `T`.
- `optional<T>`: optional value of `T`; the field may be absent.
- `map<K, V>`: lookup with data-defined keys of type `K` and values
  of type `V`.
- `variant`: value whose runtime shape is not fixed by the UDM schema.

Named record types are listed below. Enum values are listed in
[Enums](enums.md). `ingestion_name` appears only when Google SecOps
UDM ingestion uses a different field name than the YAML field key.
A `union` is a mutually exclusive field group; set at most one field
from the group. A record has schema-defined fields; a map has keys
supplied by the data.

## Record Index

- [UDM](records/udm.yaml) - A Unified Data Model event.
- [Metadata](records/metadata.yaml) - General information associated with a UDM event.
- [Attribute](records/attribute.yaml) - Attribute is a container for generic entity attributes including common attributes across core entities (such as, user or asset). For examp...
- [Network](records/network.yaml) - A network event.
- [ProxyInfo](records/proxy_info.yaml) - Proxy information.
- [Extensions](records/extensions.yaml) - Extensions to a UDM event.
- [Authentication](records/authentication.yaml) - The Authentication extension captures details specific to authentication events. General guidelines for authentication events: * Details ab...
- [LinuxUtmp](records/linux_utmp.yaml) - The LinuxUtmp extension captures details specific to Linux Utmp events.
- [WindowsEventLog](records/windows_event_log.yaml) - The WindowsEventLog extension captures details specific to Windows Event Log events.
- [ResourceUsage](records/resource_usage.yaml) - The ResourceUsage extension captures details about what is using a resource.
- [SystemEventDetails](records/system_event_details.yaml) - Captures additional details for system-level events.
- [OutlookMetadata](records/outlook_metadata.yaml) - Microsoft Outlook specific metadata.
- [Srum](records/srum.yaml) - The Srum extension captures details specific to Windows System Resource Usage Monitor (SRUM) events.
- [UserAssist](records/user_assist.yaml) - The UserAssist extension captures details specific to Windows User Assist events.
- [Vulnerabilities](records/vulnerabilities.yaml) - The Vulnerabilities extension captures details on observed/detected vulnerabilities.
- [Vulnerability](records/vulnerability.yaml) - A vulnerability.
- [Ftp](records/ftp.yaml) - FTP info.
- [Smtp](records/smtp.yaml) - SMTP info. See RFC 2821.
- [Email](records/email.yaml) - Email info.
- [Process](records/process.yaml) - Information about a process.
- [AnalyticsMetadata](records/analytics_metadata.yaml) - Stores information about an analytics metric used in a rule.
- [FindingVariable](records/finding_variable.yaml) - A record that holds the value and associated metadata for values extracted while producing a Finding.
- [SecurityResult](records/security_result.yaml) - Security related metadata for the event. A security result might be something like "virus detected and quarantined," "malicious connection...
- [Association](records/security_result_association.yaml) - Associations represents different metadata about malware and threat actors involved with an IoC.
- [AssociationAlias](records/security_result_association_association_alias.yaml) - Association Alias used to represent Mandiant Threat Intelligence.
- [Source](records/security_result_source.yaml) - Deprecated. Information about the threat intelligence source. These fields are used to model Mandiant sources.
- [ProviderMLVerdict](records/security_result_provider_ml_verdict.yaml) - Deprecated. MLVerdict result provided from threat providers, like Mandiant. These fields are used to model Mandiant sources.
- [AnalystVerdict](records/security_result_analyst_verdict.yaml) - Verdict provided by the human analyst. These fields are used to model Mandiant sources.
- [IoCStats](records/security_result_io_c_stats.yaml) - Information about the threat intelligence source. These fields are used to model Mandiant sources.
- [VerdictInfo](records/security_result_verdict_info.yaml) - Describes the threat verdict provided by human analysts and machine learning models. These fields are used to model Mandiant sources.
- [SecurityResult.Verdict](records/security_result_verdict.yaml) - Deprecated. Encapsulates the threat verdict provided by human analysts and ML models. These fields are used to model Mandiant sources.
- [ThreatCollectionItem](records/security_result_threat_collection_item.yaml) - Threat Collection that is either a threat campaign or a threat report.
- [PeFileMetadata](records/pe_file_metadata.yaml) - Metadata about a Microsoft Windows Portable Executable.
- [FileMetadata](records/file_metadata.yaml) - Metadata about a file. Place metadata about different file types here, for example data from the Microsoft Windows VersionInfo block or dig...
- [File](records/file.yaml) - Information about a file.
- [NtfsFileMetadata](records/ntfs_file_metadata.yaml) - NTFS-specific file metadata.
- [PrefetchFileMetadata](records/prefetch_file_metadata.yaml) - Windows Prefetch file metadata.
- [UsnJournal](records/usn_journal.yaml) - Information from the NTFS USN Journal.
- [AppCompatMetadata](records/app_compat_metadata.yaml) - Windows AppCompatCache (Application Compatibility) metadata.
- [FileMetadataPE](records/file_metadata_pe.yaml) - Metadata about the Portable Executable (PE) file.
- [FileMetadataPeResourceInfo](records/file_metadata_pe_resource_info.yaml) - File metadata for PE resource.
- [SignatureInfo](records/signature_info.yaml) - File signature information extracted from different tools.
- [FileMetadataSignatureInfo](records/file_metadata_signature_info.yaml) - Signature information.
- [SignerInfo](records/signer_info.yaml) - File metadata related to the signer information.
- [FileMetadataCodesign](records/file_metadata_codesign.yaml) - File metadata from the codesign utility.
- [X509](records/x509.yaml) - File certificate.
- [PDFInfo](records/pdf_info.yaml) - Information about the PDF file structure. See [https://developers.virustotal.com/reference/pdf_info](https://developers.virustotal.com/refe...
- [StringToInt64MapEntry](records/string_to_int64_map_entry.yaml)
- [FileMetadataSection](records/file_metadata_section.yaml) - File metadata section.
- [FileMetadataImports](records/file_metadata_imports.yaml) - File metadata imports.
- [ExifInfo](records/exif_info.yaml) - Exif information.
- [Prevalence](records/prevalence.yaml) - The prevalence of a resource within the customer's environment. This measures how common it is for assets to access the resource.
- [Dns](records/dns.yaml) - DNS information.
- [Question](records/dns_question.yaml) - DNS Questions. See RFC1035, section 4.1.2.
- [ResourceRecord](records/dns_resource_record.yaml) - DNS Resource Records. See RFC1035, section 4.1.3.
- [Dhcp](records/dhcp.yaml) - DHCP information.
- [Option](records/dhcp_option.yaml) - DHCP options.
- [Certificate](records/certificate.yaml) - Certificate information
- [Tls](records/tls.yaml) - Transport Layer Security (TLS) information.
- [Client](records/tls_client.yaml) - Transport Layer Security (TLS) information associated with the client (for example, Certificate or JA3 hash).
- [Server](records/tls_server.yaml) - Transport Layer Security (TLS) information associated with the server (for example, Certificate or JA3 hash).
- [Http](records/http.yaml) - Specify the full URL of the HTTP request within "target". Also specify any uploaded or downloaded file information within "source" or "targ...
- [Browser](records/browser.yaml) - Information about an entry in the web browser's local history database.
- [Cookie](records/browser_cookie.yaml) - Browser cookie.
- [Hardware](records/hardware.yaml) - Hardware specification details for a resource, including both physical and virtual hardware.
- [PlatformSoftware](records/platform_software.yaml) - Platform software information about an operating system.
- [Software](records/software.yaml) - Information about a software package or application.
- [Asset](records/asset.yaml) - Information about a compute asset such as a workstation, laptop, phone, virtual desktop, or VM.
- [User](records/user.yaml) - Information about a user.
- [TimeOff](records/time_off.yaml) - System record for leave/time-off from a Human Capital Management (HCM) system.
- [Permission](records/permission.yaml) - System permission for resource access and modification.
- [Role](records/role.yaml) - System role for resource access and modification.
- [Group](records/group.yaml) - Information about an organizational group.
- [Registry](records/registry.yaml) - Information about a registry key or value.
- [WmiPersistenceItem](records/wmi_persistence_item.yaml) - Information about a WMI persistence item.
- [Location](records/location.yaml) - Information about a location.
- [ScheduledTask](records/scheduled_task.yaml) - Deprecated: use WindowsScheduledTask for Windows scheduled tasks or ScheduledCronTask for cron jobs. Information about a scheduled task.
- [WindowsScheduledTask](records/windows_scheduled_task.yaml) - Information about a Windows scheduled task.
- [TaskAction](records/windows_scheduled_task_task_action.yaml) - The task action.
- [TaskTrigger](records/windows_scheduled_task_task_trigger.yaml) - The trigger of the scheduled task.
- [ScheduledCronTask](records/scheduled_cron_task.yaml) - Information about a scheduled cron task.
- [ScheduledAnacronTask](records/scheduled_anacron_task.yaml) - Information about a scheduled anacron task.
- [Volume](records/volume.yaml) - Information about a storage volume.
- [Service](records/service.yaml) - Information about a Windows service.
- [Resource](records/resource.yaml) - Information about a resource such as a task, Cloud Storage bucket, database, disk, logical policy, or something similar.
- [Label](records/label.yaml) - Key value labels.
- [Cloud](records/cloud.yaml) - Metadata related to the cloud environment.
- [Artifact](records/artifact.yaml) - Information about an artifact. The artifact can only be an IP.
- [Tunnels](records/tunnels.yaml) - VPN tunnels.
- [ArtifactClient](records/artifact_client.yaml) - Entity or software accessing or utilizing network resources.
- [Favicon](records/favicon.yaml) - Difference hash and MD5 hash of the domain's favicon.
- [DNSRecord](records/dns_record.yaml) - DNS record.
- [SSLCertificate](records/ssl_certificate.yaml) - SSL certificate.
- [CertSignature](records/ssl_certificate_cert_signature.yaml) - Certificate's signature and algorithm.
- [AuthorityKeyId](records/ssl_certificate_authority_key_id.yaml) - Identifies the public key to be used to verify the signature on this certificate or CRL.
- [Extension](records/ssl_certificate_extension.yaml) - Certificate's extensions.
- [Subject](records/ssl_certificate_subject.yaml) - Subject data.
- [RSA](records/ssl_certificate_rsa.yaml) - RSA public key information.
- [EC](records/ssl_certificate_ec.yaml) - EC public key information.
- [PublicKey](records/ssl_certificate_public_key.yaml) - Subject public key info.
- [Validity](records/ssl_certificate_validity.yaml) - Defines certificate's validity period.
- [PopularityRank](records/popularity_rank.yaml) - Domain's position in popularity ranks for sources such as Alexa, Quantcast, or Statvoo.
- [Tracker](records/tracker.yaml) - URL Tracker.
- [Url](records/url.yaml) - Url.
- [Domain](records/domain.yaml) - Information about a domain.
- [Noun](records/noun.yaml) - The Noun type is used to represent the different entities in an event: principal, src, target, observer, intermediary, and about. It stores...
- [Investigation](records/investigation.yaml) - Represents the aggregated state of an investigation such as categorization, severity, and status. Can be expanded to include analyst assign...
- [Tags](records/tags.yaml) - Tags are event metadata which is set by examining event contents post-parsing. For example, a UDM event may be assigned a tenant_id based o...
- [AttackDetails](records/attack_details.yaml) - MITRE ATT&CK details.
- [Tactic](records/attack_details_tactic.yaml) - Tactic information related to an attack or threat.
- [Technique](records/attack_details_technique.yaml) - Technique information related to an attack or threat.
- [BoolSequence](records/bool_sequence.yaml) - BoolSequence represents a sequence of bools.
- [BytesSequence](records/bytes_sequence.yaml) - BytesSequence represents a sequence of bytes.
- [DoubleSequence](records/double_sequence.yaml) - DoubleSequence represents a sequence of doubles.
- [Int64Sequence](records/int64_sequence.yaml) - Int64Sequence represents a sequence of int64s.
- [Uint64Sequence](records/uint64_sequence.yaml) - Uint64Sequence represents a sequence of uint64s.
- [StringSequence](records/string_sequence.yaml) - StringSequence represents a sequence of string.
- [GroupedFields](records/grouped_fields.yaml) - Grouped fields are aliases for groups of related UDM fields. All fields grouped together are of type string.
- [DataAccessIngestionLabel](records/data_access_ingestion_label.yaml) - Label used in data access for ingestion.
- [DataAccessLabels](records/data_access_labels.yaml) - Label used in data access.
- [EntityRisk](records/entity_risk.yaml) - Stores information related to the risk score of an entity.
- [RiskDelta](records/risk_delta.yaml) - Describes the difference in risk score between two points in time.
- [Id](records/id.yaml) - Identifier to identify a UDM object like a UDM event, Entity, Collection. The full identifier for persistence is created by setting the 32...
- [EntityMetadata](records/entity_metadata.yaml) - Information about the Entity and the product where the entity was created.
- [AtiPrioritization](records/ati_prioritization.yaml) - AtiPrioritization contains various fields used to calculate a priority score for an entity identified as a threat.
- [Entity](records/entity.yaml) - An Entity provides additional context about an item in a UDM event. For example, a PROCESS_LAUNCH event describes that user 'abc@example.co...
- [Relation](records/relation.yaml) - Defines the relationship between the entity (a) and another entity (b).
- [Metric](records/metric.yaml) - Stores precomputed aggregated analytic data for an entity.
- [Measure](records/metric_measure.yaml) - Describes the precomputed measure.
