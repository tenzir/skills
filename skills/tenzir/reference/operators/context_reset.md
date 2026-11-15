---
title: "context_reset"
canonical: https://tenzir.com/docs/reference/operators/context_reset
source: https://tenzir.com/docs/reference/operators/context_reset.md
section: "Docs"
---

# context_reset

> Resets a context.

Resets a context.

```tql
context_reset name:string
```

## Description

The `context_reset` operator erases all data that has been added with `context_update`.

### `name: string`

The name of the context to reset.

## Examples

### Reset a context

```tql
context_reset "ctx"
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
* [`context_save`](context_save.md)
* [`context_update`](context_update.md)
