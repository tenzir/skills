---
title: "to_redis"
canonical: https://tenzir.com/docs/reference/operators/to_redis
source: https://tenzir.com/docs/reference/operators/to_redis.md
section: "Docs"
---

# to_redis

> Writes events to Redis lists, channels, strings, sets, sorted sets, or hashes.

Writes events to Redis lists, channels, strings, sets, sorted sets, or hashes.

```tql
to_redis key:string, [command=string, message=blob|string, field=string,
         score=number, ttl=duration, url=secret, db=int, auth=record,
         tls=record]
```

## Description

The `to_redis` operator runs one Redis command per event, which writes the `message` of the event to the `key` of the event.

By default, the operator pushes to the left end of a list. Together with the default of [`from_redis`](https://tenzir.com/docs/reference/operators/from_redis.md), which pops from the right end, the list forms a queue that preserves the order of events.

The operator sends the commands of a batch of events in one round trip. When Redis rejects commands, such as when a key holds a value of a different type, the operator emits a warning and continues. When the connection drops, the operator emits a warning, reconnects with exponential backoff, and sends the commands again that Redis did not confirm. Redis may then apply a command twice.

### `key: string`

An expression that evaluates to the key for each event, or to the channel with `command="publish"`. The operator skips events without a string key.

### `command = string (optional)`

The Redis command to run for each event:

| Command   | Description                                        |
| --------- | -------------------------------------------------- |
| `lpush`   | Pushes the message to the left end of a list.      |
| `rpush`   | Pushes the message to the right end of a list.     |
| `publish` | Publishes the message to a pub/sub channel.        |
| `set`     | Sets a string key to the message.                  |
| `sadd`    | Adds the message to a set.                         |
| `zadd`    | Adds the message to a sorted set with the `score`. |
| `hset`    | Sets the hash `field` to the message.              |

Defaults to `lpush`.

### `message = blob|string (optional)`

An expression that evaluates to the value to write for each event. The operator skips events whose message is neither a string nor a blob.

Defaults to `this.print_ndjson()`.

### `field = string (optional)`

An expression that evaluates to the hash field for each event. Requires `command="hset"`.

### `score = number (optional)`

An expression that evaluates to the score for each event. Requires `command="zadd"`.

### `ttl = duration (optional)`

Sets the time to live of the written key, with millisecond precision. Each successful write resets the time to live, and a write that Redis rejects leaves it alone. Does not apply to `command="publish"`.

For commands other than `set`, the operator writes and sets the time to live together in a Lua script, so that an interruption cannot separate them. This requires permission to run scripts with `EVAL`.

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
* `{user: "tenzir", password: secret("REDIS_PASSWORD")}` authenticates as an ACL user, which requires Redis 6 or later.

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

The operator does not support Redis streams, such as with `XADD`, or Redis Cluster yet.

## Examples

### Feed a queue for another pipeline

```tql
from {severity: "high", message: "credential access detected"}
to_redis "alerts"
```

Another pipeline consumes the events in order with `from_redis "alerts"`.

### Publish events to a channel

```tql
from {severity: "high", message: "credential access detected"}
to_redis "alerts." + severity, command="publish"
```

### Cache the latest status of every host for a day

```tql
from {host: "web-1", status: "up"}
to_redis "status:" + host, command="set", message=status, ttl=1d
```

### Collect the sources of every destination in a set

```tql
from {src_ip: 10.0.0.1, dest_ip: 10.0.0.2}
to_redis "sources:" + string(dest_ip), command="sadd", message=string(src_ip)
```

### Keep the latest attributes of every user in a hash

```tql
from {user: "alice", attribute: "role", value: "admin"}
to_redis "user:" + user, command="hset", field=attribute, message=value
```

## See Also

* [`from_redis`](https://tenzir.com/docs/reference/operators/from_redis.md)
* [Send to destinations](../../guides/route/send-to-destinations.md)
* [Redis](../../integrations/redis.md)
* [D4](../../integrations/d4.md)
