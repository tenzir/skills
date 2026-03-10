# Firewall Rule

> The Firewall Rule object represents a specific rule within a firewall policy or event.


The Firewall Rule object represents a specific rule within a firewall policy or event. It contains information about a rule’s configuration, properties, and associated actions that define how network traffic is handled by the firewall.

* **Extends**: `rule`

## Attributes

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The name of the rule that generated the event.

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The unique identifier of the rule that generated the event.

**`category`**

* **Type**: `string_t`
* **Requirement**: optional

The rule category.

**`condition`**

* **Type**: `string_t`
* **Requirement**: optional

The rule trigger condition for the rule. For example: SQL\_INJECTION.

**`desc`**

* **Type**: `string_t`
* **Requirement**: optional

The description of the rule that generated the event.

**`duration`**

* **Type**: `integer_t`
* **Requirement**: optional

The rule response time duration, usually used for challenge completion time.

**`match_details`**

* **Type**: `string_t`
* **Requirement**: optional

The data in a request that rule matched. For example: ’\[“10”,“and”,“1”]’.

**`match_location`**

* **Type**: `string_t`
* **Requirement**: optional

The location of the matched data in the source which resulted in the triggered firewall rule. For example: HEADER.

**`rate_limit`**

* **Type**: `integer_t`
* **Requirement**: optional

The rate limit for a rate-based rule.

**`sensitivity`**

* **Type**: `string_t`
* **Requirement**: optional

The sensitivity of the firewall rule in the matched event. For example: HIGH.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The rule type.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The rule version. For example: `1.1`.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`file_activity`](../classes/file_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`http_activity`](../classes/http_activity.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension`](../classes/kernel_extension.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`module_activity`](../classes/module_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`process_activity`](../classes/process_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)