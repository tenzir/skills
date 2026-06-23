# compress_bz2


Compresses a stream of bytes using bz2 compression.

```tql
compress_bz2 [level=int]
```

## Description

The `compress_bz2` operator compresses bytes in a pipeline incrementally.

### `level = int (optional)`

The compression level to use. The supported values depend on the codec used. If omitted, the default level for the codec is used.

## Examples

### Export all events in a Bzip2-compressed NDJSON file

```tql
export
to_file "/tmp/backup.json.bz2" {
  write_ndjson
  compress_bz2
}
```

### Read and write Bzip2-compressed NDJSON

```tql
from_file "in.bz2" {
  decompress_bz2
  read_ndjson
}
to_file "out.bz2" {
  write_ndjson
  compress_bz2 level=18
}
```

## See Also

* [`compress_brotli`](http://docs.tenzir.com/reference/operators/compress_brotli.md)
* [`compress_gzip`](http://docs.tenzir.com/reference/operators/compress_gzip.md)
* [`compress_lz4`](http://docs.tenzir.com/reference/operators/compress_lz4.md)
* [`compress_zstd`](http://docs.tenzir.com/reference/operators/compress_zstd.md)
* [`decompress_bz2`](http://docs.tenzir.com/reference/operators/decompress_bz2.md)