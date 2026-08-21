---
title: "Normalize data"
canonical: https://tenzir.com/docs/guides/normalization
source: https://tenzir.com/docs/guides/normalization.md
section: "Docs"
---

# Normalize data

> These guides take you from source-specific events to a schema your downstream tools understand. Start with cleanup, then pick the guide for your target schema. We map sources to OCSF first and translate from there, and our explanation of normalization makes the case for why.

These guides take you from source-specific events to a schema your downstream tools understand. Start with cleanup, then pick the guide for your target schema. We map sources to OCSF first and translate from there, and our explanation of [normalization](../explanations/normalization.md) makes the case for why.

## Fix the data first

[Clean up values](normalization/clean-up-values.md) replaces null placeholders such as `"None"`, `"N/A"`, and `"-"`, converts strings to timestamps, IP addresses, and numbers, and supplies defaults for missing fields. Mapping bad values into a good schema only moves the problem.

## Choose a target schema

Pick the schema your analytics platform reads. The guides are listed alphabetically, and each one covers the decisions its schema adds.

[Map to ASIM](normalization/map-to-asim.md) maps to Microsoft Sentinel ASIM: choose the event or entity schema, populate schema and product metadata, map the role-prefixed field families, and keep the residue in `AdditionalFields`.

[Map to CIM](normalization/map-to-cim.md) maps to Splunk CIM: choose the data model and dataset, apply tags and constraints so acceleration works, and send the result to HEC with the right metadata.

[Map to ECS](normalization/map-to-ecs.md) maps to Elastic Common Schema: set `@timestamp` and `ecs.version`, choose the `event.*` categorization, map the source, destination, network, and observer fieldsets, and keep source-specific details in a custom namespace.

[Map to OCSF](normalization/map-to-ocsf.md) maps to OCSF, our default target: identify the event class, map by attribute group, handle unmapped fields, and validate with `ocsf_cast`.

[Map to UDM](normalization/map-to-udm.md) maps to Google SecOps UDM: choose the event type, populate metadata and participant nouns, convert values to UDM enums, and keep the residue in `additional`.

## Ship the mapping

A mapping that lives in a package gets a test, a version, and one place to fix a field. [Onboard a data source](../tutorials/onboard-a-data-source.md) builds one from a single log line and ships it as an installable package.

## See also

* [Parse string fields](parsing/parse-string-fields.md)
* [Create a package](packages/create-a-package.md)
* [Write tests](testing/write-tests.md)
* [Normalization](../explanations/normalization.md)
