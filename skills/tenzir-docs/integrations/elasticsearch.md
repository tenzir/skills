# Elasticsearch


[Elasticsearch](https://www.elastic.co/elasticsearch) is a search and observability suite for unstructured data. Tenzir can send events to Elasticsearch and emulate a Elasticsearch-compatible Bulk API endpoint.

When sending data to Elasticsearch, Tenzir uses the [Bulk API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html) and attempts to maximally batch events for throughput, accumulating multiple events before shipping them within a single API call. You can control batching behavior with the `max_content_length` and `buffer_timeout` options.

Use `to_elasticsearch` to send events to Elasticsearch Bulk API endpoints.

For more details, see the documentation for the [`to_elasticsearch`](/reference/operators/to_elasticsearch.md) operator.

Tenzir can also present a Elasticsearch-compatible REST API via the [`accept_elasticsearch`](/reference/operators/accept_elasticsearch.md) operator.

## Examples

### Query documents from a Elasticsearch index

Use [`from_http`](/reference/operators/from_http.md) to query the [Search API](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html). The Search API supports `GET` and `POST` requests to `/{index}/_search`. When you provide a request body, `from_http` uses `post` by default.

```tql
from_http "https://localhost:9200/main/_search",
  body={
    size: 100,
    query: {match_all: {}},
    sort: [{"@timestamp": {order: "desc"}}],
  } {
  read_json
}
unroll hits.hits
this = hits.hits._source
```

Add an `Authorization` header if your Elasticsearch cluster requires authentication.

### Export large result sets with `search_after`

For larger exports, prefer `search_after` with a stable sort. Return a request record from `paginate` to replace the request body for each next page. The next request keeps the same URL, method, and headers unless the request record changes them.

Keep only the response parser inside the `from_http` subpipeline. Operators such as `unroll` belong after `from_http`, so the pagination lambda receives the whole search response envelope.

```tql
from_http "https://localhost:9200/main/_search",
  body={
    size: 1000,
    query: {match_all: {}},
    sort: [{"@timestamp": "asc"}, {"_id": "asc"}],
  },
  paginate=(x => {
    body: {
      size: 1000,
      query: {match_all: {}},
      sort: [{"@timestamp": "asc"}, {"_id": "asc"}],
      search_after: x.hits.hits[-1].sort,
    },
  } if x.hits.hits != []) {
  read_json
}
unroll hits.hits
this = hits.hits._source
```

Add an `Authorization` header if your Elasticsearch cluster requires authentication.

### Export large result sets with scroll

Use the [Scroll API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-scroll) when you need a server-side search context for a long-running export. Start with a search request that includes a `scroll` query parameter, then return a request record that switches the next URL to `/_search/scroll` and sends the latest `_scroll_id` in the body:

```tql
let $search = "https://localhost:9200/main/_search?scroll=10m"
let $scroll = "https://localhost:9200/_search/scroll"


from_http $search,
  body={
    size: 10000,
    query: {match_all: {}},
  },
  paginate=(x => {
    url: $scroll,
    body: {
      scroll: "10m",
      scroll_id: x._scroll_id,
    },
  } if x.hits.hits != []) {
  read_json
}
unroll hits.hits
this = hits.hits._source
```

The paginated request inherits the `POST` method from the initial request because the initial request has a body. It also keeps the configured headers. Close the scroll context when the export is complete, because Elasticsearch keeps the search context alive until the scroll timeout expires.

### Send events to a Elasticsearch index

Send an example event to the `main` index:

```tql
from {event: "example"}
to_elasticsearch "1.2.3.4:9200", action="create", index="main"
```

Instead of treating the entire event as a document to be indexed by Elasticsearch, you can designate a nested record as the document:

```tql
from {category: "qux", doc_id: "XXX", event: {foo: "bar"}}
to_elasticsearch "localhost:9200", id=doc_id, doc=event, action="update", index=category
```

The above example updates the document with ID `XXX` with the contents from the nested field `event`.

### Accept data by emulating Elasticsearch

Tenzir can act as a drop-in replacement for Elasticsearch by accepting data via a Bulk API endpoint. This allows you to point your [Logstash](https://www.elastic.co/logstash) or Beats instances to Tenzir instead.

```tql
accept_elasticsearch "0.0.0.0:9200", keep_actions=true
publish "elasticsearch"
```

This pipeline accepts data on port 9200 and publishes all received events on the `elasticsearch` topic for further processing by other pipelines.

Use `accept_elasticsearch` for new pipelines that receive bulk ingestion data.

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

## See Also

* [OpenSearch](opensearch.md)