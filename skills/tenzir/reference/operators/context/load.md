# context::load

> Loads context state.

Loads context state.

```tql
context::load name:string
```

## Description

The `context::load` operator replaces the state of the specified context with its (binary) input.

### `name: string`

The name of the context whose state to update.

## Examples

### Replace the database of a GeoIP context

```tql
from_file "ultra-high-res.mmdb", mmap=true
context::load "ctx"
```

## See Also

* [`context::create_bloom_filter`](https://tenzir.com/docs/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](https://tenzir.com/docs/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](https://tenzir.com/docs/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](https://tenzir.com/docs/reference/operators/context/enrich.md)
* [`context::erase`](https://tenzir.com/docs/reference/operators/context/erase.md)
* [`context::inspect`](https://tenzir.com/docs/reference/operators/context/inspect.md)
* [`context::list`](https://tenzir.com/docs/reference/operators/context/list.md)
* [`context::remove`](https://tenzir.com/docs/reference/operators/context/remove.md)
* [`context::reset`](https://tenzir.com/docs/reference/operators/context/reset.md)
* [`context::save`](https://tenzir.com/docs/reference/operators/context/save.md)
* [`context::update`](https://tenzir.com/docs/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)
