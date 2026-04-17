---
name: update-documentation
description: >-
  Coordinate docs.tenzir.com updates alongside code changes. Use when preparing
  the `.docs/` checkout, creating a matching docs branch, opening a
  `tenzir/docs` pull request, or cross-linking docs and code PRs. Also use when
  the user mentions "update the docs", "docs PR", ".docs/", or when a code
  change affects user-facing behavior that should be reflected on
  docs.tenzir.com.
metadata:
  requires:
    skills:
      - technical-writing
---

# Update Documentation

Handle the operational workflow around docs.tenzir.com changes.

## Workflow

1. Ensure `.docs/` exists and is up to date by cloning `tenzir/docs` or
   fetching from `origin`.
2. Create or check out a topic branch in `.docs/` that matches the parent repo
   branch name.
3. Author the content update in `.docs/` using the docs repository's own
   documentation guidance and conventions.
4. Run relevant documentation checks if the docs repository provides them.
5. File a `tenzir/docs` pull request from `.docs/`.
6. Cross-link the pull requests using one shared compact footer pattern:
   - In the docs PR, append a final `<sub>...</sub>` footer line such as
     `🔗 Code PR: tenzir/tenzir#6048`.
   - In the code PR, append or extend the final `<sub>...</sub>` footer with
     `🔗 Docs PR: tenzir/docs#261`.
   - Prefer that footer over dedicated `Code PR` or `Docs PR`
     sections. If a footer already exists, add another `<br>`-separated line
     instead of creating a second footer.
7. Summarize what changed and note any follow-up work.

## Branching

Keep the `.docs/` branch name aligned with the code branch whenever possible.
If the code change spans multiple repositories, use the code branch as the
source of truth for naming and cross-links.

## PR cross-link format

Keep docs/code cross-links in a compact footer at the end of each PR
description. When multiple issues share the same relationship in the code PR
footer, enumerate them after one magic word on one line to keep the footer
compact. Use separate lines only when the relationship differs.

Docs PR example:

```markdown
<sub>
🔗 Code PR: tenzir/tenzir#1234
</sub>
```

Code PR example:

```markdown
<sub>
🔗 Docs PR: tenzir/docs#261<br>
✅ Resolves TNZ-150, TNZ-151
</sub>
```

## Cross-Checks

Before opening the docs PR:

1. Confirm the changed pages still fit their Diataxis section.
2. Check nearby pages and "See also" links for follow-on edits.
3. Ensure code samples, paths, and UI labels match the current product
   behavior.
