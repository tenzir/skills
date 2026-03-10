# Actor

> The Actor object contains details about the user, role, application, service, or process that initiated or performed a specific activity.


The Actor object contains details about the user, role, application, service, or process that initiated or performed a specific activity.

## Attributes

**`process`**

* **Type**: [`process`](process.md)
* **Requirement**: recommended

The process that initiated the activity.

**`user`**

* **Type**: [`user`](user.md)
* **Requirement**: recommended

The user that initiated the activity or the user context from which the activity was initiated.

**`app_name`**

* **Type**: `string_t`
* **Requirement**: optional

The client application or service that initiated the activity. This can be in conjunction with the `user` if present. Note that `app_name` is distinct from the `process` if present.

**`app_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of the client application or service that initiated the activity. This can be in conjunction with the `user` if present. Note that `app_name` is distinct from the `process.pid` or `process.uid` if present.

**`authorizations`**

* **Type**: [`authorization`](authorization.md)
* **Requirement**: optional

Provides details about an authorization, such as authorization outcome, and any associated policies related to the activity/event.

**`idp`**

* **Type**: [`idp`](idp.md)
* **Requirement**: optional

This object describes details about the Identity Provider used.

**`invoked_by`**

* **Type**: `string_t`
* **Requirement**: optional

The name of the service that invoked the activity as described in the event.

**`session`**

* **Type**: [`session`](session.md)
* **Requirement**: optional

The user session from which the activity was initiated.

## Constraints

At least one of: `process`, `user`, `invoked_by`, `session`, `app_name`, `app_uid`

## Used By

* [`account_change`](../classes/account_change.md)
* [`admin_group_query`](../classes/admin_group_query.md)
* [`api_activity`](../classes/api_activity.md)
* [`application_lifecycle`](../classes/application_lifecycle.md)
* [`authentication`](../classes/authentication.md)
* [`authorize_session`](../classes/authorize_session.md)
* [`compliance_finding`](../classes/compliance_finding.md)
* [`config_state`](../classes/config_state.md)
* [`data_security_finding`](../classes/data_security_finding.md)
* [`datastore_activity`](../classes/datastore_activity.md)
* [`detection_finding`](../classes/detection_finding.md)
* [`device_config_state_change`](../classes/device_config_state_change.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`email_activity`](../classes/email_activity.md)
* [`email_file_activity`](../classes/email_file_activity.md)
* [`email_url_activity`](../classes/email_url_activity.md)
* [`entity_management`](../classes/entity_management.md)
* [`event_log`](../classes/event_log.md)
* [`file_activity`](../classes/file_activity.md)
* [`file_hosting`](../classes/file_hosting.md)
* [`file_query`](../classes/file_query.md)
* [`file_remediation_activity`](../classes/file_remediation_activity.md)
* [`folder_query`](../classes/folder_query.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`group_management`](../classes/group_management.md)
* [`http_activity`](../classes/http_activity.md)
* [`inventory_info`](../classes/inventory_info.md)
* [`job_query`](../classes/job_query.md)
* [`kernel_activity`](../classes/kernel_activity.md)
* [`kernel_extension`](../classes/kernel_extension.md)
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
* [`patch_state`](../classes/patch_state.md)
* [`peripheral_device_query`](../classes/peripheral_device_query.md)
* [`process_activity`](../classes/process_activity.md)
* [`process_query`](../classes/process_query.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)
* [`scan_activity`](../classes/scan_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`service_query`](../classes/service_query.md)
* [`session_query`](../classes/session_query.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`software_info`](../classes/software_info.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`user_access`](../classes/user_access.md)
* [`user_inventory`](../classes/user_inventory.md)
* [`user_query`](../classes/user_query.md)
* [`vulnerability_finding`](../classes/vulnerability_finding.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)