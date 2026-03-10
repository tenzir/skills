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
