---
title: Interprocess Messaging
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/interprocess-messaging
last_modified: 2026-04-01T20:48:26.136Z
version: 8.5
---

# Interprocess Messaging

The fields in the Interprocess Messaging data model describe transactional requests in programmatic interfaces. This enables you to establish the data requirements for a domain and create apps that support each other. The Interprocess Messaging data model enables reporting on

- messaging queues such as Tibco, MSMQ, Apache ESB, IBM MQ, and XMPP.
- IPC interfaces like RPC and WMI.
- Web interfaces such as SOAP and REST.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with the Interprocess Messaging event dataset

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Interprocess_Messaging | messaging |

## Fields for the Interprocess Messaging event dataset

The following table lists the extracted and calculated fields for the event dataset in the model. Note that it does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| All_Interprocess_Messaging | ` dest ` | string | The destination of the message. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . |  |

| All_Interprocess_Messaging | ` dest_bunit ` | string | The business unit of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Interprocess_Messaging | ` dest_category ` | string | The type of message destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. | prescribed values: ` queue ` , ` topic ` |

| All_Interprocess_Messaging | ` dest_priority ` | string | The priority of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Interprocess_Messaging | ` duration ` | number | The number of seconds from message call to message response. Can be derived by getting the difference between the ` request_sent_time ` and the ` message_received_time ` . |  |
| All_Interprocess_Messaging | ` endpoint ` | string | The endpoint that the message accessed during the RPC (remote procedure call) transaction. |  |
| All_Interprocess_Messaging | ` endpoint_version ` | string | The version of the endpoint accessed during the RPC (remote procedure call) transaction, such as ` 1.0 ` or ` 1.22 ` . |  |
| All_Interprocess_Messaging | ` message ` | string | A command or reference that an RPC (remote procedure call) reads or responds to. |  |
| All_Interprocess_Messaging | ` message_consumed_time ` | time | The time that the RPC (remote procedure call) read the message and was prepared to take some sort of action. |  |
| All_Interprocess_Messaging | ` message_correlation_id ` | string | The message correlation identification value. |  |
| All_Interprocess_Messaging | ` message_delivered_time ` | time | The time that the message producer sent the message. |  |
| All_Interprocess_Messaging | ` message_delivery_mode ` | string | The message delivery mode. Possible values depend on the type of message-oriented middleware (MOM) solution in use. They can be words like ` Transient ` (meaning the message is stored in memory and is lost if the server dies or restarts) or ` Persistent ` (meaning the message is stored both in memory and on disk and is preserved if the server dies or restarts). They can also be numbers like ` 1 ` , ` 2 ` , and so on. |  |
| All_Interprocess_Messaging | ` message_expiration_time ` | time | The time that the message expired. |  |
| All_Interprocess_Messaging | ` message_id ` | string | The message identification. |  |
| All_Interprocess_Messaging | ` message_priority ` | string | The priority of the message. Important jobs that the message queue should answer no matter what receive a higher ` message_priority ` than other jobs, ensuring they are completed before the others. |  |
| All_Interprocess_Messaging | ` message_properties ` | string | An arbitrary list of message properties. The set of properties displayed depends on the message-oriented middleware (MOM) solution that you are using. |  |
| All_Interprocess_Messaging | ` message_received_time ` | time | The time that the message was received by a message-oriented middleware (MOM) solution. |  |
| All_Interprocess_Messaging | ` message_redelivered ` | boolean | Indicates whether or not the message was redelivered. |  |
| All_Interprocess_Messaging | ` message_reply_dest ` | string | The name of the destination for replies to the message. |  |
| All_Interprocess_Messaging | ` message_type ` | string | The type of message, such as ` call ` or ` reply ` . |  |
| All_Interprocess_Messaging | ` parameters ` | string | Arguments that have been passed to an endpoint by a REST call or something similar. A sample parameter could be something like ` foo=bar ` . |  |
| All_Interprocess_Messaging | ` payload ` | string | The message payload. |  |
| All_Interprocess_Messaging | ` payload_type ` | string | The type of payload in the message. The payload type can be text (such as ` json ` , ` xml ` , and ` raw ` ) or binary (such as ` compressed ` , ` object ` , ` encrypted ` , and ` image ` ). |  |
| All_Interprocess_Messaging | ` request_payload ` | string | The content of the message request. |  |
| All_Interprocess_Messaging | ` request_payload_type ` | string | The type of payload in the message request. The payload type can be text (such as ` json ` , ` xml ` , and ` raw ` ) or binary (such as ` compressed ` , ` object ` , ` encrypted ` , and ` image ` ). |  |
| All_Interprocess_Messaging | ` request_sent_time ` | time | The time that the message request was sent. |  |
| All_Interprocess_Messaging | ` response_code ` | string | The response status code sent by the receiving server. Ranges between ` 200 ` and ` 404 ` . |  |
| All_Interprocess_Messaging | ` response_payload_type ` | string | The type of payload in the message response. The payload type can be text (such as ` json ` , ` xml ` , and ` raw ` ) or binary (such as ` compressed ` , ` object ` , ` encrypted ` , and ` image ` ). |  |
| All_Interprocess_Messaging | ` response_received_time ` | time | The time that the message response was received. |  |
| All_Interprocess_Messaging | ` response_time ` | number | The amount of time it took to receive a response, in seconds. |  |
| All_Interprocess_Messaging | ` return_message ` | string | The response status message sent by the message server. |  |
| All_Interprocess_Messaging | ` rpc_protocol ` | string | The protocol that the message server uses for remote procedure calls (RPC). Possible values include ` HTTP REST ` , ` SOAP ` , and ` EJB ` . |  |

| All_Interprocess_Messaging | ` status ` | boolean | The status of the message response. | prescribed values: ` pass ` , ` fail ` |
| All_Interprocess_Messaging | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |
