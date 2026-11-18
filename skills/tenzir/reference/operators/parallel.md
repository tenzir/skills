---
title: "parallel"
canonical: https://tenzir.com/docs/reference/operators/parallel
source: https://tenzir.com/docs/reference/operators/parallel.md
section: "Docs"
---

# parallel

> Annotates desired parallelization degree.

Annotates desired parallelization degree.

```tql
parallel [jobs:int, fuse=string, limit_partitions=int] { … }
```

## Description

The [`parallel`](parallel.md) operator marks the operators in its subpipeline to run on multiple cores. It applies the same mechanism as the `// parallelism:` comment, which covers a whole pipeline, to a section of one.

Tenzir replicates only those operators that can work on any batch they receive, such as [`where`](where.md), [`drop`](drop.md), and assignments, including those that call [`ocsf_cast`](../functions/ocsf_cast.md). Operators that combine related events, such as [`summarize`](summarize.md), [`group`](group.md), and [`deduplicate`](deduplicate.md), receive a stream partitioned by their own key fields, so every event of a group reaches the instance that owns it. Tenzir leaves the remaining operators, including sources and most sinks, at a single instance. Our explanation of [parallel execution](../../explanations/executor.md#parallel-execution) covers which operators fall into which category.

Reach for `parallel` when profiling points at a section of a pipeline rather than at the pipeline as a whole. When you run a pipeline with `tenzir run` on your machine, prefer the `// parallelism:` comment to parallelize all of it.

Parallelism in deployments

A deployment runs its pipelines without the `// parallelism:` comment and the `--parallelism` option. To parallelize a pipeline that a deployment runs, wrap its expensive section in `parallel`.

Parallelism reorders events

Operator instances work at different speeds, so a block can emit events in a different order than it received them. Avoid `parallel` when the event order carries meaning.

### `jobs: int (optional)`

The number of instances to run each replicated operator on. Must be greater than zero.

Defaults to `8`, or to the number of available cores if that is lower.

### `fuse = string (optional)`

Controls which operator-to-operator channels inside the block are [fused](../../explanations/executor.md#operator-fusion), i.e., run run-to-completion without a buffer in between:

* `"none"`: never fuse a channel.
* `"parallel"`: fuse only matched lane-to-lane channels between parallelizable operators.
* `"all"`: fuse every channel.

Defaults to the surrounding pipeline’s setting, which is `"parallel"` unless a `// parallelism:` directive in a local run says otherwise.

### `limit_partitions = int (optional)`

The upper bound on the number of instances for operators whose input must be partitioned by key, such as [`summarize`](summarize.md), [`group`](group.md), and [`deduplicate`](deduplicate.md). Must be greater than zero.

Defaults to the surrounding pipeline’s setting, which is `4` unless a `// parallelism:` directive in a local run says otherwise.

### `{ … }`

The subpipeline to parallelize. It may transform events, end in a sink, or start with its own source. It must not produce bytes.

## Examples

### Parse JSON in parallel

Parse raw JSON strings on four cores:

```tql
subscribe "raw"
parallel 4 {
  parsed = data.parse_json()
}
```

### Deduplicate flows in parallel

Operators that need related events together partition their input themselves, so a block around them needs no routing configuration:

```tql
subscribe "events"
parallel 4 {
  deduplicate src_ip, dst_ip, dst_port
}
```

Tenzir routes every event with the same `src_ip`, `dst_ip`, and `dst_port` to the same instance of [`deduplicate`](deduplicate.md). Raise `limit_partitions` to spread those keys over more than the default four instances:

```tql
subscribe "events"
parallel 8, limit_partitions=8 {
  deduplicate src_ip, dst_ip, dst_port
}
```

### Trade memory for throughput

A block of CPU-bound operators can gain throughput by giving every channel inside it its own buffer instead of running fused:

```tql
subscribe "events"
parallel 4, fuse="none" {
  this = ocsf_cast(this)
  where severity_id >= 4
}
```

### Parallelize one section of a pipeline

Cast to OCSF on eight cores while the surrounding operators stay on one:

```tql
from_file "/var/log/events/*.json", watch=10s
parallel {
  this = ocsf_cast(this)
  where severity_id >= 4
}
to_file "/tmp/tenzir/high-severity.json" { write_ndjson }
```

## See Also

* [`each`](each.md)
* [`group`](group.md)
* [`load_balance`](load_balance.md)
* [Executor](../../explanations/executor.md)
* [Fan out with subpipelines](../../guides/route/fan-out-with-subpipelines.md)
