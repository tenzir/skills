---
title: "Search across data stores"
description: "Run federated searches across heterogeneous SIEMs, databases, EDRs, and archives in one normalized TQL pipeline."
canonical: https://tenzir.com/docs/guides/search/search-across-data-stores
source: https://tenzir.com/docs/guides/search/search-across-data-stores.md
section: "Docs"
---

# Search across data stores

> Run federated searches across heterogeneous SIEMs, databases, EDRs, and archives in one normalized TQL pipeline.

When an investigation starts with an IP address or a hostname, the evidence is rarely in one place: network flows sit in ClickHouse, authentication logs live in Splunk or Axiom, endpoint telemetry lives in Microsoft Defender or SentinelOne, and older records rest in S3 Parquet archives. **Federated search** queries each store where the data already lives, normalizes the matching rows into a shared schema, and combines the results in a single pipeline without centralizing all telemetry first.

This guide shows how to combine independent store queries with [`merge`](../../reference/operators/merge.md), fan investigation requests across stores with [`fork_merge`](../../reference/operators/fork_merge.md), push filters written on normalized OCSF fields back into each target’s native query, and continue straight into enrichment, detection, or routing.

## Combine independent searches with `merge`

Use [`merge`](../../reference/operators/merge.md) when you already know the indicator and time range and want to query several stores concurrently into one stream. Each `merge` block starts with its own source, pushes its selective filters into that target, normalizes the matches into a common shape, and stamps a provenance field before joining the main stream.

The following pipeline searches ClickHouse, Splunk, and Microsoft Defender for connections to the same destination IP during a one-hour window, aligns all three to OCSF Network Activity fields, and sorts the combined timeline:

```tql
let $indicator = 192.0.2.42
let $start = 2026-09-01T10:00:00Z
let $end = 2026-09-01T11:00:00Z


from_clickhouse table="ocsf.network_activity",
  host="clickhouse.example.com",
  password=secret("CLICKHOUSE_PASSWORD")
where dst_endpoint.ip == $indicator and time >= $start and time < $end
select time, src_endpoint.ip, dst_endpoint.ip
source = "clickhouse"
merge {
  from_splunk "https://splunk.example.com:8089",
    index="network",
    earliest=$start,
    latest=$end,
    headers={Authorization: secret("splunk-rest-authorization")}
  where dest_ip == $indicator
  this = {
    time: _time,
    src_endpoint: {ip: src_ip.ip()},
    dst_endpoint: {ip: dest_ip.ip()},
    source: "splunk",
  }
}
merge {
  from_microsoft_defender "DeviceNetworkEvents",
    azure_auth={
      tenant_id: secret("AZURE_TENANT_ID"),
      client_id: secret("AZURE_CLIENT_ID"),
      client_secret: secret("AZURE_CLIENT_SECRET"),
    },
    start=$start,
    end=$end
  where ActionType == "ConnectionSuccess" and RemoteIP == $indicator
  this = {
    time: Timestamp,
    src_endpoint: {ip: LocalIP.ip()},
    dst_endpoint: {ip: RemoteIP.ip()},
    source: "defender",
  }
}
sort time
head 500
```

