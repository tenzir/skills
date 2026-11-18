---
title: "context_save"
canonical: https://tenzir.com/docs/v6.22.0/reference/operators/context_save
source: https://tenzir.com/docs/v6.22.0/reference/operators/context_save.md
section: "Docs"
---

# context_save

> Saves context state.

Saves context state.

```tql
context_save name:string
```

## Description

The `context_save` operator dumps the state of the specified context into its (binary) output.

### `name: string`

The name of the context whose state to save.

## Examples

### Store the database of a GeoIP context

```tql
context_save "ctx"
to_file "snapshot.mmdb"
```

## See Also

* [`context_create_bloom_filter`](context_create_bloom_filter.md)
* [`context_create_geoip`](context_create_geoip.md)
* [`context_create_lookup_table`](context_create_lookup_table.md)
* [`context_enrich`](context_enrich.md)
* [`context_erase`](context_erase.md)
* [`context_inspect`](context_inspect.md)
* [`context_list`](context_list.md)
* [`context_load`](context_load.md)
* [`context_remove`](context_remove.md)
* [`context_reset`](context_reset.md)
* [`context_update`](context_update.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
