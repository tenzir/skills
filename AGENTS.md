# Tenzir Skills

This repository contains reusable, user-facing skills for coding agents in the
Tenzir ecosystem.

## Organization

The `skills/` tree mixes hand-maintained skills with generated ones, and the
surrounding metadata files keep the collection installable, discoverable, and
internally consistent.

We use `.claude-plugin/marketplace.json` to put the skills into different
groups. This is for `npx skills` to pick this up and _not_ a claude-only
mechanism. Every skill directory in `skills/` must be referenced exactly once in
this file.

The following skills are generated or synced from another repository and must
not be edited by hand here:

- `skills/tenzir-asim/`
- `skills/tenzir-cef/`
- `skills/tenzir-cim/`
- `skills/tenzir-ecs/`
- `skills/tenzir-edm/`
- `skills/tenzir/`
- `skills/tenzir-leef/`
- `skills/tenzir-ocsf/`
- `skills/tenzir-udm/`

## Skill authoring guidelines

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
https://tenzir.com/docs/guides/ai-workbench/use-agent-skills/.

## Validation

Install Lefthook once per clone:

```bash
uvx lefthook install
```

Pushing runs the pre-push quality gate automatically.
