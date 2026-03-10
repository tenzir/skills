# MITRE ATT&CK®

> The [MITRE ATT&CK®](https://attack.mitre.org) object describes the tactic, technique & sub-technique associated to an attack as defined in ATT&CK MatrixTM.


The [MITRE ATT\&CK®](https://attack.mitre.org) object describes the tactic, technique & sub-technique associated to an attack as defined in ATT\&CK MatrixTM.

## Attributes

**`version`**

* **Type**: `string_t`
* **Requirement**: recommended

The ATT\&CK MatrixTM version.

**`sub_technique`**

* **Type**: [`sub_technique`](sub_technique.md)
* **Requirement**: optional

The Sub Technique object describes the sub technique ID and/or name associated to an attack, as defined by ATT\&CK MatrixTM.

**`tactic`**

* **Type**: [`tactic`](tactic.md)
* **Requirement**: optional

The Tactic object describes the tactic ID and/or name that is associated to an attack, as defined by ATT\&CK MatrixTM.

**`tactics`**

* **Type**: [`tactic`](tactic.md)
* **Requirement**: optional

The Tactic object describes the tactic ID and/or tactic name that are associated with the attack technique, as defined by ATT\&CK MatrixTM.

**`technique`**

* **Type**: [`technique`](technique.md)
* **Requirement**: optional

The Technique object describes the technique ID and/or name associated to an attack, as defined by ATT\&CK MatrixTM.

## Constraints

At least one of: `tactic`, `technique`, `sub_technique`

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
* [`incident_finding`](../classes/incident_finding.md)
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
* [`security_finding`](../classes/security_finding.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)