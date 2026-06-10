<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/261556/network-traffic-data-model -->

# Network Traffic Data Model

This model describes network traffic.

Examples of Event Types from Network Devices:

- FortiGate-traffic-allowed
- IOS-NETFLOW-BI
- FortiGate-NetFlow
- FortiProxy-NetFlow
- ASA-Built-Conn
- PAN-OS-TRAFFIC-end-allow
- PAN-OS-TRAFFIC-start-allow

Examples of Event Types from hosts:

- Win-Sysmon-3-Network-Connect-IPv4
- Win-Sysmon-3-Network-Connect-IPv6
- Win-Security-5156

The full list is available in Resources > Event Types > Regular Traffic > Permit Traffic :

- Permitted Network Traffic
- Permitted BiNetflow
- Permitted Netflow

In addition to attributes in Base Event Data Model, the following attributes are present in Network Traffic Data Model.

| Event Attribute | Type | Name | Description |
| --- | --- | --- | --- |
| srcIpAddr | IP | Source IP | Source IP of a device as identified in the event. |
| srcName | string | Source Host Name | Source device's hostname as identified in the log, can also be enriched using reverse lookup of the source IP address. |
| destIpAddr | IP | Destination IP | Destination IP of a device as identified in the event. |
| destName | string | Destination Host Name | Destination device's hostname as identified in the log, can also be enriched using reverse lookup of the destination IP address. |
| srcMACAddr | Source MAC | Source MAC | Source MAC address in the event |
| destMACAddr | string | Destination MAC | Destination Layer 2 MAC Address in the log |
| ipProto | uint16 | IP Protocol | IP Protocol, e.g. TCP, UDP, ICMP etc as defined in IP RFPs |
| srcIpPort | uint16 | Source TCP/UDP Port | This is the source TCP or UDP port as identified in the event |
| destIpPort | uint16 | Destination TCP/UDP Port | This is the destination TCP or UDP port as identified in the event |
| postNATSrcIpAddr | IP | Post-NAT Source IP | The Source IP after Firewall Outbound Network Address Translation (NAT). This is often present in Firewall Address translation logs |
| preNATDestIpAddr | IP | Pre-NAT Destination IP | The Destination IP before Firewall Inbound Network Address Translation (NAT) - often present in Firewall Address translation log |
| postNATSrcIpPort | uint16 | Post-NAT Source Port | The Source TCP/UDP Port after Firewall Outbound Network Address Translation (NAT) - often present in Firewall Address translation log |
| preNATDestIpPort | uint16 | Pre-NAT Destination Port | The Destination TCP/UDP Port before Firewall Inbound Network Address Translation (NAT) - often present in Firewall Address translation log |
| fwRule | string |  | Firewall Policy that triggered the event |
| fwAction | string |  | Action taken by the network appliance |
| icmpId | uint64 | ICMP Id | ICMP Id in the ICMP header after the IPv4 header |
| icmpType | uint16 | ICMP Type | ICMP Type as defined in RFP, e.g. Echo Reply, Echo Response, Destination Unreachable etc. This attribute is generally present in ICMP Traffic log and Netflow. |
| icmpCode | uint16 | ICMP Code | ICMP Code for each Type. This attribute is generally present in ICMP Traffic log and Netflow. |
| tcpFlags |  |  |  |
| srcASNum32 | uint32 | Source Autonomous System Number32 | The Autonomous System Number (ASN) to which Source IP belongs. ASN is a unique identifier that is globally available and allows its autonomous system to exchange routing information with other systems. This attribute is generally present in Netflow. |
| destASNum32 | uint32 | Destination Autonomous System Number32 | The Autonomous System Number (ASN) to which Destination IP belongs. ASN is a unique identifier that is globally available and allows its autonomous system to exchange routing information with other systems. This attribute is generally present in Netflow. |
| srcVLAN | uint16 | Source VLAN | The VLAN to which the Source Network Interface belongs. Source network interface through which a packet enters a network device. |
| destVLAN |  |  |  |
| srcIntfName | string | Source Interface Name | Name of the network interface through which a packet enters a network device. This information is typically present in Firewall logs. |
| destIntfName |  |  |  |
| srcDevPort | string | Source Device Port | Name of the network port through which a packet enters a network device. This information is typically present in Firewall logs. |
| destDevPort | string | Destination Device Port | Name of the network port through which a packet exits a network device. This information is typically present in Firewall logs. |
| srcSnmpIntfIndex | uint16 | Source Interface SNMP Index | SNMP index of the network interface through which a packet enters a network device. This information is typically present in Firewall logs. |
| destSnmpIntfIndex | uint16 | Destination Interface SNMP Index | SNMP index of the network interface through which a packet exits a network device. This information is typically present in Firewall logs. |
| srcDestTCPFlags | uchar | Sent TCP flags | TCP flags sent from Source to Destination, as found in a packet reported by Netflow. The various combinations of SYN, URG, ACK, PSH, FIN, and RST are presented in logical OR; e.g. 3: SYN FIN, 11: SYN FIN PSH etc |
| destSrcTCPFlags | uchar | Received TCP flags | TCP flags sent from Destination to Source as found in a packet reported by Netflow. The various combinations of SYN, URG, ACK, PSH, FIN, and RST are presented in logical OR; e.g. 3: SYN FIN, 11: SYN FIN PSH etc |
| srcFwZone | string | Source Firewall Zone | Source Firewall Zone found in Firewall logs |
| destFwZone | string | Destination Firewall Zone | DestinationFirewall Zone found in Firewall logs |
| sentPkts64 | uint64 | Sent Packets in 64 bit precision | Number of packets sent by a host. This is 64bit version. |
| recvPkts64 | uint64 | Received Packets in 64 bit precision | Number of packets received by a host. This is 64bit version. |
| totPkts64 | uint64 | Total Packets in 64 bit precision | Total number of sent and received packets by a host. This is 64bit version. |
| sentBytes64 | uint64 | Sent Bytes in 64 bit precision | Number of bytes sent by a host. This has 64bit resolution. |
| recvBytes64 | uint64 | Received Bytes in 64 bit precision | Number of bytes received by a host. This has 64bit resolution. |
| totBytes64 | uint64 | Total Bytes in 64 bit precision | Total number of sent and received bytes by a host. This has 64bit resolution |
| srcGeoCountry | string | Source Country | The Country in which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoCountry | string | Destination Country | The Country in which the Destination IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoState | string | Source State | The State in the country in which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoState | string | Destination State | The State in the Country in which the Destination IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoCity | string | Source City | The City in which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoCity | string | Destination City | The City in which the Destination IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoLatitude | string | Source Latitude | The latitude on which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoLatitude | string | Destination Latitude | The latitude on which the Destination IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoLongitude | string | Source Longitude | The longitude on which the Source IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoLongitude | string | Destination Longitude | The longitude on which the Destination IP in event is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoOrg | string | Source Organization | The Organization to which the Source IP in event belongs. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoOrg | string | Destination Organization | The Organization to which the Destination IP in event belongs. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcGeoCountryCodeStr | string | Source Country Code | The Country Code in which the Source IP is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| destGeoCountryCodeStr | string | Destination Country Code | The Country Code in which the Destination IP is located. This information is collected by doing a IP GeoDB lookup for external IPs, and CMDB lookup for internal IPs. The latter requires users to add CMDB Device location information in FortiSIEM GUI. |
| srcTos | uchar | Source TOS | Source Type of Service (ToS) field present in the IPv4 header. Typically present in Netflow. It provides an indication of the quality of service desired. |
| dstTos | uchar | Destination TOS | Destination Type of Service (ToS) field present in the IPv4 header. Typically present in Netflow. It provides an indication of the quality of service desired. |
| seqNum | uint64 | Sequence Number | TCP Sequence number field in TCP header. |
| tcpAckNum | uint64 | TCP ACK Number | TCP Acknowledgement number field in TCP header. |
| tcpOffset | uint32 | TCP Offset | TCP Data Offset field in TCP header |
| tcpReserved | uint32 | TCP Reserved | TCP Reserved field in TCP header |
| tcpWindow | uint32 | TCP Window | TCP Window field in TCP header |
| tcpUrgentPointer | uint32 | TCP URGENT Pointer | TCP Urgent Pointer field in TCP header |
| tcpLen | uint32 | TCP Length | TCP length field in TCP header |
| udpLen | uint32 | UDP Length | UDP length field in UDP header |
| ipVersion | uint16 | IP Version | IP Version found in IP header |
| ipHeaderLength | uint16 | IP Header Length | IP Header Length found in IP header |
| ipTotalLength | uint16 | IP Total Length | IP Total Length found in IP header |
| ipId | uint16 | IP ID | IP ID found in IP header |
| ipFlags | uint16 | IP Flags | IP Flags found in IP header |
| ipFragOffset | uint16 | IP Fragment Offset | IP Fragment Offset found in IP header |
| ipTtl | uint16 | IP TTL | IP Time to Live (TTL) field found in IP header |
| ipChecksum | uint16 | IP Checksum | IP Checksum found in IP header |
