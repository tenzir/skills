# context::remove


Deletes a context.

```tql
context::remove name:string
```

## Description

The `context::remove` operator deletes the specified context.

### `name: string`

The name of the context to delete.

## Examples

### Delete a context

```tql
context::delete "ctx"
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
* [`context::reset`](http://docs.tenzir.com/reference/operators/context/reset.md)
* [`context::save`](http://docs.tenzir.com/reference/operators/context/save.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)