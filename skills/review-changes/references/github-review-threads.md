# GitHub Review Threads

Use this reference when the review includes existing GitHub PR feedback or when
you need to recommend how to respond to a reviewer.

## Decision Rules

### Resolve without reply

Use this when the fix is obvious and the commit itself is enough:

- Typo fixes
- Straightforward bug fixes
- Small refactors that match the reviewer's suggestion exactly

### Reply, then resolve

Use this when the fix needs a short explanation:

- Non-obvious implementation choices
- Partial fixes where you addressed the spirit but not the letter of the
  comment
- Alternate approaches to what the reviewer suggested

### Discuss before acting

Use this when:

- The comment is ambiguous or could be read multiple ways
- Acting on it would conflict with another requirement or reviewer's feedback
- It would change the design substantially — scope creep risk

### Respectfully disagree

Explain the constraint or tradeoff, keep the thread open, and let the reviewer
close it. Provide concrete reasoning — "I considered that but chose X
because…" is useful; "I disagree" is not.

## Reply Style

- Keep replies short and factual.
- Reference the commit SHA when a fix has landed.
- Do not thank excessively or add filler.

Examples:

```text
Fixed in abc1234.
```

```text
Fixed in abc1234. Kept the current structure because it matches the existing
pattern in config loading.
```

```text
Good catch. Went with an enum instead of the suggested string constant —
same intent but catches typos at compile time. Fixed in abc1234.
```

## Thread Resolution

Resolve only after the fix is pushed or the discussion is genuinely complete.
Do not resolve open disagreements on behalf of the reviewer.

When automating replies with `gh api graphql`, use the thread ID from the
GitHub review thread and reply before resolving.

## What a GIT Finding Looks Like

When existing review comments need attention, surface them as GIT-prefixed
findings:

```markdown
### 🟠 P2 · 💬 GIT-1 · Unaddressed reviewer concern about error handling · 90%

- **File:** src/api.cpp:88
- **Issue:** @reviewer flagged that the new endpoint swallows parse errors,
  but no follow-up commit addresses it.
- **Reasoning:** The reviewer's concern is valid — silent parse failures will
  make debugging difficult for users.
- **Evidence:** Review comment from 2 days ago, no subsequent commits touch
  the error path.
- **Suggestion:** Add error propagation as the reviewer suggested, reply with
  the fix SHA, then resolve the thread.
```

## Common False Positives to Avoid

- Treating resolved threads as open findings — check thread status before
  reporting.
- Surfacing old review comments from previous review rounds that have already
  been addressed in subsequent commits.
- Reporting nit-level review comments as P2+ findings — match the severity to
  the reviewer's intent.
