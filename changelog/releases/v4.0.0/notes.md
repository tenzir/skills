This release ships the skills as Claude Code and Codex plugins and rebuilds the OCSF skill on structured YAML schema data from the official OCSF compiler. It also removes the developer and package management skills from the public collection.

## 💥 Breaking changes

### Removal of developer skills

The public `tenzir/skills` collection no longer includes the following developer workflow skills:

- `tenzir-commit-changes`
- `tenzir-create-pull-requests`
- `tenzir-design-system`
- `tenzir-ship`
- `tenzir-update-docs`
- `tenzir-technical-writing`

*By @mavam in #38.*

### Removal of the package management skill

The `tenzir-manage-packages` skill is no longer available. Use the `tenzir` skill for package documentation and implementation guidance.

*By @mavam in #35.*

## 🚀 Features

### Claude Code plugin support

These skills now install as a Claude Code plugin through the Tenzir marketplace, alongside the existing Codex plugin:

```
/plugin marketplace add tenzir/agent-plugins
/plugin install skills@tenzir
```

Installing with `npx skills` continues to work unchanged.

*By @mavam in #40.*

### Codex plugin support

Install the public Tenzir skills as one Codex plugin:

```sh
codex plugin marketplace add tenzir/agent-plugins
codex plugin add skills@tenzir
```

The plugin loads the canonical collection directly from `tenzir/skills`, so plugin updates do not require a second copy of the skills.

*By @mavam in #39.*

### OCSF release notes in the OCSF skill

The `tenzir-ocsf` skill now includes the upstream OCSF release notes for each schema version, so agents can answer what changed in a release beyond the added and removed classes, objects, and profiles.

Each version directory has a `changelog.md` with that release's section of the OCSF changelog, for example `v1.9.0/changelog.md`. The development snapshot carries the unreleased changes. Entries link to the upstream pull requests.

*By @zedoraps in #44.*

## 🔧 Changes

### Structured YAML schema data in the OCSF skill

The `tenzir-ocsf` skill now provides the OCSF schema as structured YAML instead of Markdown pages, so agents get exact, complete schema data for every class and object.

Each version directory contains indexes (`classes.yaml`, `objects.yaml`, `profiles.yaml`, `categories.yaml`, `types.yaml`, `attributes.yaml`, `version.yaml`) and one fully resolved file per class and object, for example `v1.9.0/classes/process_activity.yaml`. Each file lists every attribute, including inherited attributes, optional attributes, and attributes added by profiles, together with requirement levels, enum values, constraints, associations, observable type IDs, and deprecation details:

```yaml
attributes:
  actor:
    caption: Actor
    type: object_t
    object: actor
    requirement: required
    group: primary
```

Attributes are ordered by requirement level, numeric enum values use integer keys, and inherited attributes carry everything a mapping needs in a compact form, usually a single line, with the description left to the parent:

```yaml
  severity_id: {caption: Severity ID, type: integer_t, requirement: required, group: classification, sibling: severity, enum: {0: Unknown, 1: Informational, 2: Low, 3: Medium, 4: High, 5: Critical, 6: Fatal, 99: Other}, from: base_event}
```

The class index lists the activities of each class, and the skill now includes step-by-step guidance for mapping events to OCSF.

Objects now list the classes and objects that reference them, and the attribute dictionary lists where each attribute is used. Extension classes, objects, and patches of core items live under `{version}/extensions/{extension}/`. The OCSF introduction, FAQs, and articles moved to `docs/`.

*By @zedoraps in #43.*

## 🐞 Bug fixes

### Local skill marketplace loading

The local Tenzir skills marketplace now loads and installs as a single `skills` plugin in Codex and Claude Code. This fixes the missing `source` error and mismatched plugin names. Individual skills remain discoverable with `npx skills`.

*By @mavam in #41.*

### OCSF deprecation notices

The `tenzir-ocsf` skill now identifies deprecated OCSF classes, objects, profiles, attributes, and enum values, including the version and recommended replacement. For example, the OCSF 1.9.0 User Access Management page now directs users to the User Management class.

This helps agents avoid obsolete schema elements when answering OCSF questions.

*By @zedoraps in #37.*

### OCSF object constraints

The `tenzir-ocsf` skill now lists the attribute constraints of OCSF objects, not just those of event classes. For example, the Network Endpoint page now states that at least one of `ip`, `uid`, `name`, `hostname`, `svc_name`, `instance_uid`, `interface_uid`, `interface_name`, or `domain` must be set, and the Vulnerability page states that exactly one of `advisory`, `cve`, or `cwe` applies. Objects that inherit constraints from a parent object, such as Device from Endpoint, show the inherited rules.

This helps agents produce OCSF events that satisfy the schema's "at least one of" and "exactly one of" requirements on nested objects.

*By @zedoraps in #42.*

### OCSF schema parity with the official compiler

The `tenzir-ocsf` skill now matches the OCSF schema as the official OCSF tooling resolves it, so agents see the same requirements, enum values, and inherited attributes as the OCSF schema browser.

Previously, attributes that a class or object only partially redefined lost details from their parent. For example, Process Activity didn't mark `activity_id` and `actor` as required and omitted the `0` (Unknown) and `99` (Other) activity values, and Device listed only two of the device `type_id` values. Some required attributes, such as `time` and `activity_id` on Detection Finding, were missing entirely. For OCSF 1.0.0 through 1.3.0, classes missed most Base Event attributes, including `class_uid` and `time`.

Additional fixes:

- Objects list inherited attributes, applicable profiles, and the object's observable type ID. Profiles list the objects they apply to.
- Data types show observable type IDs, and the Observable object lists all observable `type_id` values.
- Classes show their class-specific `class_uid` value.
- Findings and Discovery are listed as base classes rather than event classes.
- Windows extension classes show their full class UID, for example `201001` for Registry Key Activity, and extension objects use their schema names, such as `reg_key`.

*By @zedoraps in #43.*
