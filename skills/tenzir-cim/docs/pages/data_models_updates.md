---
title: Updates
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/updates
last_modified: 2026-04-01T20:48:26.226Z
version: 8.5
---

# Updates

The fields in the Updates data model describe patch management events from individual systems or central management tools.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with the Updates event and search datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| Updates | update |
| status |
| Update_Errors | update |
| error |

## Fields for the Updates event datasets and Update_Errors search dataset

The following table lists the extracted and calculated fields for the event datasets and search dataset in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| Updates | ` dest ` | string | The system that is affected by the patch change. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | - recommended - required for pytest-splunk-addon |
| Updates | ` dest_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| Updates | ` dest_category ` | string |
| Updates | ` dest_priority ` | string |
| Updates | ` dest_should_update ` | boolean |
| Updates | ` dvc ` | string | The device that detected the patch event, such as a patching or configuration management server. You can alias this from more specific fields, such as ` dvc_host ` , ` dvc_ip ` , or ` dvc_name ` . | required for pytest-splunk-addon |
| Updates | ` file_hash ` | string | The checksum of the patch package that was installed or attempted. |  |
| Updates | ` file_name ` | string | The name of the patch package that was installed or attempted. | required for pytest-splunk-addon |
| Updates | ` severity ` | string | The severity associated with the patch event. | prescribed values: ` critical ` , ` high ` , ` medium ` , ` low ` , ` informational ` |
| Updates | ` severity_id ` | number | The numeric or vendor specific severity indicator corresponding to the event severity. |  |
| Updates | ` signature ` | string | The name of the patch requirement detected on the client (the dest), such as ` MS08-067 ` or ` RHBA-2013:0739 ` . Note: This is a string value. Use ` signature_id ` for numeric indicators. | - recommended - required for pytest-splunk-addon |
| Updates | ` signature_id ` | int | The ID of the patch requirement detected on the client (the src). Note: Use ` signature ` for human-readable signature names. | - recommended - required for pytest-splunk-addon |
| Updates | ` status ` | string | Indicates the status of a given patch requirement. | - recommended - required for pytest-splunk-addon - prescribed values: Following are some prescribed values: - ` available ` : The patch or update is ready but not necessarily installed. - ` installed ` : The patch or update is successfully installed. - ` invalid ` : The patch or update is detected as invalid. - ` "restart required" ` : A restart is required after the patch installed. - ` "failure" ` : The installation patch or update failed to install. |
| Updates | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Do not define extractions for this field when writing add-ons. |  |
| Updates | ` vendor_product ` | string | The vendor and product of the patch monitoring product, such as ` Lumension Patch Manager ` . This field can be automatically populated by ` vendor ` and ` product ` fields in your data. | recommended |
