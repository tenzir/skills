<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/887813/system-configuration-change-data-model -->

# System Configuration Change Data Model

This data model describes host or user level configuration changes such as

- Network Device Configuration Changes
- Host system or user settings changes
- Cloud system or user level settings changes

Example events:

- FortiGate-event-config-change
- FortiWeb-20201 (A FortiWeb administrator configured a connection to a Syslog server)
- Win-Security-5448 (Windows Filtering Platform provider has been changed)
- Win-Security-4950 (A Windows Firewall setting has changed)
- MS_OFFICE365_EntraID_Set_MFA_registration_policy
- Win-Firewall-AS-2004 (A rule has been added to the Windows Defender Firewall exception list)

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| srcIpAddr | IP | Source IP | Source IP of from where the change was made |
| srcName | string | Source Host Name | Source IP’s hostname |
| destIpAddr | IP | Destination IP | IP of the device where the change was made |
| destName | string | Destination Host Name | Destination IP’s host name |
| hostIpAddr | IP | Host IP | IP of the device where the change was made |
| hostName | string | Host Name | Host IP’s host name |
| user | string | User | User who made the change |
| addedItem | string | Added Item | Item that was added to config |
| deletedItem | string | Deleted Item | Item that was removed from config |
| configValue | string | Configuration Value | Latest configuration value |
| osObjName | string | OS Object Name | Configuration Object that was edited |
| objectPath | string | OS Object Path | Configuration Object Path |
| osObjValue | string | OS Object Value | Value of edited configutarion object |
| oldSVNVersion | string | Old SVN version | Previous SVN version of Network Device Config File |
| newSVNVersion | string | New SVN Version | New SVN version of Network Device Config File |
