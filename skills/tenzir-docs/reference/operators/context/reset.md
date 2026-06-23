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

* [`context::create_bloom_filter`](http://docs.tenzir.com/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](http://docs.tenzir.com/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](http://docs.tenzir.com/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](http://docs.tenzir.com/reference/operators/context/enrich.md)
* [`context::erase`](http://docs.tenzir.com/reference/operators/context/erase.md)
* [`context::inspect`](http://docs.tenzir.com/reference/operators/context/inspect.md)
* [`context::list`](http://docs.tenzir.com/reference/operators/context/list.md)
* [`context::load`](http://docs.tenzir.com/reference/operators/context/load.md)
* [`context::remove`](http://docs.tenzir.com/reference/operators/context/remove.md)
* [`context::save`](http://docs.tenzir.com/reference/operators/context/save.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)