---
title: "from_redis"
canonical: https://tenzir.com/docs/reference/operators/from_redis
source: https://tenzir.com/docs/reference/operators/from_redis.md
section: "Docs"
---

# from_redis

> Pops items from Redis lists or receives messages from Redis pub/sub channels.

Pops items from Redis lists or receives messages from Redis pub/sub channels.

```tql
from_redis key:string|list<string>, [command=string, count=int,
           metadata_field=field, url=secret, db=int, auth=record, tls=record]
```

## Description

The `from_redis` operator reads from a Redis server. It produces one event per list item or pub/sub message with a `message` field of type `blob`.

By default, the operator pops items from the right end of one or more lists. Producers that push to the left end then form a queue that the operator consumes in FIFO order. The operator waits on the server with a blocking pop instead of polling.

Popping an item removes it from the list. When the pipeline stops gracefully, the operator lets a pop in flight finish and emits its items, which takes up to a second with a responsive server. When the pipeline is cancelled, such as by a second interrupt, the operator stops at once. It then pushes the items that it popped but did not emit back to the end of the list that they came from, so that the next consumer receives them in their original order. If that fails for 10 seconds, the node logs an error with the number of items. Items that downstream operators drop, such as [`head`](https://tenzir.com/docs/reference/operators/head.md) after its limit, count as emitted. Use `count` instead of [`head`](https://tenzir.com/docs/reference/operators/head.md) to pop an exact number of items.

A cancelled pipeline also hands back the items of the pop in flight, as long as the server answers it within 1.5 seconds. Otherwise, the node logs an error.

When the connection drops, the operator emits a warning and reconnects with exponential backoff. An item that the server sent while the connection failed is lost.

### `key: string|list<string>`

The key of the list to pop from, or the channel to subscribe to.

With a list, the operator pops from the first list that has an item, in the order of the list. With `command="psubscribe"`, the keys are glob-style channel patterns, such as `alerts.*`.

### `command = string (optional)`

The Redis operation that reads the data:

| Command      | Description                                                 |
| ------------ | ----------------------------------------------------------- |
| `rpop`       | Pops items from the right end of the lists with `BRPOP`.    |
| `lpop`       | Pops items from the left end of the lists with `BLPOP`.     |
| `subscribe`  | Receives messages from the channels with `SUBSCRIBE`.       |
| `psubscribe` | Receives messages from matching channels with `PSUBSCRIBE`. |

Pub/sub delivers each message only to the subscribers that are connected when a client publishes it. Messages published while the operator reconnects are lost.

Defaults to `rpop`.

### `count = int (optional)`

Exit successfully after emitting `count` events. With a list command, the operator never pops more than `count` items.

### `metadata_field = field (optional)`

The field that receives a record with the origin of every event:

| Field     | Type     | Description                                       |
| --------- | -------- | ------------------------------------------------- |
| `key`     | `string` | The list that the item came from. Only for lists. |
| `channel` | `string` | The channel of the message. Only for pub/sub.     |
| `pattern` | `string` | The pattern that matched. Only with `psubscribe`. |

### `url = secret (optional)`

The URL of the Redis server, in the form `redis://[user:password@]host[:port][/db]`. The `rediss` scheme enables TLS. You can also pass `host` or `host:port` without a scheme.

Percent-encode reserved characters in the user and password, such as `@` as `%40`.

Defaults to `redis://localhost:6379`.

### `db = int (optional)`

The database to select after connecting. Overrides the database in the URL.

Defaults to `0`.

### `auth = record (optional)`

The credentials for the connection. Each value can be a string or a secret.

* `{password: secret("REDIS_PASSWORD")}` authenticates as the default user.
* `{user: "analyzer", password: secret("REDIS_PASSWORD")}` authenticates as an ACL user, which requires Redis 6 or later.

An `auth` record replaces the credentials in the URL.

### `tls = record (optional)`

TLS configuration. Provide an empty record (`tls={}`) to enable TLS with defaults or set fields to customize it.

```tql
{
  skip_peer_verification: bool, // skip certificate verification.
  cacert: string,               // CA bundle to verify peers.
  certfile: string,             // client certificate to present.
  keyfile: string,              // private key for the client certificate.
  min_version: string,          // minimum TLS version (`"1.0"`, `"1.1"`, `"1.2"`, "1.3"`).
  ciphers: string,              // OpenSSL cipher list string.
  client_ca: string,            // CA to validate client certificates.
  require_client_cert: bool,    // require clients to present a certificate.
}
```

The `client_ca` and `require_client_cert` options are only valid for operators that accept incoming client connections.

Any value not specified in the record will either be picked up from the configuration or if not configured will not be used by the operator.

See the [Node TLS Setup guide](../../guides/node-setup/configure-tls.md) for more details.

Without `tls`, the scheme of the URL decides whether the operator uses TLS.

## Limitations

The operator does not support Redis streams and consumer groups, such as with `XREADGROUP`, or Redis Cluster yet.

## Examples

### Parse JSON items from multiple lists

```tql
from_redis ["alerts", "notices"], metadata_field=redis
this = {...string(message).parse_json(), queue: redis.key}
```

### Receive messages from matching channels

```tql
from_redis "alerts.*", command="psubscribe", metadata_field=redis
this = {channel: redis.channel, message: string(message)}
```

### Connect with TLS and an ACL user

```tql
from_redis "queue",
  url="rediss://redis.example.com:6380",
  auth={user: "tenzir", password: secret("REDIS_PASSWORD")}
this = string(message).parse_json()
```

### Consume a D4 analyzer queue

A D4 server keeps the queues of its analyzers in database 2. For sensor data of type 1, the queue holds the file names of gzip-compressed pcap files. Read the files and decode their packets with [`each`](https://tenzir.com/docs/reference/operators/each.md):

```tql
from_redis "analyzer:1:2b5c0f6a-9d3c-4b8e-8f1d-7a1b2c3d4e5f",
  url="redis://d4.example.org:6380", db=2
each {
  from_file string($this.message) {
    decompress_gzip
    read_pcap
  }
}
this = decapsulate(this)
```

## See Also

* [`to_redis`](https://tenzir.com/docs/reference/operators/to_redis.md)
* [Read from message brokers](../../guides/collect/read-from-message-brokers.md)
* [Redis](../../integrations/redis.md)
* [D4](../../integrations/d4.md)
