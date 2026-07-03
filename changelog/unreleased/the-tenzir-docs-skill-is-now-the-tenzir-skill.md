---
title: The tenzir-docs skill is now the tenzir skill
type: breaking
authors:
  - mavam
  - claude
created: 2026-07-03T07:24:27.162139Z
prs:
  - 27
---

The `tenzir-docs` skill is now called `tenzir`. The skill remains the bundled
Tenzir documentation—TQL, operators, functions, integrations, and
deployment—and its `SKILL.md` now adds a "Beyond the docs" section with live
entry points to the changelog, blog, solutions, and the full site index at
`https://tenzir.com/llms.txt`, reflecting that tenzir.com and the
documentation now live in one place.

Reinstall the skill under its new name:

Before:

```sh
npx skills add tenzir/skills@tenzir-docs
```

After:

```sh
npx skills remove tenzir-docs
npx skills add tenzir/skills@tenzir
```

Skills that declared a dependency on `tenzir-docs` (such as
`tenzir-manage-packages`) now require `tenzir` instead.
