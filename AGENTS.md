# Tenzir Skills

This repository contains reusable, user-facing skills for coding agents in the
Tenzir ecosystem.

## Organization

The `skills/` tree mixes hand-maintained skills with generated ones, and the
surrounding metadata files keep the collection installable, discoverable, and
internally consistent.

Three manifests describe this collection, each for a different consumer:

- `.claude-plugin/marketplace.json` groups the skills for `npx skills` to pick
  up. Despite the directory it sits in, it follows the
  [Agent Skills](https://agentskills.io) schema and is _not_ a Claude Code
  marketplace. Every skill directory in `skills/` (that is, every directory
  containing a `SKILL.md`) must be referenced exactly once in this file.
- `.codex-plugin/plugin.json` is the Codex plugin manifest.
- `.claude-plugin/plugin.json` is the Claude Code plugin manifest.

Both `plugin.json` files expose the `skills/` tree wholesale as the `skills`
plugin of the `tenzir` marketplace in
[tenzir/agent-plugins](https://github.com/tenzir/agent-plugins). Keep their
`version` fields in sync with each other.

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

Three places list skills and must stay consistent:

1. `skills/` directory — source of truth
2. `.claude-plugin/marketplace.json` — validated by CI
3. `README.md` skills table — update manually when adding or removing skills

The two `plugin.json` files need no update, because they expose the `skills/`
tree wholesale.

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
