---
title: "context_create_lookup_table"
canonical: https://tenzir.com/docs/reference/operators/context_create_lookup_table
source: https://tenzir.com/docs/reference/operators/context_create_lookup_table.md
section: "Docs"
---

# context_create_lookup_table

> Creates a lookup table context.

Creates a lookup table context.

```tql
context_create_lookup_table name:string
```

## Description

The `context_create_lookup_table` operator constructs a new context of type [lookup table](../../explanations/enrichment.md#lookup-table).

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
context_create_lookup_table "ctx"
```

## See Also

* [`context_create_bloom_filter`](context_create_bloom_filter.md)
* [`context_create_geoip`](context_create_geoip.md)
* [`context_enrich`](context_enrich.md)
* [`context_erase`](context_erase.md)
* [`context_inspect`](context_inspect.md)
* [`context_list`](context_list.md)
* [`context_load`](context_load.md)
* [`context_remove`](context_remove.md)
* [`context_reset`](context_reset.md)
* [`context_save`](context_save.md)
* [`context_update`](context_update.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
* [Enrich with threat intel](../../guides/enrich/enrich-with-threat-intel.md)
* [Enrich with asset inventory](../../guides/enrich/enrich-with-asset-inventory.md)
* [Enrichment](../../explanations/enrichment.md)
