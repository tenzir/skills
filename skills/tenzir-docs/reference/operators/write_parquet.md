# write_parquet


Transforms event stream to a Parquet byte stream.

```tql
write_parquet [compression_level=int, compression_type=str]
```

## Description

[Apache Parquet](https://parquet.apache.org/) is a columnar storage format that a variety of data tools support.

### `compression_level = int (optional)`

An optional compression level for the corresponding compression type. This option is ignored if no compression type is specified.

Defaults to the compression type’s default compression level.

### `compression_type = str (optional)`

Specifies an optional compression type. Supported options are `zstd` for [Zstandard](http://facebook.github.io/zstd/) compression, `brotli` for [brotli](https://www.brotli.org) compression, `gzip` for [gzip](https://www.gzip.org) compression, and `snappy` for [snappy](https://google.github.io/snappy/) compression.

Why would I use this over the `compress` operator?

The Parquet format offers more efficient compression compared to the [`compress`](compress.md) operator. This is because it compresses the data column-by-column, leaving metadata that needs to be accessed frequently uncompressed.

## Examples

Write a Parquet file:

```tql
load_file "/tmp/data.json"
read_json
write_parquet
```

## See Also

* [`read_bitz`](read_bitz.md)
* [`read_parquet`](read_parquet.md)
* [`to_hive`](to_hive.md)
* [`write_bitz`](write_bitz.md)
* [`write_feather`](write_feather.md)