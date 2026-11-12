---
title: "ocsf_trim"
canonical: https://tenzir.com/docs/v7.0.0/reference/functions/ocsf_trim
source: https://tenzir.com/docs/v7.0.0/reference/functions/ocsf_trim.md
section: "Docs"
---

# ocsf_trim

> Drops fields from an OCSF event record to reduce its size.

Drops fields from an OCSF event record to reduce its size.

```tql
ocsf_trim(x:record, [drop_optional=bool, drop_recommended=bool]) -> record
```

## Description

The `ocsf_trim` function removes fields from the OCSF event `x` based on their requirement level in the OCSF schema. It applies the same rules as the [`ocsf_trim`](https://tenzir.com/docs/v7.0.0/reference/operators/ocsf_trim) operator.

Use the function for both top-level and nested OCSF events. To transform the whole event, write `this = ocsf_trim(this)`. For an OCSF event in a field, write `ocsf = ocsf_trim(ocsf)`, or use [`map`](https://tenzir.com/docs/v7.0.0/reference/functions/map.md) to transform a list of events. The [`ocsf_trim`](https://tenzir.com/docs/v7.0.0/reference/operators/ocsf_trim) operator is deprecated.

Unlike the operator, which drops events whose OCSF version or class it cannot resolve, the function returns `null` with a warning and keeps the rest of the event. It also returns `null` with a warning when `x` is not a record, and returns `null` without a warning when `x` is `null`.

### `x: record`

The OCSF event to trim.

### `drop_optional = bool (optional)`

Whether to remove fields that the OCSF schema marks as optional.

Defaults to `true`.

### `drop_recommended = bool (optional)`

Whether to remove fields that the OCSF schema marks as recommended.

Defaults to `false`.

## Examples

### Transform a top-level event

Replace an existing `ocsf_trim` operator call with an assignment:

```tql
this = ocsf_trim(this)
```

The function returns `null` when it cannot resolve the event’s OCSF version or class. To preserve the original event for routing, assign the result to a separate field and check it before replacing `this`.

### Trim an OCSF event in a field

```tql
from {
  raw_data: "…",
  ocsf: {
    class_uid: 4001,
    metadata: {version: "1.9.0"},
    activity_id: null,
    message: "",
    enrichments: [],
    src_endpoint: {},
    unmapped: {custom: null, empty: []},
  },
}
ocsf = ocsf_trim(ocsf)
```

```tql
{
  raw_data: "…",
  ocsf: {
    class_uid: 4001,
    metadata: {
      version: "1.9.0",
    },
    activity_id: null,
    message: "",
    src_endpoint: {},
  },
}
```

### Compare trimming levels side by side

```tql
from {
  ocsf: {
    class_uid: 4001,
    metadata: {version: "1.9.0"},
    activity_id: null,
    message: "",
    src_endpoint: {},
  },
}
retained = ocsf_trim(ocsf, drop_optional=false)
required = ocsf_trim(ocsf, drop_optional=false, drop_recommended=true)
select retained, required
```

```tql
{
  retained: {
    class_uid: 4001,
    metadata: {
      version: "1.9.0",
    },
    activity_id: null,
    message: "",
    src_endpoint: {},
  },
  required: {
    class_uid: 4001,
    metadata: {
      version: "1.9.0",
    },
    activity_id: null,
  },
}
```

## See Also

* [`ocsf_trim`](https://tenzir.com/docs/v7.0.0/reference/operators/ocsf_trim)
* [`ocsf_compact`](https://tenzir.com/docs/v7.0.0/reference/functions/ocsf_compact.md)
* [`ocsf_cast`](https://tenzir.com/docs/v7.0.0/reference/functions/ocsf_cast.md)
* [`ocsf_derive`](https://tenzir.com/docs/v7.0.0/reference/functions/ocsf_derive.md)
* [Map to OCSF](../../guides/normalize/map-to-ocsf.md)
