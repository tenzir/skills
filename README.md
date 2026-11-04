# 🛠️ Tenzir Skills

Skills for coding agents in the Tenzir ecosystem, built on the
[Agent Skills](https://agentskills.io) standard.

## 🗂️ Skills

### 🛡️ Tenzir Users

- `tenzir`: Tenzir documentation of the latest release — TQL, operators,
  functions, integrations, deployment — plus entry points to the changelog,
  blog, and product pages

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

## 📦 Install

### As a plugin

Add the Tenzir marketplace and install `skills@tenzir`.

Codex:

```bash
codex plugin marketplace add tenzir/agent-plugins
codex plugin add skills@tenzir
```

Claude Code:

```
/plugin marketplace add tenzir/agent-plugins
/plugin install skills@tenzir
```

### With `npx skills`

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

### Tenzir 7 preview

The `tenzir-7` branch carries the `tenzir` skill built from the Tenzir 7
documentation, which is not released yet. It syncs nightly. Install it in
place of the `tenzir` skill:

```bash
npx skills add https://github.com/tenzir/skills/tree/tenzir-7/skills/tenzir
```

To keep both side by side, install it under its own name with
[skeel](https://github.com/mavam/skeel):

```bash
skeel add tenzir/skills tenzir@tenzir-7 --name tenzir-7 --apply
```

## 📄 License

[Apache-2.0](LICENSE)
