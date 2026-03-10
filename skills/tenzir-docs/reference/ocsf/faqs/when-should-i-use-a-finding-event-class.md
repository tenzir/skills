# When should I use a Finding event class?

> OCSF FAQ: When should I use a Finding event class?


A Finding in OCSF represents the result of some type of enrichment, correlation, aggregation, analysis or other processing of one or more events or alerts, producing a derived insight. Most security events and alerts are activity events with a disposition (e.g. Blocked), for example when using the Security Control profile. Findings in OCSF are not always alerts themselves, although alerts may be triggered by findings or findings might be added to an incident further downstream.

For example, an email security product may determine that a user has been phished or an email attachment is malicious. It would send an email activity event (from its standpoint an alert) containing the user and sender, supplemented by the Security Control profile with a disposition of Blocked, and information about the Malware, to its management console which in turn sends it to a SIEM.

The SIEM might receive other related events or alerts, for example for other users in the same circumstance or for general email activity from the same sender. The SIEM might enrich the events with information from a Threat Intelligence Platform or threat feed pertaining to the email sender. The result of the aggregation, and enrichment would constitute an OCSF Finding. The SIEM might create an incident that includes or refers to the finding, in the event that there are remediation steps required.

Note that in a more complex processing architecture, there may be layered findings. That is, the original event may go to product A which eventually triggers a finding. Product B meanwhile may take in a lot of other events and findings (including those from product A) and make its own findings. In the example above, the originating email alert might have been a finding from the producer’s standpoint if the event was enriched by its management system before being collected by the SIEM, which then produced a more complete finding.