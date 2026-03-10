# OSINT

> The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information.


The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The indicator type is ambiguous or there is not a related indicator for the OSINT object.
  * `1` - `IP Address`: An IPv4 or IPv6 address.
  * `2` - `Domain`: A full-qualified domain name (FQDN), subdomain, or partial domain.
  * `3` - `Hostname`: A hostname or computer name.
  * `4` - `Hash`: Any type of hash e.g., MD5, SHA1, SHA2, BLAKE, BLAKE2, SSDEEP, VHASH, etc. generated from a file, malware sample, request header, or otherwise used to identify a pertinent artifact.
  * `5` - `URL`: A Uniform Resource Locator (URL) or Uniform Resource Indicator (URI).
  * `6` - `User Agent`: A User Agent typically seen in HTTP request headers.
  * `7` - `Digital Certificate`: The serial number, fingerprint, or full content of an X.509 digital certificate.
  * `8` - `Email`: The contents of an email or any related information to an email object.
  * `9` - `Email Address`: An email address.
  * `10` - `Vulnerability`: A CVE ID, CWE ID, or other identifier for a weakness, exploit, bug, or misconfiguration.
  * `11` - `File`: A file or metadata about a file.
  * `12` - `Registry Key`: A Windows Registry Key.
  * `13` - `Registry Value`: A Windows Registry Value.
  * `14` - `Command Line`: A partial or full Command Line used to invoke scripts or other remote commands.
  * `99` - `Other`: The indicator type is not directly listed.

The OSINT indicator type ID.

**`value`**

* **Type**: `string_t`
* **Requirement**: required

The actual indicator value in scope, e.g., a SHA-256 hash hexdigest or a domain name.

**`confidence_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The normalized confidence is unknown.
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `99` - `Other`: The confidence is not mapped to the defined enum values. See the `confidence` attribute, which contains a data source specific value.

The normalized confidence refers to the accuracy of collected information related to the OSINT or how pertinent an indicator or analysis is to a specific event or finding. A low confidence means that the information collected or analysis conducted lacked detail or is not accurate enough to qualify an indicator as fully malicious.

**`tlp`**

* **Type**: `string_t`

* **Requirement**: recommended

* **Values**:

  * `AMBER` - `TLP:AMBER`: TLP:AMBER is for limited disclosure, recipients can only spread this on a need-to-know basis within their organization and its clients. Note that TLP:AMBER+STRICT restricts sharing to the organization only. Sources may use TLP:AMBER when information requires support to be effectively acted upon, yet carries risk to privacy, reputation, or operations if shared outside of the organizations involved. Recipients may share TLP:AMBER information with members of their own organization and its clients, but only on a need-to-know basis to protect their organization and its clients and prevent further harm. Note: if the source wants to restrict sharing to the organization only, they must specify TLP:AMBER+STRICT.
  * `AMBER STRICT` - `TLP:AMBER+STRICT`: TLP:AMBER is for limited disclosure, recipients can only spread this on a need-to-know basis within their organization and its clients. Note that TLP:AMBER+STRICT restricts sharing to the organization only. Sources may use TLP:AMBER when information requires support to be effectively acted upon, yet carries risk to privacy, reputation, or operations if shared outside of the organizations involved. Recipients may share TLP:AMBER information with members of their own organization and its clients, but only on a need-to-know basis to protect their organization and its clients and prevent further harm. Note: if the source wants to restrict sharing to the organization only, they must specify TLP:AMBER+STRICT.
  * `CLEAR` - `TLP:CLEAR`: TLP:CLEAR denotes that recipients can spread this to the world, there is no limit on disclosure. Sources may use TLP:CLEAR when information carries minimal or no foreseeable risk of misuse, in accordance with applicable rules and procedures for public release. Subject to standard copyright rules, TLP:CLEAR information may be shared without restriction.
  * `GREEN` - `TLP:GREEN`: TLP:GREEN is for limited disclosure, recipients can spread this within their community. Sources may use TLP:GREEN when information is useful to increase awareness within their wider community. Recipients may share TLP:GREEN information with peers and partner organizations within their community, but not via publicly accessible channels. TLP:GREEN information may not be shared outside of the community. Note: when “community” is not defined, assume the cybersecurity/defense community.
  * `RED` - `TLP:RED`: TLP:RED is for the eyes and ears of individual recipients only, no further disclosure. Sources may use TLP:RED when information cannot be effectively acted upon without significant risk for the privacy, reputation, or operations of the organizations involved. Recipients may therefore not share TLP:RED information with anyone else. In the context of a meeting, for example, TLP:RED information is limited to those present at the meeting.
  * `WHITE` - `TLP:WHITE`: TLP:WHITE and TLP:CLEAR may be used interchangeably, TLP:WHITE is the most up to date (as of TLP 2.0) usage.

The [Traffic Light Protocol](https://www.first.org/tlp/) was created to facilitate greater sharing of potentially sensitive information and more effective collaboration. TLP provides a simple and intuitive schema for indicating with whom potentially sensitive information can be shared.

**`answers`**

* **Type**: [`dns_answer`](dns_answer.md)
* **Requirement**: optional

Any pertinent DNS answers information related to an indicator or OSINT analysis.

**`attacks`**

* **Type**: [`attack`](attack.md)
* **Requirement**: optional

MITRE ATT\&CK Tactics, Techniques, and/or Procedures (TTPs) pertinent to an indicator or OSINT analysis.

**`autonomous_system`**

* **Type**: [`autonomous_system`](autonomous_system.md)
* **Requirement**: optional

Any pertinent autonomous system information related to an indicator or OSINT analysis.

**`campaign`**

* **Type**: [`campaign`](campaign.md)
* **Requirement**: optional

The campaign object describes details about the campaign that was the source of the activity.

**`category`**

* **Type**: `string_t`
* **Requirement**: optional

Categorizes the threat indicator based on its functional or operational role.

**`comment`**

* **Type**: `string_t`
* **Requirement**: optional

Analyst commentary or source commentary about an indicator or OSINT analysis.

**`confidence`**

* **Type**: `string_t`
* **Requirement**: optional

The confidence of an indicator being malicious and/or pertinent, normalized to the caption of the confidence\_id value. In the case of ‘Other’, it is defined by the event source or analyst.

**`created_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The timestamp when the indicator was initially created or identified.

