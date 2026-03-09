# Normalize data


This guide provides an overview of data normalization in TQL. Normalization transforms raw, inconsistent data into a clean, standardized format that’s ready for analysis, storage, and sharing.

## What is normalization?

Normalization involves several key transformations:

1. **Clean up values** - Replace nulls, normalize sentinels, fix types
2. **Map to schemas** - Translate fields to a standard schema like OCSF
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


// 2. Parse into structured events
this = message.parse_json()


// 3. Clean up values
replace what="N/A", with=null
replace what="-", with=null


// 4. Map to target schema
my_source::ocsf::map


// 5. Output normalized events
publish "normalized-events"
```

## Normalization guides

Work through these guides in order for a complete normalization workflow:

### [Clean up values](normalization/clean-up-values.md)

Start by fixing data quality issues:

* Replace null placeholders (`"None"`, `"N/A"`, `"-"`)
* Normalize sentinel values
* Fix types (strings to timestamps, IPs, numbers)
* Provide default values for missing fields

### [Map to OCSF](normalization/map-to-ocsf.md)

Learn the comprehensive approach to OCSF mapping:

* Identify the correct event class
* Map fields by attribute group
* Handle unmapped fields
* Validate with `ocsf::cast`

### [Map to other schemas](normalization/map-to-other-schemas.md)

Brief guidance on alternative schemas:

* Elastic Common Schema (ECS)
* Google UDM
* Microsoft ASIM

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

## Contents

- [Clean-up-values](normalization/clean-up-values.md)
- [Map-to-ocsf](normalization/map-to-ocsf.md)
- [Map-to-other-schemas](normalization/map-to-other-schemas.md)