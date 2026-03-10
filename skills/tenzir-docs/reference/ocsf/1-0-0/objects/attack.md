# Attack

> The Attack object describes the technique and associated tactics related to an attack.


The Attack object describes the technique and associated tactics related to an attack. See [MITRE ATT\&CK®](https://attack.mitre.org).

## Attributes

**`tactics`**

* **Type**: [`tactic`](tactic.md)
* **Requirement**: required

The a list of tactic ID’s/names that are associated with the attack technique, as defined by ATT\&CK MatrixTM.

**`technique`**

* **Type**: [`technique`](technique.md)
* **Requirement**: required

The attack technique.

**`version`**

* **Type**: `string_t`
* **Requirement**: required

The ATT\&CK Matrix version.

## Used By

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
* [`process_activity`](../classes/process_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`scheduled_job_activity`](../classes/scheduled_job_activity.md)
* [`security_finding`](../classes/security_finding.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)