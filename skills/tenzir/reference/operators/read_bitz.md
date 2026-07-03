# read_bitz

> Parses bytes as BITZ format.

Parses bytes as *BITZ* format.

```tql
read_bitz
```

## Description

BITZ is short for **Bi**nary **T**en**z**ir and is our internal wire format.

Use BITZ when you need high-throughput structured data exchange with minimal overhead. BITZ is a thin wrapper around Arrow’s record batches. That is, BITZ lays out data in a (compressed) columnar fashion that makes it conducive for analytical workloads. Since it’s padded and byte-aligned, it is portable and doesn’t induce any deserialization cost, making it suitable for write-once-read-many use cases.

Internally, BITZ uses Arrow’s IPC format for serialization and deserialization, but prefixes each message with a 64 bit size prefix to support changing schemas between batches - something that Arrow’s IPC format does not support on its own. Use [`write_bitz`](https://tenzir.com/docs/reference/operators/write_bitz.md) to create `.bitz` files that you can later load again with [`read_bitz`](https://tenzir.com/docs/reference/operators/read_bitz.md).

## See Also

* [`read_feather`](https://tenzir.com/docs/reference/operators/read_feather.md)
* [`read_parquet`](https://tenzir.com/docs/reference/operators/read_parquet.md)
* [`write_bitz`](https://tenzir.com/docs/reference/operators/write_bitz.md)
* [Parse binary data](../../guides/parsing/parse-binary-data.md)
