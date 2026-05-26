# publish


Publishes events to a channel with a topic.

```tql
publish [topic:string]
```

## Description

The `publish` operator publishes events at a node in a channel with the specified topic. All [`subscribe`](/reference/operators/subscribe.md) operators on that topic receive the events immediately.

Note

The `publish` operator does not guarantee that events stay in their original order.

During shutdown, `subscribe` will wait for `publish` to drain all data before shutting down itself. This prevents data loss, as long as pub/sub do not form cycles and `publish` does not use dynamic topic names.

### `topic: string (optional)`

An optional topic for publishing events under. If unspecified, the operator publishes events to the topic `main`.

## Examples

### Publish Zeek connection logs under the fixed topic `zeek`

```tql
from_file "conn.log.gz" {
  decompress_gzip
  read_zeek_tsv
}
publish "zeek"
```

### Publish Suricata events under a dynamic topic depending on their event type

```tql
from_file "eve.json" {
  read_suricata
}
publish f"suricata.{event_type}"
```

## See Also

* [`import`](/reference/operators/import.md)
* [`subscribe`](/reference/operators/subscribe.md)
* [Quickstart](../../guides/quickstart.md)
* [Split and merge streams](../../guides/routing/split-and-merge-streams.md)
* [Write a package](../../tutorials/write-a-package.md)