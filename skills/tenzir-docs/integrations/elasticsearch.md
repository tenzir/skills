# Elasticsearch


[Elasticsearch](https://www.elastic.co/elasticsearch) is a search and observability suite for unstructured data. Tenzir can send events to Elasticsearch and emulate a Elasticsearch-compatible Bulk API endpoint.

When sending data to Elasticsearch, Tenzir uses the [Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) and attempts to maximally batch events for throughput, accumulating multiple events before shipping them within a single API call. You can control batching behavior with the `max_content_length` and `buffer_timeout` options.

Use `to_opensearch` for both OpenSearch and Elasticsearch-compatible Bulk API endpoints. There is no separate `to_elasticsearch` operator.

For more details, see the documentation for the [`to_opensearch`](/reference/operators/to_opensearch.md) operator.

Tenzir can also present a Elasticsearch-compatible REST API via the [`accept_opensearch`](/reference/operators/accept_opensearch.md) operator.

## Examples

### Send events to a Elasticsearch index

Send an example event to the `main` index:

```tql
from {event: "example"}
to_opensearch "1.2.3.4:9200", action="create", index="main"
```

Instead of treating the entire event as a document to be indexed by Elasticsearch, you can designate a nested record as the document:

```tql
from {category: "qux", doc_id: "XXX", event: {foo: "bar"}}
to_opensearch "localhost:9200", id=doc_id, doc=event, action="update", index=category
```

The above example updates the document with ID `XXX` with the contents from the nested field `event`.

### Accept data by emulating Elasticsearch

Tenzir can act as a drop-in replacement for Elasticsearch by accepting data via a Bulk API endpoint. This allows you to point your [Logstash](https://www.elastic.co/logstash) or Beats instances to Tenzir instead.

```tql
accept_opensearch "0.0.0.0:9200", keep_actions=true
publish "elasticsearch"
```

This pipeline accepts data on port 9200 and publishes all received events on the `elasticsearch` topic for further processing by other pipelines.

Use `accept_opensearch` for new pipelines that receive bulk ingestion data.

Setting `keep_actions=true` causes action objects to remain in the stream, like this:

```tql
{create:{_index:"filebeat-8.17.3"}} // 👈 action object
{"@timestamp":2025-03-31T13:42:28.068Z,log:{offset:1,file:{path:"/mounted/logfile"}},message:"hello",input:{type:"log"},host:{name:"eb21"},agent:{id:"682cfcf4-f251-4576-abcb-6c8bcadfda08",name:"eb21",type:"filebeat",version:"8.17.3",ephemeral_id:"17f74f6e-36f0-4045-93e6-c549874716df"},ecs:{version:"8.0.0"}}
{create:{_index:"filebeat-8.17.3"}} // 👈 action object
{"@timestamp":2025-03-31T13:42:28.068Z,log:{offset:7,file:{path:"/mounted/logfile"}},message:"this",input:{type:"log"},host:{name:"eb21"},agent:{id:"682cfcf4-f251-4576-abcb-6c8bcadfda08",name:"eb21",type:"filebeat",version:"8.17.3",ephemeral_id:"17f74f6e-36f0-4045-93e6-c549874716df"},ecs:{version:"8.0.0"}}
```

#### Ship data via Filebeat

Configure [Filebeat](https://www.elastic.co/beats/filebeat) as follows to ship data to Tenzir:

filebeat.yml

```yaml
output.elasticsearch:
  hosts: ["localhost:9200"]
```

Set `hosts` to the endpoint of the Tenzir pipeline accepting data.

#### Ship data via Logstash

Configure [Logstash](https://www.elastic.co/guide/en/logstash/current/plugins-outputs-elasticsearch.html) with the

`elasticsearch` output plugin to ship data to Tenzir:

pipeline.conf

```javascript
output {
  elasticsearch {
    hosts => "https://localhost:9200"
  }
}
```

Set `hosts` to the endpoint of the Tenzir pipeline accepting data.