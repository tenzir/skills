---
name: ocsf
description: Answer questions about OCSF (Open Cyber Security Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.
---

# OCSF

Look up OCSF reference documentation and answer from those sources. Only state
facts from files you read. Never invent schema details. If the documentation
doesn't cover the question, say so.

## Reading the documentation

The OCSF reference lives inside the `tenzir` skill. Invoke the skill, resolve
its directory, and read files relative to that directory.

The file tree follows this layout:

```
reference/ocsf.md                       # version table + overview
reference/ocsf/introduction.md          # conceptual introduction
reference/ocsf/faqs.md                  # FAQ index
reference/ocsf/faqs/{slug}.md           # individual FAQ
reference/ocsf/articles.md              # articles index
reference/ocsf/articles/{slug}.md       # individual article
reference/ocsf/{v}.md                   # version overview  (v = 1-7-0, …)
reference/ocsf/{v}/classes.md           # class index
reference/ocsf/{v}/classes/{name}.md    # individual class
reference/ocsf/{v}/objects.md           # object index
reference/ocsf/{v}/objects/{name}.md    # individual object
reference/ocsf/{v}/profiles.md          # profile index
reference/ocsf/{v}/profiles/{name}.md   # individual profile
reference/ocsf/{v}/extensions.md        # extension index
reference/ocsf/{v}/types.md             # type index
```

Start by reading `reference/ocsf.md` to discover available versions. Use the
latest stable version unless the user requests a specific one. Stick to one
version per answer.

## Domain knowledge

### Core concepts

**Attributes** are named fields with a data type (scalar like `string_t` or
complex like `object`). Every OCSF field has a requirement level: required,
recommended, or optional.

**Objects** group related attributes into reusable structures (`process`,
`user`, `file`, `device`, …). Objects can nest other objects.

**Event classes** define schemas for specific security events. Each class
belongs to a category and inherits from Base Event.

**Base Event** provides universal attributes (`time`, `metadata`,
`severity_id`, `message`, `observables`, `unmapped`) and serves as a catch-all
when no specific class fits.

**Profiles** are mix-ins that add cross-cutting attributes (for example
`cloud`, `container`, `host`). A class can apply multiple profiles.

**Extensions** add vendor-specific attributes without modifying the core
schema. They use a namespace prefix (for example `linux/exec_flags`).

### Event categories

| Range | Category             | Focus                                                       |
| ----- | -------------------- | ----------------------------------------------------------- |
| 1xxx  | System Activity      | OS-level: process, file, module, memory, kernel, registry   |
| 2xxx  | Findings             | Detections, vulnerabilities, incidents, compliance          |
| 3xxx  | IAM                  | Authentication, authorization, account/group changes        |
| 4xxx  | Network Activity     | General traffic and protocol-specific (DNS, HTTP, SSH, …)   |
| 5xxx  | Discovery            | Device, user, service, resource enumeration                 |
| 6xxx  | Application Activity | Web resources, API calls, file hosting, datastore ops       |
| 7xxx  | Remediation          | File, process, network, entity remediation actions          |
| 8xxx  | Unmanned             | Drones, vehicles, robots                                    |

### Naming conventions

- `snake_case` everywhere: `process_activity`, `network_endpoint`.
- Suffixes carry meaning: `_id` (enum int), `_uid` (schema-unique), `_uuid`
  (globally unique), `_name` (display label), `_time` / `_dt` (timestamp).

## Answering principles

- **Read before answering.** Every claim must trace back to a file you read.
- **Use the category table to narrow scope.** It tells you which class-ID
  range to explore for a given event type.
- **Consult the FAQs for ambiguous choices.** Read `faqs.md` for the index,
  then the relevant individual FAQ files.
- **Read multiple candidates for selection questions.** Aim for 2-4, then
  rank them.

## Entity selection scoring

When the question is "which class / object / profile fits?", rank candidates:

| Score     | Meaning             |
| --------- | ------------------- |
| 90–100 %  | Strong fit          |
| 60–89 %   | Viable, trade-offs  |
| < 60 %    | Poor fit            |

Score profiles independently — they combine freely. After ranking, explain
trade-offs and recommend when to prefer each option.
