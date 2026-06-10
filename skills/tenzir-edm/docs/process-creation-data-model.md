<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/892201/process-creation-data-model -->

# Process Creation Data Model

This includes process creation in Windows and Linux hosts.

Event from Windows Sysmon via Windows Agent:

- Win-Sysmon-1-Create-Process

Event from Linux Agent:

- LINUX_PROCESS_EXEC

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| user | string | User | User creating the process |
| procName | string | Process Name | Process name (Full path) |
| shortProcName | string | Short Process Name | Short process name (without full path) |
| procId | string | Process Id | Process Id |
| parentProcName | string | Parent Process Name | Parent Process Name (full path) |
| shortParentProcName | string | Short Parent Process Name | Short parent process name (without full path) |
| parentProcId | string | Parent Process Id | Parent Process Id |
| imageFile | string | Image File |  |
| command | string | Command | Full Command executed to create process |
| hashAlgo | string | Hash Algorithm | Hash Algorithm |
| hashCode | string | Hash Code | Hash Code |
| hashSHA256 | string | SHA256 Hash | SHA256 Hash Value |
| hashSHA512 | string | SHA512 Hash | SHA512 Hash Value |
| hashIMP | string | IMP Hash | Import hash Value – IMP Hash remains consistent even if the malware is slightly modified or repacked, making it effective for identifying related threat actor tools. |
| hashSHA1 | string | SHA1 hash | SHA1 hash |
| hashMD5 | string | MD5 hash | MD5 hash |

|  | Note : - If event contains only one specific hash values, e.g. SHA512 Hash, then that specific attribute, e.g. hashSHA512, is set. Also, hashAlgo is set to SHA512 and hashCode is set to SHA512Hash. - If event contains more than one hash values, then - All specific hash attributes are set. - Hash Algo and Code is set to the first found values in this order: IMPHash, SHA256, SHA512, SHA1, MD5 |
| --- | --- |
