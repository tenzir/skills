# Add a changelog entry

Add a changelog entry for a change.

## Gather context

Run `scripts/detect-change-scope.sh` to determine the scope for the change.

This script injects the files and diff command for the changes in scope.

## Determine key entry details

Infer the following details from the change context:

### Type

Must be one of:

- `breaking`: change that breaks the public API
- `feature`: net-new functionality that's additive to what was there before
- `change`: backwards-compatible change of existing functionality
- `bugfix`: resolution of an issue, crash, or anomaly

If the type cannot be determined with high confidence, derive them from the
dominant user-facing change.

### Title

The title acts as heading for the changelog entry and summarizes the changelog
entry from a user-facing perspective.

- Plain text only (no Markdown)
- Sentence case
- Descriptive noun phrase, not imperative command

Examples:

- Good: `OAuth support for authentication`
- Bad: `Add OAuth authentication`

### Description

The description is the detailed explanation for users. The goal is to make it
easy to understand the change without required knowledge about system internals.

Prioritize user outcomes over internal implementation details.

Include:

- The user-visible outcome
- A small concrete usage example when applicable
- Why this matters to users

Exclude:

- Internal library/framework/dependency names used only in implementation
- Internal modules/classes/functions/files
- Build or infrastructure internals
- Refactors/reorganization without user impact
- PR/commit/branch process wording

Preserve user-facing technical terms:

- CLI commands, flags, options
- Public API names, config keys, env vars
- Error messages/status codes users see

For breaking changes, be explicit about old vs new behavior and migration steps.

A good description summaries the entire change in the first sentence and uses
Markdown deliberately for user-facing terms (for example, `` `--verbose` ``).

Review checklist:

- Would someone unfamiliar with the codebase understand it?
- Does it describe outcomes rather than implementation?
- Is usage shown for new capabilities?
- Are internal-only names removed?
- Are user-facing technical terms preserved?

## Create the entry

Begin with writing the description to a temporary file, e.g.,
`/tmp/description.md`.

Then invoke `tenzir-ship` to add the entry:

```sh
uvx tenzir-ship add \
  --title "<title>" \
  --type <type> \
  --description-file /tmp/description.md \
  --pr <number> \
  --co-author <agent-name>
```

Notes:

- Pass `--root <path/to/changelog>` to `tenzir-ship` when the changelog is
  not in the top-level directory.
- In CI, include `--pr <number>` when PR number is known from `$GITHUB_EVENT_PATH`.
- Locally, omit `--pr` when auto-inference via `gh` context is available.
- Set `--co-author <agent-name>` for GitHub accounts of agent-authored entries,
  e.g, `claude` or `codex`.

On success, remove the temporary description file.
