---
name: ocsf
description: Answer questions about OCSF (Open Cybersecurity Schema Framework). Use when the user asks about OCSF classes, objects, attributes, profiles, extensions, or event normalization.
---

# OCSF

Look up OCSF reference documentation and answer from those sources. Only state facts from files you read. Never invent schema details. If the documentation does not cover the question, say so.

## Reading the documentation

Start with [index.md](index.md) to discover available versions. Use the latest stable version unless the user requests a specific one. Stick to one version per answer.

The file tree follows this layout:

```
index.md
introduction.md
faqs.md
faqs/{slug}.md
articles.md
articles/{slug}.md
{version}.md
{version}/classes.md
{version}/classes/{name}.md
{version}/objects.md
{version}/objects/{name}.md
{version}/profiles.md
{version}/profiles/{name}.md
{version}/extensions.md
{version}/extensions/{name}.md
{version}/types.md
```

## Domain knowledge

### Core concepts

**Attributes** are named fields with a data type. Every OCSF field has a requirement level: required, recommended, or optional.

**Objects** group related attributes into reusable structures. Objects can nest other objects.

**Event classes** define schemas for specific security events. Each class belongs to a category and inherits from Base Event.

**Base Event** provides universal attributes and serves as a catch-all when no more specific class fits.

**Profiles** are mix-ins that add cross-cutting attributes. A class can apply multiple profiles.

**Extensions** add vendor-specific attributes without modifying the core schema.

### Event categories

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
- Suffixes carry meaning: `_id`, `_uid`, `_uuid`, `_name`, `_time`, `_dt`.

## Answering principles

- Read before answering. Every claim must trace back to a file you read.
- Use the category table to narrow scope before diving into class pages.
- Consult [faqs.md](faqs.md) when the question is about schema choices or ambiguity.
- Read multiple candidates for selection questions and explain trade-offs.

## Documentation map

### [Introduction](introduction.md)

### [Latest classes](v1.7.0/classes.md)

### [Latest objects](v1.7.0/objects.md)

### [Latest profiles](v1.7.0/profiles.md)

### [Latest extensions](v1.7.0/extensions.md)

### [Latest types](v1.7.0/types.md)

### [FAQs](faqs.md)

### [Articles](articles.md)
