---
title: "context::inspect"
canonical: https://tenzir.com/docs/reference/operators/context/inspect
source: https://tenzir.com/docs/reference/operators/context/inspect.md
section: "Docs"
---

# context::inspect

> Resets a context.

Resets a context.

```tql
context::inspect name:string
```

## Description

The `context::inspect` operator shows details about a specified context.

### `name: string`

The name of the context to inspect.

## Examples

### Inspect a context

Add data to the lookup table:

```tql
from {x:1, y:"a"},
     {x:2, y:"b"}
context::update "ctx", key=x, value=y
```

Retrieve the lookup table contents:

```tql
context::inspect "ctx"
```

```tql
{key: 2, value: "b"}
{key: 1, value: "a"}
```

## See Also

* [`context::create_bloom_filter`](https://tenzir.com/docs/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](https://tenzir.com/docs/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](https://tenzir.com/docs/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](https://tenzir.com/docs/reference/operators/context/enrich.md)
* [`context::erase`](https://tenzir.com/docs/reference/operators/context/erase.md)
* [`context::list`](https://tenzir.com/docs/reference/operators/context/list.md)
* [`context::load`](https://tenzir.com/docs/reference/operators/context/load.md)
* [`context::remove`](https://tenzir.com/docs/reference/operators/context/remove.md)
* [`context::reset`](https://tenzir.com/docs/reference/operators/context/reset.md)
* [`context::save`](https://tenzir.com/docs/reference/operators/context/save.md)
* [`context::update`](https://tenzir.com/docs/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)
