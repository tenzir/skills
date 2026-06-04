---
title: UDM field path names for YARA-L
type: feature
authors:
  - mavam
  - codex
prs:
  - 12
created: 2026-06-04T17:58:24.497786Z
---

The `tenzir-google-udm` skill now shows both UDM field spellings when they differ, so YARA-L and ingestion workflows can use the same reference without guessing a case conversion.

For example, generated field headings now show `event_type` / `eventType` and `security_result` / `securityResult`. Use the left side in YARA-L, Detect Engine, CBN, and other dotted field-path contexts; use the right side when preparing UDM event or entity objects for Google SecOps ingestion.
