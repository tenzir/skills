---
title: Data Access
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/data-access
last_modified: 2026-04-01T20:48:24.683Z
version: 8.5
---

# Data Access

The Data Access data model is for monitoring shared data access user activity. It helps you detect a user's unauthorized data access, misuse, exfiltration, and more. It applies to events about users accessing data on servers that are shared by many other users, such as: The "file abc" on the "server xyz" was accessed (read, created, modified, shared, and so on) by a "user Bob".

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Differences Data Access and other data models such as Change and Web

Use the Data Access data model when the following conditions apply:

- The main function of the product is to access, create, share, move, modify, collaborate, and forward data by users
- The data is typically authored and managed by a regular user instead of an administrator
- The data impacts a single object such as a document

Examples of such products are Google Drive, OneDrive, SharePoint, Box, and GitHub.

Data can be shared and accessed in different forms, not only as files, but also as comments, labels, tasks, invites, and so on. Such events must also be mapped to the Data Access data model.

If the event is about the administrator's activity such as product configuration changes, data authoring and managing, which impacts multiple users or multiple files or folders, then map such activity events to the Change data model.

Web servers such as Apache, are also used for data access and data sharing. However, these products are about client-server communication instead of communication between clients. The data is authored and managed by the web administrators, and then provided to clients or users. Regular users cannot collaborate and modify the data. This is the reason for web logs being mapped to the Web data model and not mapped to the Data Access data model.

## Tags used with Data Access event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| Data_Access | data |
| access |

## Fields for Data Access event datasets

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

For even more examples, see Data Access Field Mapping .

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |
| Data_Access | ` action ` | string | The data access action taken by the user. | - recommended - prescribed values: ` commented ` , ` copied ` , ` created ` , ` deleted ` , ` disabled ` , ` downloaded ` , ` enabled ` , ` granted ` , ` forwarded ` , ` modified ` , ` read ` , ` revoked ` , ` shared ` , ` stopped ` , ` uncommented ` , ` unlocked ` , ` unshared ` , ` updated ` , ` uploaded ` , |
| Data_Access | ` app ` | string | The application involved in the event. | recommended |
| Data_Access | ` app_id ` | string | Application ID as defined by the vendor. |  |
| Data_Access | ` dest ` | string | The destination where the data resides or where it is being accessed, such as the product or application. You can alias this from more specific fields not included in this data model, such as ` dest_host ` , ` dest_ip ` , ` dest_url ` , or ` dest_name ` . | recommended |
| Data_Access | ` dest_name ` | string | Name of the destination as defined by the vendor. |  |
| Data_Access | ` dest_url ` | string | Url of the product, application, or object. |  |
| Data_Access | ` dvc ` | string | The device that reported the data access event. |  |
| Data_Access | ` email ` | string | The email address of the user involved in the event, or who initiated the event. |  |
| Data_Access | ` object ` | string | Resource object name on which the action was performed by a user. | recommended |
| Data_Access | ` object_attrs ` | string | The object's attributes and their values. The attributes and values can be those that are updated on a resource object, or those that are not updated but are essential attributes. | recommended |
| Data_Access | ` object_category ` | string | Generic name for the class of the updated resource object. Expected values may be specific to an app. For example, ` collaboration ` , ` file ` , ` folder ` , ` comment ` , ` task ` , ` note ` , and so on. | recommended |
| Data_Access | ` object_id ` | string | The unique updated resource object ID as presented to the system, if applicable. For example, a source_folder_id, doc_id. | recommended |
| Data_Access | ` object_path ` | string | The path of the modified resource object, if applicable, such as a file, directory, or volume. |  |
| Data_Access | ` object_size ` | string | The size of the modified resource object. | recommended |
| Data_Access | ` owner ` | string | Resource owner. |  |
| Data_Access | ` owner_email ` | string | Email of the resource owner. |  |
| Data_Access | ` owner_id ` | string | ID of the owner as defined by the vendor. |  |
| Data_Access | ` parent_object ` | string | Parent of the object name on which the action was performed by a user. |  |
| Data_Access | ` parent_object_id ` | string | Parent object ID |  |
| Data_Access | ` parent_object_category ` | string | Object category of the parent object on which action was performed by a user. |  |
| Data_Access | ` signature ` | string | A human-readable signature name. |  |
| Data_Access | ` signature_id ` | string | The unique identifier or event code of the event signature. | optional |
| Data_Access | ` src ` | string | The endpoint client host. | recommended |
| Data_Access | ` vendor_account ` | string | Account associated with the event. The account represents the organization, or a Cloud customer or a Cloud account. | recommended |
| Data_Access | ` user ` | string | The user involved in the event, or who initiated the event. | recommended |
| Data_Access | ` user_agent ` | string | The user agent through which the request was made, such as Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) or aws-cli/2.0.0 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0dev4 | recommended |
| Data_Access | ` user_group ` | string | The group of the user involved in the event, or who initiated the event. |  |
| Data_Access | ` user_id ` | string | The unique id of the user involved in the event. For authentication privilege escalation events, this should represent the user targeted by the escalation. | optional |
| Data_Access | ` user_name ` | string | The user name of the user or entity performing the change. For account changes, this is the account that was changed (see src_user_name). Use this field for a friendlier name, for example, with AWS events if you do not have Assets and Identities configured in Enterprise Security and are not getting a friendly name from user. | recommended |
| Data_Access | ` user_email ` | string | The email address of the user or entity involved in the event. | optional |
| Data_Access | ` user_role ` | string | The role of the user involved in the event, or who initiated the event. |  |
| Data_Access | ` user_type ` | string | The type of the user involved in the event or who initiated the event, such as IAMUser, Admin, or System. For account management events, this should represent the type of the user changed by the request. | optional |
| Data_Access | ` vendor_product ` | string | The vendor and product name of the vendor. | recommended |
| Data_Access | ` vendor_product_id ` | string | The vendor and product name ID as defined by the vendor. |  |
| Data_Access | ` vendor_region ` | string | The data center region where the change occurred, such as us-west-2. | optional |
