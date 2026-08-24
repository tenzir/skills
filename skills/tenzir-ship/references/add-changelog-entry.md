# Add a changelog entry

Add a changelog entry for a change.

## Gather context

Run `bash <skill-dir>/scripts/detect-change-scope.sh` to determine the scope for
the change.

This script prints the files and diff command for the changes in scope.

## Determine entry metadata

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

### Authors

The CLI attempts to infer the primary author when `gh` is logged in. For known
external contributions, pass the human contributor's GitHub username with
`--author`.

Authors are people. Never record a coding agent, bot, tool, provider, or model
through `--author`, `--co-author`, or entry frontmatter. Do not assume an
inferred GitHub login belongs to a person: CI and coding-agent credentials can
resolve to bots, GitHub Apps, or machine users.

After creating or updating an entry, inspect every value in its `authors`
metadata. When `gh` is available, check an inferred login with
`gh api users/<login> --jq .type`, but treat `User` only as a candidate because
machine users can report that type. Confirm from the task or pull request
context that the account belongs to a human contributor. If the inferred value
is non-human and the contributor is known, replace it with the person's GitHub
username. If no human can be identified confidently, remove `author` or
`authors` from the entry. Never guess an identity.

If the project config sets `omit_author: true`, do not record authors at
all—neither via `--author`/`--co-author` flags nor by writing `authors` into
the entry frontmatter. Validation rejects unreleased entries that carry
`authors` metadata in such projects. Check the changelog's `config.yaml` for
this option, or the `package.yaml` next to the changelog directory when no
`config.yaml` exists.

If the project config sets `require_author: true`, every unreleased entry must
carry a non-empty `authors` list. The `add` command warns when it cannot find an
author, and `validate` fails the entry. Record only confirmed human
contributors. Never guess an identity to satisfy validation.

### PR numbers

If the project config sets `omit_pr: true`, do not record PR numbers at
all—neither via `--pr` nor by writing `prs` into the entry frontmatter.
The `add` command ignores explicit `--pr` values with a warning in these
projects, and validation rejects `prs` metadata in unreleased entries. Check
the changelog's `config.yaml` for this option, or the `package.yaml` next to
the changelog directory when no `config.yaml` exists. Skip the rest of this
section.

If the project config sets `require_pr: true`, every unreleased entry must
carry `prs` metadata. Plain `validate` fails when unreleased entries are missing
PR numbers.
`validate --lenient` demotes only missing-PR issues to warnings so pre-push
hooks can pass before the first pull request exists. When you see that warning,
add the pull request number to the entry immediately after creating the pull
request.

Otherwise: if your branch already has an open pull request, the existing PR
number will be auto-inferred and you don't have to do anything.

When you are adding one or more changelog entries before creating a pull
request, manually add the PR number to the entries after having filed the PR and
obtained a definite number, e.g.:

```yaml
prs:
  - 42
```

In CI, explicitly use the PR number from `$GITHUB_EVENT_PATH`.

### Description

The description explains the change to the people who use the project. It must
not contain implementation details—internal modules, private helpers, file
paths, dependency upgrades, or refactors belong in commit messages, not in the
changelog.

Write for the end user: someone who interacts with the product through its UI,
CLI, configuration, or documented workflows. Most changelog readers are not
developers of the project—they want to know what changed in the product they
use, not how the code was restructured.

In projects where the public interface _is_ code (libraries, APIs, SDKs), treat
public functions, method signatures, endpoints, and config keys the same way you
would a CLI flag or a UI element—they are part of the user's surface and
belong in the changelog.

**Lead with the outcome.** Start the description with a single sentence that
captures what changed from the user's perspective. Then expand with context,
usage, and motivation as needed. Use Markdown deliberately for user-facing terms
(for example, `` `--verbose` ``).

**Show, don't just tell.** When a change introduces or alters any part of the
public interface—a command, flag, config key, function signature, API
endpoint—include a short usage example. A before/after snippet or a single
invocation is often enough.

**What to include:**

- The user-visible outcome
- A concrete usage example for new or changed capabilities
- Why this matters to users (motivation, not implementation reasoning)
- Migration steps for breaking changes (old behavior → new behavior)

**What to exclude:**

- Internal modules, classes, helper functions, or file paths
- Private implementation details (algorithms, data structures, internal wiring)
- Dependency or build system changes invisible to users
- Refactors or reorganizations without user impact

