<!-- Source: https://docs.fortinet.com/document/fortisiem/7.5.0/fortisiem-event-data-model/965962/network-security-finding-data-model -->

# Network Security Finding Data Model

This data model describes Host IPS / Endpoint Detection Events such as

- Network IPS Events
- Web Gateway Detection Events
- Email Security Detection Events
- Honeypot Events

Example events:

- FortiGate-ips-signature-109314060 (SMTP.X-LINK2STATE.Buffer.Overflow)
- FortiWeb-20000008 (FortiWeb Exploit Signature Detected)
- Cisco_IPS-1044/8 (Metasploit Shellcode Encoder)
- PAN-IDP-30012 (Internet Explorer Vector Markup Language Buffer Overflow)

In addition to the base event attributes, the following attributes are relevant and may be populated in this data model.

| Event Attribute | Type | Display Name | Description |
| --- | --- | --- | --- |
| srcIpAddr | IP | Source IP | Source IP of a device as identified in the event. |
| srcName | string | Source Host Name | Source device's hostname as identified in the log, can also be enriched using reverse lookup of the source IP address. |
| destIpAddr | IP | Destination IP | Destination IP of a device as identified in the event. |
| destName | string | Destination Host Name | Destination device's hostname as identified in the log, can also be enriched using reverse lookup of the destination IP address. |
| ipProto | uint16 | IP Protocol | IP Protocol, e.g. TCP, UDP, ICMP etc as defined in IP RFPs |
| srcIpPort | uint16 | Source TCP/UDP Port | This is the source TCP or UDP port as identified in the event |
| destIpPort | uint16 | Destination TCP/UDP Port | This is the destination TCP or UDP port as identified in the event |
| appName | string | Application Name | Application name if application detection is enabled |
| user | string | User | User associated with network session |
| fwRule | string | Firewall Rule | Firewall/IPS Policy that triggered the event |
| fwAction | string | Firewall Action | Action taken by the network appliance |
| webFilterAction | string | Web Filter Action | Action taken by the Web Filter module |
| ipsSignatureId | uint64 | IPS Signature Id | IPS Signature id |
| attackName | string | Attack Name | Attack Name |
| attackTactic | string | Attack Tactic | MITRE ATTACK Tactic |
| attackTechniqueId | string | Attack Technique Id | MITRE ATTACK Technique Id |
| attackTechnique | string | Attack Technique | MITRE ATTACK Technique Description |
| fileName | string | File Name | File name involved in the event |
| vulnCVEId | string | Vulnerability CVE Id | CVE ID |
| webCategory | string | Website category | Website category typically reported by Web Filters |
| infoURL | string | Informational URL | Link to more information about the event |
| downloadURL | string | Download URL | URL involved in the event |
| hashCode | string | Hash Code | Hash of process binary |
| hashAlgo | string | Hash Algorithm | Algorithm for hashCode |
| virusName | string | Malware Name | Malware Name |
| virusType | string | Malware Type | Malware Type |
| virusFamily | string | Malware Family | Malware Family |
| verdict | string | Verdict | Verdict about the malware |