**`created_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The timestamp when the indicator was initially created or identified.

**`creator`**

* **Type**: [`user`](user.md)
* **Requirement**: optional

The identifier of the user, system, or organization that contributed the indicator.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

A detailed explanation of the indicator, including its context, purpose, and relevance.

**`detection_pattern`**

* **Type**: `string_t`
* **Requirement**: optional

The specific detection pattern or signature associated with the indicator.

**`detection_pattern_type`**

* **Type**: `string_t`
* **Requirement**: optional

The detection pattern type, normalized to the caption of the detection\_pattern\_type\_id value. In the case of ‘Other’, it is defined by the event source.

**`detection_pattern_type_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`: The type is not mapped.
  * `1` - `STIX`
  * `2` - `PCRE`
  * `3` - `SIGMA`
  * `4` - `Snort`
  * `5` - `Suricata`
  * `6` - `YARA`
  * `99` - `Other`: The detection pattern type is not mapped. See the `detection_pattern_type` attribute, which contains a data source specific value.

Specifies the type of detection pattern used to identify the associated threat indicator.

**`email`**

* **Type**: [`email`](email.md)
* **Requirement**: optional

Any email information pertinent to an indicator or OSINT analysis.

**`email_auth`**

* **Type**: [`email_auth`](email_auth.md)
* **Requirement**: optional

Any email authentication information pertinent to an indicator or OSINT analysis.

**`expiration_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The expiration date of the indicator, after which it is no longer considered reliable.

**`expiration_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The expiration date of the indicator, after which it is no longer considered reliable.

**`external_uid`**

* **Type**: `string_t`
* **Requirement**: optional

A unique identifier assigned by an external system for cross-referencing.

**`file`**

* **Type**: [`file`](file.md)
* **Requirement**: optional

Any pertinent file information related to an indicator or OSINT analysis.

**`intrusion_sets`**

* **Type**: `string_t`
* **Requirement**: optional

A grouping of adversarial behaviors and resources believed to be associated with specific threat actors or campaigns. Intrusion sets often encompass multiple campaigns and are used to organize related activities under a common label.

**`kill_chain`**

* **Type**: [`kill_chain_phase`](kill_chain_phase.md)
* **Requirement**: optional

Lockheed Martin Kill Chain Phases pertinent to an indicator or OSINT analysis.

**`labels`**

* **Type**: `string_t`
* **Requirement**: optional

Tags or keywords associated with the indicator to enhance searchability.

**`location`**

* **Type**: [`location`](location.md)
* **Requirement**: optional

Any pertinent geolocation information related to an indicator or OSINT analysis.

**`malware`**

* **Type**: [`malware`](malware.md)
* **Requirement**: optional

A list of Malware objects, describing details about the identified malware.

**`modified_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The timestamp of the last modification or update to the indicator.

