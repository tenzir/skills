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
   respond to it. When the user asks to address existing GitHub review
   feedback, collect the active comments first, map each still-valid concern
   to the relevant technical lens, and surface it in the normal finding
   format before you decide how to reply or resolve. On GitHub pull requests,
   also read `references/github-pr-reviews.md` for thread state, reply, and
   resolution guidance.
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
7. **Write up the review** using the report structure below: H1, short
   introduction, `## Overview`, `## Findings`, and `## Verdict`.
8. **Produce a verdict** in the final section.

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

## Report Structure

Use this shape:

1. `# Code Review`
2. one or two sentences of context
3. `## Overview`
4. `## Findings`
5. `## Verdict`
6. optional `## Lower-confidence observations`

Prefer the example below over extra narration.

## Finding Format

Each finding must include:

- `File`: location with line numbers
- `Issue`: one-sentence problem statement
- `Reasoning`: why the behavior is wrong or risky
- `Evidence`: concrete code, types, or behavior
- `Suggestion`: a specific fix or next action

Add `Source` when a finding comes from prior review feedback. For GitHub
reviews, link directly to the review comment.

Use this heading format:

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

Use these category icons:

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

In `## Overview`, list findings like this:

```markdown
- {severity_emoji} {severity} · {category_emoji} {id} · {title} ({confidence}%) · {file}:{line}
```

Sort by severity first, then confidence. Group findings only when they share one
root cause.

## Actionability

Prefer findings that are specific, reproducible, and cheap enough to act on in
the current change. Cap output at roughly 8 findings for a normal-sized diff.

Avoid:

- speculative concerns without concrete evidence
- style nits already enforced by tooling
- rewrite suggestions without a clear risk
- pre-existing issues outside the diff
- unrelated scope creep

## Example Layout

```markdown
# Code Review

I reviewed the BITZ parser changes with a focus on payload validation and test
coverage. I found one P2 issue and one P3 gap.

## Overview

- 🟠 P2 · 🛡️ SEC-1 · Corrupted BITZ frames are accepted if garbage follows a valid Arrow stream (96%) · libtenzir/builtins/formats/bitz.cpp:209
- 🟡 P3 · 🧪 TST-1 · The new tests miss payload-corruption and compatibility coverage (93%) · test/tests/operators/bitz/round_trip.tql:1

## Findings

### 🟠 P2 · 🛡️ SEC-1 · Corrupted BITZ frames are accepted if garbage follows a valid Arrow stream · 96%

- File: libtenzir/builtins/formats/bitz.cpp:209-247
- Issue: ...
- Reasoning: ...
- Evidence: ...
- Suggestion: ...

### 🟡 P3 · 🧪 TST-1 · The new tests miss payload-corruption and compatibility coverage · 93%

- File: test/tests/operators/bitz/round_trip.tql:1-6
- Issue: ...
- Reasoning: ...
- Evidence: ...
- Suggestion: ...

## Verdict

**Needs changes**

| 🔴 P1 | 🟠 P2 | 🟡 P3 | ⚪ P4 |
| :---: | :---: | :---: | :---: |
|   0   |   1   |   1   |   0   |

- Reject BITZ frames that contain unread tail bytes after the embedded Feather stream.
- Add a regression test for malformed message payloads and a mixed legacy/new compatibility fixture.
- Merge after the parser validation bug is fixed.
```

The verdict label should be one of:

- **Ship it**: no findings, or only P4 nits.
- **Ship with fixes**: P3 or below; nothing blocking.
- **Needs changes**: at least one P2 that should be resolved before merge.
- **Blocked**: at least one P1; do not merge.

Write verdict bullets as concrete next steps.

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
responses after the technical review is complete. Carry prior feedback into
the review by translating each still-valid concern into the appropriate
technical finding.

### GitHub pull requests

When reviewing a GitHub pull request, check for existing review comments and
unresolved threads up front. If any exist, read
[reviewer feedback](references/reviewer-feedback.md) and
[GitHub pull request reviews](references/github-pr-reviews.md) before
reviewing the diff. Surface each still-valid concern as the appropriate
technical finding, and add a `Source` line that links directly to the GitHub
comment. Use the GitHub-specific reference to decide whether to reply,
resolve, discuss further, or leave the thread open.
