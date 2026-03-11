# to_kafka


Sends messages to an Apache Kafka topic.

```tql
to_kafka topic:string, [message=blob|string, key=string, timestamp=time,
         options=record, aws_iam=record, aws_region=string]
```

## Description

The `to_kafka` operator sends one message per event to a Kafka topic.

The implementation uses the official [librdkafka](https://github.com/confluentinc/librdkafka) from Confluent and supports all [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md). You can specify them via `options` parameter as `{key: value, ...}`.

The operator injects the following default librdkafka configuration values in case no configuration file is present, or when the configuration does not include them:

* `bootstrap.servers`: `localhost`
* `client.id`: `tenzir`

### `topic: string`

The Kafka topic to send messages to.

### `message = blob|string (optional)`

An expression that evaluates to the message content for each row.

Defaults to `this.print_json()` when not specified.

### `key = string (optional)`

Sets a fixed key for all messages.

### `timestamp = time (optional)`

Sets a fixed timestamp for all messages.

### `options = record (optional)`

A record of key-value configuration options for [librdkafka](https://github.com/confluentinc/librdkafka), e.g., `{"acks": "all", "batch.size": 16384}`.

The `to_kafka` operator passes the key-value pairs directly to [librdkafka](https://github.com/confluentinc/librdkafka). Consult the list of available [configuration options](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md) to configure Kafka according to your needs.

We recommend factoring these options into the plugin-specific `kafka.yaml` so that they are independent of the `to_kafka` arguments.

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

### Send JSON-formatted events to topic `events` (using default)

Stream security events to a Kafka topic with automatic JSON formatting:

```tql
subscribe "security-alerts"
where severity >= "high"
select timestamp, source_ip, alert_type, details
to_kafka "events"
```

This pipeline subscribes to security alerts, filters for high-severity events, selects relevant fields, and sends them to Kafka as JSON. Each event is automatically formatted using `this.print_json()`, producing messages like:

```json
{
  "timestamp": "2024-03-15T10:30:00.000000",
  "source_ip": "192.168.1.100",
  "alert_type": "brute_force",
  "details": "Multiple failed login attempts detected"
}
```

### Send JSON-formatted events with explicit message

```tql
subscribe "logs"
to_kafka "events", message=this.print_json()
```

### Send specific field values with a timestamp

```tql
subscribe "logs"
to_kafka "alerts", message=alert_msg, timestamp=2024-01-01T00:00:00
```

### Send data with a fixed key for partitioning

```tql
metrics
to_kafka "metrics", message=this.print_json(), key="server-01"
```

## See Also

* [`from_kafka`](/reference/operators/from_kafka.md)
* [Kafka](../../integrations/kafka.md)