# Authorization Result

> The Authorization Result object provides details about the authorization outcome and associated policies related to activity.


The Authorization Result object provides details about the authorization outcome and associated policies related to activity.

## Attributes

**`decision`**

* **Type**: `string_t`
* **Requirement**: optional

Authorization Result/outcome, e.g. allowed, denied.

**`policy`**

* **Type**: [`policy`](policy.md)
* **Requirement**: optional

Details about the Identity/Access management policies that are applicable.

## Used By

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
* [`web_resources_activity`](../classes/web_resources_activity.md)