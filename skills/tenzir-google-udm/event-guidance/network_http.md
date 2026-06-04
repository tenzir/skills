# NETWORK_HTTP Event Guidance

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`

## Applies To

- `NETWORK_HTTP`
- Usage-guide section: `NETWORK_HTTP`
- Proto enum: [Metadata.EventType](../enums/metadata_event_type.md)

## Required Fields

- metadata: Include the required fields.
- target: Represents the web server. Include device information and an optional port number. If a target port number is available, specify only one IP address in addition to the port number associated with that network connection (although multiple other machine identifiers could be provided for the target). For `target.url`, populate with the URL accessed.

## Optional Fields

- principal: Represents the client initiating the web request. Include at least one machine identifier (for example, hostname, IP, MAC, proprietary asset identifier) or a user identifier (for example, username). If a specific network connection is described and a client port number is available, specify only one IP address along with the port number associated with that network connection (although other machine identifiers could be provided to better describe the participant device). If no source port is available, you could specify any and all IP and MAC addresses, asset identifiers, and hostname values describing the principal device.
- network: Include details of the network connection. You must populate the following fields: network.ip_protocol network.application_protocol
- about: Represents other entities found in the HTTP transaction (for example, an uploaded or downloaded file).
- intermediary: Represents a proxy server (if different from the principal or target).
- metadata: Populate the other metadata fields.
- network: Populate other network fields.
- network.email: If the HTTP network connection originated from a URL that appeared in an email message, populate network.email with the details.
- network.http: If the HTTP network connection method is present, populate `network.http.method`.
- observer: Represents a passive sniffer (if present).
- security_result: Add one or more items to the security_result field to represent the malicious activity detected.

## Notes

- The NETWORK_HTTP event type represents an HTTP network connection from a principal to a target web server.
- The following example illustrates how a Sophos antivirus event of type NETWORK_HTTP would be converted to the Google SecOps UDM format.
- The following is the original Sophos antivirus event:
- Here is how you would format the same information in Proto3 using the Google SecOps UDM syntax:
- As shown in this example, the event has been divided into the following UDM categories:
- metadata: Background information about the event.
- principal: Security device that detected the event.
- target: Device that received the malicious software.
- network: Network information about the malicious host.
- security_result: Security details about the malicious software.
- additional: Vendor information outside the scope of the UDM.

## Examples

### UDM example for NETWORK_HTTP (1)

```text
date=2013-08-07 time=13:27:41 timezone="GMT" device_name="CC500ia" device_id= C070123456-ABCDE log_id=030906208001 log_type="Anti-Virus" log_component="HTTP" log_subtype="Virus" status="" priority=Critical fw_rule_id=0 user_name="john.smith" iap=7 av_policy_name="" virus="TR/ElderadoB.A.78" url="altostrat.fr/img/logo.gif" domainname="altostrat.fr" src_ip=10.10.2.10 src_port=60671 src_country_code= dst_ip=203.0.113.31 dst_port=80 dst_country_code=FRA
```

### UDM example for NETWORK_HTTP (2)

```text
metadata {
  event_timestamp: "2013-08-07T13:27:41+00:00"
  event_type: NETWORK_HTTP
  product_name: "Sophos Antivirus"
  product_log_id: "030906208001"
}

principal {
  hostname: "CC500ia"
  asset_id: "Sophos.AV:C070123456-ABCDE"
  ip: "10.10.2.10"
  port: 60671
  user {  userid: "john.smith" }
}

target {
  hostname: "altostrat.fr"
  ip: "203.0.113.31"
  port: 80
  url: "altostrat.fr/img/logo.gif"
}

network {
  ip_protocol: TCP
 }

security_result {
  about {
    url: "altostrat.fr/img/logo.gif"
    category: SOFTWARE_MALICIOUS
    category_details: "Virus"
    threat_name: "TR/ElderadoB.A.78"
    severity: HIGH                   # Google Security Operations-normalized severity
    severity_details: "Critical"    # Vendor-specific severity string
  }
}

additional { "dst_country_code" : "FRA", "iap" : "7" "fw_rule_id" : "0" }
```
