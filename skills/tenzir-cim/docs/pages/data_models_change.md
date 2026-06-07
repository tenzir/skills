---
title: Change
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/change
last_modified: 2026-04-01T20:48:24.512Z
version: 8.5
---

# Change

The Change data model replaces the Change Analysis data model, which is deprecated as of software version 4.12.0.

Change.Endpoint is for administrative and policy types of changes to infrastructure security devices, servers, and endpoint detection and response (EDR) systems. The Endpoint data model is for monitoring endpoint clients including, but not limited to, end user machines, laptops, and bring your own devices (BYOD). If an event is about an endpoint process, service, file, port, and so on, see the Endpoint data model.

The fields in the Change data model describe `Create `, `Read `, `Update `, and `Delete `activities from any data source.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

## Difference between the Endpoint and Change data models

The Change data model is built to make administrator type changes that include changes in devices, servers, Cloud environments, and endpoint detection and response (EDR) systems. EDR systems are mapped to the Change data model and the Endpoint dataset, but not mapped to the endpoints clients.

The Endpoint data model replaces the Application State data model. The Application State data model was deprecated in CIM version 4.12.0. The architecture of the Endpoint data model is different than the Application State data model. Each data set is directly searchable as DataModel.DataSet rather than by node name.

The fields and tags in the Endpoint data model describe service or process inventory and state, such as Unix daemons, Windows services, running processes on any OS, or similar systems.

The Endpoint data model is for monitoring endpoint clients including, but not limited to, end user machines, laptops, and bring your own devices (BYOD). If an event is about an endpoint process, service, file, port, and so on, then it relates to the Endpoint data model. For administrative and policy types of changes to infrastructure security devices, servers, and endpoint detection and response (EDR) systems, see Change.Endpoint in the Change data model.

Note: The structure "Change.Endpoint" represents "DataModel.DataSet".

## Tags used with Change event datasets

The following tags act as constraints to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| All_Changes | change |

| \|____ Auditing_Changes | audit |

| \|____ Endpoint_Changes | endpoint |

| \|____ Network_Changes | network |

| \|____ Account_Management | account |

| \|____ Instance_Changes | instance |

The Endpoint_Changes dataset includes events associated with the administrative changes for configurations, policies, and so on of EDR systems.

The Auditing_Changes dataset includes events associated with auditing service changes. These include device audit services such as stop, start, restart, disable, reconfigure, audit log clear, and so on.

## Fields for Change event datasets

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

For even more examples, see Change Field Mapping .

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |

-
-
-

| All_Changes | ` action ` | string | The action attempted on the resource, regardless of success or failure. | recommended required for pytest-splunk-addon prescribed values: ` acl_modified ` , ` cleared ` , ` created ` , ` deleted ` , ` modified ` , ` stopped ` , ` lockout ` , ` read ` , ` logoff ` , ` updated ` , ` started ` , ` restarted ` , ` unlocked ` |

-
-
- | All_Changes | ` change_type ` | string | The type of change, such as ` filesystem ` or ` AAA ` (authentication, authorization, and accounting). | recommended required for pytest-splunk-addon prescribed values: NA |

-
- | All_Changes | ` command ` | string | The command that initiated the change. | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` dest ` | string | The resource where change occurred. You can alias this from more specific fields not included in this data model, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended required for pytest-splunk-addon |
| All_Changes | ` dest_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| All_Changes | ` dest_category ` | string |
| All_Changes | ` dest_priority ` | string |

-
- | All_Changes | ` dvc ` | string | The device that reported the change, if applicable, such as a FIP or CIM server. You can alias this from more specific fields not included in this data model, such as ` dvc_host ` , ` dvc_ip ` , or ` dvc_name ` . | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` image_id ` | string | For create instance events, this field represents the image ID used for creating the instance such as the OS, applications, installed libraries, and so on. | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` object ` | string | Name of the affected object on the resource (such as a router interface, user account, or server volume). | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` object_attrs ` | string | The object's attributes and their values. The attributes and values can be those that are updated on a resource object, or those that are not updated but are essential attributes. | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` object_category ` | string | Generic name for the class of the updated resource object. Expected values may be specific to an app, for example: registry, directory, file, group, user, bucket, instance. | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` object_id ` | string | The unique updated resource object ID as presented to the system, if applicable (for instance, a SID, UUID, or GUID value). | recommended required for pytest-splunk-addon |

-
- | All_Changes | ` object_path ` | string | The path of the modified resource object, if applicable (such as a file, directory, or volume). | recommended required for pytest-splunk-addon |

- | All_Changes | ` result ` | string | The vendor-specific result of a change, or clarification of an action status. For instance, status=failure may be accompanied by result=blocked by policy or result=disk full. | recommended |
| All_Changes | ` result_id ` | string | A result indicator for an ` action ` status. | recommended |
| All_Changes | ` src ` | string | The resource where the change was originated. You can alias this from more specific fields not included in the data model, such as ` src_host ` , ` src_ip ` , or ` src_name ` . | recommended |
| All_Changes | ` src_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for these fields when writing add-ons. |
| All_Changes | ` src_category ` | string |
| All_Changes | ` src_priority ` | string |

