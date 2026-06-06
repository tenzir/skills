---
title: Alerts
url: https://help.splunk.com/en/data-management/common-information-model/8.5/data-models/alerts
last_modified: 2026-04-01T20:48:25.546Z
version: 8.5
---

# Alerts

The fields and tags in the Alerts data model describe the alerts produced by alerting systems, such as Nagios or NetCool, for use in Splunk correlation searches or dashboards. They are not to be used to describe Splunk Alerts or Notable Events, which are already modeled in other contexts.

Note: A dataset is a component of a data model. In versions of the Splunk platform prior to version 6.5.0, these were referred to as data model objects.

Events in the Alerts data model are vendor agnostic, which means that they are not specific to a vendor. The events in the Alerts data model are higher level event constructs or metadata events that carry new knowledge based on multiple basic events. However, an event that pertains to multiple lower basic level is not always mapped to the Alerts data model.

The following example indicates that an event occurred three times. However, this is not a high level event with any new meaning or metadata. It does not pertain to the Alerts data model, but is merely an aggregation of three individual events and is reporting three UDP packets:

CODE Copy [May 11 06:24:18 2020 SE-002 BUSDEV-001: NetScreen device_id=BUSDEV-001 [someadmin]system-alert-00016: Port scan! From 10.0.0.15:31859 to 1.0.0.4:443, proto UDP (zone Untrust int redundant1.3). Occurred 3 times. (2020-05-11 06:24:18)]

```text
`[May 11 06:24:18 2020 SE-002 BUSDEV-001: NetScreen device_id=BUSDEV-001 [someadmin]system-alert-00016: Port scan! From 10.0.0.15:31859 to 1.0.0.4:443, proto UDP (zone Untrust int redundant1.3). Occurred 3 times. (2020-05-11 06:24:18)]`
```

Non-security alerts should not be mapped to the Alerts data model such as IT alerts as displayed in the following example from Cisco UCS:

CODE Copy prevSeverity="major",dn="sys/switch-A/slot-1/switch-ether/port-10/rx-stats", occur="5",ack="yes",lc="",type="switch-software",highestSeverity="minor",severity="major",tags="network", created="2020-10-14T10:48:51",rule="equipment-iocard-unsupported-connectivity", changeSet="",descr="FC pool node-wwn-assignment node-default is empty", lastTransition="2020-10-14T10:47:27",cause="default-hostpack-missing-versions",id="31212",code="F0463",origSeverity="major",site="", system_name="ta-factory",address="172.16.107.244"

```text
`prevSeverity="major",dn="sys/switch-A/slot-1/switch-ether/port-10/rx-stats", occur="5",ack="yes",lc="",type="switch-software",highestSeverity="minor",severity="major",tags="network", created="2020-10-14T10:48:51",rule="equipment-iocard-unsupported-connectivity", changeSet="",descr="FC pool node-wwn-assignment node-default is empty", lastTransition="2020-10-14T10:47:27",cause="default-hostpack-missing-versions",id="31212",code="F0463",origSeverity="major",site="", system_name="ta-factory",address="172.16.107.244"`
```

## Tags used with the Alerts event dataset

The following tag acts as constraint to identify your events as being relevant to this data model. For more information, see How to use these reference tables .

| Dataset name | Tag name |
| --- | --- |
| Alerts | alert |

## Fields for the Alerts event dataset

The following table lists the extracted and calculated fields for the event dataset in the model. The table does not include any inherited fields. For more information, see How to use these reference tables .

The key for using the column titled "Notes" or "Abbreviated list of example values" is as follows:

- Recommended : Add-on developers make their best effort attempts to map these event fields. If these fields are not populated, then the event is not very useful.
- Required : Add-on developers must map these event fields when using the pytest-splunk-addon to test for CIM compatibility. See pytest-splunk-addon documentation .
- Prescribed values : Permitted values that can populate the fields, which Splunk is using for a particular purpose. Other valid values exist, but Splunk is not relying on them.
- Other values : Other example values that you might see.

| Dataset name | Field name | Data type | Description | Notes |
| --- | --- | --- | --- | --- |

