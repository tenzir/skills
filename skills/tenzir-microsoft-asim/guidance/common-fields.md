# Common Fields

Source: [ASIM common schema fields reference](https://learn.microsoft.com/en-us/azure/sentinel/normalization-common-fields).

Common fields appear across ASIM schemas. A schema page may override common
field guidance for that schema, such as allowed `EventType` values or the
`EventSchemaVersion` value.

## Mapping notes

- Preserve source-specific details that do not map cleanly in `AdditionalFields`.
- Normalize `EventVendor` and `EventProduct` to ASIM's accepted designators
  when possible instead of copying arbitrary source strings.
- Treat common device fields as the shared vocabulary for source, target, and
  reporting systems.
- Use the generated field pages to check whether a common field is mandatory,
  recommended, optional, conditional, or an alias in each schema.

## Vendor and product values

ASIM maintains normalized vendor and product names for `EventVendor` and
`EventProduct`. If a mapping targets an unlisted vendor or product, keep the
mapping explicit and expect that the upstream ASIM list may need expansion.

## Schema updates

Common fields can change over time and then affect every schema that includes
the common fragments. The generated `source.md` page records the exact Azure
Sentinel commit used for this skill.
