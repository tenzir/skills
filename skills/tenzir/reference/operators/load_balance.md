---
title: "load_balance"
canonical: https://tenzir.com/docs/reference/operators/load_balance
source: https://tenzir.com/docs/reference/operators/load_balance.md
section: "Docs"
---

# load_balance

> Routes the data to one of multiple subpipelines.

Routes the data to one of multiple subpipelines.

```tql
load_balance $name=list { … }
load_balance over:list { … }
```

## Description

The `load_balance` operator spawns a nested pipeline for each element in the given list. Incoming events are distributed to exactly one of the nested pipelines. This operator may reorder the event stream.

With a named binding (`$name=list`), each worker subpipeline receives its list element in `$name`. The list expression resolves against the enclosing scope before opening the subpipeline scope, so `load_balance $target=$target { … }` reads the outer `$target` list on the right-hand side and binds the per-worker `$target` inside the subpipeline. As a shorthand, passing an unnamed list (`over`) binds each element to `$over`.

In a parallel pipeline, `load_balance` runs in at most as many parallel instances as there are targets. Each target has one nested pipeline, assigned to one instance. If the requested parallelism exceeds the number of targets, the operator uses fewer instances.

### `$name=list`

A named binding whose right-hand side evaluates to a non-empty constant list. Inside each spawned subpipeline, `$name` holds one element from the list.

### `over: list`

Shorthand for an unnamed target list. Evaluates to a non-empty constant list and binds each element to `$over` inside the spawned subpipeline.

### `{ … }`

The nested pipeline to spawn for each element in the list. Inside the subpipeline, `$name` (or `$over` when using the unnamed shorthand) resolves to the worker’s assigned list element.

The given subpipeline must end with a sink. This limitation might be removed in future versions.

## Examples

### Route data to multiple TCP ports

```tql
let $endpoints = ["192.168.0.30:8080", "192.168.0.30:8081"]


subscribe "input"
load_balance $endpoint=$endpoints {
  to_tcp $endpoint { write_json }
}
```

### Route data to multiple Splunk endpoints

```tql
let $targets = [{
  ip: 192.168.0.30,
  token: "example-token-1234",
}, {
  ip: 192.168.0.31,
  token: "example-token-5678",
}]


subscribe "input"
load_balance $target=$targets {
  let $endpoint = f"{$target.ip}:8080"
  to_splunk $endpoint, hec_token=$target.token
}
```

## See Also

* [`fork`](fork.md)
* [`group`](group.md)
* [`publish`](publish.md)
* [Fan out with subpipelines](../../guides/route/fan-out-with-subpipelines.md)
* [Load-balance pipelines](../../guides/route/load-balance-pipelines.md)
