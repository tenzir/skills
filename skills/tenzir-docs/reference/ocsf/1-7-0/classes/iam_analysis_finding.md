# IAM Analysis Finding (2008)

> This finding represents an IAM analysis result, which evaluates IAM policies, access patterns, and IAM configurations for potential security risks.


This finding represents an IAM analysis result, which evaluates IAM policies, access patterns, and IAM configurations for potential security risks. The analysis can focus on either an identity (user, role, service account) or a resource to assess permissions, access patterns, and security posture within the IAM domain. Note: Use `permission_analysis_results` for identity-centric analysis (evaluating what an identity can do) and `access_analysis_result` for resource-centric analysis (evaluating who can access a resource). These complement each other for comprehensive IAM security assessment. Note: If the Finding is an incident, i.e. requires incident workflow, also apply the `incident` profile or aggregate this finding into an `Incident Finding`.

* **Category**: Findings
* **Extends**: `finding`
* **UID**: `2008`

## Attributes

### Classification

**`activity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event activity is unknown.
  * `1` - `Create`: A finding was created.
  * `2` - `Update`: A finding was updated.
  * `3` - `Close`: A finding was closed.
  * `99` - `Other`: The event activity is not mapped. See the `activity_name` attribute, which contains a data source specific value.

The normalized identifier of the finding activity.

**`category_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `2` - `Findings`: Findings events report findings, detections, and possible resolutions of malware, anomalies, or other actions performed by security products.

The category unique identifier of the event.

**`class_uid`**

* **Type**: `integer_t`
* **Requirement**: required
* **Values**:
  * `2008` - `IAM Analysis Finding`: This finding represents an IAM analysis result, which evaluates IAM policies, access patterns, and IAM configurations for potential security risks. The analysis can focus on either an identity (user, role, service account) or a resource to assess permissions, access patterns, and security posture within the IAM domain. Note: Use `permission_analysis_results` for identity-centric analysis (evaluating what an identity can do) and `access_analysis_result` for resource-centric analysis (evaluating who can access a resource). These complement each other for comprehensive IAM security assessment. Note: If the Finding is an incident, i.e. requires incident workflow, also apply the `incident` profile or aggregate this finding into an `Incident Finding`.

The unique identifier of a class. A class describes the attributes available in an event.

**`severity_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The event/finding severity is unknown.
  * `1` - `Informational`: Informational message. No action required.
  * `2` - `Low`: The user decides if action is needed.
  * `3` - `Medium`: Action is required but the situation is not serious at this time.
  * `4` - `High`: Action is required immediately.
  * `5` - `Critical`: Action is required immediately and the scope is broad.
  * `6` - `Fatal`: An error occurred but it is too late to take remedial action.
  * `99` - `Other`: The event/finding severity is not mapped. See the `severity` attribute, which contains a data source specific value.

The normalized identifier of the event/finding severity.The normalized severity is a measurement the effort and expense required to manage and resolve an event or incident. Smaller numerical values represent lower impact events, and larger numerical values represent higher impact events.

**`type_uid`**

* **Type**: `long_t`

* **Requirement**: required

* **Values**:

  * `200800` - `IAM Analysis Finding: Unknown`
  * `200801` - `IAM Analysis Finding: Create`: A finding was created.
  * `200802` - `IAM Analysis Finding: Update`: A finding was updated.
  * `200803` - `IAM Analysis Finding: Close`: A finding was closed.
  * `200899` - `IAM Analysis Finding: Other`

The event/finding type ID. It identifies the event’s semantics and structure. The value is calculated by the logging system as: `class_uid * 100 + activity_id`.

**`activity_name`**

* **Type**: `string_t`
* **Requirement**: optional

The finding activity name, as defined by the `activity_id`.

**`category_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event category name, as defined by category\_uid value: `Findings`.

**`class_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event class name, as defined by class\_uid value: `IAM Analysis Finding`.

**`severity`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding severity, normalized to the caption of the `severity_id` value. In the case of ‘Other’, it is defined by the source.

**`type_name`**

* **Type**: `string_t`
* **Requirement**: optional

The event/finding type name, as defined by the type\_uid.

### Context

**`metadata`**

* **Type**: [`metadata`](../objects/metadata.md)
* **Requirement**: required

The metadata associated with the event or a finding.

**`confidence_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The normalized confidence is unknown.
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `99` - `Other`: The confidence is not mapped to the defined enum values. See the `confidence` attribute, which contains a data source specific value.

