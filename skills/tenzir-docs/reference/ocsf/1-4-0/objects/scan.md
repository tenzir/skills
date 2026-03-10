# Scan

> The Scan object describes characteristics of a proactive scan.


The Scan object describes characteristics of a proactive scan.

* **Extends**: `_entity`

## Attributes

**`type_id`**

* **Type**: `integer_t`

* **Requirement**: required

* **Values**:

  * `0` - `Unknown`: The type is unknown.
  * `1` - `Manual`: The scan was manually initiated by the user or administrator.
  * `2` - `Scheduled`: The scan was started based on scheduler.
  * `3` - `Updated Content`: The scan was triggered by a content update.
  * `4` - `Quarantined Items`: The scan was triggered by newly quarantined items.
  * `5` - `Attached Media`: The scan was triggered by the attachment of removable media.
  * `6` - `User Logon`: The scan was started due to a user logon.
  * `7` - `ELAM`: The scan was triggered by an Early Launch Anti-Malware (ELAM) detection.
  * `99` - `Other`: The scan type id is not mapped. See the `type` attribute, which contains a data source specific value.

The type id of the scan.

**`name`**

* **Type**: `string_t`
* **Requirement**: recommended

The administrator-supplied or application-generated name of the scan. For example: “Home office weekly user database scan”, “Scan folders for viruses”, “Full system virus scan”

**`uid`**

* **Type**: `string_t`
* **Requirement**: recommended

The application-defined unique identifier assigned to an instance of a scan.

**`type`**

* **Type**: `string_t`
* **Requirement**: optional

The type of scan.

## Constraints

At least one of: `name`, `uid`

## Used By

* [`file_remediation_activity`](../classes/file_remediation_activity.md)
* [`network_remediation_activity`](../classes/network_remediation_activity.md)
* [`process_remediation_activity`](../classes/process_remediation_activity.md)
* [`remediation_activity`](../classes/remediation_activity.md)
* [`scan_activity`](../classes/scan_activity.md)