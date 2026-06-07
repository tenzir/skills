# Tenzir Skills

This repository contains the shared Tenzir skill collection: reusable skills
for coding agents in and around the Tenzir ecosystem.

## Organization

The `skills/` tree mixes hand-maintained skills with generated ones, and the
surrounding metadata files keep the collection installable, discoverable, and
internally consistent.

We use `.claude-plugin/marketplace.json` to put the skills into different
groups. This is for `npx skills` to pick this up and _not_ a claude-only
mechanism. Every skill directory in `skills/` (that is, every directory
containing a `SKILL.md`) must be referenced exactly once in this file.

The following skills are produced by generator scripts or synced from another
repository and must not be edited by hand in this repository. Change the source
listed below instead, then regenerate or let the sync workflow update this repo.

- `skills/tenzir-google-udm/`: generated from
  `scripts/generate-google-udm-skill.py` and synced by
  `.github/workflows/sync-google-udm-skill.yaml`.
- `skills/tenzir-asim/`: generated from
  `scripts/generate-microsoft-asim-skill.py` and synced by
  `.github/workflows/sync-asim-skill.yaml`.
- `skills/tenzir-ocsf/`: generated from `scripts/generate-ocsf-skill.py` and
  synced by `.github/workflows/sync-ocsf-skill.yaml`.
- `skills/tenzir-docs/`: generated from
  `scripts/generate-tenzir-docs-skill.py` and synced by
  `.github/workflows/sync-docs-skill.yaml`.
- `skills/tenzir-ship/`: synced from `tenzir/ship:skills/tenzir-ship/` through
  `tenzir/ship:.github/workflows/sync-skills.yaml` via
  `.github/workflows/sync.yaml`.

Three places list skills and must stay consistent:

1. `skills/` directory — source of truth
2. `.claude-plugin/marketplace.json` — validated by CI
3. `README.md` skills table — update manually when adding or removing skills

### `tenzir-docs` page references in workflow skills

Workflow skills (e.g., `tenzir-manage-packages`) point to
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

## Skill authoring guidelines

Adhere to the following guidelines when creating content.

### Descriptions

Skill descriptions are the primary triggering mechanism. Write them to be
slightly "pushy": include both what the skill does and the natural phrases a
user might say when they need it. Descriptions should cover implicit triggers
(for example, a user saying "ship this" should trigger the pull request skill
even without the words "pull request").

Do not put tool invocations (specific CLI commands, flags, or API calls) into
SKILL.md bodies unless the skill is correcting a specific mistake the model
would otherwise make. Prefer explaining intent and letting the model choose the
best way to accomplish each step.

### Writing style

Use positive, action-oriented language when writing skill instructions. Focus on
what successful behavior looks like, what sequence to follow, and what evidence
marks the task complete. The space of possible mistakes is much larger than the
desired path, so describe the desired path instead of enumerating what to avoid.

### Cross-references

Skills that compose with other skills must declare the relationship explicitly:

1. **Metadata**: list hard dependencies under `metadata.requires.skills` in the
   SKILL.md frontmatter so that tooling can resolve the dependency graph. List
   conditional delegation targets under `metadata.uses.skills` with a concise
   `when` condition.
2. **Body**: mention the dependent or used skill by name at the point where
   delegation happens, so the model knows when and why to load it.

Keep cross-references minimal. Only declare `requires` when the skill cannot
perform its workflow without the other skill. Use `uses` when one skill's
workflow conditionally delegates a branch to another skill. Do not add a
relationship just because two skills cover related topics.

## Documentation

Keep the README as a concise reference.

The primary user-facing documentation with is at
https://docs.tenzir.com/guides/ai-workbench/use-agent-skills/.

## Validation

Install Lefthook once per clone:

```bash
uvx lefthook install
```

Pushing runs the pre-push quality gate automatically.
