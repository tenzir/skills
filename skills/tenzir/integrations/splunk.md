---
title: "Splunk integration"
description: "Collect, index, and analyze machine-generated data for monitoring, searching, and troubleshooting."
canonical: https://tenzir.com/integrations/splunk
source: https://tenzir.com/integrations/splunk.md
section: "Integrations"
---

# Splunk integration

> Collect, index, and analyze machine-generated data for monitoring, searching, and troubleshooting.

[Splunk](https://splunk.com) is a SIEM solution for storing and processing logs. Tenzir can receive and send data through HEC and query Splunk searches.

Splunk

## Examples

### Send data to an existing HEC endpoint

To send data from a pipeline to a Splunk [HTTP Event Collector (HEC)](https://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector) endpoint, use the [`to_splunk`](https://tenzir.com/docs/reference/operators/to_splunk.md) operator.

For example, deploy the following pipeline to forward [Suricata](suricata.md) alerts to Splunk:

```tql
subscribe "suricata"
where @name == "suricata.alert"
to_splunk "https://1.2.3.4:8088", hec_token="TOKEN", tls_no_verify=true
```

Replace `1.2.3.4` with the IP address of your Splunk host and `TOKEN` with your HEC token.

For more details, see the documentation for the [`to_splunk`](https://tenzir.com/docs/reference/operators/to_splunk.md) operator.

### Collect Splunk search results

Use [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) to run a bounded search through the Search Head management API and emit every result as an event. Name the indexes to read with `index` and filter the events in TQL:

```tql
from_splunk "https://splunk.example.com:8089",
  index="main",
  earliest="-15m",
  latest="-5m",
  headers={
    Authorization: secret("splunk-rest-authorization"),
  }
where sourcetype == "linux_secure" and user == "root"
publish "splunk-results"
```

Tenzir adds the filters to the search that it sends as prefilters, so Splunk drops most non-matching events before returning results. Splunk’s `search` command matches strings case-insensitively, so it can still return a few extra events, such as `ROOT` for `user == "root"`, and Tenzir applies the exact filter to every result. Tenzir also infers numbers, booleans, IP addresses, and timestamps from the strings that Splunk returns. To run your own SPL instead, pass a search as you would type it in Splunk Web, such as `search="index=main sourcetype=linux_secure | stats count by user"`. Our [SPL optimization reference](../reference/optimizations/spl.md) describes which filters reach Splunk.

Tenzir initiates the connection to Splunk. Store the complete REST API authorization header value, such as `Bearer <authentication-token>`, `Splunk <session-key>`, or `Basic <base64-encoded-credentials>`, in the `splunk-rest-authorization` secret. A HEC token doesn’t authenticate search requests.

For recurring collection, wrap [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) in [`every`](https://tenzir.com/docs/reference/operators/every.md). Use explicit overlapping time windows when Splunk can index events late, and deduplicate repeated results downstream.

### Receive HEC events

Use [`accept_splunk`](https://tenzir.com/docs/reference/operators/accept_splunk.md) to receive HEC requests directly in a Tenzir pipeline:

```tql
accept_splunk hec_token=secret("splunk-hec-token")
publish "splunk"
```

The operator listens on the standard HEC port `8088`. Configure the same token in each exporter. Event requests retain their HEC envelope, while raw requests retain the complete body for downstream parsing.

Enable HEC indexer acknowledgements when the exporter requires confirmation that a checkpoint covers each request:

```tql
accept_splunk hec_token=secret("splunk-hec-token"),
  ack=true,
  ack_timeout=10min
publish "splunk"
```

With `ack=true`, the exporter must send the same UUID in the `X-Splunk-Request-Channel` header or `channel` query parameter for event, raw, and acknowledgement requests. Tenzir returns an `ackId` for each accepted event or raw request. Queries to `/services/collector/ack` return `true` after a checkpoint containing the request commits, and continue to return `true` until `ack_timeout` expires. Until pipeline checkpointing is enabled, these queries return `false`.

For clients that still target port `9880`, set the listener explicitly:

```tql
accept_splunk "0.0.0.0:9880",
  hec_token=secret("splunk-hec-token")
publish "splunk"
```
