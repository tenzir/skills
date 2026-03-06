---
name: review-changes
description: >-
  Review code changes in Tenzir projects. Use when auditing diffs or pull
  requests for bugs, security issues, missing tests, documentation drift,
  readability problems, performance regressions, user experience issues, or
  when deciding how to respond to GitHub review comments.
---

# Review Changes

Review changed code with explicit severity and confidence.

## Scope

Focus on the changed code and behavior introduced by the diff. Pull in adjacent
unchanged code only when it is necessary to explain impact or verify whether an
issue is real.

## Rating

Rate impact separately from certainty.

| Severity | Emoji | Meaning |
| --- | --- | --- |
| P1 | 🔴 | Critical: security flaws, data loss, crashes, or release blockers |
| P2 | 🟠 | Important: broken features, serious regressions, or major correctness gaps |
| P3 | 🟡 | Should fix: smaller bugs, coverage gaps, or usability problems |
| P4 | ⚪ | Nice to have: low-impact polish or consistency issues |

Use confidence scores from 0 to 100. Only report findings with confidence 80 or
higher.

## Finding Format

Each finding must include:

- `File`: location with line numbers
- `Issue`: one-sentence problem statement
- `Reasoning`: why the behavior is wrong or risky
- `Evidence`: concrete code, types, behavior, or reviewer comment
- `Suggestion`: a specific fix or next action

Use this header format:

```markdown
### SEC-1 · P2 · Missing authorization check · 92%
```

Use these prefixes:

- `SEC`: security
- `ARC`: architecture
- `TST`: tests
- `UXD`: user experience
- `RDY`: readability
- `DOC`: documentation
- `PRF`: performance
- `GIT`: GitHub review feedback

Use these category icons when presenting a review summary:

| Prefix | Emoji | Category |
| --- | --- | --- |
| `SEC` | 🛡️ | security |
| `ARC` | 🏗️ | architecture |
| `TST` | 🧪 | tests |
| `UXD` | 🎨 | user experience |
| `RDY` | 👁️ | readability |
| `DOC` | 📖 | documentation |
| `PRF` | 🚀 | performance |
| `GIT` | 💬 | GitHub feedback |
| `GRP` | 📦 | grouped findings |

## Review Presentation

When summarizing findings for a human, present them in an emoji-led format:

```text
{severity_emoji} {severity} · {category_emoji} {id} · {title} ({confidence}%) · {file}:{line}
```

Examples:

```text
🔴 P1 · 🛡️ SEC-1 · SQL injection vulnerability (95%) · src/db.ts:45
🟠 P2 · 🏗️ ARC-1 · Circular dependency (88%) · src/modules/a.ts:12
🟡 P3 · 🧪 TST-2 · Missing edge case test (82%) · tests/api.test.ts:78
```

For GitHub findings, append the author when available:

```text
🟠 P2 · 💬 GIT-1 · Consider using constants (90%) · src/config.ts:23 (@reviewer)
```

If multiple findings collapse into one root cause, you may present a grouped
summary:

```text
╭──────────────────────────────────────────────────────────────────────────╮
│ 🟠 P2 · 📦 GRP-1 · Inconsistent error handling (3 findings)              │
╰┬─────────────────────────────────────────────────────────────────────────╯
 ├─ 🟠 P2 · 👁️ RDY-1 · Missing error check (85%) · src/api.ts:23
 ├─ 🟡 P3 · 👁️ RDY-2 · Silent failure (82%) · src/api.ts:45
 └─ 🟡 P3 · 👁️ RDY-3 · No error logging (80%) · src/api.ts:67
```

Sort summaries by severity first, then by confidence. Include a legend when the
review is long enough that readers would benefit from one.

## Actionability

Prefer findings that are specific, reproducible, and cheap enough to act on in
the current change. Avoid speculative concerns, style preferences without a
project standard, and issues outside the review scope.

## Reviewer Lenses

Load only the lenses that matter for the current diff:

- [architecture](references/architecture.md)
- [documentation](references/docs.md)
- [GitHub review threads](references/github-review-threads.md)
- [performance](references/performance.md)
- [readability](references/readability.md)
- [security](references/security.md)
- [tests](references/tests.md)
- [user experience](references/ux.md)
