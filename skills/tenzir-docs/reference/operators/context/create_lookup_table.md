# context::create_lookup_table


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

* [`context::create_bloom_filter`](http://docs.tenzir.com/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](http://docs.tenzir.com/reference/operators/context/create_geoip.md)
* [`context::enrich`](http://docs.tenzir.com/reference/operators/context/enrich.md)
* [`context::erase`](http://docs.tenzir.com/reference/operators/context/erase.md)
* [`context::inspect`](http://docs.tenzir.com/reference/operators/context/inspect.md)
* [`context::list`](http://docs.tenzir.com/reference/operators/context/list.md)
* [`context::load`](http://docs.tenzir.com/reference/operators/context/load.md)
* [`context::remove`](http://docs.tenzir.com/reference/operators/context/remove.md)
* [`context::reset`](http://docs.tenzir.com/reference/operators/context/reset.md)
* [`context::save`](http://docs.tenzir.com/reference/operators/context/save.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)
* [Use lookup tables](../../../guides/enrichment/use-lookup-tables.md)
* [Enrich with threat intel](../../../guides/enrichment/enrich-with-threat-intel.md)
* [Enrich with asset inventory](../../../guides/enrichment/enrich-with-asset-inventory.md)
* [Enrichment](../../../explanations/enrichment.md)