The normalized confidence refers to the accuracy of the rule that created the finding. A rule with a low confidence means that the finding scope is wide and may create finding reports that may not be malicious in nature.

**`priority_id`** [incident](../profiles/incident.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: No priority is assigned.
  * `1` - `Low`: Application or personal procedure is unusable, where a workaround is available or a repair is possible.
  * `2` - `Medium`: Non-critical function or procedure is unusable or hard to use causing operational disruptions with no direct impact on a service’s availability. A workaround is available.
  * `3` - `High`: Critical functionality or network access is interrupted, degraded or unusable, having a severe impact on services availability. No acceptable alternative is possible.
  * `4` - `Critical`: Interruption making a critical functionality inaccessible or a complete network interruption causing a severe impact on services availability. There is no possible alternative.
  * `99` - `Other`: The priority is not normalized.

The normalized priority. Priority identifies the relative importance of the incident or finding. It is a measurement of urgency.

**`status_id`**

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The status is unknown.
  * `1` - `New`: The Finding is new and yet to be reviewed.
  * `2` - `In Progress`: The Finding is under review.
  * `3` - `Suppressed`: The Finding was reviewed, determined to be benign or a false positive and is now suppressed.
  * `4` - `Resolved`: The Finding was reviewed, remediated and is now considered resolved.
  * `5` - `Archived`: The Finding was archived.
  * `6` - `Deleted`: The Finding was deleted. For example, it might have been created in error.
  * `99` - `Other`: The status is not mapped. See the `status` attribute, which contains a data source specific value.

The normalized status identifier of the Finding, set by the consumer.

**`access_analysis_result`**

* **Type**: [`access_analysis_result`](../objects/access_analysis_result.md)
* **Requirement**: optional

Describes access relationships and pathways between identities, resources, focusing on who can access what and through which mechanisms. This evaluates access levels (read/write/admin), access types (direct, cross-account, public, federated), and the conditions under which access is granted. Use this for resource-centric security assessments such as external access discovery, public exposure analysis, etc.

**`api`** [cloud](../profiles/cloud.md)

* **Type**: [`api`](../objects/api.md)
* **Requirement**: optional

Describes details about a typical API (Application Programming Interface) call.

**`assignee`** [incident](../profiles/incident.md)

* **Type**: [`user`](../objects/user.md)
* **Requirement**: optional

The details of the user assigned to an Incident.

**`assignee_group`** [incident](../profiles/incident.md)

* **Type**: [`group`](../objects/group.md)
* **Requirement**: optional

The details of the group assigned to an Incident.

**`comment`**

* **Type**: `string_t`
* **Requirement**: optional

A user provided comment about the finding.

**`confidence`**

* **Type**: `string_t`
* **Requirement**: optional

The confidence, normalized to the caption of the confidence\_id value. In the case of ‘Other’, it is defined by the event source.

**`confidence_score`**

* **Type**: `integer_t`
* **Requirement**: optional

The confidence score as reported by the event source.

**`device`**

* **Type**: [`device`](../objects/device.md)
* **Requirement**: optional

Describes the affected device/host. If applicable, it can be used in conjunction with `Resource(s)`.

e.g. Specific details about an AWS EC2 instance, that is affected by the Finding.

**`enrichments`**

* **Type**: [`enrichment`](../objects/enrichment.md)
* **Requirement**: optional

The additional information from an external data source, which is associated with the event or a finding. For example add location information for the IP address in the DNS answers:`[{"name": "answers.ip", "value": "92.24.47.250", "type": "location", "data": {"city": "Socotra", "continent": "Asia", "coordinates": [-25.4153, 17.0743], "country": "YE", "desc": "Yemen"}}]`

**`is_suspected_breach`** [incident](../profiles/incident.md)

* **Type**: `boolean_t`
* **Requirement**: optional

A determination based on analytics as to whether a potential breach was found.

**`priority`** [incident](../profiles/incident.md)

* **Type**: `string_t`
* **Requirement**: optional

The priority, normalized to the caption of the priority\_id value. In the case of ‘Other’, it is defined by the event source.

**`raw_data`**

* **Type**: `string_t`
* **Requirement**: optional

The raw event/finding data as received from the source.

**`raw_data_hash`**

* **Type**: [`fingerprint`](../objects/fingerprint.md)
* **Requirement**: optional

The hash, which describes the content of the raw\_data field.

**`raw_data_size`**

* **Type**: `long_t`
* **Requirement**: optional

The size of the raw data which was transformed into an OCSF event, in bytes.

**`remediation`**

* **Type**: [`remediation`](../objects/remediation.md)
* **Requirement**: optional

Describes the recommended remediation steps to address identified issue(s).

**`risk_details`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

Describes the risk associated with the finding.

**`risk_level`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The risk level, normalized to the caption of the risk\_level\_id value.

**`risk_level_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: optional

* **Values**:

  * `0` - `Info`
  * `1` - `Low`
  * `2` - `Medium`
  * `3` - `High`
  * `4` - `Critical`
  * `99` - `Other`: The risk level is not mapped. See the `risk_level` attribute, which contains a data source specific value.

The normalized risk level id.

**`risk_score`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`
* **Requirement**: optional

The risk score as reported by the event source.

**`status`**

* **Type**: `string_t`
* **Requirement**: optional

The normalized status of the Finding set by the consumer normalized to the caption of the status\_id value. In the case of ‘Other’, it is defined by the source.

**`ticket`** [incident](../profiles/incident.md)

* **Type**: [`ticket`](../objects/ticket.md)
* **Requirement**: optional

The linked ticket in the ticketing system.

**`tickets`** [incident](../profiles/incident.md)

* **Type**: [`ticket`](../objects/ticket.md)
* **Requirement**: optional

The associated ticket(s) in the ticketing system. Each ticket contains details like ticket ID, status, etc.

**`unmapped`**

* **Type**: [`object`](../objects/object.md)
* **Requirement**: optional

The attributes that are not mapped to the event schema. The names and values of those attributes are specific to the event source.

**`vendor_attributes`**

* **Type**: [`vendor_attributes`](../objects/vendor_attributes.md)
* **Requirement**: optional

The Vendor Attributes object can be used to represent values of attributes populated by the Vendor/Finding Provider. It can help distinguish between the vendor-provided values and consumer-updated values, of key attributes like `severity_id`. The original finding producer should not populate this object. It should be populated by consuming systems that support data mutability.

### Occurrence

**`time`**

* **Type**: `timestamp_t`
* **Requirement**: required

The normalized event occurrence time or the finding creation time.

**`timezone_offset`**

* **Type**: `integer_t`
* **Requirement**: recommended

The number of minutes that the reported event `time` is ahead or behind UTC, in the range -1,080 to +1,080.

**`count`**

* **Type**: `integer_t`
* **Requirement**: optional

The number of times that events in the same logical group occurred during the event Start Time to End Time period.

**`duration`**

* **Type**: `long_t`
* **Requirement**: optional

The event duration or aggregate time, the amount of time the event covers from `start_time` to `end_time` in milliseconds.

**`end_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time of the most recent event included in the finding.

**`end_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The time of the most recent event included in the finding.

**`start_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The time of the least recent event included in the finding.

**`start_time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The time of the least recent event included in the finding.

**`time_dt`** [datetime](../profiles/datetime.md)

* **Type**: `datetime_t`
* **Requirement**: optional

The normalized event occurrence time or the finding creation time.

### Primary

**`cloud`** [cloud](../profiles/cloud.md)

* **Type**: [`cloud`](../objects/cloud.md)
* **Requirement**: required

Describes details about the Cloud environment where the event or finding was created.

**`finding_info`**

* **Type**: [`finding_info`](../objects/finding_info.md)
* **Requirement**: required

Describes the supporting information about a generated finding.

**`osint`** [osint](../profiles/osint.md)

* **Type**: [`osint`](../objects/osint.md)
* **Requirement**: required

The OSINT (Open Source Intelligence) object contains details related to an indicator such as the indicator itself, related indicators, geolocation, registrar information, subdomains, analyst commentary, and other contextual information. This information can be used to further enrich a detection or finding by providing decisioning support to other analysts and engineers.

**`action_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The action was unknown. The `disposition_id` attribute may still be set to a non-unknown value, for example ‘Custom Action’, ‘Challenge’.
  * `1` - `Allowed`: The activity was allowed. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Allowed’, ‘Approved’, ‘Delayed’, ‘No Action’, ‘Count’ etc.
  * `2` - `Denied`: The attempted activity was denied. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Blocked’, ‘Rejected’, ‘Quarantined’, ‘Isolated’, ‘Dropped’, ‘Access Revoked, etc.
  * `3` - `Observed`: The activity was observed, but neither explicitly allowed nor denied. This is common with IDS and EDR controls that report additional information on observed behavior such as TTPs. The `disposition_id` attribute should be set to a value that conforms to this action, for example ‘Logged’, ‘Alert’, ‘Detected’, ‘Count’, etc.
  * `4` - `Modified`: The activity was modified, adjusted, or corrected. The `disposition_id` attribute should be set appropriately, for example ‘Restored’, ‘Corrected’, ‘Delayed’, ‘Captcha’, ‘Tagged’.
  * `99` - `Other`: The action is not mapped. See the `action` attribute which contains a data source specific value.

The action taken by a control or other policy-based system leading to an outcome or disposition. An unknown action may still correspond to a known disposition. Refer to `disposition_id` for the outcome of the action.

**`applications`**

* **Type**: [`application`](../objects/application.md)
* **Requirement**: recommended

Details about applications, services, or systems that are accessible based on the IAM analysis. For identity-centric analysis, this represents applications the identity can access. For resource-centric analysis, this represents applications that can access the resource.

**`disposition_id`** [security\_control](../profiles/security_control.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The disposition is unknown.
  * `1` - `Allowed`: Granted access or allowed the action to the protected resource.
  * `2` - `Blocked`: Denied access or blocked the action to the protected resource.
  * `3` - `Quarantined`: A suspicious file or other content was moved to a benign location.
  * `4` - `Isolated`: A session was isolated on the network or within a browser.
  * `5` - `Deleted`: A file or other content was deleted.
  * `6` - `Dropped`: The request was detected as a threat and resulted in the connection being dropped.
  * `7` - `Custom Action`: A custom action was executed such as running of a command script. Use the `message` attribute of the base class for details.
  * `8` - `Approved`: A request or submission was approved. For example, when a form was properly filled out and submitted. This is distinct from `1` ‘Allowed’.
  * `9` - `Restored`: A quarantined file or other content was restored to its original location.
  * `10` - `Exonerated`: A suspicious or risky entity was deemed to no longer be suspicious (re-scored).
  * `11` - `Corrected`: A corrupt file or configuration was corrected.
  * `12` - `Partially Corrected`: A corrupt file or configuration was partially corrected.
  * `13` - `Uncorrected`: A corrupt file or configuration was not corrected.
  * `14` - `Delayed`: An operation was delayed, for example if a restart was required to finish the operation.
  * `15` - `Detected`: Suspicious activity or a policy violation was detected without further action.
  * `16` - `No Action`: The outcome of an operation had no action taken.
  * `17` - `Logged`: The operation or action was logged without further action.
  * `18` - `Tagged`: A file or other entity was marked with extended attributes.
  * `19` - `Alert`: The request or activity was detected as a threat and resulted in a notification but request was not blocked.
  * `20` - `Count`: Counted the request or activity but did not determine whether to allow it or block it.
  * `21` - `Reset`: The request was detected as a threat and resulted in the connection being reset.
  * `22` - `Captcha`: Required the end user to solve a CAPTCHA puzzle to prove that a human being is sending the request.
  * `23` - `Challenge`: Ran a silent challenge that required the client session to verify that it’s a browser, and not a bot.
  * `24` - `Access Revoked`: The requestor’s access has been revoked due to security policy enforcements. Note: use the `Host` profile if the `User` or `Actor` requestor is not present in the event class.
  * `25` - `Rejected`: A request or submission was rejected. For example, when a form was improperly filled out and submitted. This is distinct from `2` ‘Blocked’.
  * `26` - `Unauthorized`: An attempt to access a resource was denied due to an authorization check that failed. This is a more specific disposition than `2` ‘Blocked’ and can be complemented with the `authorizations` attribute for more detail.
  * `27` - `Error`: An error occurred during the processing of the activity or request. Use the `message` attribute of the base class for details.
  * `99` - `Other`: The disposition is not mapped. See the `disposition` attribute, which contains a data source specific value.

Describes the outcome or action taken by a security control, such as access control checks, malware detections or various types of policy violations.

**`identity_activity_metrics`**

* **Type**: [`identity_activity_metrics`](../objects/identity_activity_metrics.md)
* **Requirement**: recommended

Describes usage activity and other metrics of an Identity i.e. AWS IAM User, GCP IAM Principal, etc.

**`impact`** [incident](../profiles/incident.md)

* **Type**: `string_t`
* **Requirement**: recommended

The impact , normalized to the caption of the impact\_id value. In the case of ‘Other’, it is defined by the event source.

**`impact_id`** [incident](../profiles/incident.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The normalized impact is unknown.
  * `1` - `Low`: The magnitude of harm is low.
  * `2` - `Medium`: The magnitude of harm is moderate.
  * `3` - `High`: The magnitude of harm is high.
  * `4` - `Critical`: The magnitude of harm is high and the scope is widespread.
  * `99` - `Other`: The impact is not mapped. See the `impact` attribute, which contains a data source specific value.

The normalized impact of the incident or finding. Per NIST, this is the magnitude of harm that can be expected to result from the consequences of unauthorized disclosure, modification, destruction, or loss of information or information system availability.

**`impact_score`** [incident](../profiles/incident.md)

* **Type**: `integer_t`
* **Requirement**: recommended

The impact as an integer value of the finding, valid range 0-100.

**`is_alert`** [security\_control](../profiles/security_control.md)

* **Type**: `boolean_t`
* **Requirement**: recommended

Indicates that the event is considered to be an alertable signal. Should be set to `true` if `disposition_id = Alert` among other dispositions, and/or `risk_level_id` or `severity_id` of the event is elevated. Not all control events will be alertable, for example if `disposition_id = Exonerated` or `disposition_id = Allowed`.

**`message`**

* **Type**: `string_t`
* **Requirement**: recommended

The description of the event/finding, as defined by the source.

**`observables`**

* **Type**: [`observable`](../objects/observable.md)
* **Requirement**: recommended

The observables associated with the event or a finding.

**`permission_analysis_results`**

* **Type**: [`permission_analysis_result`](../objects/permission_analysis_result.md)
* **Requirement**: recommended

Describes analysis results of permissions, policies directly associated with an identity (user, role, or service account). This evaluates what permissions an identity has been granted through attached policies, which privileges are actively used versus unused, and identifies potential over-privileged access. Use this for identity-centric security assessments such as privilege audits, dormant permission discovery, and least-privilege compliance analysis.

**`resources`**

* **Type**: [`resource_details`](../objects/resource_details.md)
* **Requirement**: recommended

Details about resources involved in the IAM analysis. For identity-centric analysis, this represents resources the identity can access. For resource-centric analysis, this represents the resource being analyzed and related resources in the access chain.

**`src_url`** [incident](../profiles/incident.md)

* **Type**: `url_t`
* **Requirement**: recommended

A Url link used to access the original incident.

**`status_code`**

* **Type**: `string_t`
* **Requirement**: recommended

The event status code, as reported by the event source.

For example, in a Windows Failed Authentication event, this would be the value of ‘Failure Code’, e.g. 0x18.

**`status_detail`**

* **Type**: `string_t`
* **Requirement**: recommended

The status detail contains additional information about the event/finding outcome.

**`user`**

* **Type**: [`user`](../objects/user.md)
* **Requirement**: recommended

Details about the identity (user, role, service account, or other principal) that is the subject of the IAM analysis. This provides context about the identity being evaluated for security risks and access patterns.

**`verdict`** [incident](../profiles/incident.md)

* **Type**: `string_t`
* **Requirement**: recommended

The verdict assigned to an Incident finding.

**`verdict_id`** [incident](../profiles/incident.md)

* **Type**: `integer_t`

* **Requirement**: recommended

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `False Positive`: The incident is a false positive.
  * `2` - `True Positive`: The incident is a true positive.
  * `3` - `Disregard`: The incident can be disregarded as it is unimportant, an error or accident.
  * `4` - `Suspicious`: The incident is suspicious.
  * `5` - `Benign`: The incident is benign.
  * `6` - `Test`: The incident is a test.
  * `7` - `Insufficient Data`: The incident has insufficient data to make a verdict.
  * `8` - `Security Risk`: The incident is a security risk.
  * `9` - `Managed Externally`: The incident remediation or required actions are managed externally.
  * `10` - `Duplicate`: The incident is a duplicate.
  * `99` - `Other`: The type is not mapped. See the `type` attribute, which contains a data source specific value.

The normalized verdict of an Incident.

**`action`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The normalized caption of `action_id`.

**`actor`** [host](../profiles/host.md)

* **Type**: [`actor`](../objects/actor.md)
* **Requirement**: optional

The actor object describes details about the user/role/process that was the source of the activity. Note that this is not the threat actor of a campaign but may be part of a campaign.

**`attacks`** [security\_control](../profiles/security_control.md)

* **Type**: [`attack`](../objects/attack.md)
* **Requirement**: optional

An array of MITRE ATT\&CK® objects describing identified tactics, techniques & sub-techniques. The objects are compatible with MITRE ATLAS™ tactics, techniques & sub-techniques.

**`authorizations`** [security\_control](../profiles/security_control.md)

* **Type**: [`authorization`](../objects/authorization.md)
* **Requirement**: optional

Provides details about an authorization, such as authorization outcome, and any associated policies related to the activity/event.

**`disposition`** [security\_control](../profiles/security_control.md)

* **Type**: `string_t`
* **Requirement**: optional

The disposition name, normalized to the caption of the disposition\_id value. In the case of ‘Other’, it is defined by the event source.

**`firewall_rule`** [security\_control](../profiles/security_control.md)

* **Type**: [`firewall_rule`](../objects/firewall_rule.md)
* **Requirement**: optional

The firewall rule that pertains to the control that triggered the event, if applicable.

**`malware`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware`](../objects/malware.md)
* **Requirement**: optional

