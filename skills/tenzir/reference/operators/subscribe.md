---
title: "subscribe"
canonical: https://tenzir.com/docs/reference/operators/subscribe
source: https://tenzir.com/docs/reference/operators/subscribe.md
section: "Docs"
---

# subscribe

> Subscribes to events from a channel with a topic.

Subscribes to events from a channel with a topic.

```tql
subscribe [topic:string...]
```

## Description

The `subscribe` operator subscribes to events from a channel with the specified topic. Multiple `subscribe` operators with the same topic receive the same events.

Subscribers propagate back pressure to publishers. If a subscribing pipeline fails to keep up, all publishers will slow down as well to a matching speed to avoid data loss.

When a deployment shuts down, `subscribe` waits for `publish` to drain all data before shutting down itself. This prevents data loss, as long as pub/sub do not form cycles.

When you stop an individual subscribing pipeline, `subscribe` first detaches from future publications, then drains the events it has already accepted. It does not wait for publishers to stop.

### `topic: string... (optional)`

Optional channel names to subscribe to. If unspecified, the operator subscribes to the topic `main`.

Each topic must be a constant: a string literal or a `let` binding of one.

## Optimizations

The operator acts on the predicates that the [optimizer](../../explanations/pipeline.md#optimization) pushes toward it. A [`where`](where.md) that follows `subscribe` becomes part of the subscription, and the deployment drops non-matching events before they enter the pipeline. This keeps back pressure and the per-pipeline queues limited to events the pipeline actually processes.

The deployment’s router evaluates most predicates before queueing, including predicates that call functions. A predicate that compares a nested field, such as `a.b == 1`, runs in the operator after queueing, and so does every predicate that follows it.

The operator also removes the fields that no later operator reads as events arrive. With a single topic, it stops after the number of events that a following [`head`](head.md) keeps, and discards what remains queued.

## Examples

### Subscribe to the events under a topic

```tql
subscribe "zeek-conn"
```

### Subscribe to the multiple topics

```tql
subscribe "alerts", "notices", "critical"
```

## See Also

* [`publish`](publish.md)
* [Split and merge streams](../../guides/route/split-and-merge-streams.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
