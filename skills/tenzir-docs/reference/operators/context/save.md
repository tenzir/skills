# context::save


Saves context state.

```tql
context::save name:string
```

## Description

The `context::save` operator dumps the state of the specified context into its (binary) output.

### `name: string`

The name of the context whose state to save.

## Examples

### Store the database of a GeoIP context

```tql
context::save "ctx"
to_file "snapshot.mmdb"
```

## See Also

* [`context::create_bloom_filter`](http://docs.tenzir.com/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](http://docs.tenzir.com/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](http://docs.tenzir.com/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](http://docs.tenzir.com/reference/operators/context/enrich.md)
* [`context::erase`](http://docs.tenzir.com/reference/operators/context/erase.md)
* [`context::inspect`](http://docs.tenzir.com/reference/operators/context/inspect.md)
* [`context::list`](http://docs.tenzir.com/reference/operators/context/list.md)
* [`context::load`](http://docs.tenzir.com/reference/operators/context/load.md)
* [`context::remove`](http://docs.tenzir.com/reference/operators/context/remove.md)
* [`context::reset`](http://docs.tenzir.com/reference/operators/context/reset.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)