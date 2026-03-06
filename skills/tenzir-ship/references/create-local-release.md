# Create a release

Cut a release in a local repository with `tenzir-ship`.

## Pre-release checks

Verify:

1. Git working tree is clean
2. CI is green on the release branch (typically `main`)
3. `uvx tenzir-ship validate` passes

Inspect the current state:

```sh
uvx tenzir-ship stats
```

If a project contains _modules_ with unreleased changes, first release each
module (without publishing) and then proceed with releasing the parent project.

## Gather release metadata

Read unreleased entries to understand all changes for this release.

### Draft introduction

The introduction summarizes the release in 2–3 sentences:

- Sentence 1 states the most impactful change that would make users want to
  upgrade
- Always write in active voice
- Only focus on user-facing impact

Read all unreleased entries and identify the single most impactful change that
would make users want to upgrade.

Severity matters more than category: a critical crash may outweigh a minor
feature, but a major new capability may outweigh a rare edge-case fix.

### Draft title

Derive the release title from the introduction.

Title rules:

- Plain text only
- Sentence case
- Descriptive noun phrase
- No Markdown formatting

## Create the release

Cut the release by running:

```sh
uvx tenzir-ship release create \
  --title "<title>" \
  --intro "<intro>" \
  --yes
```

This auto-bumps the version to the next version according to the set of
available changelog entries.

For a manual bump, pass `--patch`, `--minor`, or `--major`.

When a specific version is requested, pass an explicit version as position
argument, e.g., `create v1.2.3`.

Replace `--intro` with `--intro-file` if the introduction contains escape-worthy
characters.

## Publish the release

Publishing a release via `tenzir-ship` performs the following steps:

1. Commit the release artifacts
2. Create a (signed) git tag
3. Push to git remote
4. Create a release via the GitHub API

### Procedure

Inspect the current git changes and stage the exact set you want in the release
commit via `git add`. Then run:

```sh
uvx tenzir-ship release publish \
  --commit \
  --tag \
  --yes
```

Notes:

- The `--commit` flag commits whatever is staged
- The `--tag` option creates an annotated tag (that gets pushed automatically)
- Add `--draft` if the user requested a draft release
- Add `--prerelease` if the user requested marking the release as prerelease
- Add `--no-latest` if the user requested that the release must not be marked as latest
