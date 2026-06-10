<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/171395/dhcp-activity-data-model -->

# DHCP Activity Data Model

This includes DHCP IP Address Assignment / Release / Renew activity

Examples from Windows DHCP using Agent:

- AO-WUA-DHCP-IP-ASSIGN
- AO-WUA-DHCP-IP-LEASE-RENEW
- AO-WUA-DHCP-DNS-LEASE-DENY

Examples from Linux DHCP:

- Linux_DHCPREQUEST
- Linux_DHCPOFFER
- Linux_DHCPRELEASE

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| hostName | string | Host Name | Host requesting IP |
| hostMACAddr | string | Host MAC | MAC of host requesting IP |
| hostIpAddr | IP | Host IP | Assigned IP |
| user | string | User | Logged on user on the workstation |
| dhcpLeaseTime | uint32 | DHCP Lease Time | DHCP Lease Time |
