---
title: Shared local validation gate
type: change
authors:
  - mavam
  - codex
prs:
  - 8
created: 2026-05-12T15:12:53.733635Z
---

Maintainers can now run the same validation gate locally, in CI, during release preparation, and before Worktrunk merges:

```sh
uvx --from lefthook==2.1.6 lefthook run pre-push --all-files
```

This keeps skill validation and changelog validation aligned across the repository workflows.
