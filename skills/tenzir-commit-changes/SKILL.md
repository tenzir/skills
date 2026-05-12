---
name: tenzir-commit-changes
description: >-
  Commit changes as clean, reviewable snapshots. Use when committing, staging,
  splitting work into logical units, writing or fixing commit messages,
  creating fixup commits, or cleaning up commit history. Also use when the user
  says "commit this", "save my changes", "make a commit", or "write a better
  commit message."
---

# Commit Changes

Commit changes as clean, reviewable snapshots.

## Workflow

1. Read `git` status and the relevant diffs before deciding how many commits to
   make.
2. Split orthogonal work into separate logical units. If a file mixes unrelated
   edits, stage only the hunks for the current commit.
3. Run the relevant checks before committing. If you skip a check, say so.
4. For each commit:
   - Stage only the relevant hunks.
   - Read the staged diff before writing the message.
   - [Write the commit message](references/write-commit-messages.md) from what
     is actually staged, including the AI assistance trailer.
   - Create the commit with a real multiline message, using separate `-m`
     arguments for subject, body, and final trailer block.
   - Do not put literal `\n` escapes in a single `-m` string.
   - Amend immediately if the final message reads awkwardly.
