---
title: "ocsf_compact"
canonical: https://tenzir.com/docs/reference/functions/ocsf_compact
source: https://tenzir.com/docs/reference/functions/ocsf_compact.md
section: "Docs"
---

# ocsf_compact

> Removes enum strings from an OCSF event record that ocsfderive can rebuild.

Removes enum strings from an OCSF event record that [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) can rebuild.

```tql
ocsf_compact(x:record, [uids=bool]) -> record
```

## Description

The `ocsf_compact` function is the lossless inverse of [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md). It removes every enum string from the OCSF event `x` that [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) rebuilds exactly from its integer sibling, such as `activity_name` from `activity_id`, `severity` from `severity_id`, `type_name` from `type_uid`, or `class_name` from `class_uid`. The function recurses into nested records and lists, and treats enum lists such as `answers[].flags` as a whole.

Use it to store OCSF events with their integer identifiers only, and run [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) when reading them to restore the strings.

The function keeps every string that [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) cannot rebuild exactly:

* The string of an `Other` value, such as `activity_id: 99`, because it carries a data source specific value.
* A string that does not match its integer, so that [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) can still warn about the inconsistency.
* A string next to an integer that the enum does not define.
* A string without an integer, or next to a `null` integer.
* An enum list that contains any of the above, or whose length differs from its integer list.

By default, the function removes only enum strings. It never adds fields, changes integer values, or removes fields of any other kind.

Like [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md), the function returns `null` with a warning when it cannot resolve the OCSF version or class of `x`, or when `x` is not a record. It returns `null` without a warning when `x` is `null`.

### `x: record`

The OCSF event to compact.

### `uids = bool (optional)`

Also removes the `category_uid` and `type_uid` fields where [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) computes them from `class_uid` and `activity_id`.

Both fields are required in OCSF, so the compacted events are only valid OCSF again after [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) restored them.

When you store compacted events in a database table with dedicated columns for these fields, make the columns nullable, such as `Nullable(Int64)` in ClickHouse. A non-nullable column stores a default value like `0` instead, which [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) cannot tell apart from a real value.

Defaults to `false`.

## Examples

### Store only the integer identifiers

```tql
from {
  class_uid: 3002,
  class_name: "Authentication",
  metadata: {version: "1.9.0"},
  activity_id: 1,
  activity_name: "Logon",
  severity_id: 1,
  severity: "Informational",
  user: {name: "alice", type_id: 1, type: "User"},
}
this = ocsf_compact(this)
```

```tql
{
  class_uid: 3002,
  metadata: {
    version: "1.9.0",
  },
  activity_id: 1,
  severity_id: 1,
  user: {
    name: "alice",
    type_id: 1,
  },
}
```

### Keep data source specific values

The `Other` value `99` keeps its string, because [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) would replace it with `"Other"`:

```tql
from {
  class_uid: 3002,
  metadata: {version: "1.9.0"},
  activity_id: 99,
  activity_name: "user_login",
  status_id: 1,
  status: "Success",
}
this = ocsf_compact(this)
```

```tql
{
  class_uid: 3002,
  metadata: {
    version: "1.9.0",
  },
  activity_id: 99,
  activity_name: "user_login",
  status_id: 1,
}
```

### Remove computable identifiers

```tql
from {
  class_uid: 3002,
  category_uid: 3,
  metadata: {version: "1.9.0"},
  activity_id: 1,
  type_uid: 300201,
}
this = ocsf_compact(this, uids=true)
```

```tql
{
  class_uid: 3002,
  metadata: {
    version: "1.9.0",
  },
  activity_id: 1,
}
```

### Restore the strings when reading

A compacted event contains only the integer identifiers and the strings that carry information. Run [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) after reading it to restore the complete event:

```tql
from {
  class_uid: 4003,
  metadata: {version: "1.9.0"},
  activity_id: 2,
  answers: [{flag_ids: [1, 2]}],
}
this = ocsf_derive(this)
```

```tql
{
  class_uid: 4003,
  metadata: {
    version: "1.9.0",
  },
  activity_id: 2,
  answers: [
    {
      flag_ids: [
        1,
        2,
      ],
      flags: [
        "Authoritative Answer",
        "Truncated Response",
      ],
    },
  ],
  category_uid: 4,
  type_uid: 400302,
  activity_name: "Response",
  category_name: "Network Activity",
  class_name: "DNS Activity",
  type_name: "DNS Activity: Response",
}
```

## See Also

* [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md)
* [`ocsf_cast`](https://tenzir.com/docs/reference/functions/ocsf_cast.md)
* [`ocsf_derive`](https://tenzir.com/docs/reference/operators/ocsf_derive.md)
* [Map to OCSF](../../guides/normalize/map-to-ocsf.md)
