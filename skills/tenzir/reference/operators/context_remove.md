---
title: "context_remove"
canonical: https://tenzir.com/docs/reference/operators/context_remove
source: https://tenzir.com/docs/reference/operators/context_remove.md
section: "Docs"
---

# context_remove

> Deletes a context.

Deletes a context.

```tql
context_remove name:string
```

## Description

The `context_remove` operator deletes the specified context.

### `name: string`

The name of the context to delete.

## Examples

### Delete a context

```tql
context_remove "ctx"
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
* [`context_reset`](context_reset.md)
* [`context_save`](context_save.md)
* [`context_update`](context_update.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
