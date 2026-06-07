---
title: Authentication
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/authentication
last_modified: 2026-04-01T20:48:24.427Z
version: 8.5
---

# Authentication

The fields and tags in the Authentication data model describe login activities from any data source.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Authentication event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| Authentication | authentication |
| \|____ Default_Authentication | default |
| \|____ Insecure_Authentication | cleartext OR insecure |
| \|____ Privileged_Authentication | privileged |

## Fields for Authentication event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

For even more examples, see Authentication Field Mapping .

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |
| Authentication | ` action ` | string | The action performed on the resource. | Prescribed values: ` success ` , ` failure ` , ` pending ` , ` error ` Recommended. Also, required for pytest-splunk-addon |
| Authentication | ` app ` | string | The application involved in the event. | ` ssh ` ` splunk ` ` win:local ` ` signin.amazonaws.com ` Recommended. Also, required for pytest-splunk-addon |
| Authentication | ` authentication_method ` | string | The method used to authenticate the request. | Optional |
| Authentication | ` authentication_service ` | string | The service used to authenticate the request. | ` Okta ` , ` ActiveDirectory ` , ` AzureAD ` Optional |
| Authentication | ` cim_entity ` | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Authentication | ` dest ` | string | The target host involved in the authentication. You can alias this from more specific fields. | ` dest_host ` , ` dest_ip ` , ` dest_nt_host ` Recommended |
| Authentication | ` dest_bunit ` | string | The business unit of the authentication target. | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` dest_category ` | string | The category of the authentication target. | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. ` email_server ` or ` SOX-compliant ` |
| Authentication | ` dest_nt_domain ` | string | The name of the Active Directory used by the authentication target, if applicable. |  |
| Authentication | ` dest_priority ` | string | The priority of the authentication target. | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` duration ` | number | The amount of time for the completion of the authentication event, in seconds. |  |
| Authentication | ` process ` | number | Full path and the name of the executable for the process that attempted the logon. For example, it is a 'Process Name' in Windows such as C:\Windows\System32\svchost.exe. | Optional |
| Authentication | ` reason_id ` | string | The reason for login failure. For example "0xC0000234". | Optional |
| Authentication | ` response_time ` | number | The amount of time it took to receive a response in the authentication event, in seconds. |  |
| Authentication | ` result ` | string | The result of the authentication attempt for audittrailv2 sourcetypes. |  |
| Authentication | ` signature ` | string | A human-readable signature name. |  |
| Authentication | ` signature_id ` | string | The unique identifier or event code of the event signature. |  |
| Authentication | ` src ` | string | The source involved in the authentication. In the case of endpoint protection authentication the ` src ` is the client. | You can alias this from more specific fields. ` src_host ` , ` src_ip ` , or ` src_nt_host ` . Note: Do not confuse ` src ` with the event ` source ` or ` sourcetype ` fields. Recommended |
| Authentication | ` src_bunit ` | string | The business unit of the authentication source. | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` src_category ` | string | The category of the authentication source. | ` email_server ` or ` SOX-compliant ` |
| Authentication | ` src_nt_domain ` | string | The name of the Active Directory used by the authentication source, if applicable. |  |
| Authentication | ` src_priority ` | string | The priority of the authentication source. | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` src_user ` | string | In privilege escalation events, ` src_user ` represents the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed. Recommended |
| Authentication | ` src_user_bunit ` | string | The business unit of the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` src_user_category ` | string | The category of the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed.This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` src_user_id ` | string | The unique id of the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed. |
| Authentication | ` src_user_priority ` | string | The priority of the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` src_user_role ` | string | The role of the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed. |
| Authentication | ` src_user_type ` | string | The type of the user who initiated the privilege escalation. | This field is unnecessary when an escalation has not been performed. |
| Authentication | ` tag ` | string | This automatically-generated field is used to access tags from within data models. | Do not define extractions for this field when writing add-ons. |
| Authentication | ` user ` | string | The actual string or identifier that a user is logging in with. | This is the user involved in the event, or who initiated the event. For authentication privilege escalation events, this should represent the user string or identifier targeted by the escalation. Recommended. Also, required for pytest-splunk-addon |
| Authentication | ` user_agent ` | string | The user agent through which the request was made. ` Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ` or ` aws-cli/2.0.0 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0dev4 ` |  |
| Authentication | ` user_bunit ` | string | The business unit of the user involved in the event, or who initiated the event. | For authentication privilege escalation events this should represent the user targeted by the escalation. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` user_category ` | string | The category of the user involved in the event, or who initiated the event. | For authentication privilege escalation events, this should represent the user targeted by the escalation. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` user_id ` | string | The unique id of the user involved in the event. | For authentication privilege escalation events, this should represent the user targeted by the escalation. |
| Authentication | ` user_priority ` | string | The priority of the user involved in the event, or who initiated the event. | For authentication privilege escalation events, this should represent the user targeted by the escalation. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Authentication | ` user_role ` | string | The role of the user involved in the event, or who initiated the event. | For authentication privilege escalation events, this should represent the user role targeted by the escalation. |
| Authentication | ` user_type ` | string | The type of the user involved in the event or who initiated the event. IAMUser, Admin, or System. | For authentication privilege escalation events, this should represent the user type targeted by the escalation. |
| Authentication | ` vendor_account ` | string | The account that manages the user that initiated the request. The account represents the organization, a Cloud customer, or a Cloud account. |  |
| Failed_Authentication | ` Constraint ` | constraint | Constraint includes result field | JSON constraint now includes result field for audittrailv2 support |
| Successful_Authentication | ` Constraint ` | constraint | Constraint includes the result field | JSON constraint now includes result field for audittrailv2 support |
