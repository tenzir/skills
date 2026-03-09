# decompress_zstd


Decompresses a stream of bytes in the Zstd format.

```tql
decompress_zstd
```

## Description

The `decompress_zstd` operator decompresses bytes in a pipeline incrementally. The operator supports decompressing multiple concatenated streams of the same codec transparently.

## Examples

### Import Suricata events from a Zstd-compressed file

```tql
load_file "eve.json.zstd"
decompress_zstd
read_suricata
import
```

## See Also

* [`compress_zstd`](compress_zstd.md)
* [`decompress_brotli`](decompress_brotli.md)
* [`decompress_bz2`](decompress_bz2.md)
* [`decompress_gzip`](decompress_gzip.md)
* [`decompress_lz4`](decompress_lz4.md)