A list of Malware objects, describing details about the identified malware.

**`malware_scan_info`** [security\_control](../profiles/security_control.md)

* **Type**: [`malware_scan_info`](../objects/malware_scan_info.md)
* **Requirement**: optional

Describes details about the scan job that identified malware on the target system.

**`policy`** [security\_control](../profiles/security_control.md)

* **Type**: [`policy`](../objects/policy.md)
* **Requirement**: optional

The policy that pertains to the control that triggered the event, if applicable. For example the name of an anti-malware policy or an access control policy.

## Objects Used

* [`access_analysis_result`](../objects/access_analysis_result.md)
* [`actor`](../objects/actor.md)
* [`api`](../objects/api.md)
* [`application`](../objects/application.md)
* [`attack`](../objects/attack.md)
* [`authorization`](../objects/authorization.md)
* [`cloud`](../objects/cloud.md)
* [`device`](../objects/device.md)
* [`enrichment`](../objects/enrichment.md)
* [`finding_info`](../objects/finding_info.md)
* [`fingerprint`](../objects/fingerprint.md)
* [`firewall_rule`](../objects/firewall_rule.md)
* [`group`](../objects/group.md)
* [`identity_activity_metrics`](../objects/identity_activity_metrics.md)
* [`malware`](../objects/malware.md)
* [`malware_scan_info`](../objects/malware_scan_info.md)
* [`metadata`](../objects/metadata.md)
* [`object`](../objects/object.md)
* [`observable`](../objects/observable.md)
* [`osint`](../objects/osint.md)
* [`permission_analysis_result`](../objects/permission_analysis_result.md)
* [`policy`](../objects/policy.md)
* [`remediation`](../objects/remediation.md)
* [`resource_details`](../objects/resource_details.md)
* [`ticket`](../objects/ticket.md)
* [`user`](../objects/user.md)
* [`vendor_attributes`](../objects/vendor_attributes.md)