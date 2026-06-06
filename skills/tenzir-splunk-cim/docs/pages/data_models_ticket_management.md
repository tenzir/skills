---
title: Ticket Management
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/ticket-management
last_modified: 2026-04-01T20:48:25.470Z
version: 8.5
---

# Ticket Management

The fields and tags in the Ticket Management data model describe service requests and their states in ITIL-influenced service desks, bug trackers, simple ticket systems, or GRC systems. They can help you establish a domain's data requirements so you can create apps that support each other.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Tags used with Ticket Management event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Ticket_Management | ticketing |

| \|____Change | change |

| \|____Incident | incident |

| \|____Problem | problem |

## Fields for Ticket Management event datasets

The following table lists the extracted and calculated fields for the event datasets in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- | --- |
| All_Ticket_Management | ` affect_dest ` | string | Destinations affected by the service request. |  |
| All_Ticket_Management | ` comments ` | string | Comments about the service request. |  |
| All_Ticket_Management | ` description ` | string | The description of the service request. |  |
| All_Ticket_Management | ` dest ` | string | The destination of the service request. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . |  |

| All_Ticket_Management | ` dest_bunit ` | string | The business unit associated with the destination user or entity of the triggering events, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Ticket_Management | ` dest_category ` | string | The category of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Ticket_Management | ` dest_priority ` | string | The priority of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Ticket_Management | ` priority ` | string | The relative priority of the service request. |  |
| All_Ticket_Management | ` severity ` | string | The relative severity of the service request. |  |
| All_Ticket_Management | ` severity_id ` | number | The numeric or vendor specific severity indicator corresponding to the event severity. |  |

```text

```

| All_Ticket_Management | ` splunk_id ` | string | The unique identifier of the service request as it pertains to Splunk. For example, CODE Copy 14DA67E8-6084-4FA8-9568-48D05969C522@@_internal@@ 0533eff241db0d892509be46cd3126e30e0f6046 ` 14DA67E8-6084-4FA8-9568-48D05969C522@@_internal@@ 0533eff241db0d892509be46cd3126e30e0f6046 ` . |  |
| All_Ticket_Management | ` splunk_realm ` | string | The Splunk application or use case associated with the unique identifier (splunk_id). For example, ` es_notable ` . |  |
| All_Ticket_Management | ` src_user ` | string | The user or entity creating or triggering the ticket, if applicable. |  |

| All_Ticket_Management | ` src_user_bunit ` | string | The business unit associated with the source user or entity within the triggering events, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Ticket_Management | ` src_user_category ` | string | The category associated with the user or entity that triggered the service request. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Ticket_Management | ` src_user_priority ` | string | The priority associated with the user or entity that triggered the service request. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| All_Ticket_Management | ` status ` | string | The relative status of the service request. |  |
| All_Ticket_Management | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |
| All_Ticket_Management | ` ticket_id ` | string | An identification name, code, or number for the service request. |  |
| All_Ticket_Management | ` time_submitted ` | time | The time that the ` src_user ` submitted the service request. |  |
| All_Ticket_Management | ` user ` | string | The name of the user or entity that is assigned to the ticket, if applicable. |  |

| All_Ticket_Management | ` user_bunit ` | string | The business unit associated with the user or entity that is carrying out the service request, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Ticket_Management | ` user_category ` | string | The category associated with the user or entity that is assigned to carry out the service request, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| All_Ticket_Management | ` user_priority ` | string | The priority of the user or entity that is assigned to carry out the service request, if applicable. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Change | ` change ` | string | Designation for a request for change (RFC) that is raised to modify an IT service to resolve an ` incident ` or ` problem ` . |  |
| Incident | ` incident ` | string | The incident that triggered the service request. Can be a rare occurrence, or something that happens more frequently. An incident that occurs on a frequent basis can also be classified as a ` problem ` . |  |
| Problem | ` problem ` | string | When multiple occurrences of related incidents are observed, they are collectively designated with a single ` problem ` value. Problem management differs from the process of managing an isolated incident. Often problems are managed by a specific set of staff and through a problem management process. |  |
