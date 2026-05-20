# every


Runs a pipeline periodically at a fixed interval.

```tql
every interval:duration { … }
```

## Description

The `every` operator repeats running a pipeline indefinitely at a fixed interval. The first run starts directly when the outer pipeline itself starts.

Every `interval`, the executor spawns a new sub-pipeline. When the interval elapses, `every` stops the inputs of the running sub-pipeline, waits for it to finish processing, and then starts a new one. This means sub-pipelines with sink operators work as expected — events flow in for the duration of the interval, then the sub-pipeline flushes and restarts. Sub-pipelines without inputs (pure sources) must terminate on their own; if they run longer than `interval`, the next run starts immediately after.

The sub-pipeline either emits events—which are forwarded as the operator’s output—or ends with a sink, in which case `every` itself becomes a sink. The sub-pipeline must not produce bytes.

Source sub-pipelines must terminate on their own

`every` stops inputs to a sub-pipeline but cannot stop operators that produce data indefinitely on their own. Source operators like [`subscribe`](/reference/operators/subscribe.md) inside an `every` block will prevent the next iteration from starting.

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

### Periodically flush buffered events to an HTTP endpoint

```tql
subscribe "event-stream"
every 30s {
  to_http "https://example.org/api/ingest" {
    write_json
  }
}
```

Events flow into the sub-pipeline continuously. Every 30 seconds, `every` stops the input, causing [`to_http`](/reference/operators/to_http.md) to finish the request and wait for the response. Then a new sub-pipeline starts.

### Aggregate metrics periodically with `summarize`

```tql
subscribe "event-stream"
every 5min {
  summarize events=count(data)
}
```

When the interval elapses, `every` stops the input, which causes [`summarize`](/reference/operators/summarize.md) to emit its result. Then the sub-pipeline restarts for the next interval.

### Fetch the results from an API every 10 minutes

```tql
every 10min {
  from_http "example.org/api/threats" {
    read_json
  }
}
publish "threat-feed"
```

### Periodically import a snapshot

When the sub-pipeline ends with a sink, `every` itself becomes a sink:

```tql
every 1h {
  from_http "example.org/api/inventory" {
    read_json
  }
  import
}
```

## See Also

* [`cron`](/reference/operators/cron.md)
* [`each`](/reference/operators/each.md)
* [`to_http`](/reference/operators/to_http.md)
* [`summarize`](/reference/operators/summarize.md)
* [Fetch via HTTP and APIs](../../guides/collecting/fetch-via-http-and-apis.md)
* [Work with time](../../guides/transformation/work-with-time.md)
* [Work with lookup tables](../../guides/enrichment/work-with-lookup-tables.md)
* [Write a package](../../tutorials/write-a-package.md)