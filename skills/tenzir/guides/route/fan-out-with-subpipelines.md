---
title: "Fan out with subpipelines"
canonical: https://tenzir.com/docs/guides/route/fan-out-with-subpipelines
source: https://tenzir.com/docs/guides/route/fan-out-with-subpipelines.md
section: "Docs"
---

# Fan out with subpipelines

> This guide shows you how to fan out an event stream into subpipelines with each and group. You’ll learn when to spawn one subpipeline per event, when to keep one subpipeline per key, and how these operators differ from fixed fan-out operators like fork and loadbalance, and from merge, which adds a source rather than a branch.

This guide shows you how to fan out an event stream into subpipelines with [`each`](../../reference/operators/each.md) and [`group`](../../reference/operators/group.md). You’ll learn when to spawn one subpipeline per event, when to keep one subpipeline per key, and how these operators differ from fixed fan-out operators like [`fork`](../../reference/operators/fork.md) and [`load_balance`](../../reference/operators/load_balance.md), and from [`merge`](../../reference/operators/merge.md), which adds a source rather than a branch.

## Choose a fan-out pattern

Tenzir has several operators that send events into subpipelines. Choose the operator based on how many subpipelines you need and how events should flow into them:

| Operator                                                                      | Subpipelines                          | Event flow                                                            | Use case                                                      |
| ----------------------------------------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------- |
| [`fork`](../../reference/operators/fork.md)                 | One fixed side branch                 | Every event goes to the main pipeline and the side branch             | Archive or publish a copy while continuing processing         |
| [`merge`](../../reference/operators/merge.md)               | One fixed side source                 | The side branch produces events that join the main stream             | Pull a second input into the pipeline                         |
| [`load_balance`](../../reference/operators/load_balance.md) | One branch per configured target      | Each event goes to one target                                         | Distribute load across equivalent sinks                       |
| [`each`](../../reference/operators/each.md)                 | One fresh subpipeline per input event | Per-event values are bound to `$` variables; input is not streamed in | Run a per-event job, such as a lookup or export               |
| [`group`](../../reference/operators/group.md)               | One subpipeline per key               | Matching events are passed to the same keyed subpipeline              | Keep per-tenant, per-host, or per-session processing isolated |

Use regular transformations when every event can flow through the same linear pipeline. Use subpipeline fan-out when the pipeline structure itself depends on each event or key.

## Run one subpipeline per event

Use [`each`](../../reference/operators/each.md) when every input event describes a job to run. The nested pipeline must start with a source because `each` does not pass the input event into the subpipeline. Instead, named bindings such as `$id=case_id` expose per-event values as scoped `$` variables inside the subpipeline (omitting named bindings binds the complete event to `$this`).

The following pipeline treats incoming cases as lookup requests. Each case queries the same historical dataset for matching source IPs and annotates the matches with the case ID:

```tql
from {case_id: "C-1", ip: "10.0.0.5"},
     {case_id: "C-2", ip: "10.0.0.7"}
each $id=case_id, $ip=ip, parallel=4 {
  from {ts: 2024-01-01T10:00:00, src_ip: "10.0.0.5", action: "login"},
       {ts: 2024-01-01T10:02:00, src_ip: "10.0.0.8", action: "scan"},
       {ts: 2024-01-01T10:05:00, src_ip: "10.0.0.7", action: "download"}
  where src_ip == $ip
  case_id = $id
}
sort case_id, ts
```

```tql
{
  ts: 2024-01-01T10:00:00.000000,
  src_ip: "10.0.0.5",
  action: "login",
  case_id: "C-1",
}
{
  ts: 2024-01-01T10:05:00.000000,
  src_ip: "10.0.0.7",
  action: "download",
  case_id: "C-2",
}
```

The `parallel` option limits how many per-event jobs run at the same time. When more events arrive, `each` queues them and applies back pressure upstream until a running subpipeline finishes. Keep this value bounded for external APIs, expensive exports, or destinations with rate limits.

## Keep one subpipeline per key

Use [`group`](../../reference/operators/group.md) when events with the same key must go through the same subpipeline. Unlike `each`, the nested pipeline receives input: Tenzir sends all matching events for a key to that key’s subpipeline. Named bindings such as `$tenant=tenant` expose each key as a scoped `$` variable inside the subpipeline (a single unnamed key binds `$group`).

The following pipeline keeps tenant streams separate and computes a summary per tenant:

```tql
from {tenant: "alpha", bytes: 120},
     {tenant: "beta", bytes: 90},
     {tenant: "alpha", bytes: 80}
group $tenant=tenant {
  summarize events=count(), bytes=sum(bytes)
  tenant = $tenant
}
sort tenant
```

```tql
{
  events: 2,
  bytes: 200,
  tenant: "alpha",
}
{
  events: 1,
  bytes: 90,
  tenant: "beta",
}
```

For a pure aggregation, [`summarize`](../../reference/operators/summarize.md) is usually shorter. Use `group` when the per-key subpipeline does more than aggregate, such as keeping state, applying a keyed transformation, or writing to a key-specific sink.

## Write separate outputs per key

A common `group` pattern is to write each tenant, host, or sensor to its own file. The subpipeline ends with a sink, so `group` itself becomes a sink:

```tql
from {tenant: "alpha", message: "login"},
     {tenant: "beta", message: "scan"},
     {tenant: "alpha", message: "logout"}
group $tenant=tenant {
  to_file f"/tmp/tenzir/{$tenant}.json" {
    write_ndjson
  }
}
```

This creates one subpipeline per tenant and writes matching events to that subpipeline’s file.

## Avoid common mistakes

* Don’t use `each` for ordinary per-event transformations. Use regular TQL statements or [`parallel`](../../reference/operators/parallel.md) when every event follows the same processing steps.
* Don’t use `group` only to calculate grouped totals. Use [`summarize`](../../reference/operators/summarize.md) unless you need a full subpipeline per key.
* Don’t leave `each` unbounded for external systems. Set `parallel` to match the concurrency that the downstream service can handle.
* Remember that `each` subpipelines must start with a source, while `group` subpipelines receive the grouped input stream.
* Neither `each` nor `group` can use subpipelines that produce bytes as output.

## See Also

* [`each`](../../reference/operators/each.md)
* [`group`](../../reference/operators/group.md)
* [`fork`](../../reference/operators/fork.md)
* [`merge`](../../reference/operators/merge.md)
* [`parallel`](../../reference/operators/parallel.md)
* [`load_balance`](../../reference/operators/load_balance.md)
* [`publish`](../../reference/operators/publish.md)
* [`subscribe`](../../reference/operators/subscribe.md)
* [`summarize`](../../reference/operators/summarize.md)
* [Split and merge streams](split-and-merge-streams.md)
* [Load-balance pipelines](load-balance-pipelines.md)
