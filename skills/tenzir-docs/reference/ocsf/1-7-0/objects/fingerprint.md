# Fingerprint

> The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content.


The Fingerprint object provides detailed information about a digital fingerprint, which is a compact representation of data used to identify a longer piece of information, such as a public key or file content. It contains the algorithm and value of the fingerprint, enabling efficient and reliable identification of the associated data.

## Attributes

**`algorithm_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The algorithm is unknown.
  * `1` - `MD5`: MD5 message-digest algorithm producing a 128-bit (16-byte) hash value.
  * `2` - `SHA-1`: Secure Hash Algorithm 1 producing a 160-bit (20-byte) hash value.
  * `3` - `SHA-256`: Secure Hash Algorithm 2 producing a 256-bit (32-byte) hash value.
  * `4` - `SHA-512`: Secure Hash Algorithm 2 producing a 512-bit (64-byte) hash value.
  * `5` - `CTPH`: The ssdeep generated fuzzy checksum. Also known as Context Triggered Piecewise Hash (CTPH).
  * `6` - `TLSH`: The TLSH fuzzy hashing algorithm.
  * `7` - `quickXorHash`: Microsoft simple non-cryptographic hash algorithm that works by XORing the bytes in a circular-shifting fashion.
  * `8` - `SHA-224`: Secure Hash Algorithm 2 producing a 224-bit (28-byte) hash value.
  * `9` - `SHA-384`: Secure Hash Algorithm 2 producing a 384-bit (48-byte) hash value.
  * `10` - `SHA-512/224`: Secure Hash Algorithm 2 producing a 512-bit (64-byte) hash value truncated to a 224-bit (28-byte) hash value.
  * `11` - `SHA-512/256`: Secure Hash Algorithm 2 producing a 512-bit (64-byte) hash value truncated to a 256-bit (32-byte) hash value.
  * `12` - `SHA3-224`: Secure Hash Algorithm 3 producing a 224-bit (28-byte) hash value.
  * `13` - `SHA3-256`: Secure Hash Algorithm 3 producing a 256-bit (32-byte) hash value.
  * `14` - `SHA3-384`: Secure Hash Algorithm 3 producing a 384-bit (48-byte) hash value.
  * `15` - `SHA3-512`: Secure Hash Algorithm 3 producing a 512-bit (64-byte) hash value.
  * `16` - `xxHash H3 64-bit`: xxHash H3 producing a 64-bit hash value.
  * `17` - `xxHash H3 128-bit`: xxHash H3 producing a 128-bit hash value.
  * `99` - `Other`: The algorithm is not mapped. See the `algorithm` attribute, which contains a data source specific value.

The identifier of the normalized hash algorithm, which was used to create the digital fingerprint.

**`value`**

* **Type**: `file_hash_t`
* **Requirement**: required

The digital fingerprint value.

**`algorithm`**

* **Type**: `string_t`
* **Requirement**: optional

The hash algorithm used to create the digital fingerprint, normalized to the caption of `algorithm_id`. In the case of `Other`, it is defined by the event source.

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