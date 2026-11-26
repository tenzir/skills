---
title: "Query open archives in place"
description: "Search local and S3 Parquet archives directly with row-group skipping, column projection, or embedded DuckDB SQL without rehydrating into a SIEM."
canonical: https://tenzir.com/docs/guides/search/query-open-archives-in-place
source: https://tenzir.com/docs/guides/search/query-open-archives-in-place.md
section: "Docs"
---

# Query open archives in place

> Search local and S3 Parquet archives directly with row-group skipping, column projection, or embedded DuckDB SQL without rehydrating into a SIEM.

Retaining security telemetry in open Apache Parquet files on object storage keeps long-term storage cheap, and querying those files in place avoids paying twice to rehydrate historical logs back into a SIEM. Tenzir scans Parquet archives directly from local filesystems or immediately readable object-storage tiers (such as S3 Standard or S3 Standard-IA) using two complementary approaches: streaming scans with [`read_parquet`](../../reference/operators/read_parquet.md), and in-memory SQL queries with embedded [`from_duckdb`](../../reference/operators/from_duckdb.md). Objects kept in offline storage tiers (such as Amazon S3 Glacier Flexible Retrieval or Amazon S3 Glacier Deep Archive) must still be restored at the object-storage layer before range reads can access them.

This guide shows how to narrow archive scans with partition globs, how `read_parquet` acts on optimizer hints while preserving TQL semantics, when to query Parquet through embedded DuckDB, and how to combine archive hits with hot data stores.

## Narrow scans with partition globs

When you archive events with `partition_by` as shown in our guide on [writing partitioned files](../store/write-partitioned-files.md), high-level dimensions such as day, region, or OCSF class live in the directory path. Match only the partitions your investigation covers so Tenzir skips unrelated objects before opening a single file.

Read matching OCSF Network Activity records from a single day’s partition in Amazon S3 with [`from_s3`](../../reference/operators/from_s3.md) and [`read_parquet`](../../reference/operators/read_parquet.md), pairing a bounded `time` predicate with the target IP filter:

```tql
from_s3 "s3://security-lake/ocsf/network/eventDay=20260117/*.parquet" {
  read_parquet
}
where time >= 2026-01-17T10:00:00Z and time < 2026-01-17T11:00:00Z
where dst_endpoint.ip == 192.0.2.42
select time, src_endpoint.ip, dst_endpoint.ip, dst_endpoint.port
head 100
```

For archives stored on a local or mounted filesystem, use [`from_file`](../../reference/operators/from_file.md) with the same glob syntax:

```tql
from_file "/var/archive/ocsf/network/**/day=17/*.parquet" {
  read_parquet
}
where time >= 2026-01-17T10:00:00Z and time < 2026-01-17T11:00:00Z
where dst_endpoint.ip == 192.0.2.42
select time, src_endpoint.ip, dst_endpoint.ip, dst_endpoint.port
head 100
```

If your archive encrypts Parquet files with AES-GCM, pass the key explicitly using [`decode_base64`](../../reference/functions/decode_base64.md) and [`secret`](../../reference/functions/secret.md). Automatic format detection cannot supply the key, so always keep `read_parquet` in the subpipeline:

```tql
from_s3 "s3://security-archive/ocsf/eventDay=20260117/*.parquet" {
  read_parquet encryption_key=decode_base64(secret("PARQUET_KEY"))
}
where dst_endpoint.ip == 192.0.2.42
```

Partition globs eliminate entire directories up front, and `read_parquet` then narrows what it reads inside each matching file.

## How `read_parquet` acts on optimizer hints

