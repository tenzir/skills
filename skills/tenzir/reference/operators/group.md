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
group over:expr { … }
```

## Description

The `group` operator evaluates `over` for every incoming event and creates one subpipeline for every distinct key. Events with the same key are sent to the same subpipeline. Inside the subpipeline, `$group` refers to the key for that subpipeline.

The subpipeline receives grouped events as input. It either emits events - which are forwarded as the operator’s output - or ends with a sink, in which case `group` itself becomes a sink. The subpipeline must not produce bytes.

Use `group` when you need a full keyed subpipeline, such as a per-tenant sink or a per-session stateful transformation. For grouped aggregations only, use [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md) instead.

### `over: expr`

The expression that computes the group key for every incoming event.

### `{ … }`

The subpipeline to run for every distinct key. The subpipeline receives the matching events as input.

Inside the subpipeline, `$group` refers to the current key.

## Examples

### Summarize each tenant independently

```tql
from {tenant: "alpha", bytes: 120},
     {tenant: "beta", bytes: 90},
     {tenant: "alpha", bytes: 80}
group tenant {
  summarize events=count(), bytes=sum(bytes)
  tenant = $group
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

### Write a file per tenant

```tql
from {tenant: "alpha", message: "login"},
     {tenant: "beta", message: "scan"},
     {tenant: "alpha", message: "logout"}
group tenant {
  to_file f"/tmp/tenzir/{$group}.json" {
    write_ndjson
  }
}
```

## See Also

* [`each`](https://tenzir.com/docs/reference/operators/each.md)
* [`fork`](https://tenzir.com/docs/reference/operators/fork.md)
* [`load_balance`](https://tenzir.com/docs/reference/operators/load_balance.md)
* [`parallel`](https://tenzir.com/docs/reference/operators/parallel.md)
* [`summarize`](https://tenzir.com/docs/reference/operators/summarize.md)
* [Fan out with subpipelines](../../guides/routing/fan-out-with-subpipelines.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
