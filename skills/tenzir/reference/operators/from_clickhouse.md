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

Use this mode when you want to read a whole table and preserve named tuple fields from the table schema.

Note

ClickHouse omits `ALIAS` and `MATERIALIZED` columns from `SELECT *`. The `table` option therefore does not include such columns. To read them, use `sql` with an explicit column list.

Use exactly one of `table` or `sql`.

### `sql = string`

A custom SQL query to execute.

Use this mode when you want ClickHouse to filter, project, sort, or cast data before Tenzir reads it.

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
  require_client_cert,          // require clients to present a certificate.
}
```

The `client_ca` and `require_client_cert` options are only applied for operators that accept incoming client connections, and otherwise ignored.

Any value not specified in the record will either be picked up from the configuration or if not configured will not be used by the operator.

See the [Node TLS Setup guide](../../guides/node-setup/configure-tls.md) for more details.

## Types

Tenzir maps ClickHouse types to Tenzir types as follows:

| ClickHouse                                        | Tenzir    | Comment                                        |
| ------------------------------------------------- | --------- | ---------------------------------------------- |
| `Bool`                                            | `bool`    |                                                |
| `Int8`, `Int16`, `Int32`, `Int64`                 | `int64`   |                                                |
| `UInt8`, `UInt16`, `UInt32`, `UInt64`             | `uint64`  |                                                |
| `Float32`, `Float64`                              | `double`  |                                                |
| `String`, `FixedString(N)`                        | `string`  |                                                |
| `UUID`                                            | `string`  | Emitted as canonical UUID text.                |
| `Enum8`, `Enum16`                                 | `string`  | Emitted as the enum label.                     |
| `Decimal`, `Decimal32`, `Decimal64`, `Decimal128` | `string`  | Emitted as decimal text to preserve precision. |
| `Date`, `Date32`, `DateTime`, `DateTime64`        | `time`    |                                                |
| `IPv4`, `IPv6`                                    | `ip`      |                                                |
| `Tuple(...)`                                      | `record`  |                                                |
| `Array(T)`                                        | `list<T>` |                                                |
| `Array(UInt8)`                                    | `blob`    |                                                |
| `Nullable(T)`                                     | `T`       | Null values stay null.                         |

`Map(...)` is not currently supported. Cast unsupported columns in `sql` or omit them from the query result.

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

### Run a filtered SQL query

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
* [Read from data stores](../../guides/collecting/read-from-data-stores.md)
* [ClickHouse](../../integrations/clickhouse.md)
* [nano](../../integrations/nano.md)
