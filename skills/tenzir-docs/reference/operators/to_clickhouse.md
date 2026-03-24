# to_clickhouse


Sends events to a ClickHouse table.

```tql
to_clickhouse table=string, [host=string, port=int, user=string, password=string,
                             mode=string, primary=field, database=string,
                             tls=record]
```

## Description

### `table = string`

The name of the table you want to write to.

This can be a dynamic expression, allowing you to automatically write to different tables based on the data.

The `<database>.<table>` notation can be used to also specify a table. If no `<database>`, is provided, `"default"` will be used.

### `host = string (optional)`

The hostname for the ClickHouse server.

Defaults to `"localhost"`.

### `port = int (optional)`

The port for the ClickHouse server.

Defaults to `9000` without TLS and `9440` with TLS.

### `user = string (optional)`

The user to use for authentication.

Defaults to `"default"`.

### `password = string (optional)`

The password for the given user.

Defaults to `""`.

### `mode = string (optional)`

* `"create"` Create a table and database. Fails the table already exists.
* `"append"` Appends to an existing table. Fails if the table or database do not exist.
* `"create_append"` Creates a table and database if they do not exist. Appends if the table already exists.

Defaults to `"create_append"`.

### `primary = field (optional)`

The primary key to use when creating a table. Required for `mode = "create"` as well as for `mode = "create_append"` if the table does not yet exist.

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

Path to the key for the client certificate.

## Types

Tenzir uses ClickHouse’s [clickhouse-cpp](https://github.com/ClickHouse/clickhouse-cpp) client library to communicate with ClickHouse. The below table explains the translation from Tenzir’s types to ClickHouse:

| Tenzir     | ClickHouse                     | Comment                                                                                           |
| :--------- | :----------------------------- | :------------------------------------------------------------------------------------------------ |
| `bool`     | `UInt8`                        |                                                                                                   |
| `int64`    | `Int64`                        |                                                                                                   |
| `uint64`   | `UInt64`                       |                                                                                                   |
| `double`   | `Float64`                      |                                                                                                   |
| `ip`       | `IPv6`                         |                                                                                                   |
| `subnet`   | `Tuple(ip IPv6, length UInt8)` |                                                                                                   |
| `time`     | `DateTime64(9)`                |                                                                                                   |
| `duration` | `Int64`                        | Converted as `nanoseconds(duration)`                                                              |
| `record`   | `Tuple(...)`                   | Fields in the tuple will be named with the field name. The record must have at least one element. |
| `list<T>`  | `Array(T)`                     |                                                                                                   |
| `blob`     | `Array(UInt8)`                 | Blobs that are `null` will be represented by an empty array                                       |

Tenzir also supports `Nullable` versions of the above types (or their nested types). If a `list` itself is `null`, it will be represented by an empty `Array`. If a `record` is `null`, all elements of the `Tuple` will be null, if possible. Otherwise the event will be dropped.

### Table Creation

When a ClickHouse table is created from Tenzir, all columns except the `primary` will be created as `Nullable`. For example, a column of type `ip` will be created as `Nullable(IPv6)`, while a `list<int64>` will be created as `Array(Nullable(Int64))`.

The table will be created from the first event the operator receives. Should this first event contain unsupported types/values, an error is raised.

#### Untyped nulls

Tenzir has both typed and untyped nulls. Typed nulls have a type, but no value. They are no problem for `to_clickhouse`.

For untyped nulls, the type itself is `null`, which cannot be supported by the `to_clickhouse` operator when creating a table.

Typed and Untyped Nulls in Tenzir

```tql
from {
  typed_null: int(null),
  untyped_null: null,
}
```

Untyped nulls are usually directly caused by nulls in the input, such as in a JSON file:

```json
{
  "value": null
}
```

If your input format has untyped nulls, but you know the type, you can either define an a schema and use that when parsing the input, or you can explicitly cast the columns to their desired type:

```tql
from (
  { value: null },
  { value: 42 },
)
value = int(value) // explicit cast turns untyped into typed nulls
to_clickhouse "example_table", primary=value
```

#### Empty records

Empty records cannot be send to ClickHouse. Should an empty record appear in the first event, an error is raised.

## Examples

### Send CSV file to a local ClickHouse instance, without TLS

```tql
from "my_file.csv"
to_clickhouse table="my_table", tls=false
```

### Send OCSF data to ClickHouse

When sending OCSF data to ClickHouse, it is important to ensure that a consistent schema is sent. For this, we can use [`ocsf::cast`](/reference/operators/ocsf/cast.md). This allows us to encode the `unmapped` field as JSON and fill any missing fields with `null`, ensuring a single schema.

```tql
subscribe "ocsf"
ocsf::cast encode_variants=true, null_fill=true
to_clickhouse table=f"ocsf.{class_name.replace(" ","_")}", primary=time
```

### Create a new table with multiple fields

```tql
from { i: 42, d: 10.0, b: true, l: [42], r:{ s:"string" } }
to_clickhouse table="example", primary=i
```

This creates the following table:

```plaintext
   ┌─name─┬─type────────────────────┐
1. │ i    │ Int64                   │
2. │ d    │ Nullable(Float64)       │
3. │ b    │ Nullable(UInt8)         │
4. │ l    │ Array(Nullable(Int64))  │
5. │ r    │ Tuple(                 ↴│
   │      │↳    s Nullable(String)) │
   └──────┴─────────────────────────┘
```

## See Also

* [`ocsf::cast`](/reference/operators/ocsf/cast.md)
* [ClickHouse](../../integrations/clickhouse.md)