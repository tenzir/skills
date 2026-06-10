<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/827272/endpoint-security-finding-data-model -->

# Endpoint Security Finding Data Model

This data model describes Host IPS / Endpoint Detection Events such as

- Malware Found
- Suspicious Process Activity

Example events:

- Crowdstrike-Falcon-EppDetectionSummaryEvent-Known-Malware
- FortiClient-antiransomware-suspicious-process
- FortiEDR-Security-PUP-Block
- FortiEDR-Security-Suspicious-Blocked
- MSDefenderXDR-Alert-Execution-new
- SentinelOne-EPP-Threat_Mark_As_Threat
- S1-Singularity-Activity-4104 (STAR Manual Response Marked Event As Malicious)
- FireAMP_Cloud_Executed_malware

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| procName | string | Process Name | Process binary with full path |
| shortProcName | string | Short Process Name | Process binary only |
| procId | string | Process Id |  |
| command | string | Command | Command to execute process including full path and arguments |
| parentProcName | string | Parent Process Name | Parent Process Name (full path) |
| shortParentProcName | string | Short Parent Process Name | Short parent process name (without full path) |
| parentProcId | string | Parent Process Id | Parent Process Id |
| user | string | User | User executing command |
| fwAction | string |  | Action taken by the Endpoint |
| osType | string | Operating System Type | Operating system type |
| hashCode | string | Hash Code | Hash of process binary |
| hashAlgo | string | Hash Algorithm | Algorithm for hashCode |
| virusName | string | Malware Name | Malware Name |
| virusType | string | Malware Type | Malware Type |
| virusFamily | string | Malware Family | Malware Family |
| attackTactic | string | Attack Tactic | MITRE ATTACK Tactic |
| attackTechniqueId | string | Attack Technique Id | MITRE ATTACK Technique Id |
| attackTechnique | string | Attack Technique | MITRE ATTACK Technique Description |
| verdict | string | Verdict | Verdict about the Malware |
