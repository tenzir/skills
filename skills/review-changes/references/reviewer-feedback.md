# Reviewer feedback

Use this reference when the change already has review comments or when the user
asks how to respond to prior feedback.

Treat prior feedback as input to verify against the latest code. Re-check the
latest code first, then decide whether to fix the issue, explain the tradeoff,
ask for clarification, or note that the concern is already addressed.

For GitHub-specific thread handling, also read
[GitHub pull request reviews](github-pr-reviews.md).

## Focus areas

- **Re-check comments against the latest code.** Treat comments from previous
  review rounds as current only after confirming they still apply.
- **Distill the underlying concern.** Fold each still-valid comment into the
  relevant category — security, architecture, tests, UX, readability,
  documentation, or performance — and restate it as a normal finding before
  you draft a response.
- **Capture provenance.** When a finding originates from prior feedback, add a
  `Source` line with a link to the originating comment or note.
- **Collapse duplicates.** If several reviewers point at the same root cause,
  report it once and note the repeated concern in the evidence.
- **Separate solved from unsolved feedback.** If the latest diff already
  addresses a comment, summarize the final state and suggested reply.
- **Help with the response.** When the user asks how to reply, suggest a short,
  factual response that either points to the fix, explains the tradeoff, or
  asks for clarification.

## Decide how to handle each comment

Every substantive comment needs a decision:

### Fix and summarize

Use this when the concern is valid and the change is straightforward:

- Typos.
- Clear correctness fixes.
- Small refactors that match the reviewer's suggestion.

Summarize the fix briefly after it lands.

### Explain the fix

Use this when the change needs a short explanation:

- Non-obvious implementation choices.
- Alternate fixes that address the underlying concern with a different shape.
- Alternate approaches that solve the same problem.

### Discuss before acting

Use this when:

- The comment is ambiguous or could be read multiple ways.
- Acting on it would conflict with another requirement or another review.
- It would substantially change the design or scope.

### Respectfully disagree

Explain the constraint or tradeoff with concrete reasoning, and connect that
reasoning to why the current approach remains the right choice.

## What good handling looks like

Use the standard finding format from [the main skill](../SKILL.md). When a
finding originates from prior feedback, add a compact `Source` line with the
original comment or note URL first, then append the reviewer identity if that
helps. For example, a comment about missing coverage should surface as `TST`,
and a comment about confusing behavior should surface as `UXD`.

Example:

```markdown
- **Source:** https://example.com/reviews/456 by @alice
```

If the concern is already fixed, summarize the final state instead of reporting
it as an active finding:

```text
The latest commit adds the missing retry test. Suggested reply: "Added in
abc1234."
```

## Response style

- Keep suggested replies short and factual.
- Reference the fix when one exists.
- If you partially accepted the feedback, explain what changed and what stayed.
- If you disagree, explain the constraint or tradeoff behind the current
  approach.
- Ask for clarification when the comment could be read multiple ways.
- Keep the wording concise and specific to the technical outcome.

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

## Good review hygiene

- Treat reviewer feedback as input to verify against the latest code.
- Report earlier comments as active when the underlying concern remains in the
  latest diff.
- Group duplicate comments that point to the same root cause.
- Restate each concern at the level of the underlying issue.
- Write replies that sound factual, specific, and grounded in the code.
