---
title: "where"
canonical: https://tenzir.com/docs/reference/operators/where
source: https://tenzir.com/docs/reference/operators/where.md
section: "Docs"
---

# where

> Keeps only events for which the given predicate is true.

Keeps only events for which the given predicate is true.

```tql
where predicate:bool
```

## Description

The `where` operator only keeps events that match the provided predicate and discards all other events. Only events for which it evaluates to `true` pass. If the predicate evaluates to `null`, it is falsy, so `where` discards the event. See [Null is falsy in predicates](../expressions.md#null).

## Optimizations

A remote source, such as [`from_mysql`](from_mysql.md) or [`from_splunk`](from_splunk.md), may take over a `where` that follows it and run the filter in its target, with the target’s semantics. For example, a comparison with `null` yields `null` in SQL, so `name != "alpha"` does not keep rows where `name` is `null`, and a database may compare text without regard to case. Our [transpilation explanation](../../explanations/transpilation.md#native-semantics-vs-tql-semantics) lists the sources and how their targets differ. With `pushdown=false` on the source, the filter runs in Tenzir.

## Examples

### Keep only events where `src_ip` is `1.2.3.4`

```tql
where src_ip == 1.2.3.4
```

### Use a nested field name and a temporal constraint on the `ts` field

```tql
where id.orig_h == 1.2.3.4 and ts > now() - 1h
```

### Combine subnet, size and duration constraints

```tql
where src_ip in 10.10.5.0/25 and (orig_bytes > 1Mi or duration > 30min)
```

## See Also

* [`assert`](assert.md)
* [`drop`](drop.md)
* [`select`](select.md)
* [Filter and select data](../../guides/optimize/filter-and-select-data.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
