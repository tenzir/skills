---
title: "context::reset"
canonical: https://tenzir.com/docs/reference/operators/context/reset
source: https://tenzir.com/docs/reference/operators/context/reset.md
section: "Docs"
---

# context::reset

> Resets a context.

Resets a context.

```tql
context::reset name:string
```

## Description

The `context::reset` operator erases all data that has been added with `context::update`.

### `name: string`

The name of the context to reset.

## Examples

### Reset a context

```tql
context::reset "ctx"
```

## See Also

* [`context::create_bloom_filter`](https://tenzir.com/docs/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](https://tenzir.com/docs/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](https://tenzir.com/docs/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](https://tenzir.com/docs/reference/operators/context/enrich.md)
* [`context::erase`](https://tenzir.com/docs/reference/operators/context/erase.md)
* [`context::inspect`](https://tenzir.com/docs/reference/operators/context/inspect.md)
* [`context::list`](https://tenzir.com/docs/reference/operators/context/list.md)
* [`context::load`](https://tenzir.com/docs/reference/operators/context/load.md)
* [`context::remove`](https://tenzir.com/docs/reference/operators/context/remove.md)
* [`context::save`](https://tenzir.com/docs/reference/operators/context/save.md)
* [`context::update`](https://tenzir.com/docs/reference/operators/context/update.md)
