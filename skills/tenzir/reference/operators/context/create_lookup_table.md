# context::create_lookup_table

> Creates a lookup table context.

Creates a lookup table context.

```tql
context::create_lookup_table name:string
```

## Description

The `context::create_lookup_table` operator constructs a new context of type [lookup table](../../../explanations/enrichment.md#lookup-table).

You can also create a lookup table as code by adding it to `tenzir.contexts` in your `tenzir.yaml`:

\<prefix>/etc/tenzir/tenzir.yaml

```yaml
tenzir:
  contexts:
    my-table:
      type: lookup-table
```

### `name: string`

The name of the new lookup table.

## Examples

### Create a new lookup table context

```tql
context::create_lookup_table "ctx"
```

## See Also

* [`context::create_bloom_filter`](https://tenzir.com/docs/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](https://tenzir.com/docs/reference/operators/context/create_geoip.md)
* [`context::enrich`](https://tenzir.com/docs/reference/operators/context/enrich.md)
* [`context::erase`](https://tenzir.com/docs/reference/operators/context/erase.md)
* [`context::inspect`](https://tenzir.com/docs/reference/operators/context/inspect.md)
* [`context::list`](https://tenzir.com/docs/reference/operators/context/list.md)
* [`context::load`](https://tenzir.com/docs/reference/operators/context/load.md)
* [`context::remove`](https://tenzir.com/docs/reference/operators/context/remove.md)
* [`context::reset`](https://tenzir.com/docs/reference/operators/context/reset.md)
* [`context::save`](https://tenzir.com/docs/reference/operators/context/save.md)
* [`context::update`](https://tenzir.com/docs/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)
* [Enrich with threat intel](../../../guides/enrichment/enrich-with-threat-intel.md)
* [Enrich with asset inventory](../../../guides/enrichment/enrich-with-asset-inventory.md)
* [Enrichment](../../../explanations/enrichment.md)
