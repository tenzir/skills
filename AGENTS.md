# Repository Instructions

This repository contains the shared Tenzir skill collection: reusable skills
for coding agents in and around the Tenzir ecosystem. The `skills/` tree mixes
hand-maintained skills with generated ones, and the surrounding metadata files
keep the collection installable, discoverable, and internally consistent.

## Auto-generated skills

The following skills are produced by generator scripts and must not be
edited by hand. Change the corresponding script instead, then regenerate.

| Skill                 | Generator                               |
| --------------------- | --------------------------------------- |
| `skills/ocsf/`        | `scripts/generate-ocsf-skill.py`        |
| `skills/tenzir-docs/` | `scripts/generate-tenzir-docs-skill.py` |

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

## Keeping things in sync

Three places list skills and must stay consistent:

1. `skills/` directory — source of truth
2. `.claude-plugin/marketplace.json` — validated by CI
3. `README.md` skills table — update manually when adding or removing skills

## Validation

Run `skills-ref` across every local skill after changing anything under
`skills/`, and verify that `.claude-plugin/marketplace.json` lists each
skill exactly once:

```bash
for skill in $(find skills -name SKILL.md -print | sed 's#/SKILL.md$##'); do
  uvx skills-ref validate "$skill"
done

local_skills=$(mktemp)
marketplace_skills=$(mktemp)

find skills -name SKILL.md -print | sed 's#/SKILL.md$##' | sort | sed 's#^#./#' > "$local_skills"
jq -r '.plugins[].skills[]' .claude-plugin/marketplace.json | sort > "$marketplace_skills"

duplicates=$(uniq -d < "$marketplace_skills")
if [[ -n "${duplicates}" ]]; then
  echo "Duplicate skills in marketplace.json:"
  echo "${duplicates}"
  exit 1
fi

if ! cmp -s "$local_skills" "$marketplace_skills"; then
  echo "Mismatch between skills/ and marketplace.json:"
  diff -u "$local_skills" "$marketplace_skills" || true
  exit 1
fi
```

The same validation runs in `.github/workflows/skills-ref.yml`
for pull requests that touch the skill tree or the workflow itself, and on every push to `main`, along with a check that ensures all skills are listed exactly once in the marketplace JSON.
