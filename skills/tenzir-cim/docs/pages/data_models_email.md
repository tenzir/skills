---
title: Email
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/email
last_modified: 2026-04-01T20:48:24.844Z
version: 8.5
---

# Email

The fields and tags in the Email data model describe email traffic, whether server:server or client:server.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Email event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Email | email |

| \|____ Delivery | delivery |

| \|____ Content | content |

| \|____ Filtering | filter |

## Fields for the Email event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |

-
-
-

| All_Email | ` action ` | string | Action taken by the reporting device. | recommended required for pytest-splunk-addon prescribed values: ` delivered ` , ` blocked ` , ` quarantined ` , ` deleted ` |
| All_Email | ` delay ` | number | Total sending delay in milliseconds. |  |

-
- | All_Email | ` dest ` | string | The endpoint system to which the message was delivered. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended required for pytest-splunk-addon |

| All_Email | ` dest_bunit ` | string | The business unit of the endpoint system to which the message was delivered. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` dest_category ` | string | The category of the endpoint system to which the message was delivered. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` dest_priority ` | string | The priority of the endpoint system to which the message was delivered. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Email | ` duration ` | number | The amount of time for the completion of the messaging event, in seconds. |  |
| All_Email | ` file_hash ` | string | The hashes for the files attached to the message, if any exist. |  |
| All_Email | ` file_name ` | string | The names of the files attached to the message, if any exist. |  |
| All_Email | ` file_size ` | number | The size of the files attached the message, in bytes. |  |

-
-

| All_Email | ` internal_message_id ` | string | Host-specific unique message identifier. | required for pytest-splunk-addon other: Such as ` aid ` in sendmail, ` IMI ` in Domino, ` Internal-Message-ID ` in Exchange, and ` MID ` in Ironport). |
| All_Email | ` message_id ` | string | The globally-unique message identifier. | required for pytest-splunk-addon |
| All_Email | ` message_info ` | string | Additional information about the message. |  |
| All_Email | ` orig_dest ` | string | The original destination host of the message. The message destination host can change when a message is relayed or bounced. |  |
| All_Email | ` orig_recipient ` | string | The original recipient of the message. The message recipient can change when the original email address is an alias and has to be resolved to the actual recipient. |  |
| All_Email | ` orig_src ` | string | The original source of the message. |  |

| All_Email | ` process ` | string | The name of the email executable that carries out the message transaction. | other: ` sendmail ` , ` postfix ` , or the name of an email client |
| All_Email | ` process_id ` | number | The numeric identifier of the process invoked to send the message. |  |

-
-

| All_Email | ` protocol ` | string | The email protocol involved, such as ` SMTP ` or ` RPC ` . | required for pytest-splunk-addon prescribed values: ` smtp ` , ` imap ` , ` pop3 ` , ` mapi ` |

-
-
-

| All_Email | ` recipient ` | string | A field listing individual recipient email addresses. | recommended required for pytest-splunk-addon other: ` recipient="foo@splunk.com" ` , ` recipient="bar@splunk.com" ` |
| All_Email | ` recipient_count ` | number | The total number of intended message recipients. | required for pytest-splunk-addon |
| All_Email | ` recipient_domain ` | string | The domain name contained within the recipient email addresses. | recommended |
| All_Email | ` recipient_status ` | string | The recipient delivery status, if available. |  |
| All_Email | ` response_time ` | number | The amount of time it took to receive a response in the messaging event, in seconds. |  |
| All_Email | ` retries ` | number | The number of times that the message was automatically resent because it was bounced back, or a similar transmission error condition. |  |
| All_Email | ` return_addr ` | string | The return address for the message. |  |
| All_Email | ` size ` | number | The size of the message, in bytes. |  |

-
- | All_Email | ` src ` | string | The system that sent the message. You can alias this from more specific fields, such as ` src_host ` , ` src_ip ` , or ` src_name ` . | recommended required for pytest-splunk-addon |

| All_Email | ` src_bunit ` | string | The business unit of the system that sent the message. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` src_category ` | string | The category of the system that sent the message. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` src_priority ` | string | The priority of the system that sent the message. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

-
- | All_Email | ` src_user ` | string | The email address of the message sender. | recommended required for pytest-splunk-addon |

| All_Email | ` src_user_bunit ` | string | The business unit of the message sender. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` src_user_category ` | string | The category of the message sender. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Email | ` src_user_domain ` | string | The domain name contained within the email address of the message sender. | recommended |

| All_Email | ` src_user_priority ` | string | The priority of the message sender. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Email | ` status_code ` | string | The status code associated with the message. |  |
| All_Email | ` subject ` | string | The subject of the message. |  |
| All_Email | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |
| All_Email | ` url ` | string | The URL associated with the message, if any. |  |
| All_Email | ` user ` | string | The user context for the ` process ` . This is not the email address for the sender. For that, look at the ` src_user ` field. | required for pytest-splunk-addon |

| All_Email | ` user_bunit ` | string | The business unit of the user context for the ` process ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` user_category ` | string | The category of the user context for the ` process ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Email | ` user_priority ` | string | The priority of the user context for the ` process ` . This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Email | ` vendor_product ` | string | The vendor and product of the email server used for the email transaction. This field can be automatically populated by ` vendor ` and ` product ` fields in your data. | recommended |
| All_Email | ` xdelay ` | string | Extended delay information for the message transaction. May contain details of all the delays from all the servers in the message transmission chain. |  |
| All_Email | ` xref ` | string | An external reference. Can contain message IDs or recipient addresses from related messages. |  |

| Filtering | ` filter_action ` | string | The status produced by the filter. | other: ` accepted ` , ` rejected ` , ` dropped ` |
| Filtering | ` filter_score ` | number | Numeric indicator assigned to specific emails by an email filter. |  |
| Filtering | ` signature ` | string | The name of the filter applied. | recommended |
| Filtering | ` signature_extra ` | string | Any additional information about the filter. |  |
| Filtering | ` signature_id ` | string | The id associated with the filter name. |  |

## Search Example

An example follows for the root dataset of All_Email and datamodel of Email:

`| tstats summariesonly=t count from datamodel="Email" by All_Email.file_name `
