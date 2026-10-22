---
title: "type_of"
canonical: https://tenzir.com/docs/reference/functions/type_of
source: https://tenzir.com/docs/reference/functions/type_of.md
section: "Docs"
---

# type_of

> Retrieves the type definition of an expression.

Retrieves the type definition of an expression.

Deprecated

This function is deprecated and emits a warning. Use [`type_kind`](https://tenzir.com/docs/reference/functions/type_kind.md) instead: replace `type_of(x).kind` with `type_kind(x)`.

Until its removal, `type_of` reports the type names of the old data model, such as `int64`, `uint64`, and `double`, where [`type_kind`](https://tenzir.com/docs/reference/functions/type_kind.md) reports `int`, `uint`, and `float`.

```tql
type_of(x:any) -> record
```

## Description

The `type_of` function returns the type definition of the given value `x`.

Subject to change

This function is designed for internal use of the Tenzir Platform and its output format is subject to change without notice.

## Examples

### Retrieve the type definition of a schema

```tql
from {x: 1, y: "2"}
this = type_of(this)
```

```tql
{
  name: null,
  kind: "record",
  attributes: [],
  state: {
    fields: [
      {
        name: "x",
        type: {
          name: null,
          kind: "int64",
          attributes: [],
          state: null,
        },
      },
      {
        name: "y",
        type: {
          name: null,
          kind: "string",
          attributes: [],
          state: null,
        },
      },
    ],
  },
}
```

## See Also

* [`type_id`](https://tenzir.com/docs/reference/functions/type_id.md)
* [`type_kind`](https://tenzir.com/docs/reference/functions/type_kind.md)
