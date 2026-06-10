<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/773915/dns-activity-data-model -->

# DNS Activity Data Model

This data model can be used to describe DNS name resolution activity, including both FQDN -> IP and IP -> FQDN resolutions.

Examples from BIND

- BIND_DNS_A_Query
- BIND_DNS_PTR_Query

Examples from Cisco Umbrella:

- CiscoUmbrella-DNS-AAAA-Query-allowed
- CiscoUmbrella-DNS-AAAA-Query-blocked
- CiscoUmbrella-DNS-A-Query-allowed
- CiscoUmbrella-DNS-A-Query-blocked
- CiscoUmbrella-DNS-PTR-Query-allowed
- CiscoUmbrella-DNS-PTR-Query-blocked

Examples from FortiSIEM Windows Agent (DNS DebugLogs)

- AO-WUA-DNS-A-Query-Success
- AO-WUA-DNS-A-Query-Failed
- AO-WUA-DNS-PTR-Query-Success
- AO-WUA-DNS-PTR-Query-Failed
- AO-WUA-DNS-AAAA-Query-Success
- AO-WUA-DNS-AAAA-Query-Failed

Examples from Microsoft DNS:

- MS_DNS_A_Success
- MS_DNS_A_Fail
- MS_DNS_AAAA_Success
- MS_DNS_AAAA_Fail
- MS_DNS_PTR_Success
- MS_DNS_PTR_Fail

Examples from other devices:

- FortiGate-dns-query

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| srcIpAddr | IP | Source IP | Source IP of a device as identified in the event. |
| destIpAddr | IP | Destination IP | Destination IP of a device as identified in the event. |
| destName | string | Destination Host Name | Destination device's hostname as identified in the log, can also be enriched using reverse lookup of the destination IP address. |
| sentBytes64 | uint64 | Sent Bytes64 | Number of bytes sent by a host. This has 64bit resolution. |
| recvBytes64 | uint64 | Received Bytes64 | Number of bytes received by a host. This has 64bit resolution. |
| totBytes64 | uint64 | Total Bytes64 | Total number of sent and received bytes by a host. This has 64bit resolution. |
| dnsQueryType | string | DNS Query Type | This is the DNS query record type such as A, AAA, PTR, etc. |
| dnsResponseCode | uint16 | DNS Response Code |  |
| dnsQueryName | string | DNS Query Name | This is the name the dns client queried the DNS server to resolve. |
| dnsQueryClass | string | DNS Query Class | DNS Query Class |
