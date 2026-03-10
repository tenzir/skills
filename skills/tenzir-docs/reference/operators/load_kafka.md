# load_kafka


Loads a byte stream from an Apache Kafka topic.

```tql
load_kafka topic:string, [count=int, exit=bool, offset=int|string, options=record,
           aws_iam=record, aws_region=string, commit_batch_size=int, commit_timeout=duration]
```

## Description

Deprecated

The `load_kafka` operator does not respect event boundaries. Consider using [`from_kafka`](from_kafka.md) instead.

The `load_kafka` operator reads bytes from a Kafka topic.

The implementation uses the official [librdkafka](https://github.com/confluentinc/librdkafka) from Confluent and supports all [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md). You can specify them via `options` parameter as `{key: value, ...}`.

The operator injects the following default librdkafka configuration values in case no configuration file is present, or when the configuration does not include them:

* `bootstrap.servers`: `localhost`
* `client.id`: `tenzir`
* `group.id`: `tenzir`
* `enable.auto.commit`: `false` (This option cannot be changed)

### `topic: string`

The Kafka topic to use.

### `count = int (optional)`

Exit successfully after having consumed `count` messages.

### `exit = bool (optional)`

Exit successfully after having received the last message.

Without this option, the operator waits for new messages after consuming the last one.

### `offset = int|string (optional)`

The offset to start consuming from. Possible values are:

* `"beginning"`: first offset
* `"end"`: last offset
* `"stored"`: stored offset
* `<value>`: absolute offset
* `-<value>`: relative offset from end

The default is `"stored"`.

### `options = record (optional)`

A record of key-value configuration options for [librdkafka](https://github.com/confluentinc/librdkafka), e.g., `{"auto.offset.reset" : "earliest", "enable.partition.eof": true}`.

The `load_kafka` operator passes the key-value pairs directly to [librdkafka](https://github.com/confluentinc/librdkafka). Consult the list of available [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md) to configure Kafka according to your needs.

We recommend factoring these options into the plugin-specific `kafka.yaml` so that they are independent of the `load_kafka` arguments.

### `commit_batch_size = int (optional)`

The operator commits offsets after receiving `commit_batch_size` messages to improve throughput. If you need to ensure exactly-once semantics for your pipeline, set this option to `1` to commit every message individually.

Defaults to `1000`.

### `commit_timeout = duration (optional)`

A timeout after which the operator commits messages, even if it accepted fewer than `commit_batch_size`. This helps with long-running, low-volume pipelines.

Defaults to `10s`.

### `aws_iam = record (optional)`

Configures explicit AWS credentials or IAM role assumption. If not specified, the operator uses the default AWS credential chain.

```tql
{
  region: string,        // AWS region for API requests.
  access_key_id: string, // AWS access key ID.
  secret_access_key: string, // AWS secret access key.
  session_token: string, // session token for temporary credentials.
  assume_role: string,   // ARN of IAM role to assume.
  session_name: string,  // session name for role assumption.
  external_id: string,   // external ID for role assumption.
}
```

The `access_key_id` and `secret_access_key` must be specified together. If neither is specified, the operator uses the default AWS credential chain:

1. Environment variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
2. Shared credentials file (`~/.aws/credentials`)
3. IAM role for Amazon EC2 or ECS task role
4. Instance metadata service

### `aws_region = string (optional)`

The AWS region used to construct the MSK authentication URL. Required when connecting to MSK with IAM authentication.

## Examples

### Read 100 JSON messages from the topic `tenzir`

```tql
load_kafka "tenzir", count=100
read_json
```

### Read Zeek Streaming JSON logs starting at the beginning

```tql
load_kafka "zeek", offset="beginning"
read_zeek_json
```

## See Also

* [`from_kafka`](from_kafka.md)
* [`to_kafka`](to_kafka.md)
* [Kafka](../../integrations/kafka.md)