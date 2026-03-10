# Remediation

> The Remediation object describes the recommended remediation steps to address identified issue(s).


The Remediation object describes the recommended remediation steps to address identified issue(s).

## Attributes

**`desc`**

* **Type**: `string_t`
* **Requirement**: required

The description of the remediation strategy.

**`cis_controls`**

* **Type**: [`cis_control`](cis_control.md)
* **Requirement**: optional

An array of Center for Internet Security (CIS) Controls that can be optionally mapped to provide additional remediation details.

**`kb_article_list`**

* **Type**: [`kb_article`](kb_article.md)
* **Requirement**: optional

A list of KB articles or patches related to an endpoint. A KB Article contains metadata that describes the patch or an update.

**`kb_articles`**

* **Type**: `string_t`
* **Requirement**: optional

The KB article/s related to the entity. A KB Article contains metadata that describes the patch or an update.

**`references`**

* **Type**: `string_t`
* **Requirement**: optional

A list of supporting URL/s, references that help describe the remediation strategy.

## Used By

* [`application_security_posture_finding`](../classes/application_security_posture_finding.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`file_remediation_activity`](../classes/file_remediation_activity.md)
* [`iam_analysis_finding`](../classes/iam_analysis_finding.md)
* [`network_remediation_activity`](../classes/network_remediation_activity.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)