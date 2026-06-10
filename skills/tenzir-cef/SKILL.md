---
name: tenzir-cef
description: >-
  Answer questions and produce mappings for ArcSight CEF (Common Event
  Format), the OpenText/Micro Focus SIEM interchange format, and the
  ArcSight ESM event schema behind it: CEF headers, severity, escaping
  rules, the predefined extension dictionary, custom and flex fields
  (cs1-cs6, cn1-cn3, cfp1-cfp4, flexString, flexDate), user-defined
  extensions, date formats, and ESM data fields with script aliases.
  Use when generating, parsing, validating, or mapping logs to or from
  CEF, building ArcSight SmartConnector or FlexConnector integrations,
  ingesting CEF into a SIEM such as Microsoft Sentinel
  CommonSecurityLog, or when the user mentions CEF payloads,
  pipe-delimited CEF:0 headers, or ArcSight event fields.
---

# Common Event Format

CEF (Common Event Format) is ArcSight's text-based event interchange format, now maintained by OpenText. A CEF event is a single line consisting of an optional syslog prefix, a pipe-delimited header, and a flat list of space-separated `key=value` extensions:

```
CEF:Version|Device Vendor|Device Product|Device Version|Device Event Class ID|Name|Severity|[Extension]
```

Use [extensions.yaml](extensions.yaml) as the authoritative reference for the predefined extension keys: exact key spelling, expanded full name, data type, length, producer/consumer audience, and the CEF specification version that introduced the key. If a key is not present there, it is not a predefined CEF extension.

Behind CEF sits the ArcSight ESM event schema: every CEF full name is an ESM script alias (for example `act` expands to `deviceAction` in the Device group). Use [catalog.yaml](catalog.yaml) to pick a schema group and `groups/<group>.yaml` for its fields.

## Data files

- Use [extensions.yaml](extensions.yaml) to look up predefined CEF extension keys.
- Use [catalog.yaml](catalog.yaml) to choose an ESM event schema group, then `groups/<group>.yaml` for its data fields.
- Use [docs/overview.md](docs/overview.md) for the CEF header fields, severity, and character encoding and escaping rules.
- Use [docs/special-mappings.md](docs/special-mappings.md) for the documented firewall, anti-virus, email, wireless, and IPv6 mapping conventions.
- Use [docs/user-defined-extensions.md](docs/user-defined-extensions.md) for naming and limitations of non-predefined keys.
- Use [docs/date-formats.md](docs/date-formats.md) for the accepted timestamp formats.
- Use [docs/esm-data-fields.md](docs/esm-data-fields.md) for how ESM labels, script aliases, and turbo levels relate.
- Use [docs/field-suffixes.md](docs/field-suffixes.md) for the geographical and resource attribute suffixes.
- Use [source.md](source.md) for upstream provenance and counts.

## Format rules

- Encode CEF events as UTF-8.
- The header has seven pipe-delimited fields followed by the extension field; none of the seven may be omitted.
- Escape `\` as `\\` and `|` as `\|` in header values; the pipe needs no escaping in extension values.
- Escape `=` as `\=` in extension values; newlines are allowed only in extension values, as `\n` or `\r`.
- Severity is an integer 0-10 or one of Unknown, Low, Medium, High, Very-High; higher means more important.
- The Device Event Class ID uniquely identifies the event type per product and is at most 1023 characters.
- Extensions are `key=value` pairs separated by single spaces; each key may appear at most once.
- Prefer predefined keys from [extensions.yaml](extensions.yaml); never set keys whose audience is consumer when producing events.
- Pair every custom and flex field with its Label counterpart (for example `cs1` with `cs1Label`) and keep labels unique within an event.
- Name user-defined extensions `VendornameProductnameExplanatoryKeyName`, alphanumeric and as short as possible; never reuse a predefined key name.
- Express timestamps as milliseconds since epoch or one of the formats in [docs/date-formats.md](docs/date-formats.md).

## Question routing

- **What does key X mean, what type or length does it have, who may set it?** Use [extensions.yaml](extensions.yaml).
- **How do I build or parse the CEF header, escape characters, or encode severity?** Read [docs/overview.md](docs/overview.md).
- **Which ESM field backs a CEF key, or what fields does schema group X contain?** Follow `esm_groups` in [extensions.yaml](extensions.yaml) into [catalog.yaml](catalog.yaml) and `groups/<group>.yaml`.
- **How do I map firewall, anti-virus, email, wireless, or IPv6 events?** Read [docs/special-mappings.md](docs/special-mappings.md).
- **There is no predefined key for my data.** Read [docs/user-defined-extensions.md](docs/user-defined-extensions.md).
- **How do I encode timestamps?** Read [docs/date-formats.md](docs/date-formats.md).
- **What do labels, script aliases, and turbo levels mean in ESM?** Read [docs/esm-data-fields.md](docs/esm-data-fields.md).
- **What do the Geo or resource attribute suffixes mean?** Read [docs/field-suffixes.md](docs/field-suffixes.md).
- **What upstream source backs this skill?** Use [source.md](source.md).
