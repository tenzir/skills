---
title: ArcSight CEF skill
type: feature
authors:
  - mavam
  - claude
prs:
  - 23
created: 2026-06-10T16:50:02.014433Z
---

Added `tenzir-cef`, a generated ArcSight CEF (Common Event Format) reference skill for generating, parsing, and mapping CEF events, bundled with the ArcSight ESM event schema behind the format.

The skill exposes all 174 predefined extension keys from the OpenText extension dictionary as YAML — exact key spelling, expanded full name, data type, length, producer/consumer audience, and the CEF specification version that introduced each key — alongside the full ESM event schema: 479 data fields across 18 groups with labels, script aliases, types, and turbo levels. Extension keys whose full name resolves to an ESM script alias are crosswalked to their schema groups. Markdown guidance covers the CEF header, severity, character escaping, special mappings, user-defined extensions, and date formats. Upstream quirks, such as the duplicated `dmac` row and mid-word line-wrap artifacts in key names, are normalized and documented in the source notes.
