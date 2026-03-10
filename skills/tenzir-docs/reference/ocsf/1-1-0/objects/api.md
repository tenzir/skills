# API

> The API, or Application Programming Interface, object represents  information pertaining to an API request and response.


The API, or Application Programming Interface, object represents information pertaining to an API request and response.

## Attributes

**`operation`**

* **Type**: `string_t`
* **Requirement**: required

Verb/Operation associated with the request

**`request`**

* **Type**: [`request`](request.md)
* **Requirement**: recommended

Details pertaining to the API request.

**`response`**

* **Type**: [`response`](response.md)
* **Requirement**: recommended

Details pertaining to the API response.

**`group`**

* **Type**: [`group`](group.md)
* **Requirement**: optional

The information pertaining to the API group.

**`service`**

* **Type**: [`service`](service.md)
* **Requirement**: optional

The information pertaining to the API service.

**`version`**

* **Type**: `string_t`
* **Requirement**: optional

The version of the API service.

## Used By

* [`account_change`](../classes/account_change.md)
* [`api_activity`](../classes/api_activity.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`base_event`](../classes/base_event.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`config_state`](../classes/config_state.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`device_config_state_change`](../classes/device_config_state_change.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`file_activity`](../classes/file_activity.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`incident_finding`](../classes/incident_finding.md)
* [`inventory_info`](../classes/inventory_info.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension`](../classes/kernel_extension.md)
* [`memory_activity`](../classes/memory_activity.md)
* [`module_activity`](../classes/module_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`patch_state`](../classes/patch_state.md)
* [`process_activity`](../classes/process_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`scan_activity`](../classes/scan_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`user_access`](../classes/user_access.md)
* [`user_inventory`](../classes/user_inventory.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)