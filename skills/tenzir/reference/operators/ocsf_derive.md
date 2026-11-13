---
title: "ocsf_derive"
canonical: https://tenzir.com/docs/reference/operators/ocsf_derive
source: https://tenzir.com/docs/reference/operators/ocsf_derive.md
section: "Docs"
---

# ocsf_derive

> Automatically assigns enum strings from their integer counterparts and vice versa.

Automatically assigns enum strings from their integer counterparts and vice versa.

Deprecated

The `ocsf_derive` operator is deprecated and emits a warning. Use the [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md) function for both top-level and nested OCSF events. To transform the whole event, assign the function result to `this`:

```tql
this = ocsf_derive(this)
```

The function returns `null` with a warning when it cannot resolve the OCSF version or class, while the operator drops those events. Assign the result to a separate field before replacing `this` if you need to inspect or route the original event.

```tql
ocsf_derive
```

## Description

The `ocsf_derive` operator performs bidirectional enum derivation for OCSF events by automatically assigning enum string values based on their integer counterparts and vice versa.

The operator preserves the original field order from the input record and appends derived fields to the end of the record that contains them.

The operator also computes the required `category_uid` and `type_uid` fields when they are missing or `null`. The `category_uid` follows from the class, and the `type_uid` is `class_uid * 100 + activity_id`, where the operator falls back to `activity_name` if `activity_id` is missing. The operator then derives `category_name` and `type_name` from them. It keeps existing values and warns when a `type_uid` does not match `class_uid` and `activity_id`.

## Examples

### Integer to string

```tql
from {
  metadata: {
    version: "1.9.0",
  },
  class_uid: 1001,
  activity_id: 1,
}
ocsf_derive
```

```tql
{
  metadata: {
    version: "1.9.0",
  },
  class_uid: 1001,
  activity_id: 1,
  category_uid: 1,
  type_uid: 100101,
  activity_name: "Create",
  category_name: "System Activity",
  class_name: "File System Activity",
  type_name: "File System Activity: Create",
}
```

### String to Integer

```tql
from {
  metadata: {
    version: "1.9.0",
  },
  class_uid: 1001,
  activity_name: "Read",
}
ocsf_derive
```

```tql
{
  metadata: {
    version: "1.9.0",
  },
  class_uid: 1001,
  activity_name: "Read",
  category_uid: 1,
  type_uid: 100102,
  activity_id: 2,
  category_name: "System Activity",
  class_name: "File System Activity",
  type_name: "File System Activity: Read",
}
```

### Bidirectional enum validation

```tql
from {
  metadata: {
    version: "1.9.0",
  },
  class_uid: 1001,
  activity_id: 1,
  activity_name: "Delete",  // Inconsistent with activity_id=1
}
ocsf_derive
```

```tql
{
  metadata: {
    version: "1.9.0",
  },
  class_uid: 1001,
  activity_id: 1,
  activity_name: "Delete",
  category_uid: 1,
  type_uid: 100101,
  category_name: "System Activity",
  class_name: "File System Activity",
  type_name: "File System Activity: Create",
}
```

This emits a warning about inconsistent values and preserves both original values without modification, allowing you to decide how to handle the conflict.

```plaintext
warning: found inconsistency between `activity_id` and `activity_name`
  |
  | ocsf_derive
  | ~~~~~~~~~~~~
  |
  = note: got 1 ("Create") and "Delete" (4)
```

## See Also

* [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md)
* [`ocsf_compact`](https://tenzir.com/docs/reference/functions/ocsf_compact.md)
* [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md)
* [`ocsf_trim`](https://tenzir.com/docs/reference/operators/ocsf_trim.md)
* [Map to OCSF](../../guides/normalize/map-to-ocsf.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
