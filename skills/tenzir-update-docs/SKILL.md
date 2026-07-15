---
name: tenzir-update-docs
description: >-
  Coordinate documentation updates alongside code changes. Use when preparing
  the `.docs/` checkout, creating a matching docs branch, opening a
  `tenzir/content` documentation pull request, or cross-linking docs and code
  PRs. Also use when the user mentions "update the docs", "docs PR", ".docs/",
  or when a code change affects user-facing behavior that should be reflected
  in the documentation on tenzir.com.
metadata:
  requires:
    skills:
      - tenzir-technical-writing
---

# Update Documentation

Handle the operational workflow around documentation changes. The docs live in
the `tenzir/content` repository (which also hosts the tenzir.com website)
under `website/src/content/docs/`.

## Workflow

All docs changes take place in `.docs/`, which is a clone of `tenzir/content`.
Clone `.docs` if it doesn't exist. Otherwise fetch the latest refs from origin.

1. Create or check out a topic branch in `.docs/` that matches the parent repo
   branch name.
2. Author the content update under `website/src/content/docs/` using the
   repository's own documentation guidance and conventions (read its
   `website/README.md` first).
3. Run relevant documentation checks if the repository provides them
   (`bun run check` in `website/`).
4. File a `tenzir/content` pull request from `.docs/`.
5. Cross-link the pull requests using one shared compact footer pattern:
   - In the docs PR, append a final `<sub>...</sub>` footer block that links
     the code PR and references the same Linear issue(s), for example
     `⚙️ Code PR: tenzir/tenzir#6048<br>🎫 References TNZ-150, TNZ-151`.
   - In the code PR, append or extend the final `<sub>...</sub>` footer with
     `📚 Docs PR: tenzir/content#261`.
   - Use GitHub shorthand for PR links in both directions, such as
     `tenzir/tenzir#6048` or `tenzir/content#261`, instead of full URLs. Use
     full URLs only for deep links that shorthand cannot express, such as a
     specific comment.
   - If a footer already exists, add another `<br>`-separated line instead of
     creating a second footer.
6. Apply the `automerge` label to the docs PR. This marks the companion PR as
   ready for CI to squash-merge after the linked code PR lands and the docs
   checks pass.
7. Summarize what changed and note any follow-up work.

## Branching

Keep the `.docs/` branch name aligned with the code branch whenever possible.
If the code change spans multiple repositories, use the code branch as the
source of truth for naming and cross-links.

## PR cross-link format

Keep docs/code cross-links in a compact footer at the end of each PR
description. In the docs PR footer, reference the same Linear issue(s) with a
non-closing word such as `references` so the companion docs PR does not move
the issue independently. When multiple issues share the same relationship,
enumerate them after one magic word on one line to keep the footer compact.
Use separate lines only when the relationship differs.

Docs PR example:

```markdown
<sub>
⚙️ Code PR: tenzir/tenzir#1234<br>
🎫 References TNZ-150, TNZ-151
</sub>
```

Code PR example:

```markdown
<sub>
📚 Docs PR: tenzir/content#261<br>
✅ Closes TNZ-150, TNZ-151<br>
📎 Related: tenzir/tenzir#5999
</sub>
```

## Cross-Checks

Before opening the docs PR:

1. Confirm the changed pages still fit their Diataxis section.
2. Check nearby pages and "See also" links for follow-on edits.
3. Ensure code samples, paths, and UI labels match the current product
   behavior.
