---
title: Network Traffic Field Mapping
url: https://help.splunk.com/en/data-management/common-information-model/8.5/field-mappings/network-traffic-field-mapping
last_modified: 2026-04-01T20:48:26.501Z
version: 8.5
---

# Network Traffic Field Mapping

The following shows an example of how network traffic events map differently from various cloud providers to CIM data model field names.

See the Network Traffic data model for full field descriptions.

## Source flow example

The source flow event from Google Cloud Platform (GCP) and Amazon Web Services (AWS) is a good way to see a common event and how each cloud provider maps to CIM data model field names.

### GCP source flow

A sample GCP source flow follows:

Click expand or collapse to show or hide the example.

```text
{
   "resource":{
      "labels":{
         "subnetwork_id":"4884528796030499819",
         "subnetwork_name":"default",
         "location":"us-central1-c",
         "project_id":"gsa-project-151018"
      },
      "type":"gce_subnetwork"
   },
   "timestamp":"2020-05-13T18:10:27.15490124Z",
   "jsonPayload":{
      "src_vpc":{
         "subnetwork_name":"default",
         "vpc_name":"default",
         "project_id":"gsa-project-151018"
      },
      "dest_location":{
         "country":"usa",gce_subnetwork
         "asn":15169,
         "continent":"America"
      },
      "src_instance":{
         "region":"us-central1",
         "vm_name":"gke-cluster-1-default-pool-cc3d3622-09nt",
         "zone":"us-central1-c",
         "project_id":"gsa-project-151018"          /** -----  vendor_account
      },
      "start_time":"2020-05-13T18:10:22.594437852Z", /** -----  duration start time
      "rtt_msec":"0",                               /** -----  response_time
      "bytes_sent":"5300",                          /** -----  bytes_out, bytes_in, bytes
      "reporter":"SRC",                             /** -----  direction
      "packets_sent":"40",                          /** -----  packets_out, packets_in, packets
      "end_time":"2020-05-13T18:10:22.614528620Z",  /** -----  duration end time
      "connection":{
         "protocol":6,                              /** -----  transport
         "src_port":44114,                          /** -----  src_port
         "dest_ip":"173.255.116.127",               /** -----  dest_ip, dest, dvc
         "src_ip":"10.128.15.212",                  /** -----  src_ip, src, dvc
         "dest_port":443                            /** -----  dest_port
      }
   },
   "insertId":"atlo5sg16t94yf",
   "logName":"projects/gsa-project-151018/logs/compute.googleapis.com%2Fvpc_flows",
   "receiveTimestamp":"2020-05-13T18:10:27.15490124Z"
}
```

### AWS source flow

A sample AWS source flow follows:

Click expand or collapse to show or hide the example.

```text
2
772089552793            /** -----  account-id
eni-099b0af8dd18f05bd   /** -----  dvc
103.137.144.25          /** -----  src_ip, src
103.137.144.26          /** -----  dest_ip, dest
443                     /** -----  src_port
22271                   /** -----  dest_port
6                       /** -----  transport
19                      /** -----  packets
10984                   /** -----  bytes
1589294114              /** -----  duration
1589294114              /** -----  duration
ACCEPT
OK
```

### Source flow field mapping

Using the login success from GCP as a base sample, and comparing it to a similar event from AWS is a good way to see the similarities and differences per common CIM field names.

| Source example data | Provider field name | CIM field name |
| --- | --- | --- |
| Device example data | Provider field name | CIM field name |
| Source port example data | Provider field name | CIM field name |
| Destination example data | Provider field name | CIM field name |
| Destination port example data | Provider field name | CIM field name |
| Transport example data | Provider field name | CIM field name |
| Duration start time example data | Provider field name | CIM field name |
| Duration end time example data | Provider field name | CIM field name |
| Bytes example data | Provider field name | CIM field name |
| Packets example data | Provider field name | CIM field name |
| Direction example data | Provider field name | CIM field name |
| Vendor account example data | Provider field name | CIM field name |
| GCP ` 10.128.15.212 ` | data.jsonPayload.connection.src_ip | - src_ip - src - dvc if reporter=SRC |
| AWS ` 103.137.144.25 ` | srcaddr | - src_ip - src |
| GCP ` 10.128.15.212 ` | data.jsonPayload.connection.src_ip | dvc if reporter=SRC |
| AWS ` eni-099b0af8dd18f05bd ` | interface-id | dvc |
| GCP ` 44114 ` | data.jsonPayload.connection.src_port | src_port |
| AWS ` 443 ` | srcport | src_port |
| GCP ` 173.255.116.127 ` | data.jsonPayload.connection.dest_ip | - dest_ip - dest - dvc if reporter=DEST |
| AWS ` 103.137.144.26 ` | dstaddr | - dest - dest_ip |
| GCP ` 443 ` | data.jsonPayload.connection.dest_port | dest_port |
| AWS ` 22271 ` | dstport | dest_port |
| GCP ` 6 ` | data.jsonPayload.connection.protocol | transport |
| AWS ` 6 ` | protocol | transport |
| GCP ` 2020-05-13T18:10:22.594437852Z ` | data.jsonPayload.start_time | duration, calculated from start_time and end_time |
| AWS ` 1589294114 ` | start | duration, calculated from start_time and end_time |
| GCP ` 2020-05-13T18:10:22.614528620Z ` | data.jsonPayload.end_time | duration, calculated from start_time and end_time |
| AWS ` 1589294114 ` | end | duration, calculated from start_time and end_time |
| GCP ` 5300 ` | data.jsonPayload.bytes_sent | - bytes_out if reporter=SRC - bytes_in - bytes |
| AWS ` 10984 ` | bytes | bytes |
| GCP ` 40 ` | data.jsonPayload.packets_sent | - packets_out if reporter=SRC - packets_in - packets |
| AWS ` 19 ` | packets | packets |
| GCP ` SRC ` | data.jsonPayload.reporter | direction |
| AWS n/a | n/a | n/a |
| GCP ` gsa-project-151018 ` | data.jsonPayload.src_instance.project_id | vendor_account if reporter=SRC |
| AWS ` 772089552793 ` | account-id | vendor_account |
