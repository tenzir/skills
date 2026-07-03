# context::save

> Saves context state.

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

* [`context::create_bloom_filter`](https://tenzir.com/docs/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](https://tenzir.com/docs/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](https://tenzir.com/docs/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](https://tenzir.com/docs/reference/operators/context/enrich.md)
* [`context::erase`](https://tenzir.com/docs/reference/operators/context/erase.md)
* [`context::inspect`](https://tenzir.com/docs/reference/operators/context/inspect.md)
* [`context::list`](https://tenzir.com/docs/reference/operators/context/list.md)
* [`context::load`](https://tenzir.com/docs/reference/operators/context/load.md)
* [`context::remove`](https://tenzir.com/docs/reference/operators/context/remove.md)
* [`context::reset`](https://tenzir.com/docs/reference/operators/context/reset.md)
* [`context::update`](https://tenzir.com/docs/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)
