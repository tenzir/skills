# Trigger a remote release

Before triggering the workflow, verify release preconditions locally:

1. Ensure the current branch is `main`.
2. Ensure local `main` and `origin/main` are in sync (no ahead/behind commits).

If either check fails, abort.

## Locate GitHub Actions workflow

Find the workflow file that triggers releases in this repository. Look for a
`workflow_dispatch` workflow under `.github/workflows/` whose job calls
`tenzir/ship/.github/workflows/release.yaml` or whose name/filename suggests
it is the release entrypoint (common names: `release.yaml`,
`trigger-release.yaml`, `publish.yaml`).

```sh
grep -rl "workflow_dispatch" .github/workflows/ | xargs grep -l "release" 2>/dev/null
```

Use the discovered filename for all `gh workflow run` invocations below. If
more than one candidate matches, prefer the one that explicitly delegates to
`tenzir/ship/.github/workflows/release.yaml`.

## Determine release inputs

Inspect the workflow to understand its shape. The release workflow in this
repository accepts these common inputs:

- **intro**: Summarize unreleased entries in `changelog/unreleased/` into 1–2
  sentences describing the release highlights.
- **title**: Identify the lead topic—the single most important change from a
  user's perspective.
- **bump**: Optional manual bump for a stable release (`patch`, `minor`, or
  `major`). Leave this unset or use `auto` unless the user explicitly requests
  a manual bump.
- **version**: Optional explicit stable version. During an active RC phase,
  use this only to leave the RC cycle and ship a different stable release
  target.
- **rc**: Optional boolean that creates or continues the release-candidate
  series for the resolved stable version.

If you encounter other inputs, make reasonable choices and inform the user.

## Trigger the workflow

Pick the invocation that matches the requested workflow. Replace
`<workflow-file>` with the filename discovered above.

### Stable release with auto-inferred bump

```sh
gh workflow run <workflow-file> \
  -f intro="<intro text>" \
  -f title="<title>"
```

Do not specify a version bump unless explicitly requested. The workflow will
pick the appropriate bump according to the changelog entry types. For a project
whose latest stable release is `0.x`, a breaking entry triggers a minor bump and
automatic inference never selects `1.0.0`. Use `bump=major` or an explicit
`version=1.0.0` when the user chooses to declare the first stable release.
Starting with `1.0.0`, breaking entries trigger major bumps. If an outstanding
release candidate exists, this same version-less invocation
promotes the latest RC to its matching stable release automatically. This is
the only promotion path for the active RC. Promotion is cumulative: entries
added to the unreleased queue after the last candidate snapshot are folded
into the stable release and consumed from the queue.

### Stable release with manual bump

```sh
gh workflow run <workflow-file> \
  -f intro="<intro text>" \
  -f title="<title>" \
  -f bump=<patch|minor|major>
```

### Release candidate

```sh
gh workflow run <workflow-file> \
  -f intro="<intro text>" \
  -f title="<title>" \
  -f rc=true
```

To override the inferred stable base for the RC, prefer a manual bump such as
`-f rc=true -f bump=minor`. Pass a stable `version` only when the user needs an
exact base version.

Once an RC series exists, the workflow has three outcomes only:

- Trigger another RC with `-f rc=true` to continue the same RC series.
- Trigger the normal stable workflow without `rc`, `bump`, or `version` to
  promote the latest candidate.
- Use `bump` or an explicit later stable `version` only when the user wants to
  leave the RC cycle and ship a different stable release instead.

Reject an explicit stable `version` that matches the active RC base.

## Monitor the run

Wait briefly for the run to register, find its ID, then watch it.

Verify:

- If the run succeeds, report the GitHub release URL.
- A project whose workflow passes `create-github-release: false` to the
  reusable workflow stops after pushing the tag, so no release exists to link.
  Report the tag and the run URL instead of treating the missing release as a
  failure.
- If it fails, report the run URL so the user can inspect the logs.
