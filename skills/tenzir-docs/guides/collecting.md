# Overview


This guide provides an overview of data collection in TQL. You’ll learn about the different approaches for ingesting data from various sources.

TQL provides two types of input operators:

* **`from_*` operators** like [`from_file`](/reference/operators/from_file.md) and [`from_http`](/reference/operators/from_http.md) read bytes and parse them using a [subpipeline](../reference/programs.md#parsing-subpipelines).

* **Direct event operators** like [`from_kafka`](/reference/operators/from_kafka.md) and [`from_udp`](/reference/operators/from_udp.md) produce structured events directly without an intermediate byte stream.

Migration note

The `from_*` family of operators supersedes the older `load_*` operators that produce bytes. While `load_*` operators remain supported, prefer the newer `from_*` variants which provide a more unified experience with built-in format inference.

For example, `from_file "data.csv"` replaces `load_file "data.csv" | read_csv`.

## Collection patterns

Different data sources require different collection approaches.

### Files and cloud storage

Read local files, watch directories for changes, or access cloud storage:

```tql
// Single file with automatic format detection
from_file "/var/log/app.json"


// Watch a directory for new files
from_file "/incoming/*.csv", watch=true


// Cloud storage with glob patterns
from_file "s3://bucket/data/**/*.parquet"
```

See the [file reading guide](collecting/read-and-watch-files.md) for details.

### HTTP and APIs

Fetch data from web APIs with authentication, pagination, and retry handling:

```tql
from_http "https://api.example.com/events",
  headers={"Authorization": "Bearer " + secret("API_TOKEN")}
```

See the [HTTP and API guide](collecting/fetch-via-http-and-apis.md) for pagination patterns and advanced configurations.

### Message brokers

Subscribe to topics or queues from Apache Kafka, AMQP, Amazon SQS, and Google Cloud Pub/Sub:

```tql
from_kafka "security-events", offset="end"
```

See the [message broker guide](collecting/read-from-message-brokers.md) for broker-specific configurations.

### Network data

Receive data over TCP or UDP sockets, or capture packets from network interfaces:

```tql
// UDP syslog receiver
from_udp "0.0.0.0:514"


// TCP with TLS
from "tcp://0.0.0.0:8443", tls=true
```

See the [network data guide](collecting/get-data-from-the-network.md) for socket configurations and packet capture.

## Sending data to destinations

For routing data to outputs, see the [Routing guides](routing/send-to-destinations.md), which cover destination operators, file output, load balancing, and pipeline connections.

## See also

* [Read and watch files](collecting/read-and-watch-files.md)
* [Fetch via HTTP and APIs](collecting/fetch-via-http-and-apis.md)
* [Read from message brokers](collecting/read-from-message-brokers.md)
* [Get data from the network](collecting/get-data-from-the-network.md)
* [Send to destinations](routing/send-to-destinations.md)

## Contents

- [Read-and-watch-files](collecting/read-and-watch-files.md)
- [Fetch-via-http-and-apis](collecting/fetch-via-http-and-apis.md)
- [Read-from-message-brokers](collecting/read-from-message-brokers.md)
- [Get-data-from-the-network](collecting/get-data-from-the-network.md)