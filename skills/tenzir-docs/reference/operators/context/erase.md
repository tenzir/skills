# context::erase


Removes entries from a context.

```tql
context::erase name:string, key=any
```

## Description

The `context::erase` operator removes data from a context.

Use the `key` argument to specify the field in the input that should be deleted from the context.

### `name: string`

The name of the context to remove entries from.

### `key = any`

The field that represents the enrichment key in the data.

## Examples

### Delete entries from a context

```plaintext
from {network: 10.0.0.1/16}
context::erase "network-classification", key=network
```

## See Also

* [`context::create_bloom_filter`](http://docs.tenzir.com/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](http://docs.tenzir.com/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](http://docs.tenzir.com/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](http://docs.tenzir.com/reference/operators/context/enrich.md)
* [`context::inspect`](http://docs.tenzir.com/reference/operators/context/inspect.md)
* [`context::list`](http://docs.tenzir.com/reference/operators/context/list.md)
* [`context::load`](http://docs.tenzir.com/reference/operators/context/load.md)
* [`context::remove`](http://docs.tenzir.com/reference/operators/context/remove.md)
* [`context::reset`](http://docs.tenzir.com/reference/operators/context/reset.md)
* [`context::save`](http://docs.tenzir.com/reference/operators/context/save.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)