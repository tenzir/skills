---
title: "publish"
canonical: https://tenzir.com/docs/reference/operators/publish
source: https://tenzir.com/docs/reference/operators/publish.md
section: "Docs"
---

# publish

> Publishes events to a channel with a topic.

Publishes events to a channel with a topic.

```tql
publish [topic:string]
```

## Description

The `publish` operator publishes events in a channel of the deployment with the specified topic. All [`subscribe`](subscribe.md) operators on that topic receive the events immediately.

Note

The `publish` operator does not guarantee that events stay in their original order.

When a deployment shuts down, `subscribe` waits for `publish` to drain all data before shutting down itself. This prevents data loss, as long as pub/sub do not form cycles.

### `topic: string (optional)`

An optional topic for publishing events under. If unspecified, the operator publishes events to the topic `main`.

The topic must be a constant: a string literal or a `let` binding of one. A deployment reads the topics from the pipeline definition, so that it can start subscribers before the publishers that feed them.

### Parallelism

When you enable [parallelism](../../explanations/executor.md#parallel-execution), Tenzir can run `publish` on several cores at once.

## Examples

### Publish Zeek connection logs under the fixed topic `zeek`

```tql
from_file "conn.log.gz" {
  decompress_gzip
  read_zeek_tsv
}
publish "zeek"
```

## See Also

* [`subscribe`](subscribe.md)
* [Split and merge streams](../../guides/route/split-and-merge-streams.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
