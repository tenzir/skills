---
name: tenzir-edm
description: Answer questions about the FortiSIEM Event Data Model (EDM), Fortinet's normalized event attribute model. Use when the user asks about the FortiSIEM EDM, FortiSIEM event attributes, attribute types or display names, FortiSIEM data models or event categories, FortiSIEM parser attribute mapping, or mapping events into FortiSIEM.
---

# FortiSIEM Event Data Model (EDM)

The FortiSIEM Event Data Model describes how FortiSIEM normalizes parsed log data into named event attributes, grouped into data models per event category.
EDM is this skill's shorthand for the model; Fortinet itself uses no acronym.
Use this skill to choose the right data model, inspect event attributes, explain attribute types and display names, and map events into FortiSIEM event attributes for built-in or custom parsers.

The generated YAML files are the authoritative reference for this skill.
If an attribute, type, display name, or data model is not present in the YAML data, say that it is not documented here.
Use [source.md](source.md) only as the final provenance anchor for the documented FortiSIEM version and raw page copies.

## How the FortiSIEM event data model fits together

FortiSIEM normalizes events into flat records of typed event attributes, documented as 21 data models, one per event category.
The base event data model lists attributes present in every FortiSIEM event, split into attributes set automatically by the parsing framework and attributes a parser must set.
Every other data model adds the attributes relevant to one event category, on top of the base attributes.
Each data model's `summary` names example event types that follow it; the full event type list lives in the FortiSIEM product under Resources > Event Types.

An event attribute is a typed name contract: the same attribute keeps its name, type, and meaning across all data models that use it.
Attribute types use a small vocabulary: `DATE`, `double`, `IP`, `string`, `uchar`, `uint16`, `uint32`, `uint64`.
Type values in the YAML data are copied verbatim from the Fortinet pages, which contain occasional case variants and errors; treat case-insensitive matches as the same type.
A few attributes have empty type, display name, and description cells upstream; when a type is missing, use the documented `src` or `dest` counterpart attribute, such as `srcVLAN` for `destVLAN`, as the guide.
Attribute names are camelCase and use role prefixes: `src` for the source of the activity, `dest` for its destination, `host` for the host the event refers to, and `ph` for attributes set by the FortiSIEM (Phoenix) framework itself, such as `phRecvTime` and `phEventCategory`.
Display names are the human-readable labels shown in the FortiSIEM GUI; use attribute names, not display names, in parsers and queries.
Some data models group attributes into named sections, recorded per attribute in the `section` key.

This document covers the curated cross-device data models only.
The full FortiSIEM attribute dictionary (thousands of attributes) is only browsable in the product under Admin > Device Support > Event Attributes; treat attributes outside the YAML data as undocumented here.

## Data files

- Use [catalog.yaml](catalog.yaml) to choose a data model and find the model data file.
- Use `models/<model>.yaml` to map an event into one data model.
- Use [attributes.yaml](attributes.yaml) directly as the attribute-name to attribute-file manifest.
- Use `attributes/<attribute>.yaml` for attribute meaning across data models.
- Use `docs/<page>.md` for the raw Fortinet page content backing a data model.

## Mapping rules

- Start from the event category, choose the data model in [catalog.yaml](catalog.yaml), then load the model file.
- Populate the base event attributes first, then the attributes of the selected data model that the source provides.
- Keep attribute names exactly as documented; they are case-sensitive camelCase identifiers.
- Match the documented attribute type when producing values; convert source values rather than changing the attribute.
- Reuse an existing attribute with the same meaning before inventing a source-specific name; check `attributes/<attribute>.yaml` for cross-model meaning.
- When no documented attribute fits, keep the original source field name and say that the attribute is not documented here.

## Question routing

| Question pattern | Start here |
| --- | --- |
| Which data model fits this event? | [catalog.yaml](catalog.yaml), then the selected model file |
| What attributes does data model X contain? | `models/<model>.yaml` |
| What does attribute Y mean, and where is it used? | [attributes.yaml](attributes.yaml), then `attributes/<attribute>.yaml` |
| Which attributes does every event carry? | [models/base_event.yaml](models/base_event.yaml) |
| What did the original Fortinet page say? | `docs/<page>.md` |
| Which FortiSIEM version backs this data? | [source.md](source.md) |

For provenance, the documented FortiSIEM version, and raw page copies, use [source.md](source.md) as the last anchor.
