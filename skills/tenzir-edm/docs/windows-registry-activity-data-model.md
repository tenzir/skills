<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/977589/windows-registry-activity-data-model -->

# Windows Registry Activity Data Model

This data model describes activities around windows registry entries

Example of Events from Registry monitoring via Windows Agent:

- AO-WUA-Registry-Added
- AO-WUA-Registry-Modified
- AO-WUA-Registry-Removed

Example of Events from Sysmon Registry monitoring:

- Win-Sysmon-12-Registry-DeleteValue
- Win-Sysmon-12-Registry-DeleteKey
- Win-Sysmon-12-Registry-CreateValue
- Win-Sysmon-12-Registry-CreateKey
- Win-Sysmon-13-Registry-SetValue
- Win-Sysmon-14-Registry-RenameValue
- Win-Sysmon-14-Registry-RenameKey

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| user | string | User | User who performed registry action |
| regKeyPath | string | Registry Key Path | Registry Key |
| regValueName | string | Registry Value Name | Registry Value |
| oldRegValue | string | Old Registry Value | Old Registry Value |
| newRegValue | string | New Registry Value | New Registry Value |
