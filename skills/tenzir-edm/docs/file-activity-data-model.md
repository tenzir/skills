<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/218396/file-activity-data-model -->

# File Activity Data Model

This describes file read/write/create/delete/move/permission change / content change activity.

Events from Windows Sysmon via Windows Agent:

- Win-Sysmon-11-FileCreate
- Win-Sysmon-11-FileDelete
- Win-Sysmon-11-FileDelete-archived

Events from Windows Agent UEBA:

- FINS-Windows-file-created
- FINS-Windows-file-deleted
- FINS-Windows-file-moved
- FINS-Windows-file-read
- FINS-Windows-file-renamed
- FINS-Windows-file-written

Events from Windows Agent FIM via Windows Agent:

- AO-WUA-FileMon-Added: A windows file or directory created
- AO-WUA-FileMon-Modified: A windows file or directory modified
- AO-WUA-FileMon-Removed: A windows file or directory deleted
- AO-WUA-FileMon-ArchivedBitChange: A windows file archive bit changed
- AO-WUA-FileMon-OwnershipChange: A windows file or directory ownership changed
- AO-WUA-FileMon-PermissionChange: A windows file or directory permission changed
- AO-WUA-FileMon-Renamed-New-Name: A windows file or directory renamed: shows new name
- AO-WUA-FileMon-Renamed-Old-Name: A windows file or directory renamed: shows old name
- AO-WUA-FileMon-BaselineChange: A Windows file baseline changed

Events from Linux Agent FIM via Linux Agent:

- FSM_LINUX_FILE_ACCESS
- FSM_LINUX_FILE_OPEN
- FSM_LINUX_FILE_CREATE
- FSM_LINUX_FILE_DELETE
- FSM_LINUX_FILE_MODIFY
- FSM_LINUX_FILE_CLOSE
- FSM_LINUX_FILE_UNMOUNT
- FSM_LINUX_FILE_MOVED
- FSM_LINUX_FILE_MOVED_FROM
- FSM_LINUX_FILE_MOVED_TO
- FSM_LINUX_FILE_ATTRIB_CHANGE

Events from File Content Monitoring via Windows/Linux Agent:

- PH_DEV_MON_FILE_CONTENT_CHANGE

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| user | string | User | User doing file activity |
| domain | string | Domain | User’s Windows’s domain |
| fileName | string | File Name | File Name |
| fileType | string | File Type | File Type |
| procName | string | Process Name | Process doing file activity |
| activityName | string | Activity Name | File Activity Name (read, write etc) |
| resourceName | string | Resource Name | Resource involved in File Activity |
| oldSVNVersion | string | Old SVN version | Previous SVN version of monitored File |
| newSVNVersion | string | New SVN Version | New SVN version of monitored File |
