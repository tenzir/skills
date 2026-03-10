# Cloud

> The Cloud object describes the cloud computing environment where an event or finding originated.


The Cloud object describes the cloud computing environment where an event or finding originated. It provides comprehensive context about the cloud infrastructure, including the cloud service provider, account or subscription details, organizational structure, geographic regions, availability zones, and logical partitions.

## Attributes

**`provider`**

* **Type**: `string_t`
* **Requirement**: required

The unique name of the Cloud services provider where the event or finding was created, such as AWS, MS Azure, GCP, etc.

**`region`**

* **Type**: `string_t`
* **Requirement**: recommended

The cloud region where the event or finding was created, as defined by the cloud provider.

Examples:

* AWS: Region where the event occurred (`us-east-1`, `eu-west-1`)
* Azure: Region where the event occurred (`East US`, `West Europe`)
* GCP: Region where the event occurred (`us-central1`, `europe-west1`)
* Oracle Cloud: Region where the event occurred (`us-ashburn-1`, `uk-london-1`)

**`account`**

* **Type**: [`account`](account.md)
* **Requirement**: optional

The Account object containing details about the cloud account, subscription, or billing unit where the event or finding was created. This object includes properties such as the account name, unique identifier, type, labels, and tags.

Examples:

* AWS: Account object with `name`, `uid` (Account ID), `type`, and other account properties
* Azure: Subscription object with `name`, `uid` (Subscription ID), `type`, and subscription metadata
* GCP: Project object with `name`, `uid` (Project ID), `type`, and project attributes
* Oracle Cloud: Compartment object with `name`, `uid` (Tenancy OCID), `type`, and compartment details

**`cloud_partition`**

* **Type**: `string_t`
* **Requirement**: optional

The logical grouping or isolated segment within a cloud provider’s infrastructure where the event or finding was created, often used for compliance, governance, or regional separation.

Examples:

* AWS: Partition where the event occurred (`aws`, `aws-cn`, `aws-us-gov`)
* Azure: Cloud environment where the event occurred (`AzureCloud`, `AzureUSGovernment`, `AzureChinaCloud`)

**`org`**

* **Type**: [`organization`](organization.md)
* **Requirement**: optional

The Organization object containing details about the organizational unit or management structure that governs the account, subscription, or project where the event or finding was created. This object includes properties such as the organization name, unique identifier, type, and other organizational metadata.

Examples:

* AWS: Organization object with `name`, `uid` (Organization ID), `type`, and other organizational properties
* Azure: Management Group object with `name`, `uid` (Management Group ID), `type`, and management group metadata
* GCP: Organization object with `name`, `uid` (Organization ID), `type`, and organizational attributes
* Oracle Cloud: Tenancy object with `name`, `uid` (Tenancy OCID), `type`, and tenancy details

**`project_uid`**

* **Type**: `string_t`
* **Requirement**: optional

The unique identifier of a Cloud project.

**`zone`**

* **Type**: `string_t`
* **Requirement**: optional

The availability zone in the cloud region where the event or finding was created, as defined by the cloud provider.

Examples:

* AWS: Availability zone where the event occurred (`us-east-1a`, `us-east-1b`)
* Azure: Availability zone where the event occurred (`1`, `2`, `3` within a region)
* GCP: Availability zone where the event occurred (`us-central1-a`, `us-central1-b`)
* Oracle Cloud: Availability zone where the event occurred (`AD-1`, `AD-2`, `AD-3`)

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
* [`peripheral_activity`](../classes/peripheral_activity.md)
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