# Repository Instructions

## Auto-generated skills

The following skills are produced by generator scripts and must not be
edited by hand. Change the corresponding script instead, then regenerate.

| Skill | Generator |
| --- | --- |
| `skills/ocsf/` | `scripts/generate-ocsf-skill.py` |
| `skills/tenzir-docs/` | `scripts/generate-tenzir-docs-skill.py` |

## Validation

Run `skills-ref` across every local skill after changing anything under
`skills/`:

```bash
for skill in $(find skills -name SKILL.md -print | sed 's#/SKILL.md$##'); do
  uvx skills-ref validate "$skill"
done
```

The same validation runs in `.github/workflows/skills-ref.yml`
for pull requests that touch the skill tree or the workflow itself.
