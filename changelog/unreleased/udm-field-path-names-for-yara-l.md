---
title: UDM field name forms for mapping and YARA-L
type: feature
authors:
  - mavam
  - codex
prs:
  - 12
created: 2026-06-04T17:58:24.497786Z
---

The `tenzir-google-udm` skill now shows both UDM field spellings when they differ, so mapping and detection workflows can use the same reference.

For example, generated field headings now show `event_type` / `eventType` and `security_result` / `securityResult`. Use the right side when mapping logs into UDM event or entity objects for Google SecOps UDM API ingestion; use the left side in YARA-L, Detect Engine, CBN, and other dotted field-path contexts.
