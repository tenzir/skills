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

* [`context::create_bloom_filter`](/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](/reference/operators/context/create_geoip.md)
* [`context::enrich`](/reference/operators/context/enrich.md)
* [`context::erase`](/reference/operators/context/erase.md)
* [`context::inspect`](/reference/operators/context/inspect.md)
* [`context::list`](/reference/operators/context/list.md)
* [`context::load`](/reference/operators/context/load.md)
* [`context::remove`](/reference/operators/context/remove.md)
* [`context::reset`](/reference/operators/context/reset.md)
* [`context::save`](/reference/operators/context/save.md)
* [`context::update`](/reference/operators/context/update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)
* [Enrich with threat intel](../../../guides/enrichment/enrich-with-threat-intel.md)
* [Enrich with network inventory](../../../guides/enrichment/enrich-with-network-inventory.md)
* [Enrichment](../../../explanations/enrichment.md)