# 🛠️ Tenzir Skills

Skills for coding agents in the Tenzir ecosystem, built on the
[Agent Skills](https://agentskills.io) standard.

## 🗂️ Skills

### 🛡️ Tenzir Users

| Skill                          | Description                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------- |
| `tenzir-docs`                  | Tenzir documentation — TQL, operators, functions, integrations, deployment       |
| `tenzir-google-udm`            | Google SecOps UDM schema and normalization guidance — fields, event/entity types |
| `tenzir-ocsf`                  | OCSF schema reference — event classes, objects, attributes, profiles, extensions |
| `tenzir-create-package`        | Create library-quality Tenzir packages with UDOs, tests, examples, and pipelines |

### 🏗️ Tenzir Contributors

| Skill                              | Description                                                           |
| ---------------------------------- | --------------------------------------------------------------------- |
| `tenzir-commit-changes`            | Stage, split, and commit changes with clean messages                  |
| `tenzir-create-pull-requests`      | Open PRs, add changelog entries, cross-link docs PRs                  |
| `tenzir-review-changes`            | Code review with severity ratings and structured findings             |
| `tenzir-design-system`             | Frontend design tokens, components, and brand assets                  |
| `tenzir-ship`                      | Changelog entries, release notes, and GitHub releases                 |
| `tenzir-update-docs`               | Coordinate docs.tenzir.com updates alongside code changes             |
| `tenzir-technical-writing`         | Technical documentation style following Google's developer docs guide |

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
npx skills add tenzir/skills@tenzir-commit-changes
npx skills add tenzir/skills@tenzir-technical-writing
npx skills add tenzir/skills@tenzir-docs
npx skills add tenzir/skills@tenzir-google-udm
npx skills add tenzir/skills@tenzir-ocsf
```

## Generated skills

`tenzir-docs` is generated from the structured Markdown bundle published by
[`tenzir/docs`](https://github.com/tenzir/docs/releases/tag/latest).

`tenzir-ocsf` is generated directly from the upstream
[`ocsf-schema`](https://github.com/ocsf/ocsf-schema) and
[`ocsf-docs`](https://github.com/ocsf/ocsf-docs) repositories.

`tenzir-google-udm` is generated from the upstream
[`googleapis/googleapis`](https://github.com/googleapis/googleapis) UDM and
Entity protocol buffers plus targeted Google SecOps documentation guidance for
field population, required fields, field-path prefixes, datatypes, and examples.

## 🧩 Dependencies

This repo uses a richer YAML frontmatter metadata structure to express skill
dependencies between sibling skills.

Use unrolled YAML arrays:

```yaml
---
name: tenzir-create-pull-requests
description: Create and update pull requests for Tenzir projects.
metadata:
  requires:
    skills:
      - tenzir-commit-changes
      - tenzir-update-docs
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
