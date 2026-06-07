---
name: tenzir-cim
description: >-
  Answer questions and produce mappings for the Splunk Common Information Model
  (CIM), including CIM Add-on aliases such as SA-CIM, CommonInformationModel,
  and SA-CommonInformationModel. Use when the user mentions CIM data
  models/datamodels/DMs, datasets/data model objects, fields, field aliases,
  calculated/eval fields, tags, constraints, lookups/lookup tables, macros,
  normalization, mapping logs or events to CIM, CIM compliance,
  pytest-splunk-addon, technical add-ons/TAs, Splunk Enterprise Security/ES,
  data model acceleration, pivots, tstats, or datamodel searches.
---

# Splunk Common Information Model

Version: 8.5.0

CIM is organized around *data models*. Each data model contains *datasets*,
historically called data model objects. Datasets inherit fields and constraints
from parent datasets. Event datasets ultimately inherit from `BaseEvent`; search
datasets inherit from `BaseSearch`. All Splunk data model datasets can use the
base fields `_time`, `host`, `source`, and `sourcetype`.

- *Tags* and constraints decide which events belong in a dataset.
- *Fields* describe the effective normalized shape that searches, dashboards,
  pivots, and downstream apps expect. Each field entry states whether it is
  `base`, `declared`, `calculated`, or `inherited`.
- *Calculated field entries* include a `calculation` block because they create
  or normalize fields at search time.
- *Lookup files* document expected values, translations, and enrichments, such
  as actions, protocols, HTTP statuses, DNS reply codes, endpoint statuses, and
  severities.

## Data files

- Use [data/catalog.yaml](data/catalog.yaml) to choose a data model and find the generated files.
- Use `data/models/<model>.yaml` to inspect datasets, tags, constraints, and the effective `fields` map for one CIM data model.
- Use [data/fields.yaml](data/fields.yaml) to find field-specific files.
- Use `data/fields/<field>.yaml` to inspect lookup links and where a field is declared or calculated across models and datasets.
- Use [data/lookups.yaml](data/lookups.yaml) and `data/lookups/<lookup>.yaml` for lookup-backed values, translations, and enrichments.
- Use [docs/index.yaml](docs/index.yaml) and `docs/pages/*.md` for Splunk CIM 8.5 prose guidance.
- Use [source.md](source.md) for provenance and generation counts.

## Mapping rules

- Start from the event semantics, choose the closest CIM data model in
  [data/catalog.yaml](data/catalog.yaml), then choose the dataset whose tags and
  constraints match the event.
- Apply all required tags and parent dataset tags implied by the dataset parent chain.
- Populate useful app-documented fields first, especially fields marked
  `recommended` or `required`.
- Treat fields with `source: calculated` or a `calculation` block as
  app-provided normalizations; when mapping a source, still populate the
  underlying source fields needed by those calculations when possible.
- Prefer specific fields such as `src_ip`, `dest_ip`, `user`, `signature`, or
  `vendor_product` over broad fields when the data source provides them.
- Use lookup files to normalize, translate, or enrich values when a lookup
  documents semantics for a field.
- Preserve source-specific details outside CIM fields when the app-derived
  reference has no normalized CIM field.

## Question routing

- Which CIM model should this log map to? [data/catalog.yaml](data/catalog.yaml), then the closest model file.
- What tags or constraints identify a dataset? `data/models/<model>.yaml`.
- What fields does a dataset include? `fields` in `data/models/<model>.yaml`.
- What does field X mean? [data/fields.yaml](data/fields.yaml), then `data/fields/<field>.yaml`.
- What values are expected for a field? Field `expected_values`, then [data/lookups.yaml](data/lookups.yaml).
- What does Splunk say about CIM workflows? [docs/index.yaml](docs/index.yaml).
- What source produced this skill? [source.md](source.md).
