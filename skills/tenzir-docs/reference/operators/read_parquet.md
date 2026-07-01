# read_parquet


Reads events from a Parquet byte stream.

```tql
read_parquet
```

## Description

Reads events from a [Parquet](https://parquet.apache.org/) byte stream.

[Apache Parquet](https://parquet.apache.org/) is a columnar storage format that a variety of data tools support.

MMAP Parsing

When using theis with the [`from_file`](http://docs.tenzir.com/reference/operators/from_file.md) operator, we recommend passing the `mmap=true` option to `from_file` to give the parser full control over the reads, which leads to better performance and memory usage.

Limitation

Tenzir currently assumes that all Parquet files use metadata recognized by Tenzir. We plan to lift this restriction in the future.

## Examples

Read a Parquet file:

```tql
from_file "/tmp/data.prq", mmap=true {
  read_parquet
}
```

## See Also

* [`read_feather`](http://docs.tenzir.com/reference/operators/read_feather.md)
* [`write_parquet`](http://docs.tenzir.com/reference/operators/write_parquet.md)