Unlike remote databases whose targets transpile operators and execute them with target-specific semantics, [`read_parquet`](../../reference/operators/read_parquet.md) acts on [local hints](../../explanations/transpilation.md#transpiled-targets-vs-local-hints) from the optimizer and always preserves exact TQL semantics. The [`where`](../../reference/operators/where.md), [`select`](../../reference/operators/select.md), and [`head`](../../reference/operators/head.md) operators remain in the pipeline and run on what `read_parquet` produces, so null handling, string matching, and type behavior stay identical to TQL everywhere else.

When `read_parquet` heads the subpipeline of [`from_s3`](../../reference/operators/from_s3.md), [`from_file`](../../reference/operators/from_file.md), [`from_google_cloud_storage`](../../reference/operators/from_google_cloud_storage.md), or [`from_azure_blob_storage`](../../reference/operators/from_azure_blob_storage.md), it uses three hints to minimize both I/O and decoding work:

* **Row-group skipping.** The reader inspects each row group’s min/max statistics in the Parquet footer and skips row groups whose statistics rule out a match (surviving row groups can still hold zero matching rows once decoded). This is most effective on sorted or clustered timestamp or numeric columns such as `time`. Tenzir’s Parquet pruner does not prune on min/max statistics for fixed-length byte arrays such as typed `ip` fields (`dst_endpoint.ip`), which are evaluated while decoding, so pairing an IP filter with a bounded `time` predicate is what lets the reader skip entire row groups.
* **Column projection.** The reader decodes only the columns and nested record fields referenced by `select`, `summarize`, and `where`. A filter that calls a function conservatively keeps all columns.
* **Early stop.** Decoding and fetching stop as soon as enough matching events satisfy `head`.

On object stores, `read_parquet` reads the file footer first and then issues HTTP range requests for only the selected column chunks, one row group at a time. Because it releases each row group after decoding while prefetching the next, memory usage stays bounded by two row groups rather than the total file size.

To confirm which predicates, columns, and row limits a pipeline passes to `read_parquet`, see our explanation of [inspecting a transpiled pipeline](../../explanations/transpilation.md#inspect-a-transpiled-pipeline).

## Query Parquet files with embedded DuckDB SQL

When an archive investigation requires SQL joins across separate Parquet datasets, window functions, or multi-file SQL analytics, run [`from_duckdb`](../../reference/operators/from_duckdb.md) with an in-memory database (`":memory:"`) and a `sql` query. DuckDB runs embedded inside Tenzir with no external database server to deploy, reads Parquet globs directly, and streams the query results into the rest of your TQL pipeline.

The following pipeline joins a day’s archived flow Parquet files against an asset inventory Parquet file and ranks the top outbound talkers by asset owner:

```tql
from_duckdb ":memory:",
  sql=r#"
    SELECT
      f.src_ip,
      a.owner,
      count(*) AS connections,
      sum(f.bytes_out) AS total_bytes
    FROM '/var/archive/flows/day=17/*.parquet' f
    LEFT JOIN '/var/archive/assets/inventory.parquet' a
      ON f.src_ip = a.ip
    WHERE f.bytes_out > 1000000
    GROUP BY f.src_ip, a.owner
    ORDER BY total_bytes DESC
    LIMIT 50
  "#
```

In `sql` mode, DuckDB executes the SQL query as written without TQL pushdown, and any operators you append after `from_duckdb` continue processing the returned rows in TQL.

Choose the reader that fits your workload:

* Use `from_s3` or `from_file` with `read_parquet` for direct object-store range reads, encrypted Parquet files (`encryption_key`), strict TQL semantics, and streaming scans that compose cleanly with TQL filters and normalization.
* Use `from_duckdb ":memory:"` with `sql` when you need SQL joins across multiple Parquet files or DuckDB-specific SQL functions.

## Combine archive hits with hot data stores

Historical investigations often span both cold object-store archives and hot tables in a database or SIEM. Use [`merge`](../../reference/operators/merge.md) to query an S3 Parquet archive and a hot ClickHouse table in the same pipeline, tag each source tier, enrich the combined hits with a lookup-table context via [`context_enrich`](../../reference/operators/context_enrich.md), and order the result by time:

```tql
let $indicator = 192.0.2.42
let $start = 2026-01-17T00:00:00Z
let $end = 2026-01-18T00:00:00Z


from_s3 "s3://security-lake/ocsf/network/eventDay=202601*/*.parquet" {
  read_parquet
}
where time >= $start and time < $end
where dst_endpoint.ip == $indicator
select time, src_endpoint.ip, dst_endpoint.ip, dst_endpoint.port
tier = "archive"
merge {
  from_clickhouse table="ocsf.network_activity",
    host="clickhouse.example.com",
    password=secret("CLICKHOUSE_PASSWORD")
  where time >= $start and time < $end
  where dst_endpoint.ip == $indicator
  select time, src_endpoint.ip, dst_endpoint.ip, dst_endpoint.port
  tier = "hot"
}
context_enrich "assets", key=src_endpoint.ip, into=src_asset
sort time
```

The S3 branch skips row groups whose `time` statistics fall outside the window and reads only the needed column chunks via range requests, ClickHouse pushes the filters and projection into SQL over its hot table, and both streams converge into a single enriched timeline.

Querying in place is designed for selective investigations and analytics over stored files. When you instead want to feed an entire historical Parquet archive back through a live detection pipeline with exact event-time ordering, timestamp shifting, or paced replay, follow our guide on [replaying historical events](../replay/replay-historical-events.md).

## See also

* [Push queries to data stores](push-queries-to-data-stores.md)
* [Search across data stores](search-across-data-stores.md)
* [Write partitioned files](../store/write-partitioned-files.md)
* [Replay historical events](../replay/replay-historical-events.md)
* [Amazon S3](https://tenzir.com/product/integrations/amazon/s3.md)
* [DuckDB](https://tenzir.com/product/integrations/duckdb.md)
* [Transpilation](../../explanations/transpilation.md)
* [Pipeline](../../explanations/pipeline.md)
* [Optimizations](../../reference/optimizations.md)
