---
name: create-pull-requests
description: >-
  Ship changes via pull request in Tenzir projects. Use when the user wants to
  open a PR, push a branch, add or update changelog entries, create a pull
  request for review, or when they say "ship this", "open a PR", "send this for
  review", or "push and create a pull request." Also use for follow-up changes
  to an existing PR.
metadata:
  requires:
    skills:
      - commit-changes
      - tenzir-ship
      - update-documentation
---

# Create Pull Requests

Create pull requests and keep their changelog current.

## Workflow

1. Ensure changes are committed in coherent units. Use the `commit-changes`
   skill for staging, splitting, and writing commit messages.
2. Scan the current context for related issues before drafting the PR body.
   Check the user request, surrounding conversation, branch name, commit
   messages, any existing changelog entry, existing PR text, and any available
   issue-tracker context. If the tracker is available, determine whether each
   issue should close on merge or should only be linked.
3. Create a pull request from the current worktree branch.
4. Add and commit a changelog entry. Do not create or edit changelog entries
   manually here; use the `tenzir-ship` skill for generating, formatting, and
   updating the entry.
5. If the change affects user-facing behavior documented on docs.tenzir.com,
   follow the `update-documentation` skill to open a companion docs PR and
   cross-link the two PRs.
6. Push the branch.

When doing follow-up edits, ensure that the changelog entries remain in sync
with the changed functionality by routing any entry updates through
`tenzir-ship` rather than editing changelog files by hand.

## PR footer

Always look for related issues and companion PRs before finalizing the PR
description.

- Scan the current context first: user prompt, branch name, recent commits,
  existing changelog text if any, PR title/body draft, and companion docs or
  follow-up PRs.
- If tracker context is available, confirm which issues this PR should affect.
- Use one compact `<sub>...</sub>` footer at the very end of the PR body.
- Put that footer in the PR description itself, not in a PR comment.
- If a footer already exists, extend it instead of creating a new section or a
  second footer.
- Keep it terse and machine-readable: prefer one directive or link per line and
  join lines with `<br>`.
- If no reliable issue reference or companion PR is available after scanning,
  omit that line or ask the user when the linkage matters.

For Linear, use its magic words explicitly in that footer:

- Use a closing word such as `closes` when the issue should move toward done
  and close on merge.
- Use a non-closing word such as `references`, `related to`, or `part of`
  when the PR should be linked without closing the issue.
- Emojis may prefix a line for readability, but they do not replace Linear's
  magic words. Keep the actual keyword text intact.
- Even if the branch name or PR title already mentions the issue ID, still add
  the footer when you want the close-vs-link intent to be explicit.
- When multiple issues share the same relationship, enumerate them after one
  magic word on one line to keep the footer compact, for example
  `✅ Closes TNZ-82, TNZ-499, TNZ-108, TNZ-109`.
- Use separate lines only when the relationship differs, for example one line
  for `closes` and another for `references`.
- When there is a companion docs PR, add a plain line such as
  `📚 Docs PR: tenzir/docs#261` to the same footer block rather than creating
  a dedicated section.

Example footer:

```markdown
<sub>
📚 Docs PR: tenzir/docs#261<br>
✅ Closes TNZ-150, TNZ-151<br>
🎫 References TNZ-152<br>
📎 Related: https://github.com/tenzir/tenzir/issues/6048#issuecomment-1234567890
</sub>
```

## PR body

Use this template for the pull request description:

```markdown
## 🔍 Problem

<!-- What is the problem, gap, or pain point this PR addresses? -->

## 🛠️ Solution

<!-- How does this PR address the problem? -->

## 💬 Review

<!-- Where should reviewers focus? Architecture decisions, trade-offs, risks, open questions. -->

<!-- Append a final <sub>...</sub> footer here for issue and companion-PR links. -->
```

Instructions:

- The target audience is a senior software engineer. Be brief and to the point.
- Replace each HTML comment with a terse explanation.
- Prefer bullet lists over elaborate prose.
- The diff speaks for itself, don't explain what files you changed.
- Put the footer at the very end of the PR body so issue trackers can parse it
  reliably and related PR links stay visually compact.
