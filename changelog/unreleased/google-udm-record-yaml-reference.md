---
title: Google UDM record YAML reference
type: change
authors:
  - mavam
  - codex
prs:
  - 16
created: 2026-06-07T07:17:07.758036Z
---

The Google UDM skill now exposes record definitions as YAML leaves rather than Markdown message pages. Record YAML uses data-centric type shapes such as `list<T>`, `optional<T>`, `map<K, V>`, `variant`, and field `union`s, making event and entity fields easier for agents to scan when mapping logs into UDM.
