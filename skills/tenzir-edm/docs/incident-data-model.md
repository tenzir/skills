<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/165396/incident-data-model -->

# Incident Data Model

The following data model describes a FortiSIEM Incident. Each Incident is also an event with phEventCategory = 1. In addition to attributes in Base Event Data Model, the following attributes are present in Incident Data Model. These attributes must not be set for an event.

Note : Do NOT set these attributes in custom parsers.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| incidentId | uint64 | Incident ID | Unique ID of a FortiSIEM Incident |
| incidentTitle | string | Incident Title | This is defined in a Rule and copied over from the Rule that triggered the Incident. |
| phIncidentCategory | string | Incident Category | This is defined in a Rule and copied over from the Rule that triggered the Incident. |
| phSubIncidentCategory | string | Incident Subcategory | This is defined in a Rule and copied over from the Rule that triggered the Incident. |
| incidentFirstSeen | DATE | Incident First Occurrence Time | The first time an Incident happened. |
| incidentLastSeen | DATE | Incident Last Occurrence Time | The last time an Incident happened. When an Incident with the same parameter occurs, the count variable is updated and the Incident Last Occurrence time is advanced. |
| incidentSrc | string | Incident Source | This field collects a set of Incident fields that can be considered as a source: srcIpAddr, srcName,srcUser. They are recorded as comma separated Attribute:Value format. |
| incidentTarget | string | Incident Target | This field collects a set of Incident fields that can be considered as a Target: destIpAddr, destName, hostIpAddr, hostName, user, targetUser. They are recorded as comma separated Attribute:Value format. |
| incidentDetail | string | Incident Detail | This field collects the remaining Incident fields that are neither Incident Source nor Incident Target |
| incidentRptIp | IP | Incident Reporting IP | This field captures the reporting IP of the events that triggered an Incident. In the case there are multiple reporting IPs, only 1 is chosen. |
| incidentRptDevName | string | Incident Reporting Device | The reporting device name of the events that triggered an Incident. In the case there are multiple reporting IPs, only 1 is chosen. |
| incidentRptDevStatus | uint16 | Incident Reporting Device Status | This fields records the CMDB status of an Incident Reporting device. 1: Pending, 2: Approved, 3: Unmanaged |
| incidentStatus | uint16 | Incident Status | Incident management status is recorded. 0: Active, 1: Auto Cleared, 2:Manually Cleared. When an Incident is triggered, it becomes Active. An Incident can be cleared by the System, when the clearing condition in the rule is met or at the end of day for non-security Incidents. A user can also clear an Incident from GUI. |
| incidentTagName | string | Incident Tag Name | The Tag assigned to an Incident from the GUI. |
| attackTactic | string | Attack Tactic | MITRE Attack Tactic. This is defined in a Rule and copied over from the Rule that triggered the Incident. |
| attackTechnique | string | Attack Technique | MITRE Attack Technique. This is defined in a Rule and copied over from the Rule that triggered the Incident. |
| incidentClearedTime | DATE | Incident Cleared Time | When an Incident is cleared, then the Incident clearing time is recorded in this field. |
| incidentClearedUser | string | Incident Cleared User | When an Incident is cleared, then the user clearing the Incident is recorded in this field. |
| incidentClearedReason | string | Incident Cleared Reason | When an Incident is cleared, then the reason for clearing the Incident is recorded in this field. The reason is entered via GUI. |
| incidentNotiStatus | string | Incident Notification Status | This field repsents the status of incident notification (Success or Failed). When an Incident triggers, notification can happen via email, HTTPS, external ticketing system etc. |
| incidentNotiRecipients | string | Incident Notification Recipients | If an Incident notification is sent out via email, then the email recipients are recorded in this field. |
| incidentTicketId | string | Incident Ticket ID | This is the ID of a Ticket/Case in FortiSIEM. A Ticket/Case can be opened from a FortiSIEM Incident. |
| incidentTicketStatus | uint16 | Incident Ticket Status | This is the status of a Ticket/Case in FortiSIEM. A Ticket/Case can be opened from a FortiSIEM Incident. Possible values are 0: New, 1: Assigned, 2:Closed, 3: InProgress, 4: Reopened, 5: OverDue, 6: None |
| incidentTicketUser | string | Incident Ticket User | This is the user who is assigned a Ticket/Case in FortiSIEM. A Ticket/Case can be opened from a FortiSIEM Incident. |
