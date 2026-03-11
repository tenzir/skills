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

* [`context::create_bloom_filter`](/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](/reference/operators/context/enrich.md)
* [`context::inspect`](/reference/operators/context/inspect.md)
* [`context::list`](/reference/operators/context/list.md)
* [`context::load`](/reference/operators/context/load.md)
* [`context::remove`](/reference/operators/context/remove.md)
* [`context::reset`](/reference/operators/context/reset.md)
* [`context::save`](/reference/operators/context/save.md)
* [`context::update`](/reference/operators/context/update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)