---
title: Consolidated Tenzir package management skill
type: breaking
authors:
  - mavam
  - codex
created: 2026-05-27T09:16:40.215654Z
---

The package management workflow is now centered on `tenzir-manage-packages`, a single skill for adding, inspecting, updating, extending, refactoring, deprecating, and removing library-quality Tenzir package capabilities with UDOs, tests, examples, disabled-by-default pipelines, inputs, contexts, and schema mappings such as OCSF, Google UDM, ECS, and ASIM.

Before:

```sh
npx skills add tenzir/skills@tenzir-create-parser-package
npx skills add tenzir/skills@tenzir-create-ocsf-mapping
```

After:

```sh
npx skills add tenzir/skills@tenzir-manage-packages
```

Use the new skill for parser package work, schema mapping work, and broader package lifecycle management.
