# 🛠️ Tenzir Skills

Skills for coding agents in the Tenzir ecosystem, built on the
[Agent Skills](https://agentskills.io) standard.

## 🗂️ Skills

### 🛡️ Tenzir Users

- `tenzir`: Tenzir documentation — TQL, operators, functions, integrations,
  deployment — plus entry points to the changelog, blog, and product pages
- `tenzir-manage-packages`: Package lifecycle routing for manifests, UDOs,
  pipelines, tests, and mappings

### 🧬 Schemas

- `tenzir-asim`: Microsoft Sentinel ASIM reference — schemas, fields,
  aliases, entities, enums
- `tenzir-cef`: ArcSight CEF reference — headers, extension dictionary,
  ESM event schema, timestamps
- `tenzir-cim`: Splunk CIM reference — data models, datasets, fields,
  tags, constraints, lookups
- `tenzir-ecs`: Elastic Common Schema reference — fields, fieldsets,
  categorization, mapping guidance
- `tenzir-edm`: FortiSIEM Event Data Model reference — data models,
  event attributes, types, display names
- `tenzir-leef`: IBM QRadar LEEF reference — headers, delimiters, predefined
  event attributes, timestamps
- `tenzir-ocsf`: OCSF schema reference — event classes, objects, attributes,
  profiles, extensions
- `tenzir-udm`: Google SecOps UDM schema and normalization guidance —
  fields, event/entity types

### 🏗️ Tenzir Contributors

- `tenzir-commit-changes`: Stage, split, and commit changes with clean messages
- `tenzir-create-pull-requests`: Open PRs, add changelog entries, cross-link docs
  PRs
- `tenzir-design-system`: Brand tokens, design principles and invariants, and
  logos for web UIs, documents, slides, and diagrams
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
npx skills add tenzir/skills@tenzir
npx skills add tenzir/skills@tenzir-asim
npx skills add tenzir/skills@tenzir-cef
npx skills add tenzir/skills@tenzir-cim
npx skills add tenzir/skills@tenzir-ecs
npx skills add tenzir/skills@tenzir-edm
npx skills add tenzir/skills@tenzir-leef
npx skills add tenzir/skills@tenzir-ocsf
npx skills add tenzir/skills@tenzir-udm
```

## 📄 License

[Apache-2.0](LICENSE)
