# Write commit messages

Write clear, consistent Git commit messages in Tenzir projects.

## Goal

Help a future reader understand what changed and why. Lead with the effect of
the change. That is often user-facing, but internal commits can describe
correctness, performance, batching, or cleanup outcomes when those matter more.

## Format

```text
<subject>

<body>
```

A subject line alone is enough for tiny, obvious commits. If a reader would ask
"why?", add a body.

## Before writing

If nothing is staged yet, read the relevant working-tree diff to decide what
belongs in the commit. After staging, read the staged diff and write the
message from that exact snapshot. Identify:

1. The single logical change.
2. The motivation or bug.
3. Any consequence worth noting, such as test updates or cleanup.

## Subject line

- Keep it under 50 characters.
- Use the imperative mood.
- Capitalize the first word.
- Do not end it with a period.
- Describe the effect of the change, not just the mechanics.
- For performance or correctness work, name the invariant, failure mode, or
  cost you changed.

## Body

- Wrap at 72 characters.
- Explain what changed and why.
- Separate it from the subject with a blank line.
- Use active voice and present tense.
- Prefer one to three short paragraphs.

## Writing style

Write for someone reading the log in six months. Avoid narrating only code
motion when you can describe the outcome instead.

Perspective: Write from users' capabilities and needs, not technical
implementation.

Good: "Add DNS resolution operator"
Bad: "Implement dns_lookup as builtin plugin"

Voice: Use active voice and present tense.

Good: "Fix crash when input file is empty"
Bad: "Fixed a bug that was causing crashes"

## Examples

```text
Add slice function for substring extraction
```

```text
Fix crash when input file is empty

The parser assumed at least one byte of input. Now it handles
empty files gracefully by returning an empty result.

Resolves: #456
```

```text
Remove deprecated export command

Use `to` instead. The export command has been deprecated since v4.0.
```

## Commit mechanics

- Use separate `-m` arguments for the subject and body.
- Do not put literal `\n` escapes in a single `-m` string.
- Use `git commit --fixup <SHA1>` for commits meant to be squashed.
- Reference issues when relevant with `Resolves: #123` or `See also: #456`.
