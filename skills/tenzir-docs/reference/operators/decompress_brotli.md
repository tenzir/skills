# decompress_brotli


Decompresses a stream of bytes in the Brotli format.

```tql
decompress_brotli
```

## Description

The `decompress_brotli` operator decompresses bytes in a pipeline incrementally. The operator supports decompressing multiple concatenated streams of the same codec transparently.

## Examples

### Import Suricata events from a Brotli-compressed file

```tql
load_file "eve.json.brotli"
decompress_brotli
read_suricata
import
```

## See Also

* [`compress_brotli`](/reference/operators/compress_brotli.md)
* [`decompress_bz2`](/reference/operators/decompress_bz2.md)
* [`decompress_gzip`](/reference/operators/decompress_gzip.md)
* [`decompress_lz4`](/reference/operators/decompress_lz4.md)
* [`decompress_zstd`](/reference/operators/decompress_zstd.md)