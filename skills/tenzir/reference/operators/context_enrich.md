---
title: "context_enrich"
canonical: https://tenzir.com/docs/reference/operators/context_enrich
source: https://tenzir.com/docs/reference/operators/context_enrich.md
section: "Docs"
---

# context_enrich

> Enriches events with data from a context.

Enriches events with data from a context.

```tql
context_enrich name:string, key=any,
               [into=field, mode=string, format=string, await_context=bool]
```

## Description

The `context_enrich` operator enriches every event with what a context holds for the event’s key. The deployment’s configuration declares the context, as the reference for [context files](../contexts.md) describes.

What the enrichment adds depends on the type of context:

* A lookup table adds the value stored under the key, or `null`. A subnet key in the table also matches the IP addresses and subnets it contains.
* A Bloom filter adds `true` for a key it may hold, and `null` otherwise.
* A GeoIP context adds a record of what its database holds for an IP address, or `null`. The first enrichment waits until the database has loaded.

### `name: string`

The name of the context to enrich with.

### `key = any`

The field that holds the enrichment key.

### `into = field (optional)`

The field into which to write the enrichment.

Defaults to the context name (`name`).

### `mode = string (optional)`

The mode of the enrichment operation:

* `set`: overwrites the field specified by `into`.
* `append`: appends into the list specified by `into`. If `into` is `null` or an `empty` list, a new list is created. If `into` is not a list, the enrichment will fail with a warning.

Defaults to `set`.

### `format = string (optional)`

The style of the enriched value:

* `plain`: formats the enrichment as retrieved from the context.
* `ocsf`: formats the enrichment as an [OCSF Enrichment](https://schema.ocsf.io/1.4.0-dev/objects/enrichment?extensions=) object with fields `created_time`, `data`, `name`, `provider`, and `value`.

Defaults to `plain`.

### `await_context = bool (optional)`

Waits for a context to be created and populated before enriching events. A new context becomes ready when its `context_update` operator finishes processing its input. Contexts populated at creation and persisted contexts are ready immediately.

This option requires `--nova=true`. It defaults to `false`.

For example, use it when a separate pipeline creates and populates a context at startup:

```tql
from {x: 1}
context_enrich "ctx", key=x, await_context=true
```

## Parallelism

In a [parallel pipeline](../../explanations/executor.md#parallel-execution), multiple instances of `context_enrich` enrich concurrently. Every enrichment is an atomic read from the shared context. Context updates can take effect between enrichments, as they can with a single instance.

## Examples

### Enrich with a lookup table

Declare a lookup table in the configuration:

contexts/ctx.yaml

```yaml
type: lookup-table
```

Add data to the lookup table:

```tql
from {x:1, y:"a"},
     {x:2, y:"b"}
context_update "ctx", key=x, value=y
```

Enrich with the table:

```tql
from {x:1}
context_enrich "ctx", key=x
```

```tql
{
  x: 1,
  ctx: "a",
}
```

### Enrich as OCSF Enrichment

Assume the same table preparation as above, but followed by a different call to `context_enrich` using the `format` option:

```tql
from {x:1}
context_enrich "ctx", key=x, format="ocsf"
```

```tql
{
  x: 1,
  ctx: {
    created_time: 2024-11-18T16:35:48.069981,
    data: "a",
    name: "x",
    provider: "ctx",
    value: 1,
  }
}
```

### Enrich by appending to an array

Enrich twice with the same context and accumulate enrichments into an array:

```tql
from {x:1}
context_enrich "ctx", key=x, into=enrichments, mode="append"
context_enrich "ctx", key=x, into=enrichments, mode="append"
```

```tql
{
  x: 1,
  enrichments: [
    "a",
    "a",
  ]
}
```

## See Also

* [`context_update`](context_update.md)
* [Contexts](../contexts.md)
* [Declare contexts](../../guides/enrich/declare-contexts.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
* [Enrich with threat intel](../../guides/enrich/enrich-with-threat-intel.md)
* [Enrich with asset inventory](../../guides/enrich/enrich-with-asset-inventory.md)
* [Learn idiomatic TQL](../../tutorials/learn-idiomatic-tql.md)
* [Enrichment](../../explanations/enrichment.md)

Parallelizable: a parallel pipeline may run this operator on several cores at once.
