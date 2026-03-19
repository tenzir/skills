# Trigger a remote release

Before triggering the workflow, verify release preconditions locally:

1. Ensure the current branch is `main`.
2. Ensure local `main` and `origin/main` are in sync (no ahead/behind commits).

If either check fails, abort.

## Locate GitHub Actions workflow

Identify the CI release workflow file, e.g., `.github/workflows/release.yaml`.

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
- **version**: Optional explicit stable version, used for exact overrides or
  when promoting a specific stable release.
- **rc**: Optional boolean that creates or continues the release-candidate
  series for the resolved stable version.

If you encounter other inputs, make reasonable choices and inform the user.

## Trigger the workflow

Pick the invocation that matches the requested workflow.

### Stable release with auto-inferred bump

```sh
gh workflow run release.yaml \
  -f intro="<intro text>" \
  -f title="<title>"
```

Do not specify a version bump unless explicitly requested. The workflow will
pick the appropriate bump according to the changelog entry types. If an
outstanding release candidate exists, this same invocation promotes the latest
RC to its matching stable release automatically.

### Stable release with manual bump

```sh
gh workflow run release.yaml \
  -f intro="<intro text>" \
  -f title="<title>" \
  -f bump=<patch|minor|major>
```

### Release candidate

```sh
gh workflow run release.yaml \
  -f intro="<intro text>" \
  -f title="<title>" \
  -f rc=true
```

To override the inferred stable base for the RC, prefer a manual bump such as
`-f rc=true -f bump=minor`. Pass a stable `version` only when the user needs an
exact base version.

Once an RC series exists, keep the workflow on that series: trigger another RC
with `-f rc=true`, or trigger the normal stable workflow without `rc` to
promote the latest candidate. Do not try to bypass the RC snapshot with an
explicit stable version or a manual bump.

## Monitor the run

Wait briefly for the run to register, find its ID, then watch it.

Verify:

- If the run succeeds, report the GitHub release URL.
- If it fails, report the run URL so the user can inspect the logs.
