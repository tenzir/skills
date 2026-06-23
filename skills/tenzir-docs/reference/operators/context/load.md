# context::load


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

* [`context::create_bloom_filter`](http://docs.tenzir.com/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](http://docs.tenzir.com/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](http://docs.tenzir.com/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](http://docs.tenzir.com/reference/operators/context/enrich.md)
* [`context::erase`](http://docs.tenzir.com/reference/operators/context/erase.md)
* [`context::inspect`](http://docs.tenzir.com/reference/operators/context/inspect.md)
* [`context::list`](http://docs.tenzir.com/reference/operators/context/list.md)
* [`context::remove`](http://docs.tenzir.com/reference/operators/context/remove.md)
* [`context::reset`](http://docs.tenzir.com/reference/operators/context/reset.md)
* [`context::save`](http://docs.tenzir.com/reference/operators/context/save.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)