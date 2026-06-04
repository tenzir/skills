# Schema Semantics

Source: [Advanced Security Information Model schemas](https://learn.microsoft.com/en-us/azure/sentinel/normalization-about-schemas).

ASIM schemas model activities and entities with a consistent set of field
names. Start a mapping by identifying the activity type, then inspect the
candidate generated schema pages for mandatory and recommended fields.

## Field classes

- `Mandatory` fields are expected in normalized events for that schema.
- `Recommended` fields should be normalized when the source provides them.
- `Optional` fields can remain unnormalized when they are not needed.
- `Conditional` fields become required when the field they follow is populated.
- `Alias` fields are conditional convenience fields for analyst queries.

## Entities and roles

ASIM represents users, devices, processes, applications, and similar objects
with repeatable entity field sets. When a record has multiple entities of the
same type, role prefixes such as `Src`, `Dst`, `Actor`, `Acting`, `Target`,
and `Parent` identify which entity the field describes.

When a source has entity identifiers that do not map to normalized fields,
keep the source value in its original form or place it in `AdditionalFields`.
When a field stores an identifier with multiple possible formats, populate
the matching `Type` field when the schema defines one.

## Aliases

Aliases make interactive queries friendlier, but reusable detections,
analytics rules, and workbooks should prefer the aliased normalized field.

## Logical types

Logical types document value expectations that Log Analytics does not always
enforce. Examples include enumerated strings, normalized date/time values,
IP addresses, FQDNs, hostnames, hash strings, confidence levels, risk levels,
and schema versions.
