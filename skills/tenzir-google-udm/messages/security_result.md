# SecurityResult

Security related metadata for the event. A security result might be something like "virus detected and quarantined," "malicious connection blocked," or "sensitive data included in document foo.doc." Each security result, of which there may be more than one, may either pertain to the whole event, or to a specific object or device referenced in the event (e.g. a malicious file that was detected, or a sensitive document sent as an email attachment). For security results that apply to a particular object referenced in the event, the security_results message MUST contain details about the implicated object (such as process, user, IP, domain, URL, IP, or email address) in the about field. For security results that apply to the entire event (e.g. SPAM found in this email), the about field must remain empty.

- **Full name**: `google.backstory.SecurityResult`
- **Fields**: `48`
- **Nested messages**: `8`
- **Nested enums**: `11`

## Nested messages

- [SecurityResult.Association](security_result_association.md)
- [SecurityResult.Source](security_result_source.md)
- [SecurityResult.ProviderMLVerdict](security_result_provider_ml_verdict.md)
- [SecurityResult.AnalystVerdict](security_result_analyst_verdict.md)
- [SecurityResult.IoCStats](security_result_io_c_stats.md)
- [SecurityResult.VerdictInfo](security_result_verdict_info.md)
- [SecurityResult.Verdict](security_result_verdict.md)
- [SecurityResult.ThreatCollectionItem](security_result_threat_collection_item.md)

## Nested enums

- [SecurityResult.VerdictResponse](../enums/security_result_verdict_response.md)
- [SecurityResult.IoCStatsType](../enums/security_result_io_c_stats_type.md)
- [SecurityResult.VerdictType](../enums/security_result_verdict_type.md)
- [SecurityResult.SecurityCategory](../enums/security_result_security_category.md)
- [SecurityResult.AlertState](../enums/security_result_alert_state.md)
- [SecurityResult.Action](../enums/security_result_action.md)
- [SecurityResult.ProductSeverity](../enums/security_result_product_severity.md)
- [SecurityResult.ProductConfidence](../enums/security_result_product_confidence.md)
- [SecurityResult.ProductPriority](../enums/security_result_product_priority.md)
- [SecurityResult.ThreatStatus](../enums/security_result_threat_status.md)
- [SecurityResult.ThreatCollectionType](../enums/security_result_threat_collection_type.md)

## Fields

### `about`

- **Number**: `1`
- **Cardinality**: `singular`
- **Type**: [`Noun`](noun.md)
- **JSON name**: `about`

If the security result is about a specific entity (Noun), add it here. This field is not populated when the SecurityResult appears in a detection.

### `category`

- **Number**: `2`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.SecurityCategory`](../enums/security_result_security_category.md)
- **JSON name**: `category`

The security category. This field is not populated when the SecurityResult appears in a detection.

### `category_details`

- **Number**: `3`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `categoryDetails`

For vendor-specific categories. For web categorization, put type in here such as "gambling" or "porn". This field is not populated when the SecurityResult appears in a detection.

### `threat_name`

- **Number**: `4`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `threatName`

A vendor-assigned classification common across multiple customers (for example, "W32/File-A", "Slammer"). This field is not populated when the SecurityResult appears in a detection.

### `rule_set`

- **Number**: `29`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleSet`

The curated detection's rule set identifier. (for example, "windows-threats") This is primarily set in rule-generated detections and alerts.

### `rule_set_display_name`

- **Number**: `30`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleSetDisplayName`

The curated detections rule set display name. This is primarily set in rule-generated detections and alerts.

### `ruleset_category_display_name`

- **Number**: `41`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `rulesetCategoryDisplayName`

The curated detection rule set category display name. (for example, if rule_set_display_name is "CDIR SCC Enhanced Exfiltration", the rule_set_category is "Cloud Threats"). This is primarily set in rule-generated detections and alerts.

### `rule_id`

- **Number**: `16`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleId`

A vendor-specific ID for a rule, varying by observer type (e.g. "08123", "5d2b44d0-5ef6-40f5-a704-47d61d3babbe").

### `rule_name`

- **Number**: `5`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleName`

Name of the security rule (e.g. "BlockInboundToOracle").

### `display_name`

- **Number**: `49`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `displayName`

The display name of the security result. This is populated from 'name_override' Outcome Variable, if present. Otherwise, this field is not set.

### `rule_version`

- **Number**: `20`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleVersion`

