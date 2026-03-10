# Event Classes

> Complete listing of OCSF 1.0.0 event classes by category.


Complete listing of event classes by category.

## Other

* [Base Event (0)](classes/base_event.md): The base event is a generic and concrete event.

## System Activity

* [File System Activity (1001)](classes/file_activity.md): File System Activity events report when a process performs an action on a file or folder.
* [Kernel Extension Activity (1002)](classes/kernel_extension.md): Kernel Extension events report when a driver/extension is loaded or unloaded into the kernel
* [Kernel Activity (1003)](classes/kernel_activity.md): Kernel Activity events report when an process creates, reads, or deletes a kernel resource.
* [Memory Activity (1004)](classes/memory_activity.md): Memory Activity events report when a process has memory allocated, read/modified, or other manipulation activities - such as a buffer overflow or turning off data execution protection (DEP).
* [Module Activity (1005)](classes/module_activity.md): Module Activity events report when a process loads or unloads the `module`.
* [Scheduled Job Activity (1006)](classes/scheduled_job_activity.md): Scheduled Job Activity events report activities related to scheduled jobs or tasks.
* [Process Activity (1007)](classes/process_activity.md): Process Activity events report when a process launches, injects, opens or terminates another process, successful or otherwise.

## Findings

* [Security Finding (2001)](classes/security_finding.md): Security Finding events describe findings, detections, anomalies, alerts and/or actions performed by security products

## Identity & Access Management

* [Account Change (3001)](classes/account_change.md): Account Change events report when specific user account management tasks are performed, such as a user/role being created, changed, deleted, renamed, disabled, enabled, locked out or unlocked.
* [Authentication (3002)](classes/authentication.md): Authentication events report authentication session activities such as user attempts a logon or logoff, successfully or otherwise.
* [Authorize Session (3003)](classes/authorize_session.md): Authorize Session events report privileges or groups assigned to a new user session, usually at login time.
* [Entity Management (3004)](classes/entity_management.md): Entity Management events report activity by a managed client, a micro service, or a user at a management console.
* [User Access Management (3005)](classes/user_access.md): User Access Management events report management updates to a user’s privileges.
* [Group Management (3006)](classes/group_management.md): Group Management events report management updates to a group, including updates to membership and permissions.

## Network Activity

* [Network Activity (4001)](classes/network_activity.md): Network Activity events report network connection and traffic activity.
* [HTTP Activity (4002)](classes/http_activity.md): HTTP Activity events report HTTP connection and traffic information.
* [DNS Activity (4003)](classes/dns_activity.md): DNS Activity events report DNS queries and answers as seen on the network.
* [DHCP Activity (4004)](classes/dhcp_activity.md): DHCP Activity events report MAC to IP assignment via DHCP from a client or server.
* [RDP Activity (4005)](classes/rdp_activity.md): Remote Desktop Protocol (RDP) Activity events report remote client connections to a server as seen on the network.
* [SMB Activity (4006)](classes/smb_activity.md): Server Message Block (SMB) Protocol Activity events report client/server connections sharing resources within the network.
* [SSH Activity (4007)](classes/ssh_activity.md): SSH Activity events report remote client connections to a server using the Secure Shell (SSH) Protocol.
* [FTP Activity (4008)](classes/ftp_activity.md): File Transfer Protocol (FTP) Activity events report file transfers between a server and a client as seen on the network.
* [Email Activity (4009)](classes/email_activity.md): Email events report activities of emails.
* [Network File Activity (4010)](classes/network_file_activity.md): Network File Activity events report activities on a cloud file storage service such as Box, MS OneDrive, or Google Drive.
* [Email File Activity (4011)](classes/email_file_activity.md): Email File Activity events report files within emails.
* [Email URL Activity (4012)](classes/email_url_activity.md): Email URL Activity events report URLs within an email.

## Discovery

* [Device Inventory Info (5001)](classes/inventory_info.md): Device Inventory Info events report device inventory data.
* [Device Config State (5002)](classes/config_state.md): Device Config State events report device configuration data.

## Application Activity

* [Web Resources Activity (6001)](classes/web_resources_activity.md): Web Resources Activity events describe actions executed on a set of Web Resources.
* [Application Lifecycle (6002)](classes/application_lifecycle.md): Application Lifecycle events report installation, removal, start, stop of an application or service.
* [API Activity (6003)](classes/api_activity.md): API events describe general CRUD (Create, Read, Update, Delete) API activities, e.g. (AWS Cloudtrail)
* [Web Resource Access Activity (6004)](classes/web_resource_access_activity.md): Web Resource Access Activity events describe successful/failed attempts to access a web resource over HTTP.