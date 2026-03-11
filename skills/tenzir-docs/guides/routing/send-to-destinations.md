# Send to destinations


This guide shows you how to send data to various destinations using TQL output operators. You’ll learn about destination operators, file output patterns, and expression-based serialization.

## Destination operators

TQL provides `to_*` operators for sending events to various destinations. These operators accept expressions for flexible serialization.

### Message brokers

Send events to message brokers like [Kafka](../../integrations/kafka.md).

Send to Kafka with automatic JSON formatting:

```tql
subscribe "security-events"
to_kafka "events"
```

Specify explicit serialization with the `message` parameter:

```tql
subscribe "logs"
to_kafka "events", message=this.print_json()
```

The `message` parameter accepts any expression that evaluates to a string or blob.

### Analytics platforms

Send data to platforms like [Splunk](../../integrations/splunk.md), [OpenSearch](../../integrations/opensearch.md), and [Elasticsearch](../../integrations/elasticsearch.md).

Send to a Splunk HEC endpoint:

```tql
subscribe "logs"
to_splunk "https://splunk.example.com:8088",
  hec_token=secret("SPLUNK_HEC_TOKEN")
```

Send to OpenSearch with index routing:

```tql
subscribe "security"
to_opensearch "https://opensearch.example.com:9200",
  action="index",
  index="security-events"
```

### Cloud services

Route events to cloud destinations like [Amazon SQS](../../integrations/amazon/sqs.md) and [Google Cloud Pub/Sub](../../integrations/google/cloud-pubsub.md).

Send to SQS:

```tql
subscribe "notifications"
to_sqs "https://sqs.us-east-1.amazonaws.com/123456789/queue"
```

Send to Pub/Sub:

```tql
subscribe "events"
to_gcp_pubsub "projects/my-project/topics/events"
```

## File output

For writing to files, use `write_*` operators followed by `save_*` operators. This two-operator pattern separates serialization from storage.

Write JSON to a local file:

```tql
subscribe "logs"
write_json
save_file "output.json"
```

Write compressed Parquet:

```tql
export
write_parquet
save_file "archive.parquet.zst"
```

Write JSON Lines to [S3](../../integrations/amazon/s3.md):

```tql
write_json
save_file "s3://bucket/logs/events.jsonl"
```

Send NDJSON over [TCP](../../integrations/tcp.md):

```tql
write_json
save_tcp "collector.example.com:5044"
```

## Expression-based serialization

Destination operators use expressions for flexible message formatting:

### Serialize the entire event

Serialize as JSON (the default for most operators):

```tql
to_kafka "events", message=this.print_json()
```

Serialize as compact JSON without nulls:

```tql
to_kafka "events", message=this.print_json(include_nulls=false)
```

### Serialize specific fields

Send only a specific field:

```tql
to_kafka "alerts", message=alert_message
```

Combine fields into a formatted string:

```tql
to_kafka "metrics", message=f"{host}: {metric_name}={value}"
```

### Dynamic routing

Route events to different destinations based on content:

```tql
to_kafka f"events.{event_type}", message=this.print_json()
```

## See also

* [Load-balance pipelines](load-balance-pipelines.md)
* [Split and merge streams](split-and-merge-streams.md)
* [`to_kafka`](/reference/operators/to_kafka.md)
* [`to_splunk`](/reference/operators/to_splunk.md)
* [`to_opensearch`](/reference/operators/to_opensearch.md)
* [`fork`](/reference/operators/fork.md)

## Contents

- [Split-and-merge-streams](split-and-merge-streams.md)
- [Load-balance-pipelines](load-balance-pipelines.md)