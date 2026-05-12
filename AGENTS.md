# Repository Instructions

This repository contains the shared Tenzir skill collection: reusable skills
for coding agents in and around the Tenzir ecosystem. The `skills/` tree mixes
hand-maintained skills with generated ones, and the surrounding metadata files
keep the collection installable, discoverable, and internally consistent.

## Generated and synced skills

The following skills are produced by generator scripts or synced from another
repository and must not be edited by hand in this repository. Change the source
listed below instead, then regenerate or let the sync workflow update this repo.

| Skill                 | Source of truth                         | Sync mechanism                                                                     |
| --------------------- | --------------------------------------- | ---------------------------------------------------------------------------------- |
| `skills/tenzir-ocsf/` | `scripts/generate-ocsf-skill.py`        | `.github/workflows/sync-ocsf-skill.yaml`                                           |
| `skills/tenzir-docs/` | `scripts/generate-tenzir-docs-skill.py` | `.github/workflows/sync-docs-skill.yaml`                                           |
| `skills/tenzir-ship/` | `tenzir/ship:skills/tenzir-ship/`       | `tenzir/ship:.github/workflows/sync-skills.yaml` via `.github/workflows/sync.yaml` |

## Organization

We use `.claude-plugin/marketplace.json` to put the skills into different groups. This is for `npx skills` to pick this up and _not_ a claude-only mechanism. Every skill directory in `skills/` (that is, every directory containing a `SKILL.md`) must be referenced exactly once in this file.

## Skill cross-references

Skills that compose with other skills must declare the dependency explicitly:

1. **Metadata**: list required skills under `metadata.requires.skills` in the
   SKILL.md frontmatter so that tooling can resolve the dependency graph.
2. **Body**: mention the dependent skill by name at the point where delegation
   happens, so the model knows when and why to load it.

Keep cross-references minimal — only declare a dependency when one skill's
workflow actively delegates a step to another skill. Do not add a dependency
just because two skills cover related topics.

### `tenzir-docs` page references in workflow skills

Workflow skills (e.g., `tenzir-create-parser-package`, `tenzir-create-ocsf-mapping`) point to
`tenzir-docs` pages by relative path (e.g., `guides/packages/create-a-package.md`)
instead of duplicating documentation content. These paths must stay in sync with
the generated `tenzir-docs` skill tree:

- After regenerating `tenzir-docs`, verify that every path referenced in a
  workflow skill still resolves to a file under `skills/tenzir-docs/`.
- When renaming or removing a `tenzir-docs` page, search workflow skills for
  the old path and update it.
- Never copy guide or tutorial content into a workflow skill. The skill provides
  the workflow structure (steps, results, ordering); `tenzir-docs` provides the
  domain knowledge.

## Skill descriptions

Skill descriptions are the primary triggering mechanism. Write them to be
slightly "pushy": include both what the skill does and the natural phrases a
user might say when they need it. Descriptions should cover implicit triggers
(for example, a user saying "ship this" should trigger the pull request skill
even without the words "pull request").

Do not put tool invocations (specific CLI commands, flags, or API calls) into
SKILL.md bodies unless the skill is correcting a specific mistake the model
would otherwise make. Prefer explaining intent and letting the model choose the
best way to accomplish each step.

## Skill writing style

Use positive, action-oriented language when writing skill instructions. Focus on
what successful behavior looks like, what sequence to follow, and what evidence
marks the task complete. The space of possible mistakes is much larger than the
desired path, so describe the desired path instead of enumerating what to avoid.

## Keeping things in sync

Three places list skills and must stay consistent:

1. `skills/` directory — source of truth
2. `.claude-plugin/marketplace.json` — validated by CI
3. `README.md` skills table — update manually when adding or removing skills

## Validation

Run the shared Lefthook quality gate before pushing or after changing anything
under `skills/`, `.github/workflows/`, `.claude-plugin/`, `changelog/`, or the
hook configuration:

```bash
uvx --from lefthook==2.1.6 lefthook run pre-push --all-files
```

The gate runs `scripts/validate-skills --marketplace`, which verifies every
local skill with `skills-ref` and checks that `.claude-plugin/marketplace.json`
lists each skill exactly once. It also validates `changelog/` with
`tenzir-ship`.

Install the same hook locally with:

```bash
uvx --from lefthook==2.1.6 lefthook install
```

The same Lefthook gate runs in `.github/workflows/checks.yaml` for pull requests
that touch the skill tree, workflow, changelog, or hook setup, and on every push
to `main`.
