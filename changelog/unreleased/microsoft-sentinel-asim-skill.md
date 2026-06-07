---
title: Microsoft Sentinel ASIM skill
type: feature
authors:
  - mavam
  - codex
prs:
  - 11
  - 17
created: 2026-06-04T11:26:42.47343Z
---

Added `tenzir-microsoft-asim`, a Microsoft Sentinel ASIM reference skill for mapping security telemetry to ASIM.

The generated reference currently covers 12 event schemas, 1 entity schema, 539 distinct fields, 1,426 schema field records, and 73 alias records from Microsoft Defender Docs. It now emits agent-native YAML catalogs, schema files, field files, alias data, and guidance data so agents can choose target ASIM schemas and map source telemetry with less context-window overhead.
