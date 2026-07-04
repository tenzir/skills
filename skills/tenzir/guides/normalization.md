---
title: "Normalize data"
canonical: https://tenzir.com/docs/guides/normalization
source: https://tenzir.com/docs/guides/normalization.md
section: "Docs"
---

# Normalize data

> This guide provides an overview of data normalization in TQL. Normalization transforms raw, inconsistent data into a clean, standardized format that’s ready for analysis, storage, and sharing.

This guide provides an overview of data normalization in TQL. Normalization transforms raw, inconsistent data into a clean, standardized format that’s ready for analysis, storage, and sharing.

## What is normalization?

Normalization involves several key transformations:

1. **Clean up values** - Replace nulls, normalize sentinels, fix types
2. **Map to schemas** - Translate fields to a standard schema like ASIM, CIM, ECS, OCSF, or UDM
3. **Package mappings** - Create reusable, tested mapping operators

Each step builds on the previous. Start with clean data, then map to your target schema, and finally package your mappings for production use.

## Why normalize?

Raw data from different sources varies in:

* **Field names**: `src_ip` vs `source_address` vs `client.ip`
* **Value formats**: `"true"` vs `true` vs `1` vs `"yes"`
* **Missing values**: `null` vs `""` vs `"-"` vs `"N/A"`
* **Timestamps**: Unix epochs vs ISO strings vs custom formats

Normalization solves these inconsistencies, enabling:

* Unified queries across data sources
* Reliable enrichment and correlation
* Consistent analytics and dashboards
* Interoperability with external tools

## The normalization pipeline

A typical normalization pipeline follows this structure:

```tql
// 1. Collect raw data
from_kafka "raw-events"


// 2. Parse into a structured event
event = message.parse_json()


// 3. Clean up values
replace event, what="N/A", with=null
replace event, what="-", with=null


// 4. Map to target schema
my_source::ocsf::map event=event


// 5. Preserve the raw payload after mapping
event.raw_data = move message
event.raw_data_size = event.raw_data.length_bytes()
this = event


// 6. Output normalized events
publish "normalized-events"
```

## Normalization guides

Start with cleanup, then choose the schema guide for your target platform. Schema guides are listed alphabetically by acronym.

### Clean up values

[Clean up values](normalization/clean-up-values.md) - Start by fixing data quality issues:

* Replace null placeholders (`"None"`, `"N/A"`, `"-"`)
* Normalize sentinel values
* Fix types (strings to timestamps, IPs, numbers)
* Provide default values for missing fields

### Map to ASIM

[Map to ASIM](normalization/map-to-asim.md) - Learn how to map events to Microsoft Sentinel ASIM records:

* Choose the correct ASIM event or entity schema
* Populate schema, product, and event metadata
* Map role-prefixed source, destination, actor, target, and device fields
* Preserve unmapped fields in `AdditionalFields`

### Map to CIM

[Map to CIM](normalization/map-to-cim.md) - Learn how to map events to Splunk CIM fields:

* Choose the correct CIM data model and dataset
* Apply dataset tags and constraints
* Populate normalized fields for data model acceleration
* Send mapped events to Splunk HEC with metadata

### Map to ECS

[Map to ECS](normalization/map-to-ecs.md) - Learn how to map events to Elastic Common Schema fields:

* Populate `@timestamp` and `ecs.version`
* Choose `event.kind`, `event.category`, and `event.type`
* Map source, destination, network, and observer fieldsets
* Preserve source-specific details in a custom namespace

### Map to OCSF

[Map to OCSF](normalization/map-to-ocsf.md) - Learn the comprehensive approach to OCSF mapping:

* Identify the correct event class
* Map fields by attribute group
* Handle unmapped fields
* Validate with `ocsf::cast`

### Map to UDM

[Map to UDM](normalization/map-to-udm.md) - Learn how to map events to Google SecOps UDM records:

* Choose the correct UDM event type
* Populate metadata and participant nouns
* Convert source values to UDM enums
* Preserve unmapped fields in `additional`

## When to normalize

Normalize data at the ingestion point in your pipeline:

```plaintext
Collection → Parsing → Normalization → Storage/Forwarding
              ↑
        You are here
```

Normalizing early ensures all downstream consumers work with consistent data. Avoid normalizing the same data multiple times by storing normalized events.

## See also

* [Parse string fields](parsing/parse-string-fields.md)
* [Create a package](packages/create-a-package.md)
* [Write tests](testing/write-tests.md)
* [Map data to OCSF](../tutorials/map-data-to-ocsf.md)
