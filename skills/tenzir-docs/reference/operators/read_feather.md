# read_feather


Parses an incoming Feather byte stream into events.

```tql
read_feather
```

## Description

Transforms the input [Feather](https://arrow.apache.org/docs/python/feather.html) (a thin wrapper around [Apache Arrow’s IPC](https://arrow.apache.org/docs/python/ipc.html) wire format) byte stream to event stream.

## Examples

### Publish a feather logs file

```tql
load_file "logs.feather"
read_feather
pulish "log"
```

## See Also

* [`read_parquet`](read_parquet.md)
* [`write_feather`](write_feather.md)