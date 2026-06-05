# SecurityResult

Security related metadata for the event. A security result might be something like "virus detected and quarantined," "malicious connection blocked," or "sensitive data included in document foo.doc." Each security result, of which there may be more than one, may either pertain to the whole event, or to a specific object or device referenced in the event (e.g. a malicious file that was detected, or a sensitive document sent as an email attachment). For security results that apply to a particular object referenced in the event, the security_results message MUST contain details about the implicated object (such as process, user, IP, domain, URL, IP, or email address) in the about field. For security results that apply to the entire event (e.g. SPAM found in this email), the about field must remain empty.

## Fields

### `about`

- Type: [`Noun`](noun.md) (singular)

If the security result is about a specific entity (Noun), add it here. This field is not populated when the SecurityResult appears in a detection.

### `category`

- Type: [`SecurityCategory`](../enums/security_result_security_category.md) (repeated)

The security category. This field is not populated when the SecurityResult appears in a detection.

### `category_details` / `categoryDetails`

- Type: `string` (repeated)

For vendor-specific categories. For web categorization, put type in here such as "gambling" or "porn". This field is not populated when the SecurityResult appears in a detection.

### `threat_name` / `threatName`

- Type: `string` (singular)

A vendor-assigned classification common across multiple customers (for example, "W32/File-A", "Slammer"). This field is not populated when the SecurityResult appears in a detection.

### `rule_set` / `ruleSet`

- Type: `string` (singular)

The curated detection's rule set identifier. (for example, "windows-threats") This is primarily set in rule-generated detections and alerts.

### `rule_set_display_name` / `ruleSetDisplayName`

- Type: `string` (singular)

The curated detections rule set display name. This is primarily set in rule-generated detections and alerts.

### `ruleset_category_display_name` / `rulesetCategoryDisplayName`

- Type: `string` (singular)

The curated detection rule set category display name. (for example, if rule_set_display_name is "CDIR SCC Enhanced Exfiltration", the rule_set_category is "Cloud Threats"). This is primarily set in rule-generated detections and alerts.

### `rule_id` / `ruleId`

- Type: `string` (singular)

A vendor-specific ID for a rule, varying by observer type (e.g. "08123", "5d2b44d0-5ef6-40f5-a704-47d61d3babbe").

### `rule_name` / `ruleName`

- Type: `string` (singular)

Name of the security rule (e.g. "BlockInboundToOracle").

### `display_name` / `displayName`

- Type: `string` (singular)

The display name of the security result. This is populated from 'name_override' Outcome Variable, if present. Otherwise, this field is not set.

### `rule_version` / `ruleVersion`

- Type: `string` (singular)

Version of the security rule. (e.g. "v1.1", "00001", "1604709794", "2020-11-16T23:04:19+00:00"). Note that rule versions are source-dependant and lexical ordering should not be assumed.

### `rule_type` / `ruleType`

- Type: `string` (singular)

The type of security rule.

### `rule_author` / `ruleAuthor`

- Type: `string` (singular)

Author of the security rule. This field is not populated when the SecurityResult appears in a detection.

### `rule_labels` / `ruleLabels`

- Type: [`Label`](label.md) (repeated)

A list of rule labels that can't be captured by the other fields in security result (e.g. "reference : AnotherRule", "contributor : John"). This is primarily set in rule-generated detections and alerts.

### `alert_state` / `alertState`

- Type: [`AlertState`](../enums/security_result_alert_state.md) (singular)

The alerting types of this security result. This is primarily set for rule-generated detections and alerts.

### `detection_fields` / `detectionFields`

- Type: [`Label`](label.md) (repeated)

An ordered list of values, that represent fields in detections for a security finding. This list represents mapping of names of requested entities to their values (the security result matched variables).

For Collection SecurityResults, prefer variables instead.

### `outcomes`

- Type: [`Label`](label.md) (repeated)
- Deprecated: `true`

A list of outcomes that represent the results of this security finding. This list represents a mapping of names of the requested outcomes, to a stringified version of their values.

This is only populated when the SecurityResult appears in a detection. This is deprecated. Use variables instead.

### `variables`

- Type: map<`string`, [`FindingVariable`](finding_variable.md)> (map)

A list of outcomes and match variables that represent the results of this security finding. This list represents a mapping of names of the requested outcomes or match variables, to their values.

This is only populated when the SecurityResult appears in a detection.

### `summary`

- Type: `string` (singular)

A short human-readable summary (e.g. "failed login occurred")

### `description`

- Type: `string` (singular)

A human-readable description (e.g. "user password was wrong"). This can be more detailed than the summary.

### `action`

- Type: [`Action`](../enums/security_result_action.md) (repeated)

Actions taken for this event. This field is not populated when the SecurityResult appears in a detection.

### `action_details` / `actionDetails`

- Type: `string` (singular)

The detail of the action taken as provided by the vendor. This field is not populated when the SecurityResult appears in a detection.

