# GitHub pull request reviews

Use this reference when you review a GitHub pull request that already has
review comments or unresolved threads, or when the user asks how to respond on
GitHub.

Read this alongside [reviewer feedback](reviewer-feedback.md). That file covers
how to evaluate prior feedback in general. This file covers GitHub-specific
thread state, comment links, replies, and resolution.

## Check review state early

Before you review the latest diff:

- Look for existing review comments and unresolved threads.
- Re-check comments against the latest commits before surfacing them as active
  findings.
- Skip resolved threads and comments that later commits already addressed.
- When a finding originates from a GitHub comment, link the `Source` field to
  the direct comment URL.

## Decide what to do with each thread

Every open thread needs one of these outcomes:

### Resolve directly

Use this when the fix is obvious and the latest commit makes the outcome clear:

- Typo fixes.
- Straightforward bug fixes.
- Small refactors that match the reviewer's suggestion exactly.

If the user wants a reply anyway, a short note such as `Fixed in abc1234.` is
enough.

### Reply, then resolve

Use this when the fix needs a short explanation:

- Non-obvious implementation choices.
- Partial fixes that address the spirit but not the exact suggestion.
- Alternate approaches that solve the same problem.

### Discuss before acting

Use this when:

- The comment is ambiguous or could be read multiple ways.
- Acting on it would conflict with another requirement or reviewer feedback.
- It would substantially change the design or scope.

### Respectfully disagree

Explain the constraint or tradeoff, keep the thread open, and let the reviewer
close it unless they explicitly ask you to resolve it. Give concrete reasoning.

## Thread resolution

- Resolve only after the fix is pushed or the discussion is genuinely complete.
- Reply before resolving when the change is not self-explanatory or when team
  norms expect a reply.
- Do not resolve open disagreements on behalf of the reviewer.
- If the latest code still does not address the concern, keep the thread open
  and report it as an active finding.
- Treat unresolved reviewer comments as part of the review's remaining work.

## What good GitHub handling looks like

Use the standard finding format from [the main skill](../SKILL.md). For
GitHub-originated findings, keep the `Source` line compact: use the direct
review comment URL first, then append the reviewer handle if that helps.

Example:

```markdown
- **Source:** https://github.com/owner/repo/pull/123#discussion_r456 by @alice
```

If the concern is already fixed, summarize that instead of reporting a finding:

```text
The latest commit adds the missing retry test, so I would not keep this as an
active review finding. Suggested reply: "Added in abc1234."
```

## Reply style

- Keep suggested replies short and factual.
- Reference the commit SHA when a fix has landed.
- If you partially accepted the feedback, explain what changed and what stayed.
- If you disagree, explain the constraint or tradeoff rather than only saying
  no.
- Ask for clarification when the comment could be read multiple ways.
- Avoid filler and overly grateful phrasing.

Examples:

```text
Fixed in abc1234.
```

```text
Addressed the null case in abc1234. I kept the current helper split because it
matches the rest of the module.
```

```text
I did not fold these two branches together because the retry path needs the
extra metric emission. Happy to revisit if you want a larger refactor.
```

## Common false positives to avoid

- Treating every GitHub comment as still active.
- Reporting stale comments from earlier review rounds that later commits
  already addressed.
- Resolving a disagreement on the reviewer's behalf.
- Double-reporting the same issue because multiple reviewers mentioned it.
- Suggesting a reply that sounds defensive or vague.
