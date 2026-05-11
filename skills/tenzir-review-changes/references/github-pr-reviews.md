# GitHub pull request reviews

Use this reference when you review a GitHub pull request that has
review comments or unresolved threads.

Read this alongside [reviewer feedback](reviewer-feedback.md). That file covers
how to evaluate prior feedback in general. This file covers GitHub-specific
thread state, comment links, replies, and resolution.

## Check review state early

Before you review the latest diff:

- Look for existing review comments and unresolved threads.
- Re-check comments against the latest commits before surfacing them as active
  findings.
- Treat resolved threads and addressed comments as context for understanding the
  review history.
- When the task involves existing GitHub review comments, translate each
  still-active concern into the appropriate technical finding and track each
  open thread through fix, reply, and final state.
- When a finding originates from a GitHub comment, link the `Source` field to
  the direct comment URL.

## Decide what to do with each thread

Every open thread needs one of the following outcomes.

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
- Alternate fixes that address the underlying concern with a different shape.
- Alternate approaches that solve the same problem.

### Discuss before acting

Use this when:

- The comment is ambiguous or could be read multiple ways.
- Acting on it would conflict with another requirement or reviewer feedback.
- It would substantially change the design or scope.

### Respectfully disagree

Explain the constraint or tradeoff with concrete reasoning. Keep the thread
open when the disagreement still needs reviewer input. Resolve it only when the
reviewer has already accepted the explanation or the user explicitly asks you to
close the disagreement.

## Thread resolution

- Resolve a thread after the fix is pushed or the discussion is genuinely
  complete. Treat this as the default final step for fixed or fully answered
  GitHub review feedback.
- Reply before resolving when the change benefits from explanation or when team
  norms expect a reply.
- Leave open only active concerns, unresolved disagreements, ambiguous comments,
  threads that need a reviewer decision, and threads you cannot resolve with the
  available GitHub permissions.
- Keep active concerns open, report them as findings, and include the next step
  needed to close them.
- Treat the review feedback as complete when every unresolved reviewer comment
  has a recorded outcome: resolved, replied and intentionally left open for
  reviewer input.

## What good GitHub handling looks like

Use the standard finding format from [the main skill](../SKILL.md). For
GitHub-originated findings, keep the `Source` line compact: use the direct
review comment URL first, then append the reviewer handle if that helps.
Classify the concern under the relevant technical category, then attach the
GitHub source.

Example:

```markdown
- **Source:** https://github.com/owner/repo/pull/123#discussion_r456 by @alice
```

If the concern is already fixed, summarize the final state instead of reporting
it as an active finding:

```text
The latest commit adds the missing retry test. Suggested reply: "Added in
abc1234."
```

If the concern is still active, surface it like any other finding, with the
right technical category and a `Source` line back to the thread.

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
I kept these two branches separate because the retry path needs the extra metric
emission. Happy to revisit if you want a larger refactor.
```
