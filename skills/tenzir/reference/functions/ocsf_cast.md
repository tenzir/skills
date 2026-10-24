---
title: "ocsf_cast"
canonical: https://tenzir.com/docs/reference/functions/ocsf_cast
source: https://tenzir.com/docs/reference/functions/ocsf_cast.md
section: "Docs"
---

# ocsf_cast

> Casts an OCSF event record to its OCSF type.

Casts an OCSF event record to its OCSF type.

```tql
ocsf_cast(x:record, [encode_variants=bool, null_fill=bool, timestamp_to_ms=bool]) -> record
```

## Description

The `ocsf_cast` function casts the record `x` to the OCSF event class type selected by its `metadata.version`, `metadata.profiles`, `metadata.extensions`, and `class_uid` fields. It applies the same casting rules as the [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md) operator: it warns about fields that the schema does not define and removes them, encodes free-form objects such as `unmapped`, and converts values to the types the schema expects.

Use the function when the OCSF event lives in a field rather than at the top level of the event, for example next to `raw_data` in an envelope, or in a list of events that you process with [`map`](https://tenzir.com/docs/reference/functions/map.md). Use the operator when the whole event is the OCSF event.

The function differs from the operator in three ways:

* It returns `null` with a warning when it cannot resolve the OCSF version or class of `x`, where the operator drops the event. The rest of the event stays intact, so you can route such events instead of losing them.
* It does not assign `@name`, because the schema name belongs to the whole event rather than to a field.
* It warns when `x` lacks a field that the schema requires, or violates an OCSF constraint that needs at least one or exactly one of a set of fields. These checks only emit warnings and never change the result.

The function also returns `null` with a warning when `x` is not a record, and returns `null` without a warning when `x` is `null`.

### `x: record`

The OCSF event to cast.

### `encode_variants = bool (optional)`

Setting this option to `true` emits free-form objects such as `unmapped` as JSON strings instead of records.

Defaults to `false`.

### `null_fill = bool (optional)`

When `true`, the function back-fills optional fields that do not exist in the input with `null` values.

Defaults to `false`.

### `timestamp_to_ms = bool (optional)`

Converts `time` fields representing OCSF `timestamp` fields into integer values, counting milliseconds since UNIX epoch.

Defaults to `false`.

## Examples

### Cast an OCSF event next to its raw data

```tql
from {
  raw_data: "…",
  ocsf: {
    class_uid: 4001,
    metadata: {version: "1.5.0"},
    activity_id: 1,
    time: 2026-01-01,
    unmapped: {nested: [1, "two", null]},
  },
}
ocsf = ocsf_cast(ocsf, encode_variants=true, timestamp_to_ms=true)
```

```tql
{
  raw_data: "…",
  ocsf: {
    class_uid: 4001,
    metadata: {
      version: "1.5.0",
    },
    activity_id: 1,
    time: 1767225600000,
    unmapped: "{\"nested\":[1,\"two\",null]}",
  },
}
```

### Cast a list of OCSF events

```tql
from {
  events: [
    {class_uid: 4001, metadata: {version: "1.5.0"}, src_endpoint: {ip: 192.0.2.1}},
    {class_uid: 1001, metadata: {version: "1.5.0"}, activity_id: "bad"},
  ],
}
events = events.map(x => ocsf_cast(x))
```

```tql
{
  events: [
    {
      class_uid: 4001,
      metadata: {
        version: "1.5.0",
      },
      src_endpoint: {
        ip: 192.0.2.1,
      },
    },
    {
      class_uid: 1001,
      metadata: {
        version: "1.5.0",
      },
      activity_id: null,
    },
  ],
}
```

The second event emits a warning because `activity_id` must be an integer. Both events also emit warnings for the required fields they lack.

### Keep events that fail to cast

```tql
from {ocsf: {class_uid: 1001, metadata: {version: "1.5.0"}, activity_id: 1}},
     {ocsf: {class_uid: 1001}}
validated = ocsf_cast(ocsf)
```

```tql
{
  ocsf: {
    class_uid: 1001,
    metadata: {
      version: "1.5.0",
    },
    activity_id: 1,
  },
  validated: {
    class_uid: 1001,
    metadata: {
      version: "1.5.0",
    },
    activity_id: 1,
  },
}
{
  ocsf: {
    class_uid: 1001,
  },
  validated: null,
}
```

The second event emits a warning because it lacks `metadata`. The first event emits warnings for the required fields it lacks, but still casts. A subsequent `where validated == null` selects the events to inspect or route elsewhere.

### Find missing required fields

```tql
let $event = {
  class_uid: 3002,
  category_uid: 3,
  activity_id: 1,
  type_uid: 300201,
  severity_id: 1,
  time: 2026-01-01,
  metadata: {
    version: "1.9.0",
    product: {name: "OpenSSH", vendor_name: "OpenBSD"},
  },
  service: {name: "sshd"},
}
from {ocsf: $event},
     {ocsf: {...$event, user: {type_id: 1}}}
ocsf = ocsf_cast(ocsf)
```

The function returns both events unchanged. The first event emits a warning because Authentication requires `user`. The second event has a `user`, but emits a warning because a user needs at least one of `account`, `name`, or `uid`.

## See Also

* [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md)
* [`ocsf_derive`](https://tenzir.com/docs/reference/functions/ocsf_derive.md)
* [`ocsf_trim`](https://tenzir.com/docs/reference/functions/ocsf_trim.md)
* [Map to OCSF](../../guides/normalize/map-to-ocsf.md)
