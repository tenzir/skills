<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/745682/system-process-performance-data-model -->

# System Process Performance Data Model

This data model describes system process level performance monitoring metrics collected by FortiSIEM’s own device monitoring.

The following events follow this data model – covers all device types: Windows, Linux and network devices.

- PH_DEV_MON_PROC_RESOURCE_UTIL

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| procName | string | Process Name | Name of the process |
| appName | string | Application Name | Application to which the process belongs |
| swParam | string | Software Param | Arguments with which the process runs |
| sysUpTime | uint32 | System Uptime | Process Uptime |
| cpuUtil | double | CPU Util | CPU Utilization 0-100 |
| memUtil | double | Memory Util | Memory Utilization 0-100 |
| realMemPeakKBytes | uint32 | Real Peak Memory KB | Real Memory used |
| virtMemKBytes | uint32 | Virtual Memory KB | Virtual Memory used |
| peakVirtMemKBytes | uint32 | Peak Virtual Memory KB | Peak Virtual Memory used |
| diskReadKBytesPerSec | double | Disk Read Rate KBps | Disk Read Volume in KBps |
| diskWriteKBytesPerSec | double | Disk Write Rate KBps | Disk Write Volume in KBps |
