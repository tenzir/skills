---
title: "DuckDB integration"
description: "Read from and write to DuckDB database files with an embedded DuckDB engine."
canonical: https://tenzir.com/integrations/duckdb
source: https://tenzir.com/integrations/duckdb.md
section: "Integrations"
---

# DuckDB integration

> Read from and write to DuckDB database files with an embedded DuckDB engine.

This page shows you how to use DuckDB as an embedded analytical store for Tenzir pipelines: write security telemetry to DuckDB tables with [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md), and read tables, SQL query results, or files that DuckDB can parse back into Tenzir with [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md).

[DuckDB](https://duckdb.org) is an open-source analytical database that runs inside the application that uses it. Tenzir embeds DuckDB, so there is no server to deploy and no network protocol in between: a pipeline opens a database file directly, and the same file is later available to the `duckdb` CLI, Python, R, or any other DuckDB client for analysis.

## Choose an integration path

Use the path that matches the role DuckDB plays in your deployment:

| Goal                                         | DuckDB role                                            | Tenzir building blocks                                                                                                                                                                                            |
| -------------------------------------------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Keep a local, queryable copy of telemetry    | Destination database file on the node                  | [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md)                                                                                                                                           |
| Store OCSF events per class                  | One table per event class                              | [`ocsf_cast`](https://tenzir.com/docs/reference/operators/ocsf_cast.md), [`where`](https://tenzir.com/docs/reference/operators/where.md), [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md) |
| Query retained telemetry                     | Source table or SQL query result                       | [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md)                                                                                                                                       |
| Read Parquet, CSV, or JSON files through SQL | In-memory query engine over files                      | [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) with `":memory:"` and `sql=...`                                                                                                       |
| React to rows other pipelines write          | Shared database file within a node                     | [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) with `live=true`                                                                                                                      |
| Inspect available tables and schemas         | `information_schema` and `duckdb_*()` metadata queries | [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) with `sql=...`                                                                                                                        |

## Write events

Write a stream of events into a table. The operator creates the database file and the table from the first events it receives:

```tql
subscribe "alerts"
to_duckdb "/var/lib/tenzir/alerts.duckdb", table="alerts", primary=id
```

A DuckDB table has a fixed set of typed columns. Fields without a column are dropped and values that do not fit their column become `NULL`, each with a warning. To keep all data, shape heterogeneous streams before writing them, or write each event kind to its own table:

```tql
subscribe "ocsf"
ocsf_cast
where class_uid == 4001
to_duckdb "/var/lib/tenzir/ocsf.duckdb", table="network_activity"
```

Several pipelines can write to the same database file at the same time. Every batch of events is committed, and thereby durable, as soon as it is written. Checkpoints, whose frequency `checkpoint_interval` controls, periodically move the committed data from DuckDB’s write-ahead log into the database file.

## Read events

Read a whole table:

```tql
from_duckdb "/var/lib/tenzir/alerts.duckdb", table="alerts"
```

Or let DuckDB do the heavy lifting with SQL:

```tql
from_duckdb "/var/lib/tenzir/alerts.duckdb",
  sql="SELECT src_ip, count(*) AS n FROM alerts GROUP BY src_ip ORDER BY n DESC LIMIT 10"
```

An in-memory database needs no file and turns DuckDB’s readers into a Tenzir source:

```tql
from_duckdb ":memory:", sql="SELECT * FROM 'flows/*.parquet' WHERE bytes > 1000000"
```

## Stream new rows

With `live=true`, [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) keeps running and emits rows that other pipelines in the same node append, tracked through an increasing integer column:

```tql
from_duckdb "/var/lib/tenzir/alerts.duckdb", table="alerts", live=true
publish "new-alerts"
```

## Understand file access

DuckDB opens a database file either for reading or for writing, and a file that one process has open for writing is locked for every other process. Within a Tenzir node:

* Any number of [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md) operators share one file, and appends never conflict.
* [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) reads a file that writers have open by sharing their database. Started first, it opens the file read-only, and writers for that file cannot start until it finishes.
* [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) with `live=true` always opens the file for writing, so that writers can join it and it sees their appends.

To analyze a file with the `duckdb` CLI, stop the pipelines that write to it first; they checkpoint when they end, so the file then holds all data. Do not copy a file while pipelines write to it: recent rows may still live in the separate write-ahead log, and the copy can race a checkpoint. To look at the data while writers run, query it with [`from_duckdb`](https://tenzir.com/docs/reference/operators/from_duckdb.md) inside the node, which shares the writers’ database.

## See Also

* [Read from data stores](../guides/collect/read-from-data-stores.md)
* [Send to destinations](../guides/route/send-to-destinations.md)
