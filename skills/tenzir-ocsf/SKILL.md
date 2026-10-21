---
name: tenzir-ocsf
description: Answer questions about OCSF (Open Cybersecurity Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.
metadata:
  uses:
    skills:
      - name: tenzir
        when: writing TQL that maps events to OCSF
---

# OCSF

Answer OCSF questions from the YAML schema files in this skill. They are
generated with the official OCSF schema compiler and are the authoritative
reference for names, types, requirements, enum values, constraints, profiles,
and observables. Use the Markdown docs under `docs/` for concepts and mapping
guidance. State only facts from files you read. If something is not in the
files, say that this skill does not document it.

## Versions

Use the latest stable version unless the user requests a specific one. Stick to
one version per answer.

- [1.0.0](v1.0.0/version.yaml)
- [1.1.0](v1.1.0/version.yaml)
- [1.2.0](v1.2.0/version.yaml)
- [1.3.0](v1.3.0/version.yaml)
- [1.4.0](v1.4.0/version.yaml)
- [1.5.0](v1.5.0/version.yaml)
- [1.6.0](v1.6.0/version.yaml)
- [1.7.0](v1.7.0/version.yaml)
- [1.8.0](v1.8.0/version.yaml)
- **[1.9.0](v1.9.0/version.yaml)** ← latest stable
- [1.10.0-dev](v1.10.0-dev/version.yaml) ← unreleased development snapshot

## Data files

Each version directory contains the same files:

| File | Contents |
| --- | --- |
| `{version}/version.yaml` | Status, source commit, extensions with their classes, objects, profiles, and patches, and changes since the previous version |
| `{version}/categories.yaml` | Categories with UID, description, and classes |
| `{version}/classes.yaml` | Index of all classes: name, caption, UID, category, summary, path |
| `{version}/classes/{name}.yaml` | One class, fully resolved |
| `{version}/objects.yaml` | Index of all objects: name, caption, group, summary, path |
| `{version}/objects/{name}.yaml` | One object, fully resolved |
| `{version}/profiles.yaml` | All profiles with their attributes and the classes and objects they apply to |
| `{version}/attributes.yaml` | Attribute dictionary: type, description, and the classes and objects that use each attribute |
| `{version}/types.yaml` | Data types: base type, length, range, regex, and observable type ID |
| `{version}/extensions/{extension}/classes/{name}.yaml` | Extension classes and patches of core classes |
| `{version}/extensions/{extension}/objects/{name}.yaml` | Extension objects and patches of core objects |

## Resolving names

Files refer to each other by name within the same version:

| Field | Resolves to |
| --- | --- |
| `object: actor` | `{version}/objects/actor.yaml` |
| `object: win/reg_key` | `{version}/extensions/win/objects/reg_key.yaml` |
| `extends: system` in a class | `{version}/classes/system.yaml` |
| `extends: endpoint` in an object | `{version}/objects/endpoint.yaml` |
| `profile: cloud`, `profiles: [...]` | the key in `{version}/profiles.yaml` |
| `type: ip_t` | the key in `{version}/types.yaml` |
| `category: system` | the key in `{version}/categories.yaml` |
| `patched_by: [linux]` | `{version}/extensions/linux/{classes or objects}/{same name}.yaml` |
| `referenced_by`, `used_by`, `applies_to` | class names resolve like `extends` in a class, object names like `object` |

## Mapping rules

Write OCSF mappings as TQL with the `tenzir` skill. Use this skill for the
schema decisions:

- Choose the version, then the class and its `activity_id` from `activities` in
  `v1.9.0/classes.yaml`, then the profiles the source supports.
- Set `class_uid`, `category_uid`, `activity_id`, `type_uid`, `severity_id`,
  `time`, `metadata.version`, and `metadata.product`. `type_uid` is
  `class_uid * 100 + activity_id`.
- List applied profiles in `metadata.profiles`, then fill the attributes those
  profiles add.
- Fill required attributes first, then recommended ones. Inside an object, its
  own requirement levels apply once you set the object. Satisfy `constraints`.
- Set `_id` attributes and leave their string siblings to `ocsf_derive`. For
  `99` (Other), set the sibling to the source value.
- Keep source fields without an OCSF target in `unmapped`.
- Finish with `ocsf_derive`, then `ocsf_cast`. The mapping is complete when
  `ocsf_cast` emits no warnings.

## Reading class and object files

`attributes` lists every attribute of the class or object, including
inherited attributes and attributes added by profiles, ordered by
requirement: required, recommended, then optional. An attribute that is not
listed is not part of that class or object.

Inherited attributes that are unchanged from their parent omit their
description and take one line, unless they have a long enum. They carry
everything a mapping needs. The description is in the file of the item that
`from` names:

```yaml
severity_id: {caption: Severity ID, type: integer_t, requirement: required, group: classification, sibling: severity, enum: {0: Unknown, 1: Informational, 2: Low, 3: Medium, 4: High, 5: Critical, 6: Fatal, 99: Other}, from: base_event}
```

Attributes that change anything besides the requirement, such as `activity_id`
with class-specific enum values, are listed in full with descriptions.

Top-level fields:

- `uid`: the `class_uid` of a class. `category_uid` is its category.
- `abstract: true`: a base class or object that events never use directly.
  Concrete classes extend abstract classes and inherit their attributes.
- `extends`: the parent the item inherits from.
- `profiles`: profiles that can apply to the item.
- `constraints`: `at_least_one` means at least one of the listed attributes
  must be set; `just_one` means exactly one must be set.
- `associations`: attributes that describe the same entity, e.g. `actor.user`
  and `device`.
- `observable` (objects): the observable `type_id` of the whole object.
- `referenced_by` (objects): the classes and objects that use this object, with
  the attribute names that hold it.
- `patched_by`: platform extensions that add attributes to this item.
- `extension`: the extension that defines the item. `patches` names the core
  item an extension patch modifies; the patch lists only the attributes it adds
  or changes.
- `deprecated`: `since`, `message`, and `superseded_by` for deprecated items.

Attribute fields:

- `requirement`: `required`, `recommended`, or `optional`.
- `type`: an OCSF data type from `types.yaml`. For `object_t`, `object` names
  the object. `array: true` marks a list of values.
- `profile`: the attribute belongs to that profile and is present only when the
  profile is applied. Attributes without `profile` always belong to the item.
- `from`: the ancestor that defines the attribute. Attributes without `from`
  are defined by the item itself.
- `group` (classes): `classification`, `context`, `occurrence`, or `primary`.
- `sibling`: the string attribute that carries the caption of this enum
  attribute, e.g. `activity_name` for `activity_id`.
- `observable`: the observable `type_id` for this attribute, from the
  attribute itself, its data type, or its object.
- `enum`: the allowed values. Keys are the integer values, `caption` is the label the
  sibling attribute takes.

## Searching

Read the index first, then the file it points to. These searches answer
common questions without opening many files:

- Find a class by keyword: `grep -n -i "keyword" v1.9.0/classes.yaml`
- Look up an attribute everywhere: `grep -n -A 12 "^src_endpoint:" v1.9.0/attributes.yaml`
- Jump to an attribute in a class: `grep -n -A 20 "^  actor:" v1.9.0/classes/process_activity.yaml`
- Read the description of an inherited attribute: `grep -n -A 30 "^  severity_id:" v1.9.0/classes/base_event.yaml`
- Find classes that hold an object: read `referenced_by` in `v1.9.0/objects/{name}.yaml`

## Question routing

| Question pattern | Start here |
| --- | --- |
| How do I map source X to OCSF? | Mapping rules above → `classes.yaml` → the class file; the `tenzir` skill for TQL |
| Which class fits event X? | Category table below → `classes.yaml` → candidate class files |
| What attributes does class or object Y have? | `classes.yaml` or `objects.yaml` → the item's file |
| Which values can enum attribute Z take? | The `enum` of Z in the class or object file |
| Where is attribute or object X used? | `attributes.yaml` (`used_by`) or the object's `referenced_by` |
| How do profiles work? / Which profile for X? | [Introduction: Profiles](docs/introduction/profiles.md) → `profiles.yaml` |
| What do platform extensions add? | `version.yaml` (`extensions`) → the extension files |
| How do I extend the schema? | [Introduction: Extensions](docs/introduction/extensions.md) or [Patching the Core Schema](docs/articles/patching-core-using-extensions.md) |
| How do I populate observables / model alerts? | [FAQs](docs/faqs.md) and [Articles](docs/articles.md) |
| What changed between versions? | `changes` in `version.yaml`, then compare the item files |
| Conceptual / design question | [Introduction](docs/introduction.md) → [FAQs](docs/faqs.md) |

When the question asks you to pick a class, read multiple candidates and explain
trade-offs.

## Domain knowledge

### Core concepts

**Attributes** are named fields with a data type. Every OCSF field has a
requirement level: required, recommended, or optional.

**Objects** group related attributes into reusable structures. Objects can nest
other objects.

**Event classes** define schemas for specific security events. Each class belongs
to a category and inherits from Base Event.

**Base Event** provides universal attributes and serves as a catch-all when no
more specific class fits.

**Profiles** are mix-ins that add cross-cutting attributes. A class can apply
multiple profiles.

**Extensions** add vendor-specific attributes without modifying the core schema.

### Event categories

Use the category range to narrow scope before reading individual class files.

| Range | Category | Focus |
| ----- | -------- | ----- |
| 1xxx | System Activity | OS-level: process, file, module, memory, kernel, registry |
| 2xxx | Findings | Detections, vulnerabilities, incidents, compliance |
| 3xxx | IAM | Authentication, authorization, account and group changes |
| 4xxx | Network Activity | General traffic and protocol-specific activity |
| 5xxx | Discovery | Device, user, service, and resource enumeration |
| 6xxx | Application Activity | Web resources, API calls, file hosting, datastore operations |
| 7xxx | Remediation | File, process, network, and entity remediation actions |
| 8xxx | Unmanned | Drones, vehicles, and robots |

### Naming conventions

- `snake_case` everywhere: `process_activity`, `network_endpoint`.
- Arrays use plural names: `answers`, `enrichments`, `attacks`.
- When `_id` is `Other` (`99`), the sibling string **must** be populated with
  the source value. For other values, the sibling takes the enum caption.
- `type_uid` is `class_uid * 100 + activity_id`, e.g. `100701` for Process
  Activity: Launch.

Key suffixes:

| Suffix | Meaning |
| ------ | ------- |
| `_id` | Enum integer identifier with a sibling string (same name minus `_id`). `0` = Unknown, `99` = Other. |
| `_uid` | Schema-unique or external unique identifier (integer for classification attrs, string otherwise). Sibling uses `_name`. |
| `_uuid` | Globally unique 128-bit identifier (string). No sibling. |
| `_name` | Friendly name / caption sibling for `_uid` or `_id` attributes. |
| `_time` | Timestamp (`timestamp_t`, milliseconds since epoch). |
| `_dt` | Datetime (`datetime_t`, RFC 3339 string). Added by the Date/Time profile alongside `_time` attributes. |
| `_info` / `_detail` | Object carrying supplementary information. |
| `_process` | Reference to a Process object. |
| `_ver` | Version string. |
| `_list` | Array of values. |

## Answering principles

- Read before answering. Every claim must trace back to a file you read.
- Use the indexes, the question routing table, and the category table to narrow
  scope before reading class or object files.
- Consult [FAQs](docs/faqs.md) for schema design rationale and ambiguous mappings.
- Consult [Articles](docs/articles.md) for deep-dive topics like observables,
  alerts, process parentage, and extensions.
- Read [Introduction](docs/introduction.md) sections for conceptual questions
  about the framework itself.
