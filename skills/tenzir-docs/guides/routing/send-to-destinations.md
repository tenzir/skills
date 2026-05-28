# Send to destinations


This guide shows you how to send data to various destinations using TQL output operators. You’ll learn about destination operators, file output patterns, and expression-based serialization.

## Destination operators

TQL provides `to_*` operators for sending events to various destinations. These operators accept expressions for flexible serialization.

### Message brokers

Send events to message brokers like [Kafka](../../integrations/kafka.md) and [NATS](../../integrations/nats.md).

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

Send to NATS JetStream:

```tql
subscribe "security-events"
to_nats "alerts"
```

The NATS server must have a JetStream stream that captures the subject you publish to.

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

Route events to cloud destinations like [SQS](../../integrations/amazon/sqs.md) and [Cloud Pub/Sub](../../integrations/google/cloud-pubsub.md).

Send to SQS:

```tql
subscribe "notifications"
to_amazon_sqs "sqs://notifications", message=this.print_json()
```

Send to Pub/Sub:

```tql
subscribe "events"
to_google_cloud_pubsub project_id="my-project", topic_id="events", message=this.print_ndjson()
```

## File output

For writing to files, use a `to_*` destination operator with a printing subpipeline. This pattern separates serialization from storage.

Write JSON to a local file:

```tql
subscribe "logs"
to_file "output.json" {
  write_json
}
```

Write compressed Parquet:

```tql
export
to_file "archive.parquet.zst" {
  write_parquet
}
```

Write JSON Lines to [S3](../../integrations/amazon/s3.md):

```tql
to_file "s3://bucket/logs/events.jsonl" {
  write_json
}
```

Send newline-delimited JSON over [TCP](../../integrations/tcp.md):

```tql
to_tcp "collector.example.com:5044" { write_ndjson }
```

For protocols that expect a delimiter after every message, print the event to a string and use [`write_delimited`](/reference/operators/write_delimited.md) for the byte-stream framing:

```tql
to_tcp "collector.example.com:12201" {
  write_delimited this.print_ndjson(strip_null_fields=true), "\x00"
}
```

## Expression-based serialization

Destination operators use expressions for flexible message formatting:

### Serialize the entire event

Use the default event serialization:

```tql
to_kafka "events"
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
to_kafka f"events.{event_type}"
```

## See Also

* [`fork`](/reference/operators/fork.md)
* [`to_kafka`](/reference/operators/to_kafka.md)
* [`to_opensearch`](/reference/operators/to_opensearch.md)
* [`to_splunk`](/reference/operators/to_splunk.md)
* [`to_tcp`](/reference/operators/to_tcp.md)
* [`write_delimited`](/reference/operators/write_delimited.md)
* [`write_ndjson`](/reference/operators/write_ndjson.md)
* [`print_ndjson`](/reference/functions/print_ndjson.md)
* [Load-balance pipelines](load-balance-pipelines.md)
* [Split and merge streams](split-and-merge-streams.md)

## Contents

- [Expose-data-as-server](expose-data-as-server.md)
- [Split-and-merge-streams](split-and-merge-streams.md)
- [Fan-out-with-subpipelines](fan-out-with-subpipelines.md)
- [Load-balance-pipelines](load-balance-pipelines.md)