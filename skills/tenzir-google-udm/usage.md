# Google UDM Usage Guidance

Generated from targeted sections of the Google UDM usage guide and field list.
Use these pages for field population policy, required fields, field-path
prefixes, datatype notes, and examples. Use the proto-derived schema pages
for field existence, types, numbers, JSON names, oneofs, and deprecation.

## Source

- **UDM usage guide**: https://docs.cloud.google.com/chronicle/docs/unified-data-model/udm-usage?hl=en
  - Google last updated: `2026-06-03 UTC`
- **Unified Data Model field list**: https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list?hl=en
  - Google last updated: `2026-06-03 UTC`

## Generated Guidance

- Message guidance entries: `156`
- Product-only field notes: `2`
- Event type categories: `19`
- Event guidance sections: `25`
- Entity requirement pages: `8`
- Datatype rows: `15`

## Indexes

- [Field paths](field-paths.md)
- [Datatypes](datatypes.md)
- [Event type categories](event-type-categories.md)
- [Event guidance](event-guidance.md)
- [Entity guidance](entity-guidance.md)

## Product-Only Field Notes

These usage-guide fields do not resolve to proto-derived UDM messages.

### `idm.is_alert`

- **Purpose**: Identifies whether the event is an alert.
- **Encoding**: Boolean.

### `idm.is_significant`

- **Purpose**: Specifies whether to display the alert in Enterprise Insights.
- **Encoding**: Boolean.
