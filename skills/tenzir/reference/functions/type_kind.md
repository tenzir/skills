---
title: "type_kind"
canonical: https://tenzir.com/docs/reference/functions/type_kind
source: https://tenzir.com/docs/reference/functions/type_kind.md
section: "Docs"
---

# type_kind

> Retrieves the kind of the type of a value.

Retrieves the kind of the type of a value.

```tql
type_kind(x:any) -> string
```

## Description

The `type_kind` function returns the kind of the type of `x` as a string. The result is one of `null`, `bool`, `int`, `uint`, `float`, `duration`, `time`, `string`, `blob`, `ip`, `subnet`, `secret`, `list`, or `record`.

A `null` value always has the kind `null`, even in a field that holds values of another kind in other events. The result describes only the outermost type: a list has the kind `list` and a record the kind `record`, regardless of their elements and fields.

## Examples

### Retrieve the kinds of fields

```tql
from {
  str: "hello",
  num: 42,
  float: 3.14,
  arr: [1, 2, 3],
  obj: {key: "value"},
}
this = {
  str: str.type_kind(),
  num: num.type_kind(),
  float: float.type_kind(),
  arr: arr.type_kind(),
  obj: obj.type_kind(),
}
```

```tql
{
  str: "string",
  num: "int",
  float: "float",
  arr: "list",
  obj: "record",
}
```

### Inspect a field with values of different kinds

```tql
from {x: 1}, {x: "a"}, {x: null}
kind = x.type_kind()
```

```tql
{x: 1, kind: "int"}
{x: "a", kind: "string"}
{x: null, kind: "null"}
```

### Keep only events where a field is a string

```tql
from {x: 1}, {x: "a"}, {x: null}, {x: "b"}
where x.type_kind() == "string"
```

```tql
{x: "a"}
{x: "b"}
```

## See Also

* [`type_id`](https://tenzir.com/docs/reference/functions/type_id.md)
* [`type_of`](https://tenzir.com/docs/reference/functions/type_of.md)
