# Overview


Tenzir offers a layered integration architecture. It ranges from turn-key packages at the top to native protocol connectors at the core.

## Packages

[Packages](explanations/packages.md) are 1-click deployable integrations that deliver instant value. They bundle pipelines, [enrichment contexts](explanations/enrichment.md), and configurations for common security tools like Splunk, CrowdStrike, Elastic, SentinelOne, Palo Alto, and many more.

Browse our freely available [package library on GitHub](https://github.com/tenzir/library).

## Core Integrations

Core integrations are native connectors to the ecosystem, enabling communication over numerous protocols and APIs:

* **Cloud storage**: [S3](integrations/amazon/s3.md), [GCS](integrations/google/cloud-storage.md), [Azure Blob Storage](integrations/microsoft/azure-blob-storage.md)
* **Message queues**: [Kafka](integrations/kafka.md), [SQS](integrations/amazon/sqs.md), [AMQP](integrations/amqp.md)
* **Databases**: [Snowflake](integrations/snowflake.md), [ClickHouse](integrations/clickhouse.md)
* **Network protocols**: [TCP](integrations/tcp.md), [UDP](integrations/udp.md), [HTTP](integrations/http.md), [Syslog](integrations/syslog.md)

Under the hood, core integrations use a C++ plugin abstraction to provide an [operator](reference/operators.md), [function](reference/functions.md), or [context](explanations/enrichment.md) that you can use in TQL to directly interface with the respective resource, such as a TCP socket or cloud storage bucket. We typically implement this functionality using the respective SDK, such as the [AWS SDK](https://aws.amazon.com/sdk-for-cpp/), [Google Cloud SDK](https://cloud.google.com/cpp), or [librdkafka](https://github.com/confluentinc/librdkafka), though some integrations require a custom implementation.

Dedicated Operators

For some applications, we provide a **dedicated operator** that dramatically simplifies the user experience. For example, [`to_splunk`](/reference/operators/to_splunk.md) and [`from_opensearch`](/reference/operators/from_opensearch.md) offer a streamlined interface compared to composing generic HTTP or protocol operators.

## Contents

- [Messaging](integrations/amqp.md)
- [Protocols](integrations/email.md)
- [Data Tools](integrations/clickhouse.md)
- [Security Tools](integrations/sentinelone-data-lake.md)