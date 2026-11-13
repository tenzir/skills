---
title: "from_hydrolix"
canonical: https://tenzir.com/docs/v7.0.0/reference/operators/from_hydrolix
source: https://tenzir.com/docs/v7.0.0/reference/operators/from_hydrolix.md
section: "Docs"
---

# from_hydrolix

> Reads events from a Hydrolix table or SQL query.

Reads events from a [Hydrolix](https://hydrolix.io) table or SQL query.

```tql
from_hydrolix url:string, token=string, [table=string, sql=string, port=int,
              tls=bool|record, pushdown=bool]
```

## Description

The `from_hydrolix` operator queries a Hydrolix cluster with SQL. Hydrolix stores events in time-partitioned tables in object storage, and its query engine runs the query. The operator currently connects to the [native interface](https://docs.hydrolix.io/latest/exploring-data/query-interfaces/clickhouse/) of the query engine, receives typed columns, maps them to Tenzir types, and lets Hydrolix do the work of the operators that follow it.

You can either read a `table` or run an `sql` query.

Hydrolix partitions every table by its primary timestamp. Always restrict queries to a time range on that column, so that Hydrolix reads only the partitions you need. In `table` mode, a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) after `from_hydrolix` becomes part of the query if it compares the column with a constant. Because `now()` returns a different value on every call, bind the start of the range with `let`, which evaluates it once:

```tql
let $since = now() - 1h
from_hydrolix "https://acme.hydrolix.live",
  token=secret("hydrolix-token"),
  table="security.events"
where time > $since
```

With `where time > now() - 1h` instead, Tenzir filters the events after Hydrolix returned the entire table.

Production clusters almost always enforce such a time range, with the `hdx_query_timerange_required` and `hdx_query_max_timerange_sec` query options. Queries without a fitting time range then fail, and the operator suggests how to add one.

### `url: string`

The URL of the Hydrolix cluster, for example `https://acme.hydrolix.live`. This is the same URL that you pass to [`to_hydrolix`](https://tenzir.com/docs/v7.0.0/reference/operators/to_hydrolix.md).

The operator connects to the host of the URL. The scheme decides whether the connection uses TLS: `https://` enables it and `http://` disables it, whatever the TLS defaults of the node say. Without a scheme, the `tls` argument and the node configuration decide. Other schemes are an error. The operator ignores the port, path, and query of the URL, because the native interface listens on a port of its own.

### `token = string`

The bearer token for authentication, typically a [service account token](https://docs.hydrolix.io/latest/self-managed/advanced-configuration/authentication-and-authorization/account-types/service-accounts-howto/). The operator authenticates as the special `__api_token__` user, which makes Hydrolix accept the token as password.

The account of the token needs the `select_sql` permission on the tables that you read. In `table` mode, reading the schema requires the `SHOW COLUMNS` grant, controlled by `show_columns_sql`. The `select_sql` permission implicitly grants `show_columns_sql`, so no additional permission is needed for schema access. A missing `SHOW COLUMNS` grant points to `show_columns_sql` or `select_sql`; a missing `SELECT` grant points to `select_sql`, as described in [Hydrolix’s RBAC concepts](https://docs.hydrolix.io/latest/self-managed/advanced-configuration/authentication-and-authorization/account-permissions/rbac-concepts/).

Hydrolix hides tables that an account can’t query, so a missing permission can also surface as an unknown table. The same happens for a table without a transform, because Hydrolix derives the columns of a table from its transforms.

Diagnostics don’t show the token, even if Hydrolix repeats it in an error.

### `table = string (optional)`

The table to read from, in the form `project.table`.

Use this mode to read a table as structured events. Hydrolix takes over the operators that follow, such as [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md), [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md); see [Optimizations](from_hydrolix.md#optimizations).

Use exactly one of `table` or `sql`.

### `sql = string (optional)`

A SQL query to execute.

Use this mode when you need SQL features that `table` mode doesn’t express, such as joins or [Hydrolix query options](https://docs.hydrolix.io/latest/exploring-data/query-interfaces/query-options-1/query-options-reference/) in a `SETTINGS` clause. Tenzir sends the query as is and doesn’t rewrite it, so include the time range on the primary timestamp yourself.

Use exactly one of `table` or `sql`.

### `port = int (optional)`

The port of the native interface of the query engine.

Defaults to `9440` with TLS and `9000` without TLS, the defaults of Hydrolix.

### `tls = record (optional)`

TLS configuration. Provide an empty record (`tls={}`) to enable TLS with defaults or set fields to customize it.

```tql
{
  skip_peer_verification: bool, // skip certificate verification.
  cacert: string,               // CA bundle to verify peers.
  certfile: string,             // client certificate to present.
  keyfile: string,              // private key for the client certificate.
  min_version: string,          // minimum TLS version (`"1.0"`, `"1.1"`, `"1.2"`, "1.3"`).
  ciphers: string,              // OpenSSL cipher list string.
  client_ca: string,            // CA to validate client certificates.
  require_client_cert: bool,    // require clients to present a certificate.
}
```

The `client_ca` and `require_client_cert` options are only valid for operators that accept incoming client connections.

Any value not specified in the record will either be picked up from the configuration or if not configured will not be used by the operator.

See the [Node TLS Setup guide](../../guides/node-setup/configure-tls.md) for more details.

### `pushdown = bool (optional)`

Whether Hydrolix takes over the operators that follow the operator in `table` mode. With `pushdown=false`, they stay in the pipeline and run with TQL semantics. No filter then reaches the query, so on a cluster that requires a time range, use `sql` with a query that sets one instead. See [Optimizations](from_hydrolix.md#optimizations).

Defaults to `true`.

## Types

The operator maps the column types of the query engine to Tenzir types as follows:

| Query engine                                      | Tenzir      | Comment                                                |
| ------------------------------------------------- | ----------- | ------------------------------------------------------ |
| `Bool`                                            | `bool`      |                                                        |
| `Int8`, `Int16`, `Int32`, `Int64`                 | `int64`     |                                                        |
| `UInt8`, `UInt16`, `UInt32`, `UInt64`             | `uint64`    |                                                        |
| `Int128`, `UInt128`                               | `string`    | Emitted as integer text to preserve precision.         |
| `Float32`, `Float64`                              | `double`    |                                                        |
| `String`, `FixedString(N)`                        | `string`    |                                                        |
| `JSON`                                            | `string`    | Emitted as one-line JSON text.                         |
| `UUID`                                            | `string`    | Emitted as canonical UUID text.                        |
| `Enum8`, `Enum16`                                 | `string`    | Emitted as the enum label.                             |
| `Decimal`, `Decimal32`, `Decimal64`, `Decimal128` | `string`    | Emitted as decimal text to preserve precision.         |
| `Date`, `Date32`, `DateTime`, `DateTime64`        | `time`      |                                                        |
| `Time`, `Time64`                                  | `duration`  |                                                        |
| `IPv4`, `IPv6`                                    | `ip`        |                                                        |
| `Tuple(...)`                                      | `record`    |                                                        |
| `Array(T)`                                        | `list<T>`   |                                                        |
| `Array(UInt8)`                                    | `blob`      |                                                        |
| `Map(K, V)`                                       | `record`    | One field per key.                                     |
| `Nullable(T)`                                     | `T`         | Null values stay null.                                 |
| `LowCardinality(T)`                               | Same as `T` | Dictionary encoding doesn’t change the resulting type. |

Times outside Tenzir’s range, which spans the years 1677 to 2262, become null with a warning. The operator drops columns of other types, such as geo types, with a warning. Cast them in `sql` or omit them from the query result.

Events from `table` mode have the schema name `hydrolix.<project>.<table>`, and events from `sql` mode have the schema name `hydrolix.query`.

Transforms often store fields without a column of their own in a catch-all column of type `Map(String, Nullable(String))`. It becomes a record with string values, so a field arrives as `catchall.class_uid` with the value `"4001"` rather than the number `4001`. Rows may lack a key, so access these fields with `?`, and convert the values with functions such as `int()` where needed:

```tql
let $since = now() - 1h
from_hydrolix "https://acme.hydrolix.live",
  token=secret("hydrolix-token"),
  table="security.events"
where time > $since and catchall.class_uid? == "4001"
class_uid = catchall.class_uid.int()
```

## Optimizations

When the operator reads a table, it hands Hydrolix the operators that follow it, as far as Hydrolix’s ClickHouse engine can spell them: [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md), [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md) with `count`, `min`, and `max`, including [`top`](https://tenzir.com/docs/v7.0.0/reference/operators/top.md) and [`rare`](https://tenzir.com/docs/v7.0.0/reference/operators/rare.md), [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md), and [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md), also after a [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md). Those operators leave the pipeline and run with Hydrolix’s semantics, which can differ from TQL. For example, a comparison with `NULL` yields `NULL`, so `s != "a"` does not keep rows where `s` is `null`, and a division by zero yields `null`. A query that Hydrolix rejects fails the pipeline with a hint to use `pushdown=false`. The [ClickHouse optimizations](../optimizations/clickhouse.md) page describes the rules, which `from_hydrolix` shares with [`from_clickhouse`](https://tenzir.com/docs/v7.0.0/reference/operators/from_clickhouse.md).

Hydrolix reads only the partitions within the time range that a query sets on the table’s primary timestamp, and a cluster may reject a query without one. Put a [`where`](https://tenzir.com/docs/v7.0.0/reference/operators/where.md) on the primary timestamp directly after the operator, with a constant bound such as a `let` that evaluates `now()` once. Tenzir moves such a filter ahead of [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md), [`drop`](https://tenzir.com/docs/v7.0.0/reference/operators/drop.md), and [`sort`](https://tenzir.com/docs/v7.0.0/reference/operators/sort.md), so that it constrains the table itself. After a [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md) or a [`summarize`](https://tenzir.com/docs/v7.0.0/reference/operators/summarize.md), the filter reads their result and no longer restricts the time range.

Fields of a `Map` column, such as the `catchall` map of Hydrolix’s default transform, read as `catchall['key']`. A missing key yields the default of the map’s value type: `null` for `Nullable` values, as in the `catchall` map, and `""` or `0` otherwise. Hydrolix may reject a query that reads a field below a `JSON` column in a subquery, for example for a [`select`](https://tenzir.com/docs/v7.0.0/reference/operators/select.md) or the operators after a [`head`](https://tenzir.com/docs/v7.0.0/reference/operators/head.md). Use `pushdown=false` then, or write the query yourself with `sql`, including the `SETTINGS` that your cluster needs.

## Examples

### Read the last hour of a table

```tql
let $since = now() - 1h
from_hydrolix "https://acme.hydrolix.live",
  token=secret("hydrolix-token"),
  table="security.events"
where time > $since
```

### Filter, select, and count on the server

```tql
let $since = now() - 1d
from_hydrolix "https://acme.hydrolix.live",
  token=secret("hydrolix-token"),
  table="security.events"
where time > $since and severity_id >= 4
summarize class_uid, events=count()
```

Hydrolix filters the rows and computes the counts, so Tenzir receives one event per class.

### Run a custom SQL query

```tql
from_hydrolix "https://acme.hydrolix.live",
  token=secret("hydrolix-token"),
  sql="SELECT src_ip, count() AS events FROM security.events WHERE time > now() - INTERVAL 1 DAY GROUP BY src_ip ORDER BY events DESC LIMIT 10"
```

### List the tables of a project

```tql
from_hydrolix "https://acme.hydrolix.live",
  token=secret("hydrolix-token"),
  sql="SHOW TABLES FROM security"
```

## See Also

* [`to_hydrolix`](https://tenzir.com/docs/v7.0.0/reference/operators/to_hydrolix.md)
* [Hydrolix](https://docs.tenzir.com/integrations/hydrolix)