**`modified_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The timestamp of the last modification or update to the indicator.

**`name`**

* **Type**: `string_t`
* **Requirement**: optional

The `name` is a pointer/reference to an attribute within the OCSF event data. For example: file.name.

**`references`**

* **Type**: `string_t`
* **Requirement**: optional

Provides a reference to an external source of information related to the CTI being represented. This may include a URL, a document, or some other type of reference that provides additional context or information about the CTI.

**`related_analytics`**

* **Type**: [`analytic`](analytic.md)
* **Requirement**: optional

Any analytics related to an indicator or OSINT analysis.

**`reputation`**

* **Type**: [`reputation`](reputation.md)
* **Requirement**: optional

Related reputational analysis from third-party engines and analysts for a given indicator or OSINT analysis.

**`risk_score`**

* **Type**: `integer_t`
* **Requirement**: optional

A numerical representation of the threat indicator’s risk level.

**`script`**

* **Type**: [`script`](script.md)
* **Requirement**: optional

Any pertinent script information related to an indicator or OSINT analysis.

**`severity`**

* **Type**: `string_t`
* **Requirement**: optional

Represents the severity level of the threat indicator, typically reflecting its potential impact or damage.

**`severity_id`**

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Unknown`: The event/finding severity is unknown.
  * `1` - `Informational`: Informational message. No action required.
  * `2` - `Low`: The user decides if action is needed.
  * `3` - `Medium`: Action is required but the situation is not serious at this time.
  * `4` - `High`: Action is required immediately.
  * `5` - `Critical`: Action is required immediately and the scope is broad.
  * `6` - `Fatal`: An error occurred but it is too late to take remedial action.
  * `99` - `Other`: The event/finding severity is not mapped. See the `severity` attribute, which contains a data source specific value.

The normalized severity level of the threat indicator, typically reflecting its potential impact or damage.

**`signatures`**

* **Type**: [`digital_signature`](digital_signature.md)
* **Requirement**: optional

Any digital signatures or hashes related to an indicator or OSINT analysis.

**`src_url`**

* **Type**: `url_t`
* **Requirement**: optional

The source URL of an indicator or OSINT analysis, e.g., a URL back to a TIP, report, or otherwise.

**`subdomains`**

* **Type**: `string_t`
* **Requirement**: optional

Any pertinent subdomain information - such as those generated by a Domain Generation Algorithm - related to an indicator or OSINT analysis.

**`subnet`**

* **Type**: `subnet_t`
* **Requirement**: optional

A CIDR or network block related to an indicator or OSINT analysis.

**`threat_actor`**

* **Type**: [`threat_actor`](threat_actor.md)
* **Requirement**: optional

A threat actor is an individual or group that conducts malicious cyber activities, often with financial, political, or ideological motives.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The OSINT indicator type.

**`uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier for the OSINT object.

**`uploaded_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The timestamp indicating when the associated indicator or intelligence was added to the system or repository.

**`uploaded_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The timestamp indicating when the associated indicator or intelligence was added to the system or repository.

**`vendor_name`**

* **Type**: `string_t`
* **Requirement**: optional

The vendor name of a tool which generates intelligence or provides indicators.

**`vulnerabilities`**

* **Type**: [`vulnerability`](vulnerability.md)
* **Requirement**: optional

Any vulnerabilities related to an indicator or OSINT analysis.

**`whois`**

* **Type**: [`whois`](whois.md)
* **Requirement**: optional

Any pertinent WHOIS information related to an indicator or OSINT analysis.

## Used By

* [`account_change`](../classes/account_change.md)
* [`admin_group_query`](../classes/admin_group_query.md)
* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`api_activity`](../classes/api_activity.md)
* [`application_error`](../classes/application_error.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`application_security_posture_finding`](../classes/application_security_posture_finding.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`base_event`](../classes/base_event.md)
* [`cloud_resources_inventory_info`](../classes/cloud_resources_inventory_info.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`config_state`](../classes/config_state.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`device_config_state_change`](../classes/device_config_state_change.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`event_log_actvity`](../classes/event_log_actvity.md)
* [`evidence_info`](../classes/evidence_info.md)
* [`file_activity`](../classes/file_activity.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`file_query`](../classes/file_query.md)
* [`file_remediation_activity`](../classes/file_remediation_activity.md)
* [`folder_query`](../classes/folder_query.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`iam_analysis_finding`](../classes/iam_analysis_finding.md)
* [`incident_finding`](../classes/incident_finding.md)
* [`inventory_info`](../classes/inventory_info.md)
* [`job_query`](../classes/job_query.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension_activity`](../classes/kernel_extension_activity.md)
* [`kernel_object_query`](../classes/kernel_object_query.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`module_activity`](../classes/module_activity.md)
* [`module_query`](../classes/module_query.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_connection_query`](../classes/network_connection_query.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`network_remediation_activity`](../classes/network_remediation_activity.md)
* [`networks_query`](../classes/networks_query.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`osint_inventory_info`](../classes/osint_inventory_info.md)
* [`patch_state`](../classes/patch_state.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)
* [`process_activity`](../classes/process_activity.md)
* [`process_query`](../classes/process_query.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)
* [`scan_activity`](../classes/scan_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`script_activity`](../classes/script_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`service_query`](../classes/service_query.md)
* [`session_query`](../classes/session_query.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`software_info`](../classes/software_info.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`startup_item_query`](../classes/startup_item_query.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`user_access`](../classes/user_access.md)
* [`user_inventory`](../classes/user_inventory.md)
* [`user_query`](../classes/user_query.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)