#### Examples

The following examples illustrate descriptions at different quality levels.

**Feature ✅**

> The `release create` command now accepts a `--dry-run` flag that previews the
> release without modifying any files or creating tags:
>
> ```sh
> tenzir-ship release create --dry-run
> ```
>
> This is useful for verifying the release plan before committing to it.

This works because it names the user-facing command/flag, shows how to use it,
and explains the benefit.

**Feature ❌**

> Added `DryRunMixin` to the `ReleaseCommand` class in `cli/release.py`.
> Refactored the `execute()` method to check `self.dry_run` before writing.

This fails because it references internal classes and files. A user reading the
changelog does not need to know about `DryRunMixin` or `cli/release.py`.

**Breaking change ✅**

> The `--format` flag for the `show` command has been renamed to `--output`.
>
> Before:
>
> ```sh
> tenzir-ship show --format json
> ```
>
> After:
>
> ```sh
> tenzir-ship show --output json
> ```

Clear old-vs-new comparison with concrete commands users can adapt.

**Bugfix ✅**

> The `show` command no longer misidentifies changelog entry IDs as release
> versions. Previously, entries with IDs containing version-like patterns (for
> example, `v1...`) were incorrectly treated as releases.

Describes the symptom the user would have seen and the resolution, without
mentioning the regex fix or the internal function involved.

**Change ✅**

> Validation warnings now include the file path and line number where the issue
> was found, making it easier to locate and fix problems in large changelog
> trees.

Focuses on what the user sees (better error output) rather than how it was
implemented.

#### Review checklist

- Does it describe outcomes rather than implementation?
- Is a usage example shown for new or changed capabilities?
- Are internal-only mechanics absent?
- Are user-facing technical terms preserved in code markup?

## Merge with a related unreleased entry

Before creating a new entry, inspect existing unreleased entries. If the current
change completes, corrects, or extends a change that is already documented
there, merge it into that unreleased entry instead of creating a duplicate.

Only merge when the relationship is clear from the user-facing outcome. A
related entry should describe the same feature, bug, behavior change, or
release workflow from the user's perspective. Similar file paths, nearby
implementation work, shared authors, or adjacent PR timing are not enough.

If the relationship is ambiguous, create a separate entry. Do not delete,
rewrite, or collapse unrelated unreleased entries while adding a changelog
entry. When merging is appropriate, edit only the related entry being merged
into; leave all other unreleased files intact.

When merging into an unreleased entry:

- Reconcile the title, type, and description so they describe the combined
  user-facing outcome.
- Merge list-valued frontmatter such as `authors`, `prs`, and `components`,
  preserving existing values and appending new distinct values.

Never touch already-released changelog entries outside the `unreleased`
directory.

## Create the entry

Begin with writing the description to a temporary file, e.g.,
`/tmp/description.md`.

Then invoke `tenzir-ship` to add the entry:

```sh
uvx tenzir-ship add \
  --title "<title>" \
  --type <type> \
  --description-file /tmp/description.md
```

Notes:

- If no changelog workspace exists yet and the task is setup-first, prefer
  `uvx tenzir-ship init` before creating the first entry.
- `uvx tenzir-ship add` can still bootstrap a missing changelog automatically
  when you are ready to create the first entry.
- Pass `--root <path/to/changelog>` to `tenzir-ship` when the changelog is
  not in the top-level directory.
- Add `--pr <number>` only when the PR number is already known, such as in CI.
  Otherwise rely on auto-inference or update `prs` after filing the PR. Skip
  PR numbers entirely when the config sets `omit_pr: true`.
- Use `--co-author <github-username>` only for an additional human
  contributor. Never use it to identify a coding agent or other tool.

On success, remove the temporary description file.

## Validate

After creating or editing an entry, run validation to catch issues such as
malformed metadata or fields the project's config forbids (`omit_pr`,
`omit_author`):

```sh
uvx tenzir-ship validate
```

Pass the same `--root <path/to/changelog>` you used for `add`. Fix any
reported issues before committing the entry. Metadata policies such as
`omit_pr` and `require_author` apply to unreleased entries by default. Pass
`--all-entries` to audit released entries against the current policies too.
When combined with `--all-entries`, `--lenient` also demotes missing PRs in
released entries. It never demotes missing authors or forbidden metadata.
