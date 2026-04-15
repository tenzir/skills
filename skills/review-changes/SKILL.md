---
name: review-changes
description: >-
  Review code changes in Tenzir projects. Use when auditing diffs or pull
  requests for bugs, security issues, missing tests, documentation drift,
  readability problems, performance regressions, user experience issues, or
  when deciding how to respond to pull request review comments, especially
  GitHub review comments and threads. Also use this skill whenever the user
  says "review", "look at this PR", "check my changes", "audit this diff",
  "what do you think of this code", or asks for feedback on any code they've
  written or changed — even if they don't explicitly say "code review."
---

# Review Changes

Review changed code with explicit severity and confidence.

## Process

Follow this sequence to produce a thorough, efficient review:

1. **Understand intent.** Read the PR description, commit messages, linked
   issues, and any existing reviewer feedback. Know what the change is _trying_
   to do before judging how well it does it.
2. **Load prior-feedback guidance when needed.** If the review already has
   comments or notes, read `references/reviewer-feedback.md` before reviewing
   the diff so you can check whether that feedback still applies and how to
   respond to it. On GitHub pull requests, also read
   `references/github-pr-reviews.md` for thread state, reply, and resolution
   guidance.
3. **Scan for scope.** Skim the full diff to understand what areas it touches —
   files, modules, layers. This determines which lenses to load.
4. **Select lenses.** Use the table below to pick the relevant technical
   lenses. Load only what applies; skip the rest. Readability is the baseline.
5. **Review each file.** Walk the diff file by file. Pull in adjacent unchanged
   code only when it is necessary to explain impact or verify whether an issue
   is real. Re-check prior reviewer feedback against the latest code before you
   repeat or endorse it.
6. **Synthesize.** After the file-by-file pass, look for groupable root causes.
   Multiple symptoms in different files may share one underlying problem —
   present those as a grouped finding instead of separate entries.
7. **Write up findings** using the format and presentation rules below.
8. **Produce a verdict** in the summary section.

## Lens Selection

Use this table to decide which lenses to load based on what the diff touches.
Readability is always worth loading as a baseline.

| If the diff touches…                     | Load these lenses       |
| ---------------------------------------- | ----------------------- |
| User input, auth, networking, secrets    | Security                |
| Public APIs, module boundaries           | Architecture            |
| CLI output, error messages, defaults     | UX                      |
| Hot paths, loops, queries, large data    | Performance             |
| New features, bug fixes, branching logic | Tests                   |
| Docs, README, docstrings, examples       | Documentation           |
| Anything else                            | Readability (always on) |

## Scope

Focus on the changed code and behavior introduced by the diff. Pull in adjacent
unchanged code only when it is necessary to explain impact or verify whether an
issue is real.

## Rating

Rate impact separately from certainty.

| Severity | Emoji | Meaning                                                                    |
| -------- | ----- | -------------------------------------------------------------------------- |
| P1       | 🔴    | Critical: security flaws, data loss, crashes, or release blockers          |
| P2       | 🟠    | Important: broken features, serious regressions, or major correctness gaps |
| P3       | 🟡    | Should fix: smaller bugs, coverage gaps, or usability problems             |
| P4       | ⚪    | Nice to have: low-impact polish or consistency issues                      |

Report findings with confidence ≥ 80. For findings between 60–79, mention them
briefly in a "Lower-confidence observations" section at the end, clearly marked
as uncertain. Below 60, drop them entirely.

## Finding Format

Each finding must include:

- `File`: location with line numbers
- `Issue`: one-sentence problem statement
- `Reasoning`: why the behavior is wrong or risky
- `Evidence`: concrete code, types, or behavior
- `Suggestion`: a specific fix or next action

When a finding originates from external review feedback, add an optional
`Source` field with a link to the originating comment or note. For GitHub
reviews, link directly to the review comment.

Use this header format:

```markdown
### 🟠 P2 · 🛡️ SEC-1 · Missing authorization check · 92%
```

Use these prefixes:

- `SEC`: security
- `ARC`: architecture
- `TST`: tests
- `UXD`: user experience
- `RDY`: readability
- `DOC`: documentation
- `PRF`: performance

Use these category icons when presenting a review summary:

| Prefix | Emoji | Category         |
| ------ | ----- | ---------------- |
| `SEC`  | 🛡️    | security         |
| `ARC`  | 🏗️    | architecture     |
| `TST`  | 🧪    | tests            |
| `UXD`  | 🎨    | user experience  |
| `RDY`  | 👁️    | readability      |
| `DOC`  | 📖    | documentation    |
| `PRF`  | 🚀    | performance      |
| `GRP`  | 📦    | grouped findings |

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

When a finding originates from prior review feedback, add a `Source` line with
that comment or note.

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
the current change. Cap output at roughly 8 findings for a normal-sized diff —
prioritize ruthlessly rather than dumping everything.

Avoid:

- Speculative concerns without concrete evidence in the diff.
- Style preferences that linters or formatters already enforce.
- Suggesting rewrites of working code unless there's a clear maintainability or
  correctness risk.
- Flagging pre-existing TODO/FIXME comments that aren't part of this change.
- Issues outside the review scope (e.g., unrelated files, hypothetical future
  requirements).

## Summary

End every review with:

1. A bordered summary that includes only the severity counts.
2. A verdict label.
3. One to three short, action-oriented bullets that explain the TL;DR.

Use this format:

```markdown
╭───────────────────────────────────────────╮
│ 🔴 P1: 0   🟠 P2: 1   🟡 P3: 2   ⚪ P4: 1 │
╰───────────────────────────────────────────╯
**Needs changes**:

- Fix the inconsistent error handling in `src/api.ts`, `src/jobs.ts`, and `src/worker.ts`.
- Add a retry-path test so this regression does not recur.
- Merge after the P2 issue is resolved.
```

The verdict label should be one of:

- **Ship it**: no findings, or only P4 nits.
- **Ship with fixes**: P3 or below; nothing blocking.
- **Needs changes**: at least one P2 that should be resolved before merge.
- **Blocked**: at least one P1; do not merge.

Write the bullets as a call to action. Prefer concrete next steps over vague
summaries.

Good:

- `Add the missing authorization check in the admin route.`
- `Update the docs to mention the new default timeout.`
- `Merge after the flaky retry test is fixed.`

Avoid:

- `Authorization issue.`
- `Docs need work.`
- `Some tests are missing.`

If cross-cutting themes emerged (for example, "error handling is inconsistent
across three files"), use one bullet to name the theme and the remaining
bullets to say what should happen next.

## Technical Lenses

Load only the lenses that matter for the current diff:

- [architecture](references/architecture.md)
- [documentation](references/docs.md)
- [performance](references/performance.md)
- [readability](references/readability.md)
- [security](references/security.md)
- [tests](references/tests.md)
- [user experience](references/ux.md)

## Prior Reviewer Feedback

When the change already has review comments or the user asks how to respond,
read [reviewer feedback](references/reviewer-feedback.md). Use that input to
sharpen findings, verify whether comments still apply, and draft concise
responses after the technical review is complete.

### GitHub pull requests

When reviewing a GitHub pull request, check for existing review comments and
unresolved threads up front. If any exist, read
[reviewer feedback](references/reviewer-feedback.md) and
[GitHub pull request reviews](references/github-pr-reviews.md) before
reviewing the diff. When a valid finding originates from a GitHub comment, add
a `Source` line that links directly to that comment. Use the GitHub-specific
reference to decide whether to reply, resolve, discuss further, or leave the
thread open.
