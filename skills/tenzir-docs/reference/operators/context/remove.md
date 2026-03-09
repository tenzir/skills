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

* [`context::create_bloom_filter`](create_bloom_filter.md)
* [`context::create_geoip`](create_geoip.md)
* [`context::create_lookup_table`](create_lookup_table.md)
* [`context::enrich`](enrich.md)
* [`context::erase`](erase.md)
* [`context::inspect`](inspect.md)
* [`context::list`](list.md)
* [`context::load`](load.md)
* [`context::reset`](reset.md)
* [`context::save`](save.md)
* [`context::update`](update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)