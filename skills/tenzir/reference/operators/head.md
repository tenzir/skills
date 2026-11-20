---
title: "head"
canonical: https://tenzir.com/docs/reference/operators/head
source: https://tenzir.com/docs/reference/operators/head.md
section: "Docs"
---

# head

> Limits the input to the first n events.

Limits the input to the first `n` events.

```tql
head [n:int]
```

## Description

Forwards the first `n` events and discards the rest.

`head n` is a shorthand notation for [`slice end=n`](slice.md).

### `n: int (optional)`

The number of events to keep.

Defaults to `10`.

## Optimizations

A remote source, such as [`from_mysql`](from_mysql.md) or [`from_splunk`](from_splunk.md), may take over a `head` that follows it, so that its target returns at most `n` events, as with a `LIMIT`. After a summary that the target computes, the limit counts groups. Our [optimizations reference](../optimizations.md#the-run-of-operators-after-the-source) describes which operators a source takes over.

## Examples

### Get the first 10 events

```tql
head
```

### Get the first 5 events

```tql
head 5
```

## See Also

* [`slice`](slice.md)
* [`tail`](tail.md)
* [Slice and sample data](../../guides/optimize/slice-and-sample-data.md)
