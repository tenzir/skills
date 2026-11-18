---
title: "context_create_bloom_filter"
canonical: https://tenzir.com/docs/v6.22.0/reference/operators/context_create_bloom_filter
source: https://tenzir.com/docs/v6.22.0/reference/operators/context_create_bloom_filter.md
section: "Docs"
---

# context_create_bloom_filter

> Creates a Bloom filter context.

Creates a Bloom filter context.

```tql
context_create_bloom_filter name:string, capacity=int, fp_probability=float
```

## Description

The `context_create_bloom_filter` operator constructs a new context of type [Bloom filter](../../explanations/enrichment.md#bloom-filter).

To find suitable values for the capacity and false-positive probability, consult Thomas Hurst’s [Bloom Filter Calculator](https://hur.st/bloomfilter/). The parameter `n` corresponds to `capacity` and `p` to `fp_probability`.

You can also create a Bloom filter context as code by adding it to `tenzir.contexts` in your `tenzir.yaml`:

\<prefix>/etc/tenzir/tenzir.yaml

```yaml
tenzir:
  contexts:
    my-iocs:
      type: bloom-filter
      arguments:
        capacity: 1B
        fp-probability: 0.001
```

Making changes to `arguments` of an already created context has no effect.

### `name: string`

The name of the new Bloom filter.

### `capacity = uint`

The maximum number of items in the filter that maintain the false positive probability. Adding more elements does not yield an error, but lookups will more likely return false positives.

### `fp_probability = float`

The false-positive probability of the Bloom filter.

## Examples

### Create a new Bloom filter context

```tql
context_create_bloom_filter "ctx", capacity=1B, fp_probability=0.001
```

## See Also

* [`context_create_geoip`](context_create_geoip.md)
* [`context_create_lookup_table`](context_create_lookup_table.md)
* [`context_enrich`](context_enrich.md)
* [`context_erase`](context_erase.md)
* [`context_inspect`](context_inspect.md)
* [`context_list`](context_list.md)
* [`context_load`](context_load.md)
* [`context_remove`](context_remove.md)
* [`context_reset`](context_reset.md)
* [`context_save`](context_save.md)
* [`context_update`](context_update.md)
* [Enrichment](../../explanations/enrichment.md)
