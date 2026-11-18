---
title: "context_load"
canonical: https://tenzir.com/docs/v6.22.0/reference/operators/context_load
source: https://tenzir.com/docs/v6.22.0/reference/operators/context_load.md
section: "Docs"
---

# context_load

> Loads context state.

Loads context state.

```tql
context_load name:string
```

## Description

The `context_load` operator replaces the state of the specified context with its (binary) input.

### `name: string`

The name of the context whose state to update.

## Examples

### Replace the database of a GeoIP context

```tql
from_file "ultra-high-res.mmdb", mmap=true
context_load "ctx"
```

## See Also

* [`context_create_bloom_filter`](context_create_bloom_filter.md)
* [`context_create_geoip`](context_create_geoip.md)
* [`context_create_lookup_table`](context_create_lookup_table.md)
* [`context_enrich`](context_enrich.md)
* [`context_erase`](context_erase.md)
* [`context_inspect`](context_inspect.md)
* [`context_list`](context_list.md)
* [`context_remove`](context_remove.md)
* [`context_reset`](context_reset.md)
* [`context_save`](context_save.md)
* [`context_update`](context_update.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
