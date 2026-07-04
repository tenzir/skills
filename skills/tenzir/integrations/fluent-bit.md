---
title: "Fluent Bit integration"
description: "Collect, process, and forward logs and metrics from various sources to many sinks."
canonical: https://tenzir.com/integrations/fluent-bit
source: https://tenzir.com/integrations/fluent-bit.md
section: "Integrations"
---

# Fluent Bit integration

> Collect, process, and forward logs and metrics from various sources to many sinks.

[Fluent Bit](https://fluentbit.io) is an open source observability pipeline. Tenzir embeds Fluent Bit, exposing all its [inputs](https://docs.fluentbit.io/manual/pipeline/inputs) via [`from_fluent_bit`](https://tenzir.com/docs/reference/operators/from_fluent_bit.md) and [outputs](https://docs.fluentbit.io/manual/pipeline/outputs) via [`to_fluent_bit`](https://tenzir.com/docs/reference/operators/to_fluent_bit.md)

This makes Tenzir effectively a superset of Fluent Bit.

Fluent Bit [parsers](https://docs.fluentbit.io/manual/pipeline/parsers) map to Tenzir operators that accept bytes as input and produce events as output. Fluent Bit [filters](https://docs.fluentbit.io/manual/pipeline/filters) correspond to Tenzir operators that perform event-to-event transformations. Tenzir does not expose Fluent Bit parsers and filters, only inputs and output.

Internally, Fluent Bit uses [MsgPack](https://msgpack.org/) to encode events whereas Tenzir uses [Arrow](https://arrow.apache.org) record batches. The `fluentbit` source operator transposes MsgPack to Arrow, and the `fluentbit` sink performs the reverse operation.

## Usage

An invocation of the `fluent-bit` commandline utility

```bash
fluent-bit -o input_plugin -p key1=value1 -p key2=value2 -p…
```

translates to Tenzir’s [`from_fluent_bit`](https://tenzir.com/docs/reference/operators/from_fluent_bit.md) operator as follows:

```tql
from_fluent_bit "input_plugin", options={key1: value1, key2: value2, …}
```

with the [`to_fluent_bit`](https://tenzir.com/docs/reference/operators/to_fluent_bit.md) operator working exactly analogous.

## Examples

### Ingest OpenTelemetry logs, metrics, and traces

```tql
from_fluent_bit "opentelemetry"
```

You can then send JSON-encoded log data to a freshly created API endpoint:

```bash
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"resourceLogs":[{"resource":{},"scopeLogs":[{"scope":{},"logRecords":[{"timeUnixNano":"1660296023390371588","body":{"stringValue":"{\"message\":\"dummy\"}"},"traceId":"","spanId":""}]}]}]}' \
  http://0.0.0.0:4318/v1/logs
```

### Imitate a Splunk HEC endpoint

```tql
from_fluent_bit "splunk", options = {port: 8088}
```

Use the dedicated [`to_splunk`](https://tenzir.com/docs/reference/operators/to_splunk.md) operator to send events to a Splunk HEC.

### Collect host metrics

Use Fluent Bit’s Node Exporter Metrics input plugin to collect host metrics from Linux systems:

```tql
from_fluent_bit "node_exporter_metrics", options={scrape_interval: 5}
```

### Send to Datadog

```tql
to_fluent_bit "datadog", options = {apikey: "XXX"}
```

### Send to Elasticsearch

Use Fluent Bit’s Elasticsearch output plugin to send data to Elasticsearch:

```tql
to_fluent_bit "es", options={host: "192.168.2.3", port: 9200, index: "my_index"}
```
