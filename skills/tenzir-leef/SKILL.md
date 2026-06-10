---
name: tenzir-leef
description: >-
  Answer questions and produce mappings for IBM LEEF (Log Event
  Extended Format), the QRadar event format: LEEF 1.0/2.0 headers,
  delimiters, predefined event attributes, custom event keys,
  devTime/devTimeFormat timestamps, and syslog transport. Use when
  generating, parsing, validating, or mapping logs to or from LEEF,
  building QRadar or JSA integrations and DSMs, or when the user
  mentions LEEF payloads, QRadar log formats, QID mapping, or
  key=value events with a LEEF: header.
---

# Log Event Extended Format

LEEF (Log Event Extended Format) is IBM's event format for QRadar. A LEEF event is a single line consisting of an optional syslog header, a pipe-delimited LEEF header, and a flat list of `key=value` event attributes.

The latest LEEF version is 2.0, which this skill documents. LEEF 2.0 adds one optional header field to LEEF 1.0: a delimiter character for the event attributes. Both header layouts are covered in [LEEF event components](docs/event-components.md).

Use [attributes.yaml](attributes.yaml) as the authoritative reference for the predefined event attributes: exact key spelling, value type, normalization behavior, limits, and reserved status. If an attribute is not present there, it is not a predefined LEEF attribute.

## Data files

- Use [attributes.yaml](attributes.yaml) to look up predefined event attributes.
- Use [docs/overview.md](docs/overview.md) for what LEEF is and how QRadar discovers LEEF event sources.
- Use [docs/event-components.md](docs/event-components.md) for the syslog header, the LEEF 1.0/2.0 header fields, and delimiter rules.
- Use [docs/custom-keys.md](docs/custom-keys.md) and [docs/best-practices.md](docs/best-practices.md) for non-predefined keys.
- Use [docs/date-format.md](docs/date-format.md) for `devTime`/`devTimeFormat` patterns.
- Use [source.md](source.md) for upstream provenance and counts.

## Format rules

- Encode LEEF events as UTF-8.
- A LEEF 2.0 event has the shape `<syslog header> LEEF:2.0|Vendor|Product|Version|EventID|DelimiterCharacter|key=value<delim>key=value...`; the syslog header and the delimiter field are optional.
- A LEEF 1.0 header has no delimiter field: `LEEF:1.0|Vendor|Product|Version|EventID|`; attributes are always tab-separated.
- The LEEF 2.0 delimiter is a single character or a hex value prefixed with `0x` or `x` followed by 1-4 hex digits (for example `^`, `x5E`, or `0x09`); when omitted, tab is the default.
- The EventID must be static across product languages and at most 255 characters; use `cat` to subdivide an EventID further.
- Attribute order is not enforced, but each key may appear only once per payload.
- Prefer predefined attribute keys from [attributes.yaml](attributes.yaml); create custom keys only when no predefined attribute fits, keep them single-word alphanumeric, and never reuse a predefined key name.
- Express event time with `devTime`; pair it with `devTimeFormat` (a Java SimpleDateFormat pattern) unless `devTime` is a 10- or 13-digit epoch value.

## Question routing

- **What does attribute X mean, what type is it, what are its limits?** Use [attributes.yaml](attributes.yaml).
- **How do I build or parse the LEEF header or pick a delimiter?** Read [docs/event-components.md](docs/event-components.md).
- **Which syslog header formats are accepted?** Read [docs/event-components.md](docs/event-components.md).
- **How do I encode timestamps?** Read [docs/date-format.md](docs/date-format.md) together with the `devTime` and `devTimeFormat` entries in [attributes.yaml](attributes.yaml).
- **There is no predefined key for my data.** Read [docs/custom-keys.md](docs/custom-keys.md) and [docs/best-practices.md](docs/best-practices.md).
- **How does QRadar discover and categorize LEEF events?** Read [docs/overview.md](docs/overview.md).
- **What upstream source backs this skill?** Use [source.md](source.md).
