---
title: "pipeline::detach"
canonical: https://tenzir.com/docs/reference/operators/pipeline/detach
source: https://tenzir.com/docs/reference/operators/pipeline/detach.md
section: "Docs"
---

# pipeline::detach

> Starts a pipeline in the node.

Starts a pipeline in the node.

```tql
pipeline::detach { … }, [id=string]
```

## Description

The `pipeline::detach` operator starts a hidden managed pipeline in the node, and returns as soon as the pipeline has started.

Subject to Change

This operator primarily exists for testing purposes, where it is often required to run pipelines in the background, but to be able to wait until the pipeline has started. The operator may change without further notice.

### `id = string (optional)`

Sets the pipeline’s ID explicitly, instead of assigning a random ID. This corresponds to the `id` field in the output of `pipeline::list`, and the `pipeline_id` field in the output of `metrics` and `diagnostics`.

## Examples

### Run a pipeline in the background

```tql
pipeline::detach {
  every 1min {
    version
  }
  select version
  to_stdout {
    write_lines
  }
}
```

## See Also

* [`pipeline::list`](https://tenzir.com/docs/reference/operators/pipeline/list.md)
* [`pipeline::run`](https://tenzir.com/docs/reference/operators/pipeline/run.md)
