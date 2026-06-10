<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/754816/authentication-data-model -->

# Authentication Data Model

This group includes authentication events (successful ot failed) to a host, network device, an application or a cloud service.

Examples of event types following this data model:

Windows/Linux login:

- Win-Security-4624- logon success
- Win-Security-4625 – login failed
- Generic_Unix_Successful_SSH_Login
- Generic_Unix_Failed_SSH_Login

Network device login:

- FortiGate-sslvpn-logon-success

Application Login:

- ORADB_Logon_Success
- MYSQL_Logon_Success
- Win-App-MSSQLSERVER-18454
- Win-App-MSSQLSERVER-18453

Cloud Service Login:

- AWS-CloudTrail-SIGNIN-ConsoleLogin-Success
- MS_OFFICE365_EntraID_StsLogon_UserLoggedIn
- Oracle-OCI-identitysignon-federatedloginrequest-success

The full list is available from Resources > Event Types > Security > Logon Success .

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| srcIpAddr | IP | Source IP | Source IP of a device as identified in the event. |
| destIpAddr | IP | Destination IP | Destination IP of a device as identified in the event. |
| destName | string | Destination Host Name | Destination device's hostname as identified in the log, can also be enriched using reverse lookup of the destination IP address. |
| user | string | User | User trying to login |
| domain | string | Domain | Windows domain |
| winLogonType | uint16 | Win Logon Type | Windows Logon Type, e.g. 2: Interactive - Console Llogon 3: Network – Logon 4: Batch Logon 5: Service Logon 7: User unlocks a locked workstation 9: New Credentials 10: Remote Desktop Logon 11: Cached Domaon Credential Logon |
| winLogonId | string | Win Logon Id | Windows Logon Id |
| winLogonProc | string | Windows Logon Process | The Windows process handling Windows logon |
| authenMethod | string | Authentication Method | Windows Authentication method |
| winLogonFailCode | uint64 | Win Logon Fail Code | Windows Logon Failure Codes in numerical format |
| winLogonFailCode2 | string | Win Logon Fail Code String | Windows Logon Failure Codes in string format, e.g. 0xC000006E: Unknown user name or bad password |
