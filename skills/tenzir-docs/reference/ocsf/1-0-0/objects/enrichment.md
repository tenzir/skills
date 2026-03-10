# Enrichment

> The Enrichment object provides inline enrichment data for specific attributes of interest within an event.


The Enrichment object provides inline enrichment data for specific attributes of interest within an event. It serves as a mechanism to enhance or supplement the information associated with the event by adding additional relevant details or context.

## Attributes

**`data`**

* **Type**: `json_t`
* **Requirement**: required

The enrichment data associated with the attribute and value. The meaning of this data depends on the type the enrichment record.

**`name`**

* **Type**: `string_t`
* **Requirement**: required

The name of the attribute to which the enriched data pertains.

**`value`**

* **Type**: `string_t`
* **Requirement**: required

The value of the attribute to which the enriched data pertains.

**`provider`**

* **Type**: `string_t`
* **Requirement**: recommended

The enrichment data provider name.

**`type`**

* **Type**: `string_t`
* **Requirement**: recommended

The enrichment type. For example: `location`.

## Used By

* [`account_change`](../classes/account_change.md)
* [`api_activity`](../classes/api_activity.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`base_event`](../classes/base_event.md)
* [`config_state`](../classes/config_state.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`file_activity`](../classes/file_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`inventory_info`](../classes/inventory_info.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension`](../classes/kernel_extension.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`module_activity`](../classes/module_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`process_activity`](../classes/process_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`user_access`](../classes/user_access.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)