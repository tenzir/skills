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
load_file "ultra-high-res.mmdb", mmap=true
context::load "ctx"
```

## See Also

* [`context::create_bloom_filter`](/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](/reference/operators/context/enrich.md)
* [`context::erase`](/reference/operators/context/erase.md)
* [`context::inspect`](/reference/operators/context/inspect.md)
* [`context::list`](/reference/operators/context/list.md)
* [`context::remove`](/reference/operators/context/remove.md)
* [`context::reset`](/reference/operators/context/reset.md)
* [`context::save`](/reference/operators/context/save.md)
* [`context::update`](/reference/operators/context/update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)