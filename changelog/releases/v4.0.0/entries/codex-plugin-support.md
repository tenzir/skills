---
title: Codex plugin support
type: feature
authors:
  - mavam
prs:
  - 39
created: 2026-08-30T18:58:33.713166Z
---

Install the public Tenzir skills as one Codex plugin:

```sh
codex plugin marketplace add tenzir/agent-plugins
codex plugin add skills@tenzir
```

The plugin loads the canonical collection directly from `tenzir/skills`, so
plugin updates do not require a second copy of the skills.
