---
title: ITSI Normalization
url: https://help.splunk.com/en/data-management/common-information-model/8.5/additional-normalizations/itsi-normalization
last_modified: 2026-04-01T20:48:42.815Z
version: 8.5
---

# ITSI Normalization

The following table describes field and field definitions in support of Universal Alerting in ITSI. See the details About the Content Pack for Monitoring and Alerting in Splunk ITSI Content Packs .

The key for using the column titled "Abbreviated list of example values" follows. It is relevant for TA developers and ITSI implementors such as customers, SEs, and PSEs:

- Required : Required Fields must be included.
- Recommended : Recommended Fields are helpful, but the Universal Correlation Search does not require them.
- Optional : Optional Fields are available for more advanced integrations, such as providing drilldowns.

| Field name | Data type | Description | Abbreviated list of example values |
| --- | --- | --- | --- |
| ` app ` | string | The system, service, or application that generated the alert event. Examples include "Nagios Host", "Solarwinds", "Splunk Infra Mon". | recommended for ITSI |
| ` description ` | string | The description of the alert event. Adds more detail to the ` signature ` field. | recommended for ITSI |
| ` entity_name ` | string | Used for the 'Entity Lookup Field' in the Universal Correlation Search. Default is ` <src> ` . | optional for ITSI |
| ` itsiDrilldownSearch ` | string | SPL to drill down into the details of this alert. Default is ` "index=* signature="<signature>" src="<src>" ` . | optional for ITSI |
| ` itsiDrilldownURI ` | string | External link for this alert, such as "https://bakookanet.com/alerts&alertid=1234567". | optional for ITSI |
| ` itsiDrilldownWeb ` | string | Optional Name for the link included in ` itsiDrilldownURI ` . Default is "External Drilldown for <itsiNotableTitle>" | optional for ITSI |
| ` itsiInclude ` | string | Boolean indicating whether this alert is automatically brought into ITSI as a Notable Event. If absent, ITSI assumes ` itsiInclude="true" ` . If ` itsiInclude="false" ` , ITSI does not onboard the alert. This is useful for testing or for specifically selecting which raw alerts to onboard as Notable Events. | recommended for ITSI |
| ` itsi_instruction ` | string | Text or markdown instructions for a human on how to handle this type of alert; can handle a link if encoded as markdown. See https://www.markdownguide.org . | optional for ITSI |
| ` itsiNotableTitle ` | string | Specifies which fields the Notable Event Title includes. Default is ` "<signature> - <src> (<subcomponent>)" ` . | optional for ITSI |
| ` severity_id ` | string | The numeric or vendor-specific severity indicator corresponding to the event severity. For ITSI, ` severity_id ` is one of the following values: 1 = Info or Unknown 2 = Normal or Cleared 3 = Low 4 = Medium 5 = High 6 = Critical | required for ITSI |
| ` signature ` | string | The human-friendly title of the alert event, such as 'Device Not Responding,' 'Disk Full,' or 'CPU usage too high.' | required for ITSI |
| ` src ` | string | The object that is the target, host, or object of the alert event. You can alias this field from existing fields such as ` src_host ` , ` src_ip ` , or ` src_name ` . | required for ITSI |
| ` subcomponent ` | string | Sub-component object for this alert. Further defines the ` src ` field. For example, for a "Filesystem Full" alert on "server42" for "/var": - signature = "Filesystem Full" - src = "server42" - subcomponent = "/var" Most alerts will not have a sub-component object. However, if the alert does contain a sub-component object, you must include this field. | recommended for ITSI |
| ` vendor_severity ` | string | The original vendor-specific severity/health/status string for this alert, such as up/down/ok/normal/critical/warning/red/green/minor/major. | required by ITSI |
