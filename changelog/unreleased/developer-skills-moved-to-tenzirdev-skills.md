---
title: Developer skills moved to tenzir/dev-skills
type: breaking
authors:
  - mavam
prs:
  - 38
created: 2026-08-30T10:44:13.627519Z
---

The public `tenzir/skills` collection now contains only user-facing Tenzir and
security-schema skills. Tenzir's developer workflow skills have moved to the
private `tenzir/dev-skills` repository.

Tenzir developers should install the new bundle:

```sh
npx skills add -g tenzir/dev-skills
```

External contributors who need the public `tenzir-ship` skill can install it
from its source repository:

```sh
npx skills add tenzir/ship@tenzir-ship
```
