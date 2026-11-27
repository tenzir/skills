---
title: "each"
canonical: https://tenzir.com/docs/reference/operators/each
source: https://tenzir.com/docs/reference/operators/each.md
section: "Docs"
---

# each

> Spawns a subpipeline for every incoming event, binding per-event values into the subpipeline.

Spawns a subpipeline for every incoming event, binding per-event values into the subpipeline.

```tql
each [$name=expr, …] [parallel=int] { … }
```

## Description

The `each` operator runs a fresh subpipeline for every incoming event.

With one or more named bindings (`$name=expr`), each expression is evaluated against the incoming event and bound to `$name` inside the subpipeline. Named bindings let nested `each` blocks keep enclosing bindings in scope, and let the optimizer push field projections upstream when you bind specific fields instead of `this`. Binding expressions resolve against the enclosing scope before opening the subpipeline scope, so `each $x=n + $x { … }` reads the outer `$x` on the right-hand side and binds the new `$x` inside the subpipeline. When you omit named bindings, `each` binds the complete input event record to `$this`.

The subpipeline takes no input from `each`. It either emits events (which are forwarded as the operator’s output) or ends with a sink, in which case `each` itself becomes a sink. The subpipeline must not produce bytes.

Use `each` for per-event jobs, such as running a lookup, export, or sink whose source depends on the incoming event. For keyed streams that should keep one subpipeline alive per key, use [`group`](group.md) instead.

### `$name=expr` (optional)

One or more comma-separated bindings that evaluate `expr` for every incoming event and bind the result to `$name` inside the subpipeline. Binding names must be unique within a single `each` invocation. When omitted, `each` binds the entire input event to `$this`.

### `parallel = int` (optional)

The maximum number of subpipelines that may run concurrently. Must be at least `1`. Excess events queue and start as soon as a slot frees.

Defaults to `10`.

### `{ … }`

The subpipeline to spawn for each event. Must start with a source.

Inside the subpipeline, each named `$name` refers to its bound per-event value (or `$this` refers to the complete input event when no named bindings are given).

## Parallelism

In a [parallel pipeline](../../explanations/executor.md#parallel-execution), each instance of `each` owns and runs its own child subpipelines. The `parallel` argument limits each instance separately. At a pipeline degree of `N`, up to `N * parallel` child subpipelines can therefore run at once.

For example, `// parallelism: 4` together with `each $ip=ip, parallel=10` permits up to 40 concurrent child subpipelines. Keep this combined limit in mind when a child subpipeline connects to a service with concurrency or rate limits.

## Examples

### Run a lookup per event

Use fields from the input event to parametrize a source subpipeline. This example treats the input as investigation cases and searches a historical event set for matching source IPs:

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

### Run a per-event sink

When the subpipeline ends with a sink, `each` itself becomes a sink. Use this to write a separate output file per tenant in the input:

```tql
from {tenant: "alpha"}, {tenant: "beta"}
each $tenant=tenant {
  from {tenant: $tenant, status: "ok"},
       {tenant: $tenant, status: "fail"}
  to_file f"/tmp/tenzir/{$tenant}.json" {
    write_ndjson
  }
}
```

## See Also

* [`cron`](cron.md)
* [`every`](every.md)
* [`fork`](fork.md)
* [`group`](group.md)
* [`parallel`](parallel.md)
* [`to_http`](to_http.md)
* [Fetch via HTTP and APIs](../../guides/collect/fetch-via-http-and-apis.md)
* [Fan out with subpipelines](../../guides/route/fan-out-with-subpipelines.md)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
