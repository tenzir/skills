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

### Stable release from the current queue

Cut a stable release by running:

```sh
uvx tenzir-ship release create \
  --title "<title>" \
  --intro "<intro>" \
  --yes
```

This auto-bumps the version to the next version according to the set of
available changelog entries. Auto-bumping is the best default and should always
be used unless the user explicitly asks for something different.

If the latest release is an outstanding release candidate, this same
version-less command promotes that latest RC to its matching stable release
automatically. This is the only promotion path after `release create --rc`.
Do not pass a stable version or bump flag when you mean to promote the RC.

For a manual bump, pass `--patch`, `--minor`, or `--major`. Only use this when
the automatic detection is not the right fit for the release, e.g., when a minor
feature should yield a patch instead of a minor release, or when a breaking
change only affects an internal API and a major bump would be misleading.

Only when the user explicitly provides a specific version, pass it as positional
argument. This is a rare override, for example to re-cut a release that was
tagged but failed to publish, or to align with an externally dictated version
number. During an active RC phase, only use an explicit version when it points
at a different stable release target such as `v1.2.4`, `v1.3.0`, or `v2.0.0`.
An explicit version matching the active RC base is not a promotion path and
must be rejected.

### Release candidate workflow

Create or continue a release candidate by passing `--rc`:

```sh
uvx tenzir-ship release create --rc \
  --title "<title>" \
  --intro "<intro>" \
  --yes
```

Release candidates snapshot the current unreleased queue without consuming it,
so you can iterate on `-rc.N` releases before shipping the stable release.
The stable base is inferred from the unreleased entry types; when the matching
RC series already exists, `release create --rc` increments the `-rc.N` counter.

When you are ready to ship the stable release, run the normal stable command
again without `--rc`:

```sh
uvx tenzir-ship release create \
  --title "<title>" \
  --intro "<intro>" \
  --yes
```

If an outstanding RC exists, this promotes the latest candidate to its matching
stable release automatically.

To override the inferred base, prefer a manual bump flag, for example
`release create --rc --minor`. Pass a stable version only when the user needs
an exact base version.

Once an RC series exists, the workflow has three outcomes only:

- Use `--rc` to cut another candidate in the same RC series.
- Use the stable command without a version or bump flag to promote the latest
  candidate.
- Use a manual bump or an explicit later stable version only when the user
  wants to leave the RC cycle and ship a different stable release instead.

Reject an explicit stable version that matches the active RC base.

Replace `--intro` with `--intro-file` if the introduction contains escape-worthy
characters.

## Publish the release

Publishing a release via `tenzir-ship` performs the following steps:

1. Commit the release artifacts
2. Create a (signed) git tag
3. Push to git remote
4. Create a release via the GitHub API

### Procedure

Inspect the current git changes and stage the exact set you want in the release commit via `git add`. Then run:

```sh
uvx tenzir-ship release publish \
  --commit \
  --tag \
  --yes
```

Notes:

- The `--commit` flag commits whatever is staged
- The `--tag` option creates an annotated tag (that gets pushed automatically)
- Without an explicit version, `release publish` targets the latest release,
  so the same command works for both stable releases and RCs.
- Add `--draft` if the user requested a draft release.
- `release publish` automatically treats `vX.Y.Z-rc.N` releases as GitHub
  prereleases and prevents them from being marked as latest.
- Add `--prerelease` only when the user explicitly wants to mark a stable
  version as prerelease.
- Add `--no-latest` if the user requested that a stable release must not be
  marked as latest.

After `release publish` completes, **stop**. Do not publish to package registries (npm, PyPI, etc.) manually, CI typically handles this automatically when the tag is pushed.