Each store filters its own data before returning matches: ClickHouse evaluates its `WHERE` clause over named tuple columns, Splunk searches its `network` index for `dest_ip`, and Defender appends a KQL `where` stage on `ActionType` and `RemoteIP`. Because `DeviceNetworkEvents` records both inbound and outbound connections, filtering to outbound `ConnectionSuccess` events ensures `LocalIP` maps to `src_endpoint.ip` and `RemoteIP` maps to `dst_endpoint.ip`. Because `merge` runs every branch concurrently, arrival order is undefined; the final [`sort`](../../reference/operators/sort.md) and [`head`](../../reference/operators/head.md) assemble a bounded, chronological timeline across all three sources. The same pattern extends to any other remote source, such as adding a [`from_axiom`](../../reference/operators/from_axiom.md) branch that pushes APL filters into an [Axiom](https://tenzir.com/product/integrations/axiom) dataset (see our [Axiom optimizations reference](../../reference/optimizations/axiom.md)).

## Fan investigation requests across stores with `fork_merge`

When the search parameters come from an input stream, such as a list of indicators, a set of incident tickets, or upstream alerts, use

[`fork_merge`](../../reference/operators/fork_merge.md) to send every request event to all backend branches and collect their answers back into one stream.

Because source operators produce events on their own rather than consuming an upstream stream, wrap each branch’s source inside [`each`](../../reference/operators/each.md). Inside `each`, `$this` binds the current request record so every branch can parameterize its query and time range from the same input:

```tql
from {
  ip: 192.0.2.42,
  start: 2026-09-01T10:00:00Z,
  end: 2026-09-01T11:00:00Z,
}, {
  ip: 198.51.100.17,
  start: 2026-09-01T10:00:00Z,
  end: 2026-09-01T11:00:00Z,
}
fork_merge {
  each {
    from_splunk "https://splunk.example.com:8089",
      index="network",
      earliest=$this.start,
      latest=$this.end,
      headers={Authorization: secret("splunk-rest-authorization")}
    where dest_ip == $this.ip
    this = {
      event: {
        time: _time,
        class_uid: 4001,
        activity_id: 1,
        src_endpoint: {ip: src_ip.ip()},
        dst_endpoint: {ip: dest_ip.ip()},
      },
      origin: product,
      uid: event_uid,
      backend: "splunk",
    }
  }
}, {
  each {
    from_clickhouse table="ocsf.network_activity",
      host="clickhouse.example.com",
      password=secret("CLICKHOUSE_PASSWORD")
    where dst_endpoint.ip == $this.ip
    where time >= $this.start and time < $this.end
    this = {
      event: {
        time: time,
        class_uid: class_uid,
        activity_id: activity_id,
        src_endpoint: {ip: src_endpoint.ip},
        dst_endpoint: {ip: dst_endpoint.ip},
      },
      origin: metadata.product.name,
      uid: metadata.uid,
      backend: "clickhouse",
    }
  }
}, {
  each {
    from_s3 "s3://security-archive/network/**/*.parquet" {
      read_parquet
    }
    where time >= $this.start and time < $this.end
    where dst_endpoint.ip == $this.ip
    this = {
      event: {
        time: time,
        class_uid: class_uid,
        activity_id: activity_id,
        src_endpoint: {ip: src_endpoint.ip},
        dst_endpoint: {ip: dst_endpoint.ip},
      },
      origin: metadata.product.name,
      uid: metadata.uid,
      backend: "archive",
    }
  }
}
fork_merge {
  where origin != null and uid != null
  summarize origin, uid, event=first(event), seen_in=distinct(backend)
}, {
  where origin == null or uid == null
  select origin, uid, event, seen_in=[backend]
}
sort event.time, origin, uid
head 500
```

When the same observation was routed to both a SIEM and a lake or archive, two branches return the same event. Map every branch into the same `(origin, uid)` producer namespace and stable event identifier (here, the producing product name and event UID). The second `fork_merge` keeps unidentified records safe: events with both `origin` and `uid` present are grouped with [`summarize`](../../reference/operators/summarize.md) (taking a representative record with [`first`](../../reference/functions/first.md) and collecting retrieval sources with [`distinct`](../../reference/functions/distinct.md)), while events where either key is `null` bypass grouping with `seen_in=[backend]` so unrelated records never collapse together. If you only need the first sighting of identified events and do not need `seen_in`, replace the first branch’s `summarize` with [`deduplicate`](../../reference/operators/deduplicate.md) on `origin, uid` while keeping the `null`-bypass branch intact.

In the S3 branch, `**/*.parquet` covers arbitrary date ranges without skipping partitions across midnight UTC or month boundaries, while `where time >= $this.start and time < $this.end` enforces the exact window. When your requests always stay within a single UTC day or month, you can narrow the S3 prefix explicitly (for example with `$this.start.format_time("%Y/%m/%d")`) to reduce object listings.

For large indicator lists, set `parallel` on `each` (for example `each parallel=4`) to bound the number of concurrent child subpipelines per operator instance. This caps in-flight concurrency within one instance rather than enforcing a deployment-wide or requests-per-second rate limit.

## Filter on normalized OCSF fields and still push down

Normalization does not force you to give up filter optimization. Before a pipeline runs, Tenzir’s optimizer walks predicates backwards through

[`set`](../../reference/operators/set.md) assignments, field renames, constants, record literals, `if` and `match` branches, and calls to the [`ocsf_cast`](../../reference/functions/ocsf_cast.md) function. Moving a filter ahead of normalization is distinct from what the remote target takes over: the optimizer always moves eligible predicates in front of the mapping so Tenzir never normalizes non-matching rows, and the remote source then hands its target every leading predicate that the target can spell.

Consider a pipeline that reads Windows security events from Azure Log Analytics, maps Event ID `4624` to OCSF Authentication (`class_uid: 3002`) and Event ID `4688` to OCSF Process Activity (`class_uid: 1007`) with `match`, and then filters in OCSF terms. On Windows Event `4624`, `Computer` is the host recording the logon (`dst_endpoint.hostname`), while `WorkstationName` is the originating workstation (`src_endpoint.hostname`):

```tql
from_azure_log_analytics "SecurityEvent",
  workspace_id=secret("azure-workspace-id"),
  azure_auth={
    tenant_id: secret("azure-tenant-id"),
    client_id: secret("azure-client-id"),
    client_secret: secret("azure-client-secret"),
  },
  start=2026-01-01T00:00:00Z,
  end=2026-01-02T00:00:00Z
match EventID {
  4624 => {
    this = {
      time: TimeGenerated,
      category_uid: 3,
      class_uid: 3002,
      activity_id: 1,
      type_uid: 300201,
      severity_id: 1,
      metadata: {version: "1.9.0"},
      dst_endpoint: {hostname: Computer},
      src_endpoint: {hostname: WorkstationName},
      user: {name: Account},
    }
  }
  4688 => {
    this = {
      time: TimeGenerated,
      category_uid: 1,
      class_uid: 1007,
      activity_id: 1,
      type_uid: 100701,
      severity_id: 1,
      metadata: {version: "1.9.0"},
      device: {hostname: Computer},
      user: {name: Account},
    }
  }
  _ => {
    this = {
      time: TimeGenerated,
      category_uid: 0,
      class_uid: 0,
      activity_id: 0,
      type_uid: 0,
      severity_id: 1,
      metadata: {version: "1.9.0"},
    }
  }
}
where class_uid == 3002 and dst_endpoint.hostname == "dc01"
```

Before executing the query, the optimizer rewrites the final `where` step by step:

1. Through `match EventID`, the `4688` arm (`class_uid: 1007`) and the wildcard arm (`class_uid: 0`) cannot satisfy `class_uid == 3002`, so both branches drop out of the predicate.
2. Inside the `4624` arm, `dst_endpoint.hostname == "dc01"` rewrites to `Computer == "dc01"`.
3. Both rewritten predicates (`EventID == 4624` and `Computer == "dc01"`) reach [`from_azure_log_analytics`](../../reference/operators/from_azure_log_analytics.md), so Azure Log Analytics executes both filters in KQL.

If you also cast the normalized record with `this = ocsf_cast(this)` before the `where`:

```tql
// Placed immediately after the `match` block above:
this = ocsf_cast(this)
where class_uid == 3002 and dst_endpoint.hostname == "dc01"
```

Because every branch assigns constant `class_uid` and `metadata.version` values, the schema lookup inside the `ocsf_cast` function still folds away and both predicates move ahead of `ocsf_cast` and `match`. Log Analytics takes over `EventID == 4624` in KQL. For `dst_endpoint.hostname == "dc01"`, `ocsf_cast` adds a `type_kind(Computer) == "string"` guard to match the OCSF schema type. Log Analytics cannot spell `type_kind`, so that second `where` stays right after the source in Tenzir: it still filters out non-matching events before `match` and `ocsf_cast` run, rather than executing remotely in KQL.

Analysts and shared packages can therefore write filters against OCSF fields while keeping selective work ahead of normalization and pushing the leading target-supported predicates into the store. Our explanation of [pipeline optimization](../../explanations/pipeline.md#optimization) covers these rewrites in detail, and our explanation of [inspecting a transpiled pipeline](../../explanations/transpilation.md#inspect-a-transpiled-pipeline) shows how to check which stages your target takes over on your own mappings.

## Continue the pipeline after search

Because a federated search produces a regular, normalized Tenzir event stream, the pipeline does not have to stop at printing matches. Append enrichment, detection, or routing stages directly after the merged timeline. Continuing from the `merge` pipeline above, where `src_endpoint` and `dst_endpoint` sit at the top level:

```tql
// Append directly after the `merge` pipeline above:
enrichments = []
context_enrich "assets", key=src_endpoint.ip, into=src_asset
context_enrich "threat_intel",
  key=dst_endpoint.ip,
  into=enrichments,
  mode="append",
  format="ocsf"
where enrichments.length() > 0
publish "investigation-findings"
```

When continuing from the `fork_merge` pipeline instead, where the normalized record sits under `event`, pass `key=event.src_endpoint.ip` and `key=event.dst_endpoint.ip`.

In this continuation, [`context_enrich`](../../reference/operators/context_enrich.md) attaches asset ownership and threat intelligence from declared lookup-table contexts, filters down to hits with threat-intel matches, and publishes the enriched findings with

[`publish`](../../reference/operators/publish.md) for downstream alerting or ticketing pipelines.

When historical evidence lives in object storage rather than a database or SIEM, follow our guide on [querying open archives in place](query-open-archives-in-place.md) to scan Parquet archives directly without rehydration.

## See also

* [Push queries to data stores](push-queries-to-data-stores.md)
* [Query open archives in place](query-open-archives-in-place.md)
* [Split and merge streams](../route/split-and-merge-streams.md)
* [Map to OCSF](../normalize/map-to-ocsf.md)
* [Use lookup tables](../enrich/use-lookup-tables.md)
* [Deduplicate events](../optimize/deduplicate-events.md)
* [Match events with TQL](../detect/match-events-with-tql.md)
* [Transpilation](../../explanations/transpilation.md)
* [Pipeline](../../explanations/pipeline.md)
* [Optimizations](../../reference/optimizations.md)
