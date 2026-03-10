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

* [`context::create_bloom_filter`](create_bloom_filter.md)
* [`context::create_geoip`](create_geoip.md)
* [`context::enrich`](enrich.md)
* [`context::erase`](erase.md)
* [`context::inspect`](inspect.md)
* [`context::list`](list.md)
* [`context::load`](load.md)
* [`context::remove`](remove.md)
* [`context::reset`](reset.md)
* [`context::save`](save.md)
* [`context::update`](update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)
* [Enrich with threat intel](../../../guides/enrichment/enrich-with-threat-intel.md)
* [Enrich with network inventory](../../../guides/enrichment/enrich-with-network-inventory.md)
* [Enrichment](../../../explanations/enrichment.md)