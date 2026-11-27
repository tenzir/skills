---
title: "from_iceberg"
canonical: https://tenzir.com/docs/reference/operators/from_iceberg
source: https://tenzir.com/docs/reference/operators/from_iceberg.md
section: "Docs"
---

# from_iceberg

> Reads events from an Apache Iceberg table through a REST catalog.

Reads events from an Apache Iceberg table through a REST catalog.

```tql
from_iceberg table:string, catalog=string,
  [warehouse=string, catalog_aws_service=string, token=string, aws_iam=record,
   s3_endpoint=string, s3_path_style=bool,
   gcp_service_account_key=string, gcp_project=string,
   decimal_format=string,
   snapshot_id=int, as_of=time, ref=string,
   live=bool, poll_interval=duration,
   from_snapshot_id=int, to_snapshot_id=int]
```

## Description

The `from_iceberg` operator reads events from an [Apache Iceberg](https://iceberg.apache.org) table through a REST catalog. It reads Parquet and Avro data files directly from the table’s object store, matches columns by Iceberg field ID across schema evolution, and applies Iceberg v2 Merge-on-Read delete files. You can query the current snapshot, travel to an earlier snapshot or named reference, scan a bounded range of incremental appends, or tail newly committed snapshots continuously.

Experimental

This operator is experimental. Its arguments, type mappings, and incremental scan behavior may change in future releases.

### `table: string`

The identifier of the table in the form `namespace.table_name`. Additional dots address nested namespaces, for example `prod.security.ocsf`.

### `catalog = string`

The URL of the Iceberg REST catalog, for example `https://catalog.example.com`.

When `catalog` points to an `https://*.googleapis.com` endpoint (such as Google Lakehouse) and you set neither `token` nor `catalog_aws_service`, Google Cloud authentication activates automatically using Application Default Credentials.

### `warehouse = string (optional)`

The catalog-specific warehouse identifier, for catalogs that serve multiple warehouses. Its format depends on the catalog:

* AWS Glue: the Glue catalog ID, typically the 12-digit AWS account ID.
* Amazon S3 Tables: the table bucket ARN.
* Google Lakehouse (formerly BigLake): a `bl://projects/PROJECT_ID/catalogs/CATALOG_ID` identifier, or `gs://BUCKET` for a single-bucket catalog.
* Other REST catalogs: the warehouse identifier that catalog expects.

### `catalog_aws_service = string (optional)`

Authenticates requests to an AWS-managed Iceberg REST catalog with AWS Signature Version 4:

* `"glue"`: signs for the AWS Glue Data Catalog.
* `"s3tables"`: signs for Amazon S3 Tables.

Credentials come from `aws_iam` when supplied and from the AWS default credentials provider chain otherwise. The same refreshable provider authenticates catalog requests and S3 data-file operations. Configure the AWS Region through `aws_iam`, the selected AWS profile, or the `AWS_REGION` or `AWS_DEFAULT_REGION` environment variables.

Cannot be combined with `token`, Google Cloud authentication, or a Google Cloud catalog URL.

### `token = string (optional)`

A bearer token for authenticating requests to the catalog.

Cannot be combined with `catalog_aws_service`, `gcp_service_account_key`, or `gcp_project`.

### `aws_iam = record (optional)`

Configures explicit AWS credentials or IAM role assumption. If not specified, the operator uses the AWS SDK’s default credential chain.

```tql
{
  region: string,            // AWS region for API requests.
  access_key_id: string,     // AWS access key ID.
  secret_access_key: string, // AWS secret access key.
  session_token: string,     // session token for temporary credentials.
  assume_role: string,       // ARN of IAM role to assume.
  session_name: string,      // session name for role assumption.
  external_id: string,       // external ID for role assumption.
  web_identity: record,      // OIDC web identity token configuration.
}
```

See [AWS Authentication](../aws-authentication.md) for a description of every field, the default credential chain, web identity configuration, and local authentication with the AWS CLI.

### `s3_endpoint = string (optional)`

A custom endpoint for S3-compatible object stores such as MinIO. Requests authenticate with AWS Signature Version 4, so pair this option with `aws_iam` to provide credentials.

### `s3_path_style = bool (optional)`

Uses path-style addressing (`endpoint/bucket/key`) instead of virtual-hosted addressing (`bucket.endpoint/key`).

Requires `s3_endpoint` and defaults to `true` when `s3_endpoint` is set, because most S3-compatible stores require path-style addressing. Set `s3_path_style=false` for stores that use virtual-hosted addressing.

### `gcp_service_account_key = string (optional)`

A Google service account key in JSON format. Setting this option activates Google Cloud authentication automatically for both the catalog and `gs://` object storage, minting and refreshing OAuth2 tokens without additional configuration.

Cannot be combined with `token` or `catalog_aws_service`.

### `gcp_project = string (optional)`

The Google Cloud project to bill and scope requests to, when it differs from the project of the credential. Setting this option activates Google Cloud authentication automatically.

Cannot be combined with `token` or `catalog_aws_service`.

Tables with `gs://` storage locations automatically resolve through native Google Cloud Storage unless explicit S3 settings (`aws_iam`, `catalog_aws_service`, or `s3_endpoint`) are configured.

### `decimal_format = string (optional)`

Controls how Iceberg `decimal` values decode:

* `"string"`: preserves exact decimal values as strings without losing precision.
* `"float"`: converts decimal values to `double`, which can lose precision.

Defaults to `"string"`. The setting applies recursively to decimal values nested inside structs, lists, and maps.

### `snapshot_id = int (optional)`

Reads a specific snapshot by its non-negative Iceberg snapshot ID, using that snapshot’s schema.

Mutually exclusive with `as_of`, `ref`, `live=true`, `from_snapshot_id`, and `to_snapshot_id`.

### `as_of = time (optional)`

Reads the latest snapshot committed at or before the specified timestamp, using that snapshot’s schema. Combine with `ref` to query the history of a named branch; tags are not allowed with `as_of`.

Mutually exclusive with `snapshot_id`, `live=true`, `from_snapshot_id`, and `to_snapshot_id`.

### `ref = string (optional)`

Reads from a named Iceberg branch or tag instead of the `main` branch. Must not be empty.

Mutually exclusive with `snapshot_id`. Tags are immutable snapshot references and cannot be combined with `as_of` or `live=true`.

### `live = bool (optional)`

Continuously polls the table (or the branch selected by `ref`) for newly committed snapshots and emits appended rows as they arrive.

Without `from_snapshot_id`, the operator first reads the current snapshot and then streams subsequent appends. With `from_snapshot_id`, it streams only snapshots committed after that snapshot ID.

Defaults to `false`. Mutually exclusive with `snapshot_id`, `as_of`, and `to_snapshot_id`.

### `poll_interval = duration (optional)`

The interval between metadata refreshes when `live=true`. Must be a positive duration and requires `live=true`.

Defaults to `10s`.

### `from_snapshot_id = int (optional)`

The exclusive starting snapshot ID for an incremental append scan. Must be non-negative.

In one-shot mode, the operator emits rows appended after `from_snapshot_id` up to `to_snapshot_id`, or up to the current snapshot on `ref` (or `main`) when `to_snapshot_id` is omitted. With `live=true`, it sets the initial cursor so only newer snapshots are streamed.

Mutually exclusive with `snapshot_id` and `as_of`.

### `to_snapshot_id = int (optional)`

The inclusive ending snapshot ID for a bounded incremental append scan. Must be non-negative and requires `from_snapshot_id`.

Mutually exclusive with `snapshot_id`, `as_of`, and `live=true`.

## Data types

The operator maps Iceberg types to Tenzir types as follows:

| Iceberg type                                                 | Tenzir type        | Notes                                                                                               |
| ------------------------------------------------------------ | ------------------ | --------------------------------------------------------------------------------------------------- |
| `boolean`                                                    | `bool`             |                                                                                                     |
| `int`, `long`                                                | `int64`            |                                                                                                     |
| `float`, `double`                                            | `double`           |                                                                                                     |
| `decimal(P, S)`                                              | `string`           | Exact decimal text by default; `double` when `decimal_format="float"`.                              |
| `date`                                                       | `time`             | Midnight UTC.                                                                                       |
| `time`                                                       | `duration`         | Time of day since midnight.                                                                         |
| `timestamp`, `timestamptz`, `timestamp_ns`, `timestamptz_ns` | `time`             |                                                                                                     |
| `string`                                                     | `string`           |                                                                                                     |
| `uuid`                                                       | `string`           | Canonical lowercase hyphenated UUID text.                                                           |
| `fixed(L)`, `binary`, `geometry`, `geography`                | `blob`             |                                                                                                     |
| `struct`                                                     | `record`           | Fields map recursively.                                                                             |
| `list`                                                       | `list`             | Element types map recursively.                                                                      |
| `map`                                                        | `record` or `list` | String-keyed maps become `record`; non-string-keyed maps become a `list` of `{key, value}` records. |
| `unknown`                                                    | `null`             |                                                                                                     |
| `variant`                                                    | Unsupported        | Reading a projected `variant` column fails with an error.                                           |

Tenzir `time` values represent nanosecond timestamps covering roughly the years 1678 to 2261. Any `date`, `timestamp`, or `timestamptz` value outside that representable range becomes `null`, and the operator emits one warning per affected column.

## Schema evolution and delete files

The operator reads both Parquet and Avro data files, including tables written by [`to_iceberg`](to_iceberg.md) or external engines such as Spark, Trino, and DuckDB. During decoding, columns resolve by Iceberg field ID rather than column name or position:

* Columns added after a data file was written are filled with `null`.
* Renamed fields appear under their current name in the selected schema.
* Legal Iceberg type promotions (such as `int` to `long` and `float` to `double`) widen transparently when reading older files.

For Iceberg v2 Merge-on-Read tables, the operator applies both position delete files and equality delete files while reading data files so deleted rows are excluded from the output.

## Time travel and incremental reads

The operator supports three reading modes:

* **Point-in-time snapshot reads**: Omit all snapshot arguments to read the current snapshot of the `main` branch, or select a target with `snapshot_id`, `as_of`, or `ref`. Point-in-time reads with `snapshot_id`, `as_of`, or a tag use that snapshot’s historical schema.
* **Bounded incremental append scans**: Supply `from_snapshot_id` (and optionally `to_snapshot_id`) to emit rows appended strictly after `from_snapshot_id` through the target snapshot.
* **Live tailing**: Set `live=true` to read the initial state (or start after `from_snapshot_id`) and then refresh table metadata every `poll_interval`, streaming each newly committed incremental window as it arrives.

Incremental scans follow Iceberg append semantics:

* Compaction (`replace`) snapshots are skipped silently because they rewrite existing rows without introducing new data.
* If an incremental window contains `overwrite` or `delete` snapshots, the operator skips them and emits a warning because only appended rows are emitted.
* If the starting snapshot has expired or the branch lineage was rewritten so that the starting snapshot is no longer an ancestor of the target snapshot, the scan fails with an error. For a running `live=true` reader, if snapshot expiration or a branch rollback cuts the snapshot history behind it, the operator exits with a diagnostic explaining that restarting without the saved cursor reads the table from the beginning unless you pass a current `from_snapshot_id` from the table’s active history.

When checkpointing is enabled, the operator persists bounded cursor state (the table UUID, pinned snapshot or active window, file index, row offset, and current file path) so a restarted pipeline resumes without re-reading completed files or snapshots. If the table is dropped and recreated with a different UUID between checkpoints, recovery fails instead of reading from the wrong table.

## Optimizations

The operator consumes hints pushed down by the TQL optimizer from downstream [`where`](where.md), [`select`](select.md), [`drop`](drop.md), [`summarize`](summarize.md), and [`head`](head.md) operators while preserving exact TQL semantics:

* **Filter pushdown**: Translates supported predicates into conservative Iceberg scan expressions for hidden-partition manifest pruning and column-metrics data-file pruning. Supported forms include comparisons (`==`, `!=`, `<`, `<=`, `>`, `>=`), membership (`in`), string prefix matching (`starts_with` with a constant prefix), null checks (`== null`, `!= null`), boolean logic (`and`, `or`, `not`), bare boolean fields, and nested struct paths. Unsupported expressions stay conservative and never prune files that could match. The exact TQL predicates still run locally inside the operator, so type conversions, null handling, and diagnostics match running `where` in the pipeline.
* **Column projection**: Reads only the columns referenced by downstream operators and filter predicates, including leaf pruning inside nested structs. For unfiltered zero-column queries such as `summarize count()`, the operator answers directly from snapshot metadata and the manifest list when confirmed free of delete files, without reading individual manifests or data files. When a scan does plan individual files, such as with a partition filter, whole-file tasks without delete files still count rows from manifest metadata without opening the data files.
* **Row limits**: Enforces [`head`](head.md) locally after applying delete files and filter predicates, stopping data-file decoding as soon as the limit is reached.

To keep throughput high on tables with many files in object storage, the operator plans manifests in parallel and prefetches upcoming data files concurrently while emitting files in deterministic order. This preserves reproducible file order and checkpoint recovery without needing an extra flag.

Use `--dump-opt-ir` to inspect the filter, projection, and limit hints that the optimizer attaches to `from_iceberg`:

```sh
tenzir run --dump-opt-ir '
  from_iceberg "security.ocsf", catalog="https://catalog.example.com"
  where class_uid == 1001 and time >= 2026-07-01
  select time, src_endpoint.ip, dst_endpoint.ip
  head 100
'
```

In the output, the `from_iceberg` node lists the absorbed `filter` predicates (`class_uid == 1001` and `time >= 2026-07-01`), `limit: 100`, and a `projection` containing `time`, `src_endpoint.ip`, `dst_endpoint.ip`, and the filter dependency `class_uid`. Running `--dump-opt-ir` on `from_iceberg ... | summarize events=count()` shows `projection: []`, which enables the metadata-only fast path when no delete files apply.

See the [optimizations reference](../optimizations.md) for an overview of how Tenzir optimizes sources and operators.

## Examples

### Query an OCSF table through a REST catalog

Filter by class and time, select specific nested fields, and cap the output:

```tql
from_iceberg "security.ocsf",
  catalog="https://catalog.example.com",
  token=secret("CATALOG_TOKEN")
where class_uid == 1001 and time >= 2026-07-01
select time, src_endpoint.ip, dst_endpoint.ip
head 100
```

### Read from AWS Glue

```tql
from_iceberg "security.events",
  catalog="https://glue.eu-central-1.amazonaws.com/iceberg",
  catalog_aws_service="glue",
  warehouse="123456789012"
where severity == "high"
```

### Read from Amazon S3 Tables

```tql
from_iceberg "security.events",
  catalog="https://s3tables.eu-central-1.amazonaws.com/iceberg",
  catalog_aws_service="s3tables",
  warehouse="arn:aws:s3tables:eu-central-1:123456789012:bucket/security-lake"
```

### Read from Google Lakehouse with automatic authentication

On GCE, GKE, or Cloud Run, Application Default Credentials activate automatically for `https://*.googleapis.com` catalog URLs:

```tql
from_iceberg "lake.events",
  catalog="https://biglake.googleapis.com/iceberg/v1/restcatalog",
  warehouse="bl://projects/my-project/catalogs/my-catalog"
```

Outside Google Cloud, pass a service account key with `gcp_service_account_key=secret("GCP_SA_KEY")`.

### Query a historical snapshot

Read the table state at a specific timestamp:

```tql
from_iceberg "security.ocsf",
  catalog="https://catalog.example.com",
  as_of=2026-06-15T12:00:00Z
```

Or read an exact snapshot by ID:

```tql
from_iceberg "security.ocsf",
  catalog="https://catalog.example.com",
  snapshot_id=7281940281940219
```

### Tail newly appended rows continuously

```tql
from_iceberg "security.ocsf",
  catalog="https://catalog.example.com",
  live=true,
  poll_interval=30s
where severity_id >= 4
```

## See Also

* [`to_iceberg`](to_iceberg.md)
* [Read from data stores](../../guides/collect/read-from-data-stores.md)
* [Apache Iceberg](https://tenzir.com/product/integrations/iceberg.md)
* [AWS Glue](https://tenzir.com/product/integrations/amazon/glue.md)
* [Cloud Lakehouse](https://tenzir.com/product/integrations/google/cloud-lakehouse.md)
