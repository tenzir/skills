---
name: tenzir-ocsf
description: Answer questions about OCSF (Open Cybersecurity Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.
---

# OCSF

Answer OCSF questions and make OCSF mapping decisions from the files in this
skill. The YAML schema files are authoritative for names, types, requirements,
enum values, and constraints. The Markdown docs under `docs/` explain concepts
and mapping practice; they are not versioned, so the YAML wins when they
disagree. State only facts from files you read, and say when the
files do not cover a question.

## Versions

Use v1.9.0, the latest stable version, unless the user asks for another one. Stay
within one version per answer.

Available: v1.0.0 through v1.9.0 and v1.10.0-dev (unreleased).

Paths below use `v1.9.0/`; swap in the version you need.

## Data files

All paths are relative to this skill's directory. Run searches from there.

| File | Contents |
| --- | --- |
| `v1.9.0/version.yaml` | Status, source commit, extensions, and changes since the previous version |
| `v1.9.0/changelog.md` | Upstream release notes: added, improved, deprecated, and fixed items with PR links |
| `v1.9.0/categories.yaml` | Categories with UID and classes |
| `v1.9.0/classes.yaml` | Class index: UID, category, summary, `activities`, path |
| `v1.9.0/classes/{name}.yaml` | One class, fully resolved |
| `v1.9.0/objects.yaml` | Object index: group, summary, path |
| `v1.9.0/objects/{name}.yaml` | One object, fully resolved |
| `v1.9.0/profiles.yaml` | Profiles with their attributes and `applies_to` |
| `v1.9.0/attributes.yaml` | Attribute dictionary with `used_by` |
| `v1.9.0/types.yaml` | Data types with base type, constraints, and observable type ID |
| `v1.9.0/extensions/{ext}/{classes,objects}/{name}.yaml` | Extension classes and objects, and patches of core items |

Names resolve within the same version: `object: actor` →
`objects/actor.yaml`; `object: win/reg_key` →
`extensions/win/objects/reg_key.yaml`; `extends` → the parent class or object
file; `type`, `profile`, and `category` → the key in `types.yaml`,
`profiles.yaml`, or `categories.yaml`; `patched_by: [linux]` →
`extensions/linux/{classes,objects}/{same name}.yaml`.

Searches that avoid opening many files:

- Find a class: `grep -n -i "keyword" v1.9.0/classes.yaml`
- Find an attribute and where it is used: `grep -n -A 12 "^src_endpoint:" v1.9.0/attributes.yaml`
- Jump to an attribute in a class: `grep -n -A 20 "^  actor:" v1.9.0/classes/process_activity.yaml`
- Find what holds an object: `referenced_by` in `v1.9.0/objects/{name}.yaml`

## Reading class and object files

`attributes` lists every attribute, including inherited and profile
attributes, ordered required, recommended, then optional. Attributes that
`patched_by` extensions add live only in the extension patch files; an item
without `patched_by` has no patches.

Attributes with `from` but no description are inherited unchanged; the
description is in the file that `from` names. They take one line, except that
enums with more than 12 values list their captions on the lines below, so
grep with `-A`:

```yaml
severity_id: {caption: Severity ID, type: integer_t, requirement: required, group: classification, sibling: severity, enum: {0: Unknown, 1: Informational, 2: Low, 3: Medium, 4: High, 5: Critical, 6: Fatal, 99: Other}, from: base_event}
```

Fields that need explanation:

- `uid`, `category_uid`: the class's `class_uid` and `category_uid` values.
- `abstract: true`: a parent that events never use directly.
- `profile` / `profiles` on an attribute: the attribute and its
  `requirement` apply only when that profile is applied.
- `sibling`: the string attribute that takes the enum caption, e.g.
  `activity_name` for `activity_id`.
- `enum`: keys mapped to captions, or to `caption` and `description`. Keys are
  integers, except for string-typed attributes such as `tlp`.
- `observable`: the observable `type_id` of the attribute or object.
- `constraints`: the complete, resolved constraints, inherited ones included:
  `at_least_one` (one or more listed attributes set) or `just_one` (exactly
  one set).
- `associations`: attributes that describe the same entity.
- `referenced_by` (objects): classes and objects that hold this object, with
  the attribute names.
- `extension`, `patches`: the defining extension and, for a patch, the core
  item it extends. A patch lists only what it adds or changes.
- `deprecated`, `supersedes`: deprecation details and the items this one
  replaces.

## Mapping events

Make the schema decisions in this order:

1. Pick the class by its category and the `activities` in `classes.yaml`;
   read the candidate class files and compare them. `activities` omits `0`
   (Unknown) and `99` (Other), which every class allows.
2. Set `class_uid`, `category_uid`, `activity_id`, `type_uid`
   (`class_uid * 100 + activity_id`), `severity_id`, `time`,
   `metadata.version`, and `metadata.product`.
3. Apply the profiles the source supports: list them in `metadata.profiles`
   and fill the attributes they add.
4. Fill required attributes, then recommended ones. A nested object's own
   requirement levels apply once you set it. Satisfy `constraints`. When the
   source lacks a value for a required `_id` attribute, use `0` (Unknown).
5. For an `_id` attribute set to `99` (Other), set its `sibling` to the source
   value.
6. Keep source fields without an OCSF target in `unmapped`.

## Docs

| Topic | Start here |
| --- | --- |
| Framework concepts and design | [Introduction](docs/introduction.md), [FAQs](docs/faqs.md) |
| Profiles | [Profiles](docs/introduction/profiles.md), then `profiles.yaml` |
| Extending the schema | [Extensions](docs/introduction/extensions.md), [Patching the Core Schema](docs/articles/patching-core-using-extensions.md) |
| Observables, alerts, process parentage | [Articles](docs/articles.md) |
| Changes between versions | `changelog.md` of the newer version, `changes` in `version.yaml`, then diff the item files |