-
- | Alerts | ` app ` | string | The system, service, or application that generated the alert event. Examples include, but are not limited to the following: GuardDuty, SecurityCenter, 3rd party services, win:app:trendmicro, vmware, nagios. | recommended required for pytest-splunk-addon |
| Alerts | cim_entity | string | This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Alerts | ` description ` | string | The description of the alert event. |  |

-
- | Alerts | ` dest ` | string | The object that is the target of the alert event. Examples include an email address, SNMP trap, or virtual machine id. You can alias this from more specific fields, such as ` dest_host ` , ` dest_ip ` , or ` dest_name ` . | recommended required for pytest-splunk-addon |

| Alerts | ` dest_bunit ` | string | The business unit associated with the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| Alerts | ` dest_category ` | string | The category of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| Alerts | ` dest_priority ` | string | The priority of the destination. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Alerts | ` dest_type ` | string | The type of the destination object, such as instance, storage, firewall. |  |
| Alerts | ` id ` | string | The unique identifier of the alert event. | required for pytest-splunk-addon |
| Alerts | ` mitre_technique_id ` | string | The MITRE ATT&CK technique ID of the alert event, searchable at https://attack.mitre.org/techniques . |  |

-
-
-

| Alerts | ` severity ` | string | The severity of the alert event. Note: This field is a string. Specific values are required. Use the ` severity_id ` field for severity ID fields that are integer data types. Specific values are required. Use ` vendor_severity ` for the vendor's own human-readable strings (such as ` Good ` , ` Bad ` , ` Really Bad ` , and so on). | recommended required for pytest-splunk-addon prescribed values: [critical, high, medium, low, informational]. |
| Alerts | ` severity_id ` | number | The numeric or vendor specific severity indicator corresponding to the event severity. |  |

-
-

| Alerts | ` signature ` | string | The human-friendly title of the alert event, such as 'API GetAccountPasswordPolicy was invoked using root credentials.' Split by ` signature_id ` when aggregating alert events by types. Following are some examples: Policy:IAMUser/RootCredentialUsage Callback Detectors: High Confidence C&C Server Name Match Note: Split by ` signature_id ` or ` signature ` when aggregating alert events by types. |  |

-
- | Alerts | ` signature_id ` | string | The vendor specific policy or rule that generated the alert event, such as 'Policy:IAMUser/RootCredentialUsage.'For example: Policy:IAMUser/RootCredentialUsage. 0x00011f00 | recommended |
| Alerts | ` src ` | string | The object that is the actor of the alert event. You can alias this from more specific fields, such as ` src_host ` , ` src_ip ` , or ` src_name ` . | recommended |

| Alerts | ` src_bunit ` | string | The business unit associated with the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| Alerts | ` src_category ` | string | The category of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| Alerts | ` src_priority ` | string | The priority of the source. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Alerts | ` src_type ` | string | The type of the source object, such as instance, storage, firewall. |  |
| Alerts | ` tag ` | string | This automatically generated field is used to access tags from within data models. Do not define extractions for this field when writing add-ons. |  |

-
-
-

| Alerts | ` type ` | string | The alert event type. | recommended required for pytest-splunk-addon prescribed values: ` alarm ` , ` alert ` , ` event ` , ` task ` , ` warning ` , ` unknown ` |
| Alerts | ` user ` | string | The user involved in the alert event. | recommended |

| Alerts | ` user_bunit ` | string | The business unit of the user involved in the alert event. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |

| Alerts | ` user_category ` | string | The category of the user involved in the alert event. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Alerts | ` user_name ` | string | The name of the user involved in the alert event. | recommended |

| Alerts | ` user_priority ` | string | The priority of the user involved in the alert event. This field is automatically provided by asset and identity correlation features of applications like Splunk Enterprise Security. Do not define extractions for this field when writing add-ons. |  |
| Alerts | ` vendor_account ` | string | The account associated with the alert event. The account represents the organization, or a Cloud customer or a Cloud account. |  |
| Alerts | ` vendor_region ` | string | The data center region involved in the alert event, such as us-west-2. |  |
