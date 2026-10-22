---
title: "write_parquet"
canonical: https://tenzir.com/docs/reference/operators/write_parquet
source: https://tenzir.com/docs/reference/operators/write_parquet.md
section: "Docs"
---

# write_parquet

> Transforms event stream to a Parquet byte stream.

Transforms event stream to a Parquet byte stream.

```tql
write_parquet [compression_level=int, compression_type=str, encryption_key=secret]
```

## Description

[Apache Parquet](https://parquet.apache.org/) is a columnar storage format that a variety of data tools support.

### `compression_level = int (optional)`

An optional compression level for the corresponding compression type. This option is ignored if no compression type is specified.

Defaults to the compression type’s default compression level.

### `compression_type = str (optional)`

Specifies an optional compression type. Supported options are `zstd` for [Zstandard](http://facebook.github.io/zstd/) compression, `brotli` for [brotli](https://www.brotli.org) compression, `gzip` for [gzip](https://www.gzip.org) compression, and `snappy` for [snappy](https://google.github.io/snappy/) compression.

Why would I use this over the `compress_*` operators?

The Parquet format offers more efficient compression compared to the `compress_*` operators. This is because it compresses the data column-by-column, leaving metadata that needs to be accessed frequently uncompressed.

### `encryption_key = secret (optional)`

Encrypts all columns and the file footer using Parquet modular encryption with `AES_GCM_V1`. The same AES key encrypts the columns and the footer.

Supply a raw AES key containing 16, 24, or 32 bytes. The writer does not assume an encoding or decode the key. Decode base64 text with `decode_base64(secret("PARQUET_KEY"))`, or hexadecimal text with `decode_hex`, before passing it as `encryption_key`. A secret or blob that already contains raw key bytes can be passed directly.

This argument takes key material, not a password. Tenzir does not generate or rotate the key for you.

Read the file with [`read_parquet`](https://tenzir.com/docs/reference/operators/read_parquet.md) and the same key. Without this argument, the output is unencrypted. Encryption works with the supported compression types and preserves Parquet’s ability to read selected columns and row groups.

## Examples

Write a Parquet file:

```tql
from_file "/tmp/data.json" {
  read_json
}
write_parquet
```

To write encrypted Parquet to S3, first generate 32 random bytes, a 256-bit AES key, in base64 format:

```sh
openssl rand -base64 32
```

Store the command’s output as a [Tenzir secret](../../explanations/secrets.md) named `PARQUET_KEY`. Preserve the base64 text, including any trailing `=` padding, and decode it explicitly when writing the file:

```tql
from {message: "sensitive event"}
to_s3 "s3://security-archive/events.parquet" {
  write_parquet encryption_key=decode_base64(secret("PARQUET_KEY"))
}
```

Keep the same secret to read the file with [`read_parquet`](https://tenzir.com/docs/reference/operators/read_parquet.md). Generating a new key will not let you decrypt files written with the previous key.

For a local file containing raw binary key bytes, pass its contents directly:

```tql
from {message: "sensitive event"}
write_parquet encryption_key=file_contents("/etc/tenzir/parquet.key", binary=true)
```

Generate such a file with `openssl rand -out /etc/tenzir/parquet.key 32`.

## See Also

* [`read_bitz`](https://tenzir.com/docs/reference/operators/read_bitz.md)
* [`read_parquet`](https://tenzir.com/docs/reference/operators/read_parquet.md)
* [`write_bitz`](https://tenzir.com/docs/reference/operators/write_bitz.md)
* [`write_feather`](https://tenzir.com/docs/reference/operators/write_feather.md)
