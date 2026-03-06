# Repository Instructions

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