Version of the security rule. (e.g. "v1.1", "00001", "1604709794", "2020-11-16T23:04:19+00:00"). Note that rule versions are source-dependant and lexical ordering should not be assumed.

### `rule_type`

- **Number**: `22`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleType`

The type of security rule.

### `rule_author`

- **Number**: `25`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `ruleAuthor`

Author of the security rule. This field is not populated when the SecurityResult appears in a detection.

### `rule_labels`

- **Number**: `26`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `ruleLabels`

A list of rule labels that can't be captured by the other fields in security result (e.g. "reference : AnotherRule", "contributor : John"). This is primarily set in rule-generated detections and alerts.

### `alert_state`

- **Number**: `21`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.AlertState`](../enums/security_result_alert_state.md)
- **JSON name**: `alertState`

The alerting types of this security result. This is primarily set for rule-generated detections and alerts.

### `detection_fields`

- **Number**: `23`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `detectionFields`

An ordered list of values, that represent fields in detections for a security finding. This list represents mapping of names of requested entities to their values (the security result matched variables).

For Collection SecurityResults, prefer variables instead.

### `outcomes`

- **Number**: `28`
- **Cardinality**: `repeated`
- **Type**: [`Label`](label.md)
- **JSON name**: `outcomes`
- **Deprecated**: `true`

A list of outcomes that represent the results of this security finding. This list represents a mapping of names of the requested outcomes, to a stringified version of their values.

This is only populated when the SecurityResult appears in a detection. This is deprecated. Use variables instead.

### `variables`

- **Number**: `44`
- **Cardinality**: `map`
- **Type**: map<`string`, [`FindingVariable`](finding_variable.md)>
- **JSON name**: `variables`

A list of outcomes and match variables that represent the results of this security finding. This list represents a mapping of names of the requested outcomes or match variables, to their values.

This is only populated when the SecurityResult appears in a detection.

### `summary`

- **Number**: `6`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `summary`

A short human-readable summary (e.g. "failed login occurred")

### `description`

- **Number**: `7`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `description`

A human-readable description (e.g. "user password was wrong"). This can be more detailed than the summary.

### `action`

- **Number**: `8`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Action`](../enums/security_result_action.md)
- **JSON name**: `action`

Actions taken for this event. This field is not populated when the SecurityResult appears in a detection.

### `action_details`

- **Number**: `19`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `actionDetails`

The detail of the action taken as provided by the vendor. This field is not populated when the SecurityResult appears in a detection.

### `severity`

- **Number**: `9`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ProductSeverity`](../enums/security_result_product_severity.md)
- **JSON name**: `severity`

The severity of the result.

### `confidence`

- **Number**: `10`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ProductConfidence`](../enums/security_result_product_confidence.md)
- **JSON name**: `confidence`

The confidence level of the result as estimated by the product. This field is not populated when the SecurityResult appears in a detection.

### `priority`

- **Number**: `11`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ProductPriority`](../enums/security_result_product_priority.md)
- **JSON name**: `priority`

The priority of the result. This field is not populated when the SecurityResult appears in a detection.

### `risk_score`

- **Number**: `31`
- **Cardinality**: `singular`
- **Type**: `float`
- **JSON name**: `riskScore`

The risk score of the security result.

### `confidence_score`

- **Number**: `42`
- **Cardinality**: `singular`
- **Type**: `float`
- **JSON name**: `confidenceScore`

The confidence score of the security result. This field is not populated when the SecurityResult appears in a detection.

### `analytics_metadata`

- **Number**: `43`
- **Cardinality**: `repeated`
- **Type**: [`AnalyticsMetadata`](analytics_metadata.md)
- **JSON name**: `analyticsMetadata`

Stores metadata about each risk analytic metric the rule uses. This field is not populated when the SecurityResult appears in a detection.

### `severity_details`

- **Number**: `12`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `severityDetails`

Vendor-specific severity. This field is not populated when the SecurityResult appears in a detection.

### `confidence_details`

- **Number**: `13`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `confidenceDetails`

Additional detail with regards to the confidence of a security event as estimated by the product vendor. This field is not populated when the SecurityResult appears in a detection.

