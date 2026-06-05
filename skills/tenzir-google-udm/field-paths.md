# Field Path Prefixes

Use this page to choose the right field-path prefix for rules, Detect Engine,
and configuration-based normalizer contexts.

## Field path names

This page focuses on the left-side field-path form from generated
field headings. If a message page shows `event_type` / `eventType`,
use `event_type` with the prefix required by the rule or normalizer
context, for example `$event.metadata.event_type`.

Use the right-side form when mapping logs into UDM event or entity
objects for Google SecOps UDM API ingestion, for example
`metadata.eventType`.

## Rules Engine Prefix Notes

- UDM field name formats:
- For rules engine evaluation, the prefix begins with udm.
- For configuration-based normalizer (CBN), the prefix begins with event.idm.read_only_udm.
- This document provides a list of fields available in the Unified Data Model. When specifying a field, use the following format: `<prefix>.<field_name1>.<field_name2>.<...>.<field_nameN>=<value>`

## Detect Engine

- When writing rules for Detect Engine, use the <prefix> pattern `$event` for Event fields and `$entity` for Entity fields. For example:

### Examples

- `$event.metadata.event_type`
- `$event.network.dhcp.opcode`
- `$event.principal.user.location.city`
- `$entity.graph.entity.hostname`
- `$entity.graph.metadata.product_name`

## Configuration-Based Normalizer

- When you write configuration-based normalizer (CBN) parsers, use the <prefix> pattern `event.idm.read_only_udm` for UDM Event fields and `event.idm.graph` for UDM Entity fields. For example:

### Examples

- `event.idm.read_only_udm.metadata.event_type`
- `event.idm.read_only_udm.network.dhcp.opcode`
- `event.idm.read_only_udm.principal.user.location.city`
- `event.idm.graph.entity.user.user_display_name`
- `event.idm.graph.entity.asset.hostname`

## Style Notes

- Field name and field type values can look similar. This document uses style conventions to help you identify the differences:
- Field type values use camelCase characters. For example, `platform` and `eventType`.
- Field name values use lowercase characters. For example, `platform` and `event_type`.
- Standard datatype values use lowercase characters.
