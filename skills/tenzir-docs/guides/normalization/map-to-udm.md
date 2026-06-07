# Map to UDM


This guide shows you how to map events to Google SecOps Unified Data Model (UDM) records in TQL. You’ll learn how to choose a UDM event type, populate metadata, model participants as UDM nouns, convert enum values, and preserve unmapped source fields.

Structured UDM ingestion is coming soon

Tenzir’s [`to_google_secops`](/reference/operators/to_google_secops.md) operator currently sends unstructured logs to Google SecOps. Use this guide to design and test UDM mapping operators, but don’t send structured UDM records directly with [`to_google_secops`](/reference/operators/to_google_secops.md) until structured UDM ingestion support is available.

The TQL examples in this guide build API-facing UDM records, so they use lowerCamelCase ingestion object field names such as `metadata.eventType` and `network.ipProtocol`.

## Use the UDM skill

Install the `tenzir-google-udm` skill when you want an agent to help with UDM schema decisions. See [Use agent skills](../ai-workbench/use-agent-skills.md#use-the-google-udm-skill) for installation and usage examples.

Ask the agent to use ingestion object field names when it maps logs into UDM event or entity objects for Google SecOps UDM API ingestion. When generated UDM field headings show two forms, choose the right-side lowerCamelCase ingestion object form. For example, use `metadata.eventType` and `network.ipProtocol` in the TQL output. If a heading has one name, use that spelling.

## Choose the UDM event type

Start by choosing `metadata.eventType`. This value describes the activity that the event records, not the product that emitted the log. For example, a firewall connection log maps to `NETWORK_CONNECTION`, while DNS payloads map to `NETWORK_DNS`.

For a `NETWORK_CONNECTION` event, UDM expects these core sections:

* `metadata`: The event timestamp and product context.
* `principal`: The machine that initiated the network connection.
* `target`: The destination machine if it differs from the principal.
* `network`: The protocol, ports, byte counts, and other connection details.

## Write a small mapping

The following example maps a parsed firewall connection event to UDM. It keeps the source data under `fw`, moves one-use fields into UDM, converts source strings to UDM enum values, and preserves unmapped residue in `additional`.

```tql
from {
  ts: 2024-01-15T10:30:45Z,
  action: "allowed",
  src_ip: "10.0.0.5",
  src_port: 51544,
  dst_ip: "203.0.113.10",
  dst_port: 443,
  proto: "tcp",
  bytes_out: 1280,
  bytes_in: 8192,
}


this = {fw: this}


let $ip_protocols = {
  tcp: "TCP",
  udp: "UDP",
  icmp: "ICMP",
}


let $actions = {
  allow: "ALLOW",
  allowed: "ALLOW",
  deny: "BLOCK",
  denied: "BLOCK",
  block: "BLOCK",
  blocked: "BLOCK",
}


udm.metadata = {
  eventTimestamp: move fw.ts,
  eventType: "NETWORK_CONNECTION",
  vendorName: "Example Networks",
  productName: "Example Firewall",
  productEventType: fw.action,
}


udm.principal = {
  ip: [move fw.src_ip],
  port: move fw.src_port,
}


udm.target = {
  ip: [move fw.dst_ip],
  port: move fw.dst_port,
}


udm.network = {
  ipProtocol: $ip_protocols[fw.proto.to_lower()]? else "UNKNOWN_IP_PROTOCOL",
  sentBytes: move fw.bytes_out,
  receivedBytes: move fw.bytes_in,
}


udm.securityResult = [{
  action: [$actions[fw.action.to_lower()]? else "UNKNOWN_ACTION"],
  actionDetails: fw.action,
}]


drop fw.action
drop fw.proto


this = {...udm, additional: fw}
```

```tql
{
  metadata: {
    eventTimestamp: 2024-01-15T10:30:45Z,
    eventType: "NETWORK_CONNECTION",
    vendorName: "Example Networks",
    productName: "Example Firewall",
    productEventType: "allowed",
  },
  principal: {
    ip: [
      "10.0.0.5",
    ],
    port: 51544,
  },
  target: {
    ip: [
      "203.0.113.10",
    ],
    port: 443,
  },
  network: {
    ipProtocol: "TCP",
    sentBytes: 1280,
    receivedBytes: 8192,
  },
  securityResult: [
    {
      action: [
        "ALLOW",
      ],
      actionDetails: "allowed",
    },
  ],
  additional: {},
}
```

## Apply the mapping pattern

Use the same structure for larger mappings:

* **Keep a source namespace**: Move the parsed event under a short namespace such as `fw`, `dns`, `edr`, or `event` before you create UDM fields.
* **Set `metadata.eventType` early**: Let the UDM event type drive which participant nouns and protocol fields you populate.
* **Model participants as nouns**: Use `principal` for the initiating entity, `target` for the destination, `observer` for the sensor, and `intermediary` for proxies or middleboxes.
* **Convert enum values explicitly**: Map source strings to UDM enum names such as `TCP`, `UDP`, `ALLOW`, or `BLOCK`.
* **Preserve unmapped fields**: Keep source fields that don’t have a deliberate UDM target under `additional` so reviewers can audit the mapping.

## See Also

* [`to_google_secops`](/reference/operators/to_google_secops.md)
* [Clean up values](clean-up-values.md)
* [Map to OCSF](map-to-ocsf.md)
* [Map to other schemas](map-to-other-schemas.md)
* [Create a package](../packages/create-a-package.md)
* [Write tests](../testing/write-tests.md)