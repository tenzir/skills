# 🛠️ Tenzir Skills

Skills for coding agents in the Tenzir ecosystem, built on the
[Agent Skills](https://agentskills.io) standard.

## 🗂️ Skills

### 🧬 Schemas

- `tenzir-asim`: Microsoft Sentinel ASIM reference — schemas, fields,
  aliases, entities, enums
- `tenzir-cim`: Splunk CIM reference — data models, datasets, fields,
  tags, constraints, lookups
- `tenzir-ocsf`: OCSF schema reference — event classes, objects, attributes,
  profiles, extensions
- `tenzir-udm`: Google SecOps UDM schema and normalization guidance —
  fields, event/entity types

### 🛡️ Tenzir Users

- `tenzir-docs`: Tenzir documentation — TQL, operators, functions, integrations,
  deployment
- `tenzir-manage-packages`: Package lifecycle routing for manifests, UDOs,
  pipelines, tests, and mappings

### 🏗️ Tenzir Contributors

- `tenzir-commit-changes`: Stage, split, and commit changes with clean messages
- `tenzir-create-pull-requests`: Open PRs, add changelog entries, cross-link docs
  PRs
- `tenzir-review-changes`: Code review with severity ratings and structured
  findings
- `tenzir-design-system`: Frontend design tokens, components, and brand assets
- `tenzir-ship`: Changelog entries, release notes, and GitHub releases
- `tenzir-update-docs`: Coordinate docs.tenzir.com updates alongside code changes
- `tenzir-technical-writing`: Technical documentation style following Google's
  developer docs guide

## 📦 Install

Install all skills into the current project:

```bash
npx skills add tenzir/skills
```

Or install globally:

```bash
npx skills add -g tenzir/skills
```

Install a specific skill into the current project, for example:

```bash
npx skills add tenzir/skills@tenzir-commit-changes
npx skills add tenzir/skills@tenzir-technical-writing
npx skills add tenzir/skills@tenzir-docs
npx skills add tenzir/skills@tenzir-asim
npx skills add tenzir/skills@tenzir-cim
npx skills add tenzir/skills@tenzir-ocsf
npx skills add tenzir/skills@tenzir-udm
```

## 📄 License

[Apache-2.0](LICENSE)
