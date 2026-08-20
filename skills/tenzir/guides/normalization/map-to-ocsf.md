---
title: "Map to OCSF"
canonical: https://tenzir.com/docs/guides/normalization/map-to-ocsf
source: https://tenzir.com/docs/guides/normalization/map-to-ocsf.md
section: "Docs"
---

# Map to OCSF

> This guide shows you how to write OCSF mapping operators in TQL. You’ll learn to organize mappings by attribute groups, handle unmapped fields, and finalize your output with Tenzir’s native OCSF operators. The guide assumes you’ve already identified your target OCSF event class and profiles.

This guide shows you how to write OCSF mapping operators in TQL. You’ll learn to organize mappings by attribute groups, handle unmapped fields, and finalize your output with Tenzir’s native OCSF operators. The guide assumes you’ve already identified your target OCSF event class and profiles.

OCSF Tutorial

For an end-to-end walkthrough with Zeek logs, see the [Map data to OCSF tutorial](../../tutorials/map-data-to-ocsf.md).

## Use the OCSF skill

Install the `tenzir-ocsf` skill when you want an agent to help with OCSF schema decisions. See [Use agent skills](../ai-workbench/use-agent-skills.md#use-the-ocsf-skill) for installation and usage examples.

Ask the agent to choose the OCSF version, event class, and profiles before it maps attributes. OCSF mappings should produce the required classification and occurrence attributes first, then add primary, context, and profile-specific attributes.

## Write the OCSF mapping

This section uses Palo Alto NGFW traffic logs as a running example. The namespace follows the `vendor::product::` convention, resulting in `paloalto::ngfw::ocsf::map`.

### Operator template

Use this annotated template as a starting point for creating a [user-defined operator](../packages/add-operators.md) as part of a TQL package.

We recommend organizing fields by OCSF attribute groups: classification, occurrence, context, primary.

```tql
---
args:
  named:
    - name: event
      description: The field that holds the event to map.
      type: field
      default: this
---


// --- Preamble ---------------------------------


// Keep all mapping work inside the explicit event scope.
$event = {...$event, panos: $event, ocsf: {}}


// --- OCSF: classification attributes ----------


@name = "ocsf.network_activity"
$event.ocsf.category_uid = 4
$event.ocsf.class_uid = 4001
$event.ocsf.activity_id = 6
$event.ocsf.severity_id = 1
$event.ocsf.type_uid = $event.ocsf.class_uid * 100 + $event.ocsf.activity_id


// --- OCSF: occurrence attributes --------------


$event.ocsf.time = move $event.panos.time_generated
$event.ocsf.start_time = move $event.panos.start
if $event.panos.elapsed != null {
  $event.ocsf.end_time = $event.ocsf.start_time + $event.panos.elapsed
  $event.ocsf.duration = count_milliseconds(move $event.panos.elapsed).round()
}


// --- OCSF: context attributes -----------------


// Metadata about the event source.
$event.ocsf.metadata = {
  log_name: "traffic",
  product: {
    cpe_name: "cpe:/a:paloaltonetworks:pan-os",
    name: "NGFW",
    vendor_name: "Palo Alto Networks",
  },
  original_event_uid: move $event.panos.sessionid,
  version: "1.8.0",
}
$event.ocsf.app_name = move $event.panos.app


// --- OCSF: primary attributes -----------------


// Primary attributes reflect the core semantic meaning of the event.


$event.ocsf.src_endpoint = {
  ip: move $event.panos.src,
  port: move $event.panos.sport,
}


$event.ocsf.dst_endpoint = {
  ip: move $event.panos.dst,
  port: move $event.panos.dport,
}


let $proto_nums = {tcp: 6, udp: 17, icmp: 1}
$event.ocsf.connection_info = {
  protocol_name: (move $event.panos.proto).to_lower(),
}
$event.ocsf.connection_info.protocol_num = $proto_nums[$event.ocsf.connection_info.protocol_name]? else -1


// --- OCSF: profile-specific attributes --------


// Add fields for declared profiles (host, network_proxy, etc.)
// ocsf.device = {...}
// ocsf.proxy = {...}


// --- Epilogue ---------------------------------


// Return the mapped OCSF event and preserve mapping residue.
$event = {...$event.ocsf, unmapped: $event.panos}
```

### Key principles

* **Use the event scope**: Mapping UDOs accept a named `event` field argument that defaults to `this`. Start with a spread such as `$event = {...$event, panos: $event, ocsf: {}}`, then mutate only fields under `$event`.
* **Use a source namespace**: Keep the input under a short descriptor such as `panos`, `zeek`, `okta`, or the generic `event`. This prevents name clashes with OCSF fields and keeps the remaining source fields ready for `unmapped`.
* **Use `move`**: Transfer fields with `move` to simultaneously assign and remove from source, for example `$event.ocsf.time = move $event.panos.time_generated`.
* **Only use `drop` for multi-use fields**: When a field appears in multiple mappings, drop it after the last use. Prefer `move` and single assignments.
* **Keep unmapped residue**: Fields left under the source namespace still need review or an intentional decision to preserve source-specific data.
* **Produce minimal OCSF**: Map required identifiers, required attributes, and source-specific semantics. Don’t hand-write derived sibling fields such as `activity_name`, `category_name`, or `severity`; let [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) expand the minimal event before validation.
* **Finalize the result**: After the mapper returns the OCSF event, set `type_uid` and use Tenzir’s native OCSF operators to derive enum siblings and validate the event against its schema.

Why use `$event`?

TQL has user-defined operators, but not user-defined functions yet. The explicit `event` field argument gives each mapping operator one mutable record scope that callers can pass explicitly when the parsed source event lives in a field. Keep all mapper state below `$event` until TQL has function-like abstractions for record-to-record mappings.

Think in graphs

OCSF mapping is a bipartite graph transformation: source fields form one vertex set, OCSF attributes form another, and your mapping defines the edges. Edges can be 1:1 (direct assignment), 1:n (field splitting), n:1 (aggregation), or n:m (complex transformation). Fields with no outgoing edges remain in the source namespace and become `unmapped` when the mapper returns the OCSF event.

### Package structure

Organize OCSF mappings as a package with a dispatcher and per-event-type operators:

Put the target schema first in mapping namespaces. Source-to-OCSF packages use `paloalto::ngfw::ocsf::map`. Cross-schema mappings keep the same rule, for example `paloalto::ngfw::asim::ocsf::map` for OCSF-to-ASIM mapping.

* paloalto/

  * operators/

    * ngfw/

      * ocsf/

        * map.tql Main dispatcher

        * base.tql Fallback to OCSF base event

        * events/

          * network.tql Traffic logs → Network Activity
          * dns.tql DNS logs → DNS Activity
          * threat.tql Threat logs → Security Finding

  * tests/

    * inputs/

      * traffic.json Input shared across multiple tests

    * ngfw/

      * ocsf/

        * map.tql

        * map.txt

        * base.tql

        * base.txt

        * events/

          * network.input Log sample(s)
          * network.tql Mapping for network event type
          * network.txt Mapped OCSF event(s)
          * dns.input
          * dns.tql
          * dns.txt

  * package.yaml

### Dispatcher operator

Your package should include one main mapping operator. This operator performs source-specific cleanup and shared OCSF setup, dispatches events based on the event type, and returns the mapped OCSF event:

```tql
---
args:
  named:
    - name: event
      description: The field that holds the event to map.
      type: field
      default: this
---


$event = {...$event, panos: $event, ocsf: {}}


$event.ocsf.metadata = {
  product: {
    cpe_name: "cpe:/a:paloaltonetworks:pan-os",
    name: "NGFW",
    vendor_name: "Palo Alto Networks",
  },
  version: "1.8.0",
}
$event.ocsf.severity_id = 1


match $event.panos.type {
  "TRAFFIC" => {
    paloalto::ngfw::ocsf::events::network event=$event
  }
  "DNS" => {
    paloalto::ngfw::ocsf::events::dns event=$event
  }
  "THREAT" => {
    paloalto::ngfw::ocsf::events::threat event=$event
  }
  _ => {
    paloalto::ngfw::ocsf::base event=$event
  }
}


$event = {...$event.ocsf, unmapped: $event.panos}
```

If the parser package does not set a type field, dispatch on a different field in the log that differentiates the event types.

### Test structure

Create one test file per event type:

```tql
from_file env("TENZIR_INPUT") {
  read_json
}
paloalto::ngfw::ocsf::map
ocsf_derive
ocsf_cast
```

This requires that your test file has a sibling `.input` file that the [test framework](../testing/write-tests.md) exposes through `TENZIR_INPUT`. Use the reader that matches your fixture format.

When a caller parses into a nested field or wants to add raw data after mapping, pass the mapping scope explicitly and add the additional attributes after the mapper returns:

```tql
from_file env("TENZIR_INPUT") {
  read_lines
}
panos = line.parse_json()
paloalto::ngfw::ocsf::map event=panos
panos.raw_data = move line
panos.raw_data_size = panos.raw_data.length_bytes()
this = panos
ocsf_derive
ocsf_cast
```

## Use native OCSF operators

Tenzir ships operators for completing, validating, and reducing OCSF events:

| Operator                                                                    | Purpose                                                                                                                                               |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) | Derives integer and string enum siblings in either direction and warns about inconsistent pairs.                                                      |
| [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md)     | Casts an event to the OCSF type selected by its version, class, profiles, and extensions. It warns about fields outside that schema and removes them. |
| [`ocsf_trim`](https://tenzir.com/docs/reference/operators/ocsf_trim.md)     | Removes fields according to their OCSF requirement levels when you need to reduce event size.                                                         |

Use derivation and casting at the boundary after your mapping operator returns:

```tql
paloalto::ngfw::ocsf::map
type_uid = class_uid * 100 + activity_id
ocsf_derive
ocsf_cast
```

Set `type_uid` explicitly because [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) does not currently compute it. The operator fills enum siblings such as `activity_name`, `category_name`, and `severity` from their numeric identifiers. It also works in the other direction when a mapping starts with a string sibling.

The [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md) operator is the primary schema validation gate. Your mapping is complete when it no longer emits warnings. Use options such as `null_fill=true`, `encode_variants=true`, or `timestamp_to_ms=true` only when a downstream system requires those output shapes or physical representations.

After validation, optionally run [`ocsf_trim`](https://tenzir.com/docs/reference/operators/ocsf_trim.md) to minimize events for storage or transport. Its options let you keep or drop fields that OCSF marks as optional or recommended.

Use `ocsf_cast` instead of `ocsf::apply`

The [`ocsf::apply`](https://tenzir.com/docs/reference/operators/ocsf/apply.md) operator is deprecated. Use [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md) for new pipelines.

## See also

* [Model detections in OCSF](../detection/model-detections-in-ocsf.md)
* [Clean up values](clean-up-values.md)
* [Use agent skills](../ai-workbench/use-agent-skills.md#use-the-ocsf-skill)
* [Map to ASIM](map-to-asim.md)
* [Map to CIM](map-to-cim.md)
* [Map to ECS](map-to-ecs.md)
* [Map to UDM](map-to-udm.md)
* [Map data to OCSF](../../tutorials/map-data-to-ocsf.md)
