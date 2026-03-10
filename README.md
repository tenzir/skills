# 🛠️ Tenzir Skills

Skills for coding agents in the Tenzir ecosystem, built on the
[Agent Skills](https://agentskills.io) standard.

## 📦 Install

### All skills

Install all skills into the current project:

```bash
npx skills add tenzir/skills
```

Or install globally:

```bash
npx skills add -g tenzir/skills
```

### Individual skill examples

Install a specific skill into the current project, for example:

```bash
npx skills add tenzir/skills@commit-changes
npx skills add tenzir/skills@technical-writing
npx skills add tenzir/skills@tenzir-docs
npx skills add tenzir/skills@ocsf
```

## Generated skills

`tenzir-docs` is generated from the structured Markdown bundle published by
[`tenzir/docs`](https://github.com/tenzir/docs/releases/tag/latest).

`ocsf` is generated directly from the upstream
[`ocsf-schema`](https://github.com/ocsf/ocsf-schema) and
[`ocsf-docs`](https://github.com/ocsf/ocsf-docs) repositories.

## 🧩 Dependencies

This repo uses a richer YAML frontmatter metadata structure to express skill
dependencies between sibling skills.

Use unrolled YAML arrays:

```yaml
---
name: create-pull-requests
description: Create and update pull requests for Tenzir projects.
metadata:
  requires:
    skills:
      - commit-changes
      - update-documentation
---
```

Notes:

- Use `metadata.requires.skills` for skill-to-skill dependencies.
- Write the dependency list as YAML bullets, not inline bracket syntax.
- Dependency names must match the sibling skill `name` fields exactly.
- Keep dependent skills self-contained; use dependency metadata to express
  relationships instead of copying sibling workflow instructions inline.

## 📄 License

[Apache-2.0](LICENSE)
