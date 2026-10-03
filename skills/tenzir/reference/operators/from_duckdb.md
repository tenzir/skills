---
title: "from_duckdb"
canonical: https://tenzir.com/docs/reference/operators/from_duckdb
source: https://tenzir.com/docs/reference/operators/from_duckdb.md
section: "Docs"
---

# from_duckdb

> Reads events from a DuckDB database.

Reads events from a DuckDB database.

```tql
from_duckdb uri:string, [token=secret], [tls=bool|record],
            [table=string], [sql=string], [live=bool], [tracking_column=string]
```

## Description

The `from_duckdb` operator reads data from a [DuckDB](https://duckdb.org) database. Use a local file, an in-memory database, or a remote DuckDB server over Quack. Local databases run embedded inside Tenzir.

Our [DuckDB integration](../../integrations/duckdb.md#extensions) describes the bundled extensions available to local queries.

The operator supports two query modes:

1. **Table mode**: Read all rows from a table using the `table` parameter.
2. **SQL mode**: Execute a custom SQL query using the `sql` parameter.

Use exactly one of `table` or `sql`.

Requires Nova

This operator requires the Nova execution engine. Start `tenzir` or `tenzir-node` with `--nova` to use it.

### `uri: string`

A local database path, an in-memory database name, or a Quack URI.

For a file path, the operator opens the file read-only, unless `live=true` is set. It never creates a missing file.

Use `":memory:"` for a private in-memory database that starts out empty. In combination with `sql`, this turns DuckDB’s file readers into a Tenzir source: anything DuckDB can query, including Parquet, CSV, JSON, and XLSX files, becomes a stream of events.

Use a named in-memory database, such as `":memory:alerts"`, to share data between pipelines in the same node. Pipelines using different names remain isolated. Named databases exist only while at least one operator holds them open. Once the last operator releases the database, its data disappears; reopening the same name creates an empty database. Separate nodes or CLI processes never share named in-memory databases.

Use `"quack:host[:port]"` to connect to a remote DuckDB server over [Quack](https://duckdb.org/docs/current/quack/overview). The alternative `"quack://host[:port]"` spelling is also accepted. The default port is `9494`; set the port explicitly for a TLS reverse proxy, such as `"quack:analytics.example.com:443"`. Set `token` for authentication and keep the table name in `table`, not in the URI.

### `token = secret (optional)`

The Quack server’s authentication token. Required for a `quack:` database and not accepted for local databases. Use `secret("duckdb-token")` to resolve it through Tenzir’s secret store. Do not put credentials in the URI.

### `tls = bool | record (optional)`

Controls TLS for Quack connections. Defaults to `false` for `localhost`, `127.0.0.1`, and `[::1]`, and `true` for other hosts. A record enables TLS and accepts `cacert` for a custom CA certificate file and `skip_peer_verification` to disable certificate verification. Verification is enabled by default. Node-wide TLS defaults apply.

The Quack client does not support client certificates, a minimum TLS version, or custom cipher lists. Unsupported TLS settings produce an error rather than being ignored. This option is not accepted for local databases.

### `table = string (optional)`

The name of the table to read from. Qualify the name with a schema as `schema.table`, or with a catalog and schema as `catalog.schema.table`, and double-quote components that contain special characters, such as `"my schema"."my table"`.

The resulting events carry the schema name `duckdb.<table>`.

### `sql = string (optional)`

A custom SQL query to execute. Tenzir sends the query as is and does not rewrite it, except for casting columns of types that TQL cannot represent (see [Types](from_duckdb.md#types)). The query must be a single statement; a trailing `;` is fine. Statements that modify the database, such as `INSERT`, `DELETE`, or `CREATE TABLE`, fail, including for named in-memory databases shared with other pipelines.

Use this mode for SQL features that `table` mode does not express, such as sorting, joins, aggregations, or reading files. For metadata queries, use SQL against DuckDB’s `information_schema` or `duckdb_*()` table functions.

For Quack databases, the query runs on the server: file paths, functions, macros, and metadata refer to the server, not to the Tenzir host. Remote queries must be a single `SELECT`, `SHOW`, or `DESCRIBE` statement. Other statements, including `EXPLAIN`, are not supported remotely.

The resulting events carry the schema name `duckdb.query`.

### `live = bool (optional)`

Enables continuous polling for new rows. The operator first emits every row in the table, then polls once per second for rows whose tracking column exceeds the largest value seen so far, and emits them in tracking order. The operator never finishes on its own.

Live mode assumes that rows commit in tracking order. A row that commits after a row with a larger tracking value was already emitted is skipped, for example when two writers pick keys concurrently and the larger one commits first.

For local databases, live mode opens the database for writing so that it can share the database with [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md) operators in the same node and see what they append. For Quack databases, it polls the server. See [Concurrency](from_duckdb.md#concurrency) for the local-file restrictions.

Requires `table`. Defaults to `false`.

### `tracking_column = string (optional)`

The integer column whose growth marks new rows in live mode, including `HUGEINT`, `UHUGEINT`, and `BIGNUM` columns. Use a column that only ever increases, such as an auto-incrementing key or a sequence number.

When omitted, the operator uses the table’s single-column integer primary key, and fails if there is none. Other integer columns need not increase, so the operator never picks them on its own.

The column name is case-insensitive, like all identifiers in DuckDB.

Requires `live=true`.

## Types

The operator maps DuckDB types to [Type System](../types.md) as follows:

| DuckDB Type                                                | Tenzir Type | Notes                               |
| ---------------------------------------------------------- | ----------- | ----------------------------------- |
| `BOOLEAN`                                                  | `bool`      |                                     |
| `TINYINT`, `SMALLINT`, `INTEGER`, `BIGINT`                 | `int64`     |                                     |
| `UTINYINT`, `USMALLINT`, `UINTEGER`, `UBIGINT`             | `uint64`    |                                     |
| `FLOAT`, `DOUBLE`                                          | `double`    |                                     |
| `VARCHAR`                                                  | `string`    |                                     |
| `BLOB`                                                     | `blob`      |                                     |
| `TIMESTAMP`, `TIMESTAMP_S`, `TIMESTAMP_MS`, `TIMESTAMP_NS` | `time`      |                                     |
| `TIMESTAMP WITH TIME ZONE`                                 | `time`      |                                     |
| `DATE`                                                     | `time`      | Midnight of that day                |
| `INTERVAL`                                                 | `duration`  | Intervals with months become `null` |
| `LIST`, `ARRAY`                                            | `list`      |                                     |
| `STRUCT`                                                   | `record`    |                                     |
| `MAP`                                                      | `list`      | A list of `{key, value}` records    |
| `NULL`                                                     | `null`      |                                     |
| Everything else                                            | `string`    | Cast by DuckDB, see below           |

DuckDB types without a TQL counterpart, such as `DECIMAL`, `HUGEINT`, `UUID`, `TIME`, `ENUM`, `BIT`, and `UNION`, arrive as strings in DuckDB’s own textual representation. This also applies to such types nested inside lists and structs. The operator emits a warning for every affected column.

A `time` covers the years 1678 to 2261 with nanosecond precision. Timestamps and dates outside that range, `infinity` and `-infinity`, and intervals with a month component, whose length depends on the calendar, become `null`. The operator emits a warning for every affected column.

## Optimizations

In `table` mode, the operator acts on the hints that the [optimizer](../../explanations/pipeline.md#optimization) pushes toward it by translating the operators that follow it into the `SELECT` it sends, so that DuckDB reads and returns only what the pipeline needs:

* [`where`](https://tenzir.com/docs/reference/operators/where.md) becomes a `WHERE` clause.
* [`select`](https://tenzir.com/docs/reference/operators/select.md) narrows the selected columns to the top-level columns that the pipeline reads, including those that only a filter running in Tenzir needs. Fields that do not exist in the table are left to `select`, which fills them with `null`.
* [`head`](https://tenzir.com/docs/reference/operators/head.md) adds a `LIMIT`.

For example, the pipeline

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3 and rule.starts_with("ET ")
select id, message
head 100
```

sends a query equivalent to

```sql
SELECT "id", "message", "severity", "rule"
FROM "alerts"
WHERE "severity" >= 3 AND starts_with("rule", 'ET ')
LIMIT 100
```

The result is the same whether or not a part of the pipeline runs in DuckDB. To keep it that way, the operator only translates predicates whose DuckDB semantics match TQL exactly:

* Comparisons of a column with a literal of matching kind: numbers against integer, `FLOAT`, and `DOUBLE` columns, strings against `VARCHAR` columns, and `time` values against `DATE`, `TIMESTAMP`, `TIMESTAMP_S`, `TIMESTAMP_MS`, `TIMESTAMP_NS`, and `TIMESTAMP WITH TIME ZONE` columns. Booleans compare for equality only.
* Null checks with `== null` and `!= null`.
* Membership tests with `in` and a list of such literals.
* Comparisons between two columns of the same kind. Temporal columns must share their exact type.
* Fields of `STRUCT` columns, such as `meta.level`, with the same rules as columns.
* The string functions `starts_with`, `ends_with`, and `length_bytes`, and substring search with `"needle" in haystack`. With `ignore_case=true`, `starts_with` and `ends_with` translate approximately, and so does `match_regex`, as [Approximate matching](from_duckdb.md#approximate-matching) explains.
* Arithmetic that cannot overflow: `+`, `-`, and `*` on integer columns of at most 32 bits with a literal whose magnitude is below 2^31, and any `+`, `-`, `*`, or `/` that yields a floating-point number, except division by zero.
* Expressions that consist of literals only, such as `2024-01-01 + 1d`, which are computed ahead of time.
* The boolean operators `and`, `or`, and `not`.
* Bare boolean columns.

Where DuckDB’s own semantics differ from TQL, the query spells out TQL’s:

* DuckDB considers `NaN` equal to itself and greater than every other number. A comparison of a floating-point value carries a guard that makes `NaN` compare as in TQL: `x > 1.5` becomes `x > 1.5e0 AND NOT isnan(x)`. Numbers are spelled as `DOUBLE` literals, so that DuckDB widens a `FLOAT` column to `DOUBLE` like TQL does, instead of comparing in single precision.
* DuckDB computes arithmetic in the types of its operands, so that it can overflow or lose precision where TQL does not. The query widens the column first: `n + 1 > 5` becomes `CAST(n AS BIGINT) + 1 > 5`, and `n * 0.5 > 5` computes in `DOUBLE`.
* DuckDB reads `meta.level` as the column `level` of a table `meta` if there is one. A field therefore goes into the query as `struct_extract(meta, 'level')`.
* A `VARCHAR` column with a collation, such as `COLLATE NOCASE`, compares text without regard to case, and so does every `VARCHAR` column when the database sets a `default_collation`. Such a column goes into the query with the binary collation, which compares bytes like TQL: `name == "a"` becomes `name COLLATE "binary" = 'a'`. DuckDB still skips row groups by their minimum and maximum values for such a comparison.

Literals take the column’s own type, so a comparison never depends on the session time zone. Values that Tenzir cannot represent, such as `infinity` or a `DATE` past the year 2262, compare as `null` in both places. An `ip` literal that is compared for equality with a `VARCHAR` column, or listed in an `in` test against one, becomes its canonical text, as with the [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md) operator. The predicate `src == 1.1.1.1` then matches rows whose `src` reads `1.1.1.1`.

Everything else runs in Tenzir with unchanged results. This includes:

* Columns that arrive as strings, such as `DECIMAL`, `UUID`, `ENUM`, and `UNION` columns (see [Types](from_duckdb.md#types)), and `BLOB`, `INTERVAL`, `LIST`, `ARRAY`, and `MAP` columns, including the values nested in them.
* Arithmetic on 64-bit integer columns or between two columns.
* Subnet membership tests on `VARCHAR` columns, such as `src in 10.0.0.0/8`.
* Strings that contain NUL bytes, and all other functions.

A predicate that mixes translatable and untranslatable parts is split along its `and`s: each conjunct that translates goes into the query, and the others run in Tenzir. An `or` or `not` is pushed only when all of its operands translate. When a predicate that precedes the `head` stays in Tenzir, the limit is enforced in Tenzir as well and the query has no `LIMIT`, since DuckDB cannot count rows that Tenzir has yet to filter.

In live mode, every polling query carries the `WHERE` clause and the narrowed columns, but never a `LIMIT`, since the limit counts events across polls.

A user-provided `sql` query is never rewritten. Tenzir applies the pipeline’s operators to its result.

### Approximate matching

Two kinds of predicates translate approximately. This is a deliberate exception to identical results, made so that common filters reach the database.

A predicate such as `msg.starts_with("error", ignore_case=true)` goes into the query as `starts_with(lower(msg), lower('error'))`. DuckDB lowercases one character at a time, which agrees with TQL for ASCII and most other text. TQL applies full Unicode case folding instead, which differs for a few characters: it folds `ß` to `ss`, so `"Straße".starts_with("strass", ignore_case=true)` is `true` in TQL but matches no row in DuckDB.

A predicate such as `msg.match_regex("^ERROR [0-9]+")` goes into the query as `regexp_matches(msg, '^ERROR [0-9]+')`. Both TQL and DuckDB use the RE2 library with the same options: the pattern matches anywhere in the string, `.` does not match a newline, and `^` and `$` match only at the start and end of the string. DuckDB bundles its own release of RE2, which may disagree with TQL’s on rarely used syntax.

## Remote databases

Each operator keeps its credentials and TLS settings isolated from other operators. Local-file locking rules do not apply to remote connections.

Quack is a beta protocol. Our [DuckDB integration](../../integrations/duckdb.md#quack) describes the tested client and server versions.

## Concurrency

DuckDB enforces one rule for database files: a process opens a file either for reading or for writing. Within a Tenzir node, this has two consequences:

* `from_duckdb` without `live` opens the file read-only, unless another pipeline already has it open for writing, in which case it shares that database and still only reads. While it reads, a [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md) or a live `from_duckdb` on the same file cannot start.
* `from_duckdb` with `live=true` opens the file for writing. It shares the database with every [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md) and every other reader of the same file and sees what the writers append.

Across processes, a file that any process has open for writing cannot be opened by another process at all. Read-only processes can share a file.

## Examples

### Read all rows from a table

```tql
from_duckdb "events.duckdb", table="alerts"
```

### Read from a remote server

```tql
from_duckdb "quack:analytics.example.com:443",
  token=secret("duckdb-token"), table="alerts"
```

To query a file on that server:

```tql
from_duckdb "quack:analytics.example.com:443",
  token=secret("duckdb-token"),
  sql="SELECT * FROM read_parquet('/data/alerts.parquet')"
```

### Read a table in a schema

```tql
from_duckdb "events.duckdb", table="staging.alerts"
```

### Run a custom SQL query

```tql
from_duckdb "events.duckdb",
  sql="SELECT src_ip, count(*) AS n FROM flows GROUP BY src_ip ORDER BY n DESC"
```

### Query Parquet files with DuckDB

```tql
from_duckdb ":memory:",
  sql="SELECT * FROM 'flows/*.parquet' WHERE bytes > 1000000"
```

### Read a shared in-memory table

Start a writing pipeline in the same node first and wait until it has created the table. Keep at least one pipeline using the named database running:

```tql
from_duckdb ":memory:alerts", table="alerts", live=true
```

### List the tables in a database

```tql
from_duckdb "events.duckdb",
  sql="SELECT table_schema, table_name FROM information_schema.tables"
```

### Read only the columns a pipeline uses

The `select` reaches the query, so DuckDB decodes only `id` and `message`:

```tql
from_duckdb "events.duckdb", table="alerts"
select id, message
```

### Filter rows in DuckDB

The `where` and `head` reach the query, so DuckDB returns at most 10 matching rows:

```tql
from_duckdb "events.duckdb", table="alerts"
where severity >= 3
head 10
```

### Stream new rows from a table

```tql
from_duckdb "events.duckdb", table="alerts", live=true
```

### Stream with an explicit tracking column

```tql
from_duckdb "events.duckdb", table="alerts", live=true, tracking_column="seq"
```

## See Also

* [Read from data stores](../../guides/collect/read-from-data-stores.md)
* [`to_duckdb`](https://tenzir.com/docs/reference/operators/to_duckdb.md)
* [`from_clickhouse`](https://tenzir.com/docs/reference/operators/from_clickhouse.md)
* [`from_mysql`](https://tenzir.com/docs/reference/operators/from_mysql.md)
* [DuckDB](../../integrations/duckdb.md)
