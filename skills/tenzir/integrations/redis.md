---
title: "Redis integration"
description: "Redis is an in-memory data store that applications use as a cache, message broker, and work queue. Tenzir pops items from Redis lists, subscribes to channels, and writes events to lists, channels, and keys."
canonical: https://tenzir.com/integrations/redis
source: https://tenzir.com/integrations/redis.md
section: "Integrations"
---

# Redis integration

> Redis is an in-memory data store that applications use as a cache, message broker, and work queue. Tenzir pops items from Redis lists, subscribes to channels, and writes events to lists, channels, and keys.

[Redis](https://redis.io/) is an in-memory data store that applications use as a cache, a message broker, and a work queue. Valkey and other servers that speak the Redis protocol work as well.

Use [`from_redis`](https://tenzir.com/docs/reference/operators/from_redis.md) to pop items from lists or to receive messages from pub/sub channels, and [`to_redis`](https://tenzir.com/docs/reference/operators/to_redis.md) to push events to lists, publish them to channels, or write them to strings, sets, sorted sets, and hashes.

Lists make reliable work queues: an item stays in the list until a consumer pops it, and each item goes to only one consumer. Pub/sub instead delivers every message to all subscribers that are connected at that moment, and drops it otherwise.

## Examples

### Consume a work queue

```tql
from_redis "events"
this = string(message).parse_json()
```

The defaults of both operators make a list a queue that preserves the order of events: [`to_redis`](https://tenzir.com/docs/reference/operators/to_redis.md) pushes to the left end, and [`from_redis`](https://tenzir.com/docs/reference/operators/from_redis.md) pops from the right end.

### Fill a work queue

```tql
from {severity: "high", message: "credential access detected"}
to_redis "events"
```

By default, [`to_redis`](https://tenzir.com/docs/reference/operators/to_redis.md) serializes each event with `this.print_ndjson()`.

### Subscribe to channels

```tql
from_redis "alerts.*", command="psubscribe", metadata_field=redis
this = {...string(message).parse_json(), channel: redis.channel}
```

### Connect to a secured server

```tql
from_redis "events",
  url="rediss://redis.example.com:6380/2",
  auth={user: "tenzir", password: secret("REDIS_PASSWORD")}
this = string(message).parse_json()
```

## See Also

* [`from_redis`](https://tenzir.com/docs/reference/operators/from_redis.md)
* [`to_redis`](https://tenzir.com/docs/reference/operators/to_redis.md)
* [D4 Project](d4.md)
* [Read from message brokers](../guides/collect/read-from-message-brokers.md)
* [Send to destinations](../guides/route/send-to-destinations.md)