### `severity`

- Type: [`ProductSeverity`](../enums/security_result_product_severity.md) (singular)

The severity of the result.

### `confidence`

- Type: [`ProductConfidence`](../enums/security_result_product_confidence.md) (singular)

The confidence level of the result as estimated by the product. This field is not populated when the SecurityResult appears in a detection.

### `priority`

- Type: [`ProductPriority`](../enums/security_result_product_priority.md) (singular)

The priority of the result. This field is not populated when the SecurityResult appears in a detection.

### `risk_score` / `riskScore`

- Type: `float` (singular)

The risk score of the security result.

### `confidence_score` / `confidenceScore`

- Type: `float` (singular)

The confidence score of the security result. This field is not populated when the SecurityResult appears in a detection.

### `analytics_metadata` / `analyticsMetadata`

- Type: [`AnalyticsMetadata`](analytics_metadata.md) (repeated)

Stores metadata about each risk analytic metric the rule uses. This field is not populated when the SecurityResult appears in a detection.

### `severity_details` / `severityDetails`

- Type: `string` (singular)

Vendor-specific severity. This field is not populated when the SecurityResult appears in a detection.

### `confidence_details` / `confidenceDetails`

- Type: `string` (singular)

Additional detail with regards to the confidence of a security event as estimated by the product vendor. This field is not populated when the SecurityResult appears in a detection.

### `priority_details` / `priorityDetails`

- Type: `string` (singular)

Vendor-specific information about the security result priority. This field is not populated when the SecurityResult appears in a detection.

### `url_back_to_product` / `urlBackToProduct`

- Type: `string` (singular)

URL that takes the user to the source product console for this event. This field is not populated when the SecurityResult appears in a detection.

### `threat_id` / `threatId`

- Type: `string` (singular)

Vendor-specific ID for a threat. This field is not populated when the SecurityResult appears in a detection.

### `threat_feed_name` / `threatFeedName`

- Type: `string` (singular)

Vendor feed name for a threat indicator feed. This field is not populated when the SecurityResult appears in a detection.

### `threat_id_namespace` / `threatIdNamespace`

- Type: [`Namespace`](../enums/id_namespace.md) (singular)

The attribute threat_id_namespace qualifies threat_id with an id namespace to get an unique id. The attribute threat_id by itself is not unique across Chronicle as it is a vendor specific id. This field is not populated when the SecurityResult appears in a detection.

### `threat_status` / `threatStatus`

- Type: [`ThreatStatus`](../enums/security_result_threat_status.md) (singular)

Current status of the threat This field is not populated when the SecurityResult appears in a detection.

### `attack_details` / `attackDetails`

- Type: [`AttackDetails`](attack_details.md) (singular)

MITRE ATT&CK details. This field is not populated when the SecurityResult appears in a detection.

### `first_discovered_time` / `firstDiscoveredTime`

- Type: `timestamp` (singular)

First time the IoC threat was discovered in the provider. This field is not populated when the SecurityResult appears in a detection.

### `associations`

- Type: [`Association`](security_result_association.md) (repeated)

Associations related to the threat.

### `campaigns`

- Type: `string` (repeated)
- Deprecated: `true`

Campaigns using this IOC threat. This is deprecated. Use threat_collections instead.

### `reports`

- Type: `string` (repeated)
- Deprecated: `true`

Reports that reference this IOC threat. These are the report IDs. This is deprecated. Use threat_collections instead.

### `verdict`

- Type: [`SecurityResult.Verdict`](security_result_verdict.md) (singular)
- Deprecated: `true`

Verdict about the IoC from the provider. This field is now deprecated. Use VerdictInfo instead.

### `last_updated_time` / `lastUpdatedTime`

- Type: `timestamp` (singular)

Last time the IoC threat was updated in the provider. This field is not populated when the SecurityResult appears in a detection.

### `verdict_info` / `verdictInfo`

- Type: [`VerdictInfo`](security_result_verdict_info.md) (repeated)

Verdict information about the IoC from the provider. This field is not populated when the SecurityResult appears in a detection.

### `threat_verdict` / `threatVerdict`

- Type: [`ThreatVerdict`](../enums/threat_verdict.md) (singular)

GCTI threat verdict on the security result entity. This field is not populated when the SecurityResult appears in a detection.

### `last_discovered_time` / `lastDiscoveredTime`

- Type: `timestamp` (singular)

Last time the IoC was seen in the provider data. This field is not populated when the SecurityResult appears in a detection.

### `detection_depth` / `detectionDepth`

- Type: `int64` (singular)

The depth of the detection chain. Applies only to composite detections.

### `threat_collections` / `threatCollections`

- Type: [`ThreatCollectionItem`](security_result_threat_collection_item.md) (repeated)

GTI collections associated with the security result.

## Guidance

Population guidance from the Google UDM usage guide.

### `about`

- **Purpose**: Provide a description of the security result.
- **Encoding**: Noun.

