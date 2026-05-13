# every


Runs a pipeline periodically at a fixed interval.

```tql
every interval:duration { … }
```

## Description

The `every` operator repeats running a pipeline indefinitely at a fixed interval. The first run starts directly when the outer pipeline itself starts.

Every `interval`, the executor spawns a new sub-pipeline that runs to completion. If the sub-pipeline runs longer than `interval`, the next run starts immediately.

Sub-pipelines must terminate on their own

`every` never stops a sub-pipeline — it only waits for it to finish. Operators that run indefinitely, such as [`summarize`](/reference/operators/summarize.md) without a `frequency` option, will block `every` from ever starting the next iteration. For periodic aggregation use the `options={frequency}` parameter of [`summarize`](/reference/operators/summarize.md) directly instead of wrapping it inside `every`.

## Examples

### Produce one event per second and enumerate the result

```tql
every 1s {
  from {}
}
enumerate
```

```tql
{"#": 0} // immediately
{"#": 1} // after 1s
{"#": 2} // after 2s
{"#": 3} // after 3s
// … continues like this
```

### Aggregate metrics periodically with `summarize`

Using `every` with [`summarize`](/reference/operators/summarize.md) does not work as expected because `summarize` never terminates on its own — `every` would wait forever and the aggregation would never emit results.

Instead, use the `options={frequency}` parameter of [`summarize`](/reference/operators/summarize.md):

```tql
from_tcp "127.0.0.1:5432" { read_json }
summarize events=count(data), options={frequency: 5m}
```

### Fetch the results from an API every 10 minutes

```tql
every 10min {
  from_http "example.org/api/threats" {
    read_json
  }
}
publish "threat-feed"
```

## See Also

* [`cron`](/reference/operators/cron.md)
* [`each`](/reference/operators/each.md)
* [`summarize`](/reference/operators/summarize.md)
* [Work with time](../../guides/transformation/work-with-time.md)
* [Work with lookup tables](../../guides/enrichment/work-with-lookup-tables.md)
* [Write a package](../../tutorials/write-a-package.md)