-
-
-

| All_Changes | ` status ` | string | Status of the update. | recommended required for pytest-splunk-addon prescribed values: ` success ` , ` failure ` |
| All_Changes | ` tag ` | string | This automatically generated field is used to access tags from within datamodels. Do not define extractions for this field when writing add-ons. |  |

-
- | All_Changes | ` user ` | string | The user or entity performing the change. For account changes, this is the account that was changed. See ` src_user ` for user or entity performing the change. | recommended required for pytest-splunk-addon |
| All_Changes | ` user_agent ` | string | The user agent through which the request was made, such as ` Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ` or ` aws-cli/2.0.0 Python/3.7.4 Darwin/18.7.0 botocore/2.0.0dev4 ` . |  |
| All_Changes | ` user_name ` | string | The user name of the user or entity performing the change. For account changes, this is the account that was changed (see ` src_user_name ` ). | recommended |
| All_Changes | ` user_type ` | string | The type of the user involved in the event or who initiated the event, such as IAMUser, Admin, or System. For account management events, this should represent the type of the user changed by the request. |  |
| All_Changes | ` vendor_account ` | string | The account that manages the user that initiated the request. The account represents the organization, or a Cloud customer or a Cloud account. |  |

-
- | All_Changes | ` vendor_product ` | string | The vendor and product or service that detected the change. This field can be automatically populated by ` vendor ` and ` product ` fields in your data. | recommended required for pytest-splunk-addon |
| All_Changes | ` vendor_region ` | string | The data center region where the change occurred, such as us-west-2. |  |
| Account_Management | ` dest_nt_domain ` | string | The NT domain of the destination, if applicable. | recommended |
| Account_Management | ` src_nt_domain ` | string | The NT domain of the source, if applicable. | recommended |
| Account_Management | ` src_user ` | string | For account changes, the user or entity performing the change. | recommended |
| Account_Management | ` src_user_bunit ` | string | These fields are automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |
| Account_Management | ` src_user_category ` | string |
| Account_Management | ` src_user_priority ` | string |
| Account_Management | ` src_user_name ` | string | For account changes, the user name of the user or entity performing the change. | recommended |
| Account_Management | ` src_user_type ` | string | For account management events, this should represent the type of the user changed by the request. |  |
| Network_Changes | ` dest_ip_range ` | string | For network events, the outgoing traffic for a specific destination IP address range. Specify a single IP address or an IP address range in CIDR notation. For example, 203.0.113.5 or 203.0.113.5/32. |  |
| Network_Changes | ` dest_port_range ` | string | For network events, this field represents destination port or range. For example, 80 or 8000 - 8080 or 80,443. |  |
| Network_Changes | ` direction ` | string | For network events, this field represents whether the traffic is inbound or outbound. |  |
| Network_Changes | ` rule_action ` | string | For network events, this field represents whether to allow or deny traffic. |  |
| Network_Changes | ` src_ip_range ` | string | For network events, this field represents the incoming traffic from a specific source IP address or range. Specify a single IP address or an IP address range in CIDR notation. For example, 203.0.113.5 or 203.0.113.5/32. |  |
| Network_Changes | ` src_port_range ` | string | For network events, this field represents source port or range. For example, 80 or 8000 - 8080 or 80,443. |  |
| Network_Changes | ` device_restarts ` | string | Monitor all infrastructure device restarts. |

Note: The Endpoint_Changes dataset and the Auditing_Changes dataset do not have any specific fields.
