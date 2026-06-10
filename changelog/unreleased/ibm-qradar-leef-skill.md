---
title: IBM QRadar LEEF skill
type: feature
authors:
  - mavam
  - claude
prs:
  - 20
created: 2026-06-10T14:48:24.468774Z
---

Added `tenzir-leef`, a generated IBM QRadar LEEF (Log Event Extended Format) reference skill for generating, parsing, and mapping LEEF 2.0 events.

The skill exposes all 45 predefined event attributes as YAML — exact key spelling, value type, normalization behavior, attribute limits, and reserved status — plus Markdown guidance for the syslog and LEEF headers, delimiter rules, custom event keys, and `devTime`/`devTimeFormat` timestamp patterns. Spec quirks published by IBM, such as the `identSecondlp` typo, are preserved verbatim and annotated.
