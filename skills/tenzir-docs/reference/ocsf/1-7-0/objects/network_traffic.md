# Network Traffic

> The Network Traffic object describes characteristics of network traffic over a time period.


The Network Traffic object describes characteristics of network traffic over a time period. The metrics represent network data transferred between source and destination during an observation window.

## Attributes

**`bytes`**

* **Type**: `long_t`
* **Requirement**: recommended

The total number of bytes transferred in both directions (sum of bytes\_in and bytes\_out).

**`packets`**

* **Type**: `long_t`
* **Requirement**: recommended

The total number of packets transferred in both directions (sum of packets\_in and packets\_out).

**`bytes_in`**

* **Type**: `long_t`
* **Requirement**: optional

The number of bytes sent from the destination to the source (inbound direction).

**`bytes_missed`**

* **Type**: `long_t`
* **Requirement**: optional

The number of bytes that were missed during observation, typically due to packet loss or sampling limitations.

**`bytes_out`**

* **Type**: `long_t`
* **Requirement**: optional

The number of bytes sent from the source to the destination (outbound direction).

**`chunks`**

* **Type**: `long_t`
* **Requirement**: optional

The total number of chunks transferred in both directions (sum of chunks\_in and chunks\_out).

**`chunks_in`**

* **Type**: `long_t`
* **Requirement**: optional

The number of chunks sent from the destination to the source (inbound direction).

**`chunks_out`**

* **Type**: `long_t`
* **Requirement**: optional

The number of chunks sent from the source to the destination (outbound direction).

**`end_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The end time of the observation or reporting period.

**`end_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The end time of the observation or reporting period.

**`packets_in`**

* **Type**: `long_t`
* **Requirement**: optional

The number of packets sent from the destination to the source (inbound direction).

**`packets_out`**

* **Type**: `long_t`
* **Requirement**: optional

The number of packets sent from the source to the destination (outbound direction).

**`start_time`**

* **Type**: `timestamp_t`
* **Requirement**: optional

The start time of the observation or reporting period.

**`start_time_dt`**

* **Type**: `datetime_t`
* **Requirement**: optional

The start time of the observation or reporting period.

**`timespan`**

* **Type**: [`timespan`](timespan.md)
* **Requirement**: optional

The time span object representing the duration of the observation or reporting period.

## Used By

* [`airborne_broadcast_activity`](../classes/airborne_broadcast_activity.md)
* [`dhcp_activity`](../classes/dhcp_activity.md)
* [`dns_activity`](../classes/dns_activity.md)
* [`drone_flights_activity`](../classes/drone_flights_activity.md)
* [`ftp_activity`](../classes/ftp_activity.md)
* [`http_activity`](../classes/http_activity.md)
* [`network_activity`](../classes/network_activity.md)
* [`network_file_activity`](../classes/network_file_activity.md)
* [`ntp_activity`](../classes/ntp_activity.md)
* [`rdp_activity`](../classes/rdp_activity.md)
* [`smb_activity`](../classes/smb_activity.md)
* [`ssh_activity`](../classes/ssh_activity.md)
* [`tunnel_activity`](../classes/tunnel_activity.md)
* [`web_resource_access_activity`](../classes/web_resource_access_activity.md)
* [`web_resources_activity`](../classes/web_resources_activity.md)