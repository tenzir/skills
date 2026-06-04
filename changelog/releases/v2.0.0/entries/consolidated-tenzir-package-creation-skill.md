---
title: Consolidated Tenzir package creation skill
type: breaking
authors:
  - mavam
  - codex
created: 2026-05-27T09:16:40.215654Z
---

The package creation workflow is now centered on `tenzir-create-package`, a single skill for building library-quality Tenzir packages with UDOs, tests, examples, disabled-by-default pipelines, inputs, contexts, and optional OCSF mappings.

Before:

```sh
npx skills add tenzir/skills@tenzir-create-parser-package
npx skills add tenzir/skills@tenzir-create-ocsf-mapping
```

After:

```sh
npx skills add tenzir/skills@tenzir-create-package
```

Use the new skill for parser package work, OCSF mapping work, and broader package development.
