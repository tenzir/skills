---
title: "group"
canonical: https://tenzir.com/docs/reference/operators/group
source: https://tenzir.com/docs/reference/operators/group.md
section: "Docs"
---

# group

> Routes events with the same key through the same subpipeline.

Routes events with the same key through the same subpipeline.

```tql
group $name=expr, … { … }
group over:expr { … }
```

## Description

The `group` operator evaluates one or more key expressions for every incoming event and creates one subpipeline for every distinct key (or tuple of keys). Events with the same key values are sent to the same subpipeline.

With one or more named bindings (`$name=expr`), each key is bound to its own `$name` variable inside the subpipeline. Named bindings let you group by multiple values without packing a record, and let nested `group` blocks keep enclosing bindings in scope. Key expressions resolve against the enclosing scope before opening the subpipeline scope, so `group $x=expr($x) { … }` reads the outer `$x` on the right-hand side and binds the new `$x` inside the subpipeline. As a shorthand for a single unnamed key (`over`), `$group` refers to the key inside the subpipeline.

The subpipeline receives grouped events as input. It either emits events (which are forwarded as the operator’s output) or ends with a sink, in which case `group` itself becomes a sink. The subpipeline must not produce bytes.

Use `group` when you need a full keyed subpipeline, such as a per-tenant sink or a per-session stateful transformation. For grouped aggregations only, use [`summarize`](summarize.md) instead.

### `$name=expr`

A named group binding that evaluates `expr` for every incoming event and binds the result to `$name` inside the subpipeline. Provide one or more comma-separated bindings to group by a tuple of keys. Binding names must be unique within a single `group` invocation and cannot be mixed with unnamed keys.

### `over: expr`

Shorthand for a single unnamed group key. Evaluates `expr` for every incoming event and binds `$group` inside the subpipeline. Cannot be combined with named bindings.

### `{ … }`

The subpipeline to run for every distinct key. The subpipeline receives the matching events as input.

Inside the subpipeline, each named `$name` refers to its corresponding key (or `$group` when using the single-key `over` shorthand).

### Parallelism

When you enable [parallelism](../../explanations/executor.md#parallel-execution), Tenzir can run `group` on several cores at once. It partitions the input by all group key expressions so that every event of a group reaches the same instance, which caps the number of instances at `limit_partitions`, four by default.

## Examples

### Summarize each tenant independently

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

### Group by multiple named keys

Bind computed keys to named variables to avoid mutating the input events or shadowing fields read by downstream operators:

```tql
from {ts: 2026-01-01T10:15:00Z, ip: 10.0.0.1, bytes: 100},
     {ts: 2026-01-01T10:45:00Z, ip: 10.0.0.1, bytes: 200},
     {ts: 2026-01-01T10:30:00Z, ip: 10.0.0.2, bytes: 50},
     {ts: 2026-01-01T11:05:00Z, ip: 10.0.0.1, bytes: 300}
group $hour=ts.floor(1h), $ip=ip {
  summarize first=min(ts), last=max(ts), total=sum(bytes), n=count()
  ts = $hour
  ip = $ip
}
sort ts, ip
```

```tql
{
  first: 2026-01-01T10:15:00Z,
  last: 2026-01-01T10:45:00Z,
  total: 300,
  n: 2,
  ts: 2026-01-01T10:00:00Z,
  ip: 10.0.0.1,
}
{
  first: 2026-01-01T10:30:00Z,
  last: 2026-01-01T10:30:00Z,
  total: 50,
  n: 1,
  ts: 2026-01-01T10:00:00Z,
  ip: 10.0.0.2,
}
{
  first: 2026-01-01T11:05:00Z,
  last: 2026-01-01T11:05:00Z,
  total: 300,
  n: 1,
  ts: 2026-01-01T11:00:00Z,
  ip: 10.0.0.1,
}
```

### Write a file per tenant

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

## See Also

* [`each`](each.md)
* [`fork`](fork.md)
* [`load_balance`](load_balance.md)
* [`parallel`](parallel.md)
* [`summarize`](summarize.md)
* [Fan out with subpipelines](../../guides/route/fan-out-with-subpipelines.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
