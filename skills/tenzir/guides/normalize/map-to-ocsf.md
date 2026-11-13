---
title: "Map to OCSF"
canonical: https://tenzir.com/docs/guides/normalize/map-to-ocsf
source: https://tenzir.com/docs/guides/normalize/map-to-ocsf.md
section: "Docs"
---

# Map to OCSF

> This guide covers the decisions behind an OCSF mapping: choosing the event class, keeping the mapping minimal, handling unmapped fields, and finalizing the output with Tenzir’s native OCSF functions.

This guide covers the decisions behind an OCSF mapping: choosing the event class, keeping the mapping minimal, handling unmapped fields, and finalizing the output with Tenzir’s native OCSF functions.

Want the full walkthrough?

[Onboard a data source](../../tutorials/onboard-a-data-source.md) takes one log line from a pipeline to an installable package, with this mapping as its third step. This guide covers the mapping decisions in more depth.

## Use the OCSF skill

Install the `tenzir-ocsf` skill when you want an agent to help with OCSF schema decisions. See [Use agent skills](../ai-workbench/use-agent-skills.md#use-the-ocsf-skill) for installation and usage examples.

Ask the agent to choose the OCSF version, event class, and profiles before it maps attributes. OCSF mappings should produce the required classification and occurrence attributes first, then add primary, context, and profile-specific attributes.

## Write the OCSF mapping

Mappings live in packages as operators. The tutorial linked above walks through one from a structured source event to a tested operator, and our guide on [adding operators](../packages/add-operators.md) covers arguments and operator hierarchies. The rest of this guide covers the decisions that are specific to OCSF.

### Key principles

* **Keep unmapped residue**: Source fields without an OCSF target still need review or an intentional decision to preserve source-specific data.
* **Produce minimal OCSF**: Map required identifiers, required attributes, and source-specific semantics. Don’t hand-write derived sibling fields such as `activity_name`, `category_name`, or `severity`; [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) adds them where a consumer needs them.
* **Validate in tests**: Check the mapper’s output against its schema with [`ocsf_cast`](https://tenzir.com/docs/reference/functions/ocsf_cast.md) in the package tests. Pipelines that run the mapper don’t need to repeat it.

Think in graphs

OCSF mapping is a bipartite graph transformation: source fields form one vertex set, OCSF attributes form another, and your mapping defines the edges. Edges can be 1:1 (direct assignment), 1:n (field splitting), n:1 (aggregation), or n:m (complex transformation). Fields with no outgoing edges remain in the source scope and become `unmapped` when the mapper returns the OCSF event.

### Package layout

Put the target schema first in mapping namespaces, and let the vendor that owns a schema host the mappers into it. Source-to-OCSF packages use `paloalto::ngfw::ocsf::map`, while the mappers out of OCSF live with their target: `splunk::cim::ocsf::map` for Splunk CIM and `microsoft::asim::ocsf::map` for Microsoft Sentinel ASIM.

A product with several event types needs a dispatcher that routes each recognized event type to an operator under `ocsf/events/` and falls back to the OCSF Base Event. Our tutorial on [creating the mapper](../../tutorials/onboard-a-data-source.md#create-the-mapper) shows that hierarchy together with the normalizer that wraps it, and our guide on [testing packages](../packages/test-packages.md) covers the tests and baselines that go with it.

How much of that hierarchy a package needs depends on its source. The [`amazon` package](https://tenzir.com/docs/packages/amazon/operators/vpc_flow/ocsf/map.tql) owns the parsing and ships a normalizer, because VPC Flow Logs have no built-in reader. A source that Tenzir reads natively, such as Zeek through [`read_zeek_tsv`](https://tenzir.com/docs/reference/operators/read_zeek_tsv.md) or [`read_zeek_json`](https://tenzir.com/docs/reference/operators/read_zeek_json.md), needs neither: its package starts at the mapper and dispatches on the log type.

## Use native OCSF functions

Tenzir ships functions for completing, validating, and reducing OCSF events:

* [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) derives integer and string enum siblings in either direction and warns about inconsistent pairs.
* [`ocsf_cast`](https://tenzir.com/docs/reference/functions/ocsf_cast.md) casts an event to the OCSF type selected by its version, class, profiles, and extensions. It warns about fields outside that schema and removes them, and warns about missing required fields and violated constraints.
* [`ocsf_trim`](https://tenzir.com/docs/reference/functions/ocsf_trim.md) removes fields according to their OCSF requirement levels when you need to reduce event size.
* [`ocsf_compact`](https://tenzir.com/docs/reference/functions/ocsf_compact.md) removes enum strings that [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) can rebuild when you need to reduce event size without losing information.

A mapper returns minimal OCSF. Which of these functions run afterwards is a decision of each pipeline, not part of the mapping.

The [`ocsf_cast`](https://tenzir.com/docs/reference/functions/ocsf_cast.md) function is the schema validation gate. Call it in the package tests, as our guide on [testing packages](../packages/test-packages.md#pin-the-output-schema) shows: your mapping is complete when the tests no longer emit warnings. In a pipeline, cast only when a downstream system needs the exact schema types, and use options such as `null_fill=true`, `encode_variants=true`, or `timestamp_to_ms=true` only when it requires those output shapes or physical representations.

The [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) function expands an event for consumers that expect the full set of enum fields. It computes `category_uid` and `type_uid` from `class_uid` and `activity_id`, and fills enum siblings such as `activity_name`, `category_name`, and `severity` from their numeric identifiers. It also works in the other direction when a mapping starts with a string sibling. Call it where you deliver events to such consumers:

```tql
this = ocsf_derive(this)
```

To reduce event size for storage or transport, compact the events. The [`ocsf_compact`](https://tenzir.com/docs/reference/functions/ocsf_compact.md) function removes enum strings such as `activity_name` or `severity` that [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) can rebuild from their integer siblings. It keeps every string that carries information, such as the data source specific value of an `Other` enum. Run [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) when reading the events to restore the strings:

```tql
// Before writing
this = ocsf_compact(this)


// After reading
this = ocsf_derive(this)
```

To also remove fields that OCSF marks as optional or recommended, write `this = ocsf_trim(this)`. Unlike [`ocsf_compact`](https://tenzir.com/docs/reference/functions/ocsf_compact.md), it discards their values.

### Finalize events in a field

Pass the field to the same functions when a mapper writes an OCSF event into an envelope. The surrounding fields, such as `raw_data`, stay where they are:

```tql
vendor::ocsf::map input, ocsf
ocsf = ocsf_derive(ocsf)
```

### Migrate existing operator calls

The `ocsf_derive`, `ocsf_cast`, and `ocsf_trim` operators are deprecated and emit warnings. Replace each call with an assignment to `this` using the function of the same name. Pass existing options as named function arguments, for example `this = ocsf_cast(this, null_fill=true)`.

The functions return `null` with a warning when they cannot resolve the OCSF version or class, while the operators drop those events. The `ocsf_cast` function also validates required fields and constraints, and leaves `@name` unchanged. Set the name explicitly if downstream pipelines depend on it.

Assign the result to a new field to preserve an unresolved event for inspection or routing. For example, when the OCSF event lives in `ocsf`:

```tql
validated = ocsf_cast(ocsf)
if validated == null {
  publish "ocsf-quarantine"
} else {
  ocsf = move validated
  publish "ocsf"
}
```

### Preserve incomplete observations

Map an optional object only when the source identifies it: a process name alone does not identify a process, and a port alone does not identify an endpoint. Keep such values in `unmapped` under their original keys instead of inventing identifiers to satisfy validation.

A missing required field does not change a known event’s class. A file rename without host context stays File System Activity, and [`ocsf_cast`](https://tenzir.com/docs/reference/functions/ocsf_cast.md) warns about the missing `device` but keeps the event, so you can enrich it later.

## Look up identifiers and names

Six functions translate between OCSF identifiers and their names, so a mapping never hard-codes a number it can compute:

* [`ocsf_class_uid`](https://tenzir.com/docs/reference/functions/ocsf_class_uid.md) and [`ocsf_class_name`](https://tenzir.com/docs/reference/functions/ocsf_class_name.md) convert between a class name and its `class_uid`, as in `ocsf_class_uid("DNS Activity")` and `ocsf_class_name(4003)`.
* [`ocsf_category_uid`](https://tenzir.com/docs/reference/functions/ocsf_category_uid.md) and [`ocsf_category_name`](https://tenzir.com/docs/reference/functions/ocsf_category_name.md) do the same for categories, as in `ocsf_category_uid("Findings")`.
* [`ocsf_type_uid`](https://tenzir.com/docs/reference/functions/ocsf_type_uid.md) and [`ocsf_type_name`](https://tenzir.com/docs/reference/functions/ocsf_type_name.md) cover the combination of class and activity, as in `ocsf_type_uid("SSH Activity: Fail")` and `ocsf_type_name(400704)`.

Use them where a source carries the name rather than the number, which is common for data that arrives from another OCSF producer:

```tql
class_uid = ocsf_class_uid(vendor_class)
category_uid = ocsf_category_uid(vendor_category)
```

They also make a mapping readable in the other direction. Writing `where class_uid == ocsf_class_uid("Network Activity")` in a detection says what the rule matches, while `where class_uid == 4001` makes the reader look it up.

## See also

* [Model detections in OCSF](../detect/model-detections-in-ocsf.md)
* [Clean up values](../parse/clean-up-values.md)
* [Use agent skills](../ai-workbench/use-agent-skills.md#use-the-ocsf-skill)
* [Map to ASIM](map-to-asim.md)
* [Map to CIM](map-to-cim.md)
* [Map to ECS](map-to-ecs.md)
* [Map to UDM](map-to-udm.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)
