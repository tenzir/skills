# GitHub Review Threads

Use this reference when the review includes existing GitHub PR feedback or when
you need to recommend how to respond to a reviewer.

## Decision Rules

### Resolve without reply

Use this when the fix is obvious and the commit itself is enough:

- typo fixes
- straightforward bug fixes
- small refactors that match the reviewer suggestion

### Reply, then resolve

Use this when the fix needs a short explanation:

- non-obvious implementation choices
- partial fixes
- alternate implementations of the reviewer suggestion

### Discuss before acting

Use this when the comment is ambiguous, conflicts with another requirement, or
would change the design substantially.

### Respectfully disagree

Explain the constraint or tradeoff, keep the thread open, and let the reviewer
close it.

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

## Thread Resolution

Resolve only after the fix is pushed or the discussion is genuinely complete.
Do not resolve open disagreements on behalf of the reviewer.

When automating replies with `gh api graphql`, use the thread ID from the
GitHub review thread and reply before resolving.
