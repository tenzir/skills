# Trigger a remote release

Before triggering the workflow, verify release preconditions locally:

1. Ensure the current branch is `main`.
2. Ensure local `main` and `origin/main` are in sync (no ahead/behind commits).

If either check fails, abort.

## Locate GitHub Actions workflow

Identify the CI release workflow file, e.g., `.github/workflows/release.yaml`.

## Determine release inputs

Inspect the workflow to understand its shape. Typical release inputs are:

- **intro**: Summarize unreleased entries in `changelog/unreleased/` into 1–2
  sentences describing the release highlights.
- **title**: Identify the lead topic—the single most important change from a
  user's perspective.

If you encounter other inputs, make reasonable choices and inform the user.

## Trigger the workflow

Run the workflow via `gh`:

```sh
gh workflow run release.yaml \
  -f intro="<intro text>" \
  -f title="<title>" \
  [-f bump=<patch|minor|major>]
```

Do not specify a version bump unless explicitly requested. The workflow will
pick the appropriate bump according to the changelog entry types.

## Monitor the run

Wait briefly for the run to register, find its ID, then watch it.

Verify:

- If the run succeeds, report the GitHub release URL.
- If it fails, report the run URL so the user can inspect the logs.
