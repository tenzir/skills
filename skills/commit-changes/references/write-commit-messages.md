# Write commit messages

Write clear, consistent git commit messages in Tenzir projects.

## Format

```text
<subject>

<body>
```

## Subject line

- Keep it under 50 characters.
- Use the imperative mood.
- Focus on user capability, not implementation.
- Capitalize the first letter.
- Do not end the line with a period.

## Body

- Wrap at 72 characters.
- Explain what changed and why it changed.
- Separate it from the subject with a blank line.

## Writing style

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

## Best practices

- One logical change per commit.
- Commit early and often.
- Order commits so dependencies appear in sequence.
- Write for someone reading the log in six months.
- Reference issues when relevant with `Resolves: #123` or `See also: #456`.
- Use `git commit --fixup <SHA1>` for corrections meant to be squashed.
