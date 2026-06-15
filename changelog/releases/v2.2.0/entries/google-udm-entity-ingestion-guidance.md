---
title: Google UDM entity ingestion guidance
type: change
authors:
  - mavam
  - codex
prs:
  - 14
created: 2026-06-06T07:33:19.458672Z
---

The Google UDM skill now clarifies that Entity Type Guidance values such as `USER` or `ASSET` belong to the Entity object's `metadata.entity_type` / `metadata.entityType`, while `entities.import` uses a separate `inlineSource.logType` for the context source, such as `AZURE_AD_CONTEXT`.