### `action`

- **Purpose**: Specify a security action.
- **Encoding**: Enumerated type.
- **Possible values**: Google SecOps UDM defines the following security actions:
  - `ALLOW`
  - `ALLOW_WITH_MODIFICATION`: File or email was disinfected or rewritten and still forwarded.
  - `BLOCK`
  - `QUARANTINE`: Store for later analysis (does not mean block).
  - `UNKNOWN_ACTION`

### `action_details` / `actionDetails`

- **Purpose**: Vendor-provided details of the action taken as a result of the security incident. Security actions often best translate into the more general `Security_Result.action` UDM field. However, you might need to write rules for the exact vendor-provided description of the action.
- **Encoding**: String.
- **Examples**: drop, block, decrypt, encrypt.

#### Examples

- drop, block, decrypt, encrypt.

### `category`

- **Purpose**: Specify a security category.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following security categories:
  - `ACL_VIOLATION`: Unauthorized access attempted, including attempted access to files, web services, processes, web objects, etc.
  - `AUTH_VIOLATION`: Authentication failed, such as a bad password or bad 2-factor authentication.
  - `DATA_AT_REST`: DLP: sensor data found at rest in a scan.
  - `DATA_DESTRUCTION`: Attempt to destroy/delete data.
  - `DATA_EXFILTRATION`: DLP: sensor data transmission, copy to thumb drive.
  - `EXPLOIT`: Attempted overflows, bad protocol encodings, ROP, SQL injection, etc, both network and host-based.
  - `MAIL_PHISHING`: Phishing email, chat messages, etc.
  - `MAIL_SPAM`: Spam email, message, etc.
  - `MAIL_SPOOFING`: Spoofed source email address, etc.
  - `NETWORK_CATEGORIZED_CONTENT`
  - `NETWORK_COMMAND_AND_CONTROL`: If the command and control channel is known.
  - `NETWORK_DENIAL_OF_SERVICE`
  - `NETWORK_MALICIOUS`: Command and control, network exploit, suspicious activity, potential reverse tunnel, etc.
  - `NETWORK_SUSPICIOUS`: Non-security related, for example, the URL is linked to gambling, etc.
  - `NETWORK_RECON`: Port scan detected by an IDS, probing by a web application.
  - `POLICY_VIOLATION`: Security policy violation, including firewall, proxy, and HIPS rule violations or NAC block actions.
  - `SOFTWARE_MALICIOUS`: Malware, spyware, rootkits, etc.
  - `SOFTWARE_PUA`: Potentially unwanted app, such as adware, etc.
  - `SOFTWARE_SUSPICIOUS`
  - `UNKNOWN_CATEGORY`

### `confidence`

- **Purpose**: Specify a confidence with regards to a security event as estimated by the product.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product confidence categories:
  - `UNKNOWN_CONFIDENCE`
  - `LOW_CONFIDENCE`
  - `MEDIUM_CONFIDENCE`
  - `HIGH_CONFIDENCE`

### `confidence_details` / `confidenceDetails`

- **Purpose**: Additional detail with regards to the confidence of a security event as estimated by the product vendor.
- **Encoding**: String.

### `priority`

- **Purpose**: Specify a priority with regards to a security event as estimated by the product vendor.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product priority categories:
  - `UNKNOWN_PRIORITY`
  - `LOW_PRIORITY`
  - `MEDIUM_PRIORITY`
  - `HIGH_PRIORITY`

### `priority_details` / `priorityDetails`

- **Purpose**: Vendor-specific information about the security result priority.
- **Encoding**: String.

### `rule_id` / `ruleId`

- **Purpose**: Identifier for the security rule.
- **Encoding**: String.

#### Examples

- 08123
- 5d2b44d0-5ef6-40f5-a704-47d61d3babbe

### `rule_name` / `ruleName`

- **Purpose**: Name of the security rule.
- **Encoding**: String.
- **Example**: BlockInboundToOracle.

#### Examples

- BlockInboundToOracle.

### `severity`

- **Purpose**: Severity of a security event as estimated by the product vendor using values defined by the Google SecOps UDM.
- **Encoding**: Enum.
- **Possible values**: Google SecOps UDM defines the following product severities:
  - `UNKNOWN_SEVERITY`: Non-malicious
  - `INFORMATIONAL`: Non-malicious
  - `ERROR`: Non-malicious
  - `LOW`: Malicious
  - `MEDIUM`: Malicious
  - `HIGH`: Malicious

### `severity_details` / `severityDetails`

- **Purpose**: Severity for a security event as estimated by the product vendor.
- **Encoding**: String.

### `threat_name` / `threatName`

- **Purpose**: Name of the security threat.
- **Encoding**: String.

#### Examples

- W32/File-A
- Slammer

### `url_back_to_product` / `urlBackToProduct`

- **Purpose**: URL to direct you to the source product console for this security event.
- **Encoding**: String.
