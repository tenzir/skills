# decompress_gzip


Decompresses a stream of bytes in the Gzip format.

```tql
decompress_gzip
```

## Description

The `decompress_gzip` operator decompresses bytes in a pipeline incrementally. The operator supports decompressing multiple concatenated streams of the same codec transparently.

## Examples

### Import Suricata events from a Gzip-compressed file

```tql
load_file "eve.json.gz"
decompress_gzip
read_suricata
import
```

## See Also

* [`compress_gzip`](/reference/operators/compress_gzip.md)
* [`decompress_brotli`](/reference/operators/decompress_brotli.md)
* [`decompress_bz2`](/reference/operators/decompress_bz2.md)
* [`decompress_lz4`](/reference/operators/decompress_lz4.md)
* [`decompress_zstd`](/reference/operators/decompress_zstd.md)