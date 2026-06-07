---
title: Change Analysis (deprecated)
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/change-analysis-deprecated
last_modified: 2026-04-01T20:48:31.414Z
version: 8.5
---

# Change Analysis (deprecated)

Note: This data model is deprecated as of software version 4.12.0. Use the Change data model instead.

The fields in the Change Analysis data model describe `Create `, `Read `, `Update `, and `Delete `activities from any data source.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Change Analysis event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Changes | change |
| \|____ Auditing_Changes | audit |
| \|____ Endpoint_Changes | endpoint |
| \|____ Network_Changes | network |
| \|____ Account_Management | account |

## Fields for Change Analysis event dataset

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |
| All_Changes | ` action ` | string | The action performed on the resource. | Values: ` acl_modified ` , ` cleared ` , ` created ` , ` deleted ` , ` modified ` , ` read ` , ` stopped ` , ` updated ` recommended |
| All_Changes | ` change_type ` | string | The type of change, such as ` filesystem ` or ` AAA ` (authentication, authorization, and accounting). | Values: ` restart ` recommended |
| All_Changes | ` command ` | string | The command that initiated the change. | recommended |
| All_Changes | ` dest ` | string | The resource where change occurred. You can alias this from more specific fields not included in this data model, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended |
| All_Changes | ` dest_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| All_Changes | ` dest_category ` | string |
| All_Changes | ` dest_priority ` | string |
| All_Changes | ` dvc ` | string | The device that reported the change, if applicable, such as a FIP or CIM server. You can alias this from more specific fields not included in this data model, such as ` dvc_host ` , ` dvc_ip ` , or ` dvc_name ` . | recommended |
| All_Changes | ` object ` | string | Name of the affected object on the resource (such as a router interface, user account, or server volume). | recommended |
| All_Changes | ` object_attrs ` | string | The attributes that were updated on the updated resource object, if applicable. | recommended |
| All_Changes | ` object_category ` | string | Generic name for the class of the updated resource object. Expected values may be specific to an app. | Values: ` directory ` , ` file ` , ` group ` , ` registry ` , ` user ` recommended |
| All_Changes | ` object_id ` | string | The unique updated resource object ID as presented to the system, if applicable (for instance, a SID, UUID, or GUID value). | recommended |
| All_Changes | ` object_path ` | string | The path of the modified resource object, if applicable (such as a file, directory, or volume). | recommended |
| All_Changes | ` result ` | string | The vendor-specific result of a change, or clarification of an ` action ` status. For instance, ` status=failure ` may be accompanied by ` result=blocked by policy ` or ` result=disk full ` . ` result ` is a string. Please use a ` msg_severity_id ` field (not included in the data model) for severity ID fields that are integer data types. | Values: ` lockout ` recommended |
| All_Changes | ` result_id ` | string | A result indicator for an ` action ` status. | recommended |
| All_Changes | ` src ` | string | The resource where the change was originated. You can alias this from more specific fields not included in the data model, such as ` src_host ` , ` src_ip ` , or ` src_name ` . | recommended |
| All_Changes | ` src_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| All_Changes | ` src_category ` | string |
| All_Changes | ` src_priority ` | string |
| All_Changes | ` status ` | string | Status of the update. | Values: ` success ` , ` failure ` recommended |
| All_Changes | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Do not define extractions for this field when writing add-ons. |  |
| All_Changes | ` user ` | string | The user or entity performing the change. For account changes, this is the account that was changed. See ` src_user ` for user or entity performing the change. | recommended |
| All_Changes | ` vendor_product ` | string | The vendor and product or service that detected the change. This field can be automatically populated by ` vendor ` and ` product ` fields in your data. | recommended |
| Account_Management | ` dest_nt_domain ` | string | The NT domain of the destination, if applicable. |  |
| Account_Management | ` src_nt_domain ` | string | The NT domain of the source, if applicable. |  |
| Account_Management | ` src_user ` | string | For account changes, the user or entity performing the change. |  |
| Account_Management | ` src_user_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Account_Management | ` src_user_category ` | string |
| Account_Management | ` src_user_priority ` | string |
| Filesystem_Changes | ` file_access_time ` | time | The time the file (the object of the event) was accessed. |  |
| Filesystem_Changes | ` file_acl ` | string | Access controls associated with the file affected by the event. |  |
| Filesystem_Changes | ` file_create_time ` | time | The time the file (the object of the event) was created. |  |
| Filesystem_Changes | ` file_hash ` | string | A cryptographic identifier assigned to the file object affected by the event. |  |
| Filesystem_Changes | ` file_modify_time ` | time | The time the file (the object of the event) was altered. |  |
| Filesystem_Changes | ` file_name ` | string | The name of the file that is the object of the event (without location information related to local file or directory structure). |  |
| Filesystem_Changes | ` file_path ` | string | The location of the file that is the object of the event, in local file and directory structure terms. |  |
| Filesystem_Changes | ` file_size ` | number | The size of the file that is the object of the event, in kilobytes. |  |
