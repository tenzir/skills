<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/847020/mail-activity-data-model -->

# Mail Activity Data Model

This data model can be used to describe mail traffic handling.

Example Event Types from Cisco Email Security Appliance (ESA):

- Cisco-IronPort-Mail-DeliveryComplete
- Cisco-IronPort-Mail-Aborted
- Cisco-IronPort-Mail-AVPositive-Dropped
- Cisco-IronPort-Mail-FilterDrop
- Cisco-IronPort-Mail-Drop
- Cisco-IronPort-Mail-HardBounce
- Cisco-IronPort-Mail-SoftBounce
- Cisco-IronPort-Mail-SpamQuarantine-Complete

Example Event Types from Office365 Exchange Online

- MS_OFFICE365_ThreatIntel_TIMailData_DeliveredAsSpam
- MS_OFFICE365_ThreatIntel_TIUrlClickData_BlockPage

Example Event Types from Mimecast:

- Mimecast_delivery_external_success
- Mimecast_delivery_inbound_success
- Mimecast_delivery_outbound_failed
- Mimecast_delivery_inbound_failed
- Mimecast_attachmentLogs_malicious
- Mimecast_spam_email_found
- Mimecast_attachment_protect
- Mimecast_clickLogs_allow
- Mimecast_clickLogs_block

Example Event Types from Proofpoint:

- Proofpoint-messagesDelivered-malicious
- Proofpoint-messagesDelivered-clean
- Proofpoint-messagesBlocked-clean
- Proofpoint-messagesBlocked-malicious
- Proofpoint-clicksBlocked
- Proofpoint-clicksPermitted

Example Event Types from FortiMail:

- FortiMail-Antispam-malicious-attachment-file
- FortiMail-Antispam-malicious-attachment-url
- FortiMail-Antivirus-virus-infected

Example Event Types from FortiMail Workspace:

- FortiMail-Workspace-Scan-email-mal-delivered
- FortiMail-Workspace-Scan-email-mal-quarantine
- FortiMail-Workspace-Scan-email-mal-quarantine_by_microsoft

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| senderMailAddr | string | Mail Sender | Sender mail address |
| receiverMailAddr | string | Mail Receiver | Receive mail address |
| ccMailAddr | string | Mail CC | Mail addresses in CC list |
| mailSubject | string | Mail Subject | Mail Subject |
| srcDomain | string | Source Domain | Sender mail domain |
| destDomain | string | Destination Domain | Receiver mail domain |
| fileName | string | File Name | File attachment |
| downloadURL | string | Download URL | URL found in mail |
| virusId | string | Virus/Malware Id | Malware id (found in mail) |
| virusName | string | Malware Name | Malware name (found in mail) |
| webCategory | string | Website Category | External mail domain category |
| action | string | Action | Mail Inspection Action: Quarantine, Delete, Clean |
| status | string | Status | Verdict: Malicious, Safe |
| threatLevel | string | Threat Level | Threat Level |
| threatType | string | Threat Type | Threat Type |
| threatCategory | string | Threat Category | Threat Category |
| riskScore | string | Risk Score | Risk Score |
| spamScore | string | Spam Score | Spam Score |
| infoURL | string | Informational URL | Information about a threat |
