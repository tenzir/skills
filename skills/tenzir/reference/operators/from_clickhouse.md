---
title: "from_clickhouse"
canonical: https://tenzir.com/docs/reference/operators/from_clickhouse
source: https://tenzir.com/docs/reference/operators/from_clickhouse.md
section: "Docs"
---

# from_clickhouse

> Fetches data from a ClickHouse server.

Fetches data from a ClickHouse server.

```tql
from_clickhouse [table=string, sql=string,
                 uri=string, host=string, port=int, user=string, password=string,
                 tls=bool|record]
```

## Description

The [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md) operator issues a query to a ClickHouse server. You can either provide a `table` to read or an `sql` query.

### `uri = string (optional)`

A ClickHouse connection URI in the format:

```text
clickhouse://[user[:password]@]host[:port][/database]
```

When present, the URI supplies the connection endpoint and optionally the current database.

Use `tls` separately to control TLS.

Use either `uri` or the explicit connection arguments `host`, `port`, `user`, and `password`.

### `table = string`

The table to read from.

You can qualify the table as `<database>.<table>`. If you omit the database, ClickHouse uses the current database selected by the URI or server defaults.

Use this mode when you want to read a table and preserve named tuple fields from the table schema. Tenzir pushes filters, field selections, and limits from the rest of the pipeline into the query it sends; see [Optimizations](from_clickhouse.md#optimizations).

Note

By default, ClickHouse omits `ALIAS` and `MATERIALIZED` columns from `SELECT *`, so the `table` option does not include them. To read them, use `sql` with an explicit column list.

Use exactly one of `table` or `sql`.

### `sql = string`

A custom SQL query to execute.

Use this mode when you need SQL features that `table` mode does not express, such as sorting, joins, aggregations, or casts. Tenzir sends the query as is and does not rewrite it.

For metadata queries such as `SHOW TABLES`, `DESCRIBE TABLE`, or queries against `system.tables` and `system.columns`, use `sql`.

Use exactly one of `table` or `sql`.

### `host = string (optional)`

The hostname for the ClickHouse server.

Defaults to `"localhost"`.

Mutually exclusive with `uri`.

### `port = int (optional)`

The port for the ClickHouse server.

Defaults to `9000` without TLS and `9440` with TLS.

Mutually exclusive with `uri`.

### `user = string (optional)`

The user to use for authentication.

Defaults to `"default"`.

Mutually exclusive with `uri`.

### `password = string (optional)`

The password for the given user.

Defaults to `""`.

Mutually exclusive with `uri`.

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

## Types

Tenzir maps ClickHouse types to Tenzir types as follows:

| ClickHouse                                        | Tenzir      | Comment                                                 |
| ------------------------------------------------- | ----------- | ------------------------------------------------------- |
| `Bool`                                            | `bool`      |                                                         |
| `Int8`, `Int16`, `Int32`, `Int64`                 | `int64`     |                                                         |
| `UInt8`, `UInt16`, `UInt32`, `UInt64`             | `uint64`    |                                                         |
| `Int128`, `UInt128`                               | `string`    | Emitted as integer text to preserve precision.          |
| `Time`, `Time64`                                  | `duration`  |                                                         |
| `LowCardinality(T)`                               | Same as `T` | Dictionary encoding does not change the resulting type. |
| `Float32`, `Float64`                              | `double`    |                                                         |
| `String`, `FixedString(N)`                        | `string`    |                                                         |
| `JSON`                                            | `string`    | Emitted as one-line JSON text.                          |
| `UUID`                                            | `string`    | Emitted as canonical UUID text.                         |
| `Enum8`, `Enum16`                                 | `string`    | Emitted as the enum label.                              |
| `Decimal`, `Decimal32`, `Decimal64`, `Decimal128` | `string`    | Emitted as decimal text to preserve precision.          |
| `Date`, `Date32`, `DateTime`, `DateTime64`        | `time`      |                                                         |
| `IPv4`, `IPv6`                                    | `ip`        |                                                         |
| `Tuple(...)`                                      | `record`    |                                                         |
| `Array(T)`                                        | `list<T>`   |                                                         |
| `Array(UInt8)`                                    | `blob`      |                                                         |
| `Nullable(T)`                                     | `T`         | Null values stay null.                                  |

Date and timestamp values outside Tenzir’s nanosecond timestamp range become null with a warning.

When reading JSON written with `json_type_escape_dots_in_keys=1`, use `sql` with `SETTINGS json_type_escape_dots_in_keys=1` to restore literal dotted keys. Otherwise, ClickHouse returns escaped keys such as `"a%2Eb"`. This applies to JSON written to [tables with a catch-all](../../integrations/clickhouse.md#preserve-dotted-json-keys). The `table` form does not enable this setting automatically.

`Map(...)` is not currently supported. Cast unsupported columns in `sql` or omit them from the query result.

## Optimizations

When the operator reads a table, it lets ClickHouse do the work of the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators that follow it, so that ClickHouse returns only the rows and columns that the pipeline needs. The page on [ClickHouse optimizations](../optimizations/clickhouse.md) describes which filters ClickHouse evaluates, and the [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## Examples

### Read all rows from a table

```tql
from_clickhouse table="events", tls=false
```

### Use a connection URI

```tql
from_clickhouse uri="clickhouse://default:secret@clickhouse.example.com:9000/security",
                table="events",
                tls=false
```

### Filter and select on the server

```tql
from_clickhouse table="events", tls=false
where severity >= 3 and source == "fw"
select time, message
head 50
```

ClickHouse evaluates the filter, returns only `time`, `message`, `severity`, and `source`, and stops after 50 matching rows.

### Run a custom SQL query

```tql
from_clickhouse sql="SELECT * FROM events WHERE severity >= 3 ORDER BY time DESC",
                tls=false
```

### List tables in the current database

```tql
from_clickhouse sql="SHOW TABLES", tls=false
```

### Show the columns for a table

```tql
from_clickhouse sql="DESCRIBE TABLE events", tls=false
```

## See Also

* [`to_clickhouse`](https://tenzir.com/docs/reference/operators/to_clickhouse.md)
* [Read from data stores](../../guides/collect/read-from-data-stores.md)
* [ClickHouse](../../integrations/clickhouse.md)
* [nano](../../integrations/nano.md)
