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

* [`compress_gzip`](compress_gzip.md)
* [`decompress_brotli`](decompress_brotli.md)
* [`decompress_bz2`](decompress_bz2.md)
* [`decompress_lz4`](decompress_lz4.md)
* [`decompress_zstd`](decompress_zstd.md)