---
title: "context_erase"
canonical: https://tenzir.com/docs/reference/operators/context_erase
source: https://tenzir.com/docs/reference/operators/context_erase.md
section: "Docs"
---

# context_erase

> Removes entries from a context.

Removes entries from a context.

```tql
context_erase name:string, key=any
```

## Description

The `context_erase` operator removes data from a context.

Use the `key` argument to specify the field in the input that should be deleted from the context.

### `name: string`

The name of the context to remove entries from.

### `key = any`

The field that represents the enrichment key in the data.

## Examples

### Delete entries from a context

```plaintext
from {network: 10.0.0.1/16}
context_erase "network-classification", key=network
```

## See Also

* [`context_create_bloom_filter`](context_create_bloom_filter.md)
* [`context_create_geoip`](context_create_geoip.md)
* [`context_create_lookup_table`](context_create_lookup_table.md)
* [`context_enrich`](context_enrich.md)
* [`context_inspect`](context_inspect.md)
* [`context_list`](context_list.md)
* [`context_load`](context_load.md)
* [`context_remove`](context_remove.md)
* [`context_reset`](context_reset.md)
* [`context_save`](context_save.md)
* [`context_update`](context_update.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
