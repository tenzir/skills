# Initialize a changelog project

Set up a new changelog workspace before the first entry exists.

## When to use this workflow

Prefer `tenzir-ship init` when the task is to scaffold the changelog project
itself rather than immediately add an entry.

Use it when:

- no changelog workspace exists yet
- you want to create `changelog/` and `config.yaml` interactively
- you want a non-interactive setup step in automation
- the repository uses `package.yaml` and should initialize in package mode

## Initialize the workspace

### Interactive standalone setup

```sh
uvx tenzir-ship init
```

This creates `changelog/config.yaml` and `changelog/unreleased/`.

### Non-interactive standalone setup

```sh
uvx tenzir-ship init --yes --id <project-id>
```

You may also pass optional metadata such as `--name`, `--description`, and
`--repository`.

### Package mode

```sh
uvx tenzir-ship init --package
```

Package mode reuses metadata from `package.yaml` and creates the changelog
workspace without writing an extra `config.yaml`.

## Notes

- `tenzir-ship add` can still bootstrap a missing changelog on first use.
- Prefer `init` when you want setup without creating an entry yet.
- `init` refuses to overwrite existing changelog projects.
- Pass `--root <path/to/changelog>` when initializing a non-default location.
