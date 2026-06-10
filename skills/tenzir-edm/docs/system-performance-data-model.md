<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/326870/system-performance-data-model -->

# System Performance Data Model

This data model describes system performance monitoring metrics collected by FortiSIEM's own device monitoring.

The following events follow this data model – covers all device types: Windows, Linux and network devices:

- PH_DEV_MON_SYS_UPTIME (Uptime monitoring)
- PH_DEV_MON_SYS_CPU_UTIL (CPU monitoring)
- PH_DEV_MON_SYS_PER_CPU_UTIL (CPU monitoring for each CPU)
- PH_DEV_MON_SYS_MEM_UTIL (memory monitoring)
- PH_DEV_MON_SYS_VIRT_MEM_UTIL (virtual memory monitoring)
- PH_DEV_MON_SYS_DISK_UTIL (disk space monitoring)
- PH_DEV_MON_DISK_IO_UTIL (Disk I/O Monitoring)
- PH_DEV_MON_SYS_PAGEFILE_USAGE (windows page file monitoring)
- PH_DEV_MON_NET_INTF_UTIL (Network interface utilization monitoring)

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

- CPU Monitoring
- Disk I/O Monitoring
- Disk Space Monitoring
- Memory Monitoring
- Network Interface Monitoring
- Uptime Monitoring

## CPU Monitoring

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| cpuName | string | CPU Name | CPU name (CPU-1, CPU-2) etc for multi-CPU monitoring |
| cpuUtil | double | CPU Util | CPU Util (0-100) |
| sysCpuUtil | double | System CPU Util | Linux System CPU Util (0-100) |
| userCpuUtil | double | User CPU Util | Linux User CPU Util (0-100) |

## Disk I/O Monitoring

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| diskName | string | Disk Name | Disk name |
| diskType | string | Disk Type | Disk Type |
| diskIOUtil | double | Disk Capacity Util | Disk Capacity Util (0-100) |
| diskQLen | uint32 | Disk Queue Length | Disk Queue Length |
| diskReadReqPerSec | double | Disk Read Rate req/sec | Disk Read Rate in requests/sec |
| diskWriteReqPerSec | double | Disk Write Rate req/sec | Disk Write Rate in requests/sec |
| diskReadKBytesPerSec | double | Disk Read Rate KBps | Disk Read Volume in KBps |
| diskWriteKBytesPerSec | double | Disk Write Rate KBps | Disk Write Volume in KBps |
| diskTfrKBytesPerSec | double | Disk Transfer Rate KBps | Disk Transfer Volume in KBps |

## Disk Space Monitoring

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| diskName | string | Disk Name | Disk name |
| diskUtil | double | Disk Capacity Util | Disk Capacity Util (0-100) |
| totalDiskMB | uint32 | Total Disk MB | Total Disk MB |
| freeDiskMB | uint32 | Free Disk MB | Free Disk MB |
| usedDiskMB | uint32 | Used Disk MB | Used Disk MB |

## Memory Monitoring

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| memName | string | Memory Name | Physical Memory, Virtual Memory etc |
| memUtil | double | Memory Util | Memory Util (0-100) |
| freeMemKB | uint32 | Free Memory | Free Memory in KB |
| bufMemKB | uint32 | Buffer Memory | Linux Buffer memory in KB |
| cacheMemKB | uint32 | Cache Memory | Linux Cache memory in KB |

## Network Interface Monitoring

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| intfName | string | Host Interface Name | Name of a network interface in a host. |
| isHostIntfCritical | string | Host Interface Critical | Yes if the interface is Critical; no if it is not. |
| isHostIntfWAN | string | Interface WAN Flag | Yes if the interface is WAN interface; no if it is not. |
| intfInSpeed64 | uint64 | Recv Interface Speed bps | High Speed Network Interface Speed (bits/sec). |
| intfOutSpeed64 | uint64 | Sent Interface Speed bps | High Speed Network Interface Speed (bits/sec). |
| intfAdminStatus | string | Interface Admin Status | Interface Administrative Status – Up or Down |
| intfOperStatus | string | Interface Operational Status | Interface Operational Status – Up or Down |
| inIntfUtil | double | Recv Interface Util | Ratio of Received Bits per second (derived from recvBytes) to the received network interface speed |
| outIntfUtil | double | Sent Interface Util | Ratio of Sent Bits per second (derived from sentBytes) to the sent network interface speed |
| inIntfPktErr | uint32 | Recv Packet Errors | Number of received packets that had errors. The networking stack discards these packets. |
| outIntfPktErr | uint32 | Sent Packet Errors | Number of sent packets that had errors. he networking stack discards these packets. |
| inIntfPktErrPct | double | Recv Packet Error Pct | Ratio of inIntfPktErr and the total number of received packets in an onterval |
| outIntfPktErrPct | double | Sent Packet Error Pct | Ratio of outIntfPktErr and the total number of received packets in an onterval |
| inIntfPktDiscarded | uint32 | Recv Packet Discards | Total number of received packets that were discarded by the networking stack. |
| outIntfPktDiscarded | uint32 | Sent Packet Discards | Total number of sent packets that were discarded by the networking stack. |
| inIntfPktDiscardedPct | double | Recv Packet Discard Pct | Ratio of inIntfPktDiscarded on an interface to the total number of received packets on that interface |
| outIntfPktDiscardedPct | double | Sent Packet Discard Pct | Ratio of outIntfPktDiscarded on an interface to the total number of sent packets on that interface |

## Uptime Monitoring

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostIpAddr | IP | Host IP | IP address of hostName |
| hostName | string | Host Name | Host where event occurs |
| sysUpTime | uint32 | System Uptime | System Uptime (seconds) |
| sysUpTimePct | double | System Uptime Pct | System Uptime Pct (0-100) |
