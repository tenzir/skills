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

* [`compress_brotli`](compress_brotli.md)
* [`decompress_bz2`](decompress_bz2.md)
* [`decompress_gzip`](decompress_gzip.md)
* [`decompress_lz4`](decompress_lz4.md)
* [`decompress_zstd`](decompress_zstd.md)