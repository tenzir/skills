---
title: "ocsf_derive"
canonical: https://tenzir.com/docs/reference/functions/ocsf_derive
source: https://tenzir.com/docs/reference/functions/ocsf_derive.md
section: "Docs"
---

# ocsf_derive

> Assigns enum strings of an OCSF event record from their integer counterparts and vice versa.

Assigns enum strings of an OCSF event record from their integer counterparts and vice versa.

```tql
ocsf_derive(x:record) -> record
```

## Description

The `ocsf_derive` function performs bidirectional enum derivation on the OCSF event `x`. It applies the same rules as the [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) operator: it fills a missing enum string such as `activity_name` from its integer sibling `activity_id` and vice versa, recurses into nested records and lists, and warns about inconsistent pairs without modifying them. It also computes missing `category_uid` and `type_uid` fields from `class_uid` and `activity_id`. Existing fields keep their position, and the function appends derived fields to the end of their record.

Use the function for both top-level and nested OCSF events. To transform the whole event, write `this = ocsf_derive(this)`. For an OCSF event in a field, write `ocsf = ocsf_derive(ocsf)`, or use [`map`](https://tenzir.com/docs/reference/functions/map.md) to transform a list of events. The [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md) operator is deprecated.

Unlike the operator, which drops events whose OCSF version or class it cannot resolve, the function returns `null` with a warning and keeps the rest of the event. It also returns `null` with a warning when `x` is not a record, and returns `null` without a warning when `x` is `null`.

### `x: record`

The OCSF event to complete.

## Examples

### Transform a top-level event

Replace an existing `ocsf_derive` operator call with an assignment:

```tql
this = ocsf_derive(this)
```

The function returns `null` when it cannot resolve the event’s OCSF version or class. To preserve the original event for routing, assign the result to a separate field and check it before replacing `this`.

### Derive enum siblings in a field

```tql
from {
  raw_data: "…",
  ocsf: {
    class_uid: 1001,
    metadata: {version: "1.9.0"},
    activity_id: 1,
  },
}
ocsf = ocsf_derive(ocsf)
```

```tql
{
  raw_data: "…",
  ocsf: {
    class_uid: 1001,
    metadata: {
      version: "1.9.0",
    },
    activity_id: 1,
    category_uid: 1,
    type_uid: 100101,
    activity_name: "Create",
    category_name: "System Activity",
    class_name: "File System Activity",
    type_name: "File System Activity: Create",
  },
}
```

### Derive enum siblings in a list of events

```tql
from {
  events: [
    {class_uid: 1001, metadata: {version: "1.9.0"}, activity_name: "Read"},
    {class_uid: 4003, metadata: {version: "1.9.0"}, answers: [{flag_ids: [1, 3]}]},
  ],
}
events = events.map(x => ocsf_derive(x))
```

```tql
{
  events: [
    {
      class_uid: 1001,
      metadata: {
        version: "1.9.0",
      },
      activity_name: "Read",
      category_uid: 1,
      type_uid: 100102,
      activity_id: 2,
      category_name: "System Activity",
      class_name: "File System Activity",
      type_name: "File System Activity: Read",
    },
    {
      class_uid: 4003,
      metadata: {
        version: "1.9.0",
      },
      answers: [
        {
          flag_ids: [
            1,
            3,
          ],
          flags: [
            "Authoritative Answer",
            "Recursion Desired",
          ],
        },
      ],
      category_uid: 4,
      category_name: "Network Activity",
      class_name: "DNS Activity",
    },
  ],
}
```

## See Also

* [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md)
* [`ocsf_cast`](https://tenzir.com/docs/reference/functions/ocsf_cast.md)
* [`ocsf_compact`](https://tenzir.com/docs/reference/functions/ocsf_compact.md)
* [`ocsf_trim`](https://tenzir.com/docs/reference/functions/ocsf_trim.md)
* [Map to OCSF](../../guides/normalize/map-to-ocsf.md)