### `priority_details`

- **Number**: `14`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `priorityDetails`

Vendor-specific information about the security result priority. This field is not populated when the SecurityResult appears in a detection.

### `url_back_to_product`

- **Number**: `15`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `urlBackToProduct`

URL that takes the user to the source product console for this event. This field is not populated when the SecurityResult appears in a detection.

### `threat_id`

- **Number**: `17`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `threatId`

Vendor-specific ID for a threat. This field is not populated when the SecurityResult appears in a detection.

### `threat_feed_name`

- **Number**: `27`
- **Cardinality**: `singular`
- **Type**: `string`
- **JSON name**: `threatFeedName`

Vendor feed name for a threat indicator feed. This field is not populated when the SecurityResult appears in a detection.

### `threat_id_namespace`

- **Number**: `24`
- **Cardinality**: `singular`
- **Type**: [`Id.Namespace`](../enums/id_namespace.md)
- **JSON name**: `threatIdNamespace`

The attribute threat_id_namespace qualifies threat_id with an id namespace to get an unique id. The attribute threat_id by itself is not unique across Chronicle as it is a vendor specific id. This field is not populated when the SecurityResult appears in a detection.

### `threat_status`

- **Number**: `18`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.ThreatStatus`](../enums/security_result_threat_status.md)
- **JSON name**: `threatStatus`

Current status of the threat This field is not populated when the SecurityResult appears in a detection.

### `attack_details`

- **Number**: `32`
- **Cardinality**: `singular`
- **Type**: [`AttackDetails`](attack_details.md)
- **JSON name**: `attackDetails`

MITRE ATT&CK details. This field is not populated when the SecurityResult appears in a detection.

### `first_discovered_time`

- **Number**: `33`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `firstDiscoveredTime`

First time the IoC threat was discovered in the provider. This field is not populated when the SecurityResult appears in a detection.

### `associations`

- **Number**: `34`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.Association`](security_result_association.md)
- **JSON name**: `associations`

Associations related to the threat.

### `campaigns`

- **Number**: `35`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `campaigns`
- **Deprecated**: `true`

Campaigns using this IOC threat. This is deprecated. Use threat_collections instead.

### `reports`

- **Number**: `46`
- **Cardinality**: `repeated`
- **Type**: `string`
- **JSON name**: `reports`
- **Deprecated**: `true`

Reports that reference this IOC threat. These are the report IDs. This is deprecated. Use threat_collections instead.

### `verdict`

- **Number**: `36`
- **Cardinality**: `singular`
- **Type**: [`SecurityResult.Verdict`](security_result_verdict.md)
- **JSON name**: `verdict`
- **Deprecated**: `true`

Verdict about the IoC from the provider. This field is now deprecated. Use VerdictInfo instead.

### `last_updated_time`

- **Number**: `37`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastUpdatedTime`

Last time the IoC threat was updated in the provider. This field is not populated when the SecurityResult appears in a detection.

### `verdict_info`

- **Number**: `38`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.VerdictInfo`](security_result_verdict_info.md)
- **JSON name**: `verdictInfo`

Verdict information about the IoC from the provider. This field is not populated when the SecurityResult appears in a detection.

### `threat_verdict`

- **Number**: `39`
- **Cardinality**: `singular`
- **Type**: [`ThreatVerdict`](../enums/threat_verdict.md)
- **JSON name**: `threatVerdict`

GCTI threat verdict on the security result entity. This field is not populated when the SecurityResult appears in a detection.

### `last_discovered_time`

- **Number**: `40`
- **Cardinality**: `singular`
- **Type**: `google.protobuf.Timestamp` (imported)
- **JSON name**: `lastDiscoveredTime`

Last time the IoC was seen in the provider data. This field is not populated when the SecurityResult appears in a detection.

### `detection_depth`

- **Number**: `47`
- **Cardinality**: `singular`
- **Type**: `int64`
- **JSON name**: `detectionDepth`

The depth of the detection chain. Applies only to composite detections.

### `threat_collections`

- **Number**: `48`
- **Cardinality**: `repeated`
- **Type**: [`SecurityResult.ThreatCollectionItem`](security_result_threat_collection_item.md)
- **JSON name**: `threatCollections`

GTI collections associated with the security result.
