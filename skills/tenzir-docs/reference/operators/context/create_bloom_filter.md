# context::create_bloom_filter


Creates a Bloom filter context.

```tql
context::create_bloom_filter name:string, capacity=int, fp_probability=float
```

## Description

The `context::create_bloom_filter` operator constructs a new context of type [Bloom filter](../../../explanations/enrichment.md#bloom-filter).

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
context::create_bloom_filter "ctx", capacity=1B, fp_probability=0.001
```

## See Also

* [`context::create_geoip`](http://docs.tenzir.com/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](http://docs.tenzir.com/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](http://docs.tenzir.com/reference/operators/context/enrich.md)
* [`context::erase`](http://docs.tenzir.com/reference/operators/context/erase.md)
* [`context::inspect`](http://docs.tenzir.com/reference/operators/context/inspect.md)
* [`context::list`](http://docs.tenzir.com/reference/operators/context/list.md)
* [`context::load`](http://docs.tenzir.com/reference/operators/context/load.md)
* [`context::remove`](http://docs.tenzir.com/reference/operators/context/remove.md)
* [`context::reset`](http://docs.tenzir.com/reference/operators/context/reset.md)
* [`context::save`](http://docs.tenzir.com/reference/operators/context/save.md)
* [`context::update`](http://docs.tenzir.com/reference/operators/context/update.md)
* [Enrichment](../../../explanations/enrichment.md)