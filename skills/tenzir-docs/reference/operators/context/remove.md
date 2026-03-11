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

* [`context::create_bloom_filter`](/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](/reference/operators/context/enrich.md)
* [`context::erase`](/reference/operators/context/erase.md)
* [`context::inspect`](/reference/operators/context/inspect.md)
* [`context::list`](/reference/operators/context/list.md)
* [`context::load`](/reference/operators/context/load.md)
* [`context::reset`](/reference/operators/context/reset.md)
* [`context::save`](/reference/operators/context/save.md)
* [`context::update`](/reference/operators/context/update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)