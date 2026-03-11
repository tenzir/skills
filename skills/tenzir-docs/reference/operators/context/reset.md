# context::reset


Resets a context.

```tql
context::reset name:string
```

## Description

The `context::reset` operator erases all data that has been added with `context::update`.

### `name: string`

The name of the context to reset.

## Examples

### Reset a context

```tql
context::reset "ctx"
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
* [`context::remove`](/reference/operators/context/remove.md)
* [`context::save`](/reference/operators/context/save.md)
* [`context::update`](/reference/operators/context/update.md)