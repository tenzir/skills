---
title: Splunk CIM skill
type: feature
authors:
  - mavam
  - codex
prs: []
created: 2026-06-06T19:58:14Z
---

Added `tenzir-splunk-cim`, a generated Splunk Common Information Model reference skill for mapping security telemetry to CIM.

The generator takes an unpacked `Splunk_SA_CIM` app directory as input and emits agent-native YAML catalogs for CIM data models, datasets, fields, constraints, calculated fields, index macros, and lookup-backed value lists. The generated skill also bundles core Splunk CIM 8.5 documentation as reference-only prose while keeping the app-derived YAML authoritative.
