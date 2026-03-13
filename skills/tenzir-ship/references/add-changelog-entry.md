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

- Would someone unfamiliar with the codebase understand it?
- Does it describe outcomes rather than implementation?
- Is a usage example shown for new or changed capabilities?
- Are internal-only names absent?
- Are user-facing technical terms preserved in code font?

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

- If no changelog workspace exists yet and the task is setup-first, prefer
  `uvx tenzir-ship init` before creating the first entry.
- `uvx tenzir-ship add` can still bootstrap a missing changelog automatically
  when you are ready to create the first entry.
- Pass `--root <path/to/changelog>` to `tenzir-ship` when the changelog is
  not in the top-level directory.
- In CI, include `--pr <number>` when PR number is known from `$GITHUB_EVENT_PATH`.
- Locally, omit `--pr` when auto-inference via `gh` context is available.
- Set `--co-author <agent-name>` for GitHub accounts of agent-authored entries,
  e.g, `claude` or `codex`.

On success, remove the temporary description file.
