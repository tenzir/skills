---
title: "context_update"
canonical: https://tenzir.com/docs/reference/operators/context_update
source: https://tenzir.com/docs/reference/operators/context_update.md
section: "Docs"
---

# context_update

> Updates a context with new data.

Updates a context with new data.

```tql
context_update name:string, key=any, [value=any]
```

## Description

The `context_update` operator stores data from every event in a context. It consumes its input and emits nothing. The deployment’s configuration declares the context, as the reference for [context files](../contexts.md) describes.

Use the `key` argument to specify the field in the input that should be associated with the context. The [`context_enrich`](context_enrich.md) operator uses this key to access the context.

What an update does depends on the type of context:

* A lookup table stores `value` under the key, replacing what the key held before.
* A Bloom filter adds the key. It holds keys only, so passing `value` is an error.
* A GeoIP context takes no updates, because it holds only what it loads from its source. Updating it is an error.

A context never stores secrets: the operator censors any secret in the key or value and warns about it.

Expiring entries

How long an entry of a lookup table lives is a setting of the table, not of the update. Set `create-timeout`, `write-timeout`, or `read-timeout` in the table’s [context file](../contexts.md#lookup-table).

### `name: string`

The name of the context to update.

### `key = any`

The field that represents the enrichment key in the data.

### `value = any (optional)`

The field that represents the enrichment value to associate with `key`. Only lookup tables take a value.

Defaults to `this`, so a lookup table stores the whole event.

## Examples

### Populate a lookup table with data

Declare a lookup table in the configuration:

contexts/ctx.yaml

```yaml
type: lookup-table
```

Add data to the lookup table via `context_update`:

```tql
from {x:1, y:"a"},
     {x:2, y:"b"}
context_update "ctx", key=x, value=y
```

Enrich with the table in another pipeline:

```tql
from {x:2}
context_enrich "ctx", key=x
```

```tql
{
  x: 2,
  ctx: "b",
}
```

### Store a computed value

The value can be any expression:

```tql
from {x:1},
     {x:2}
context_update "ctx", key=x, value=x*x
```

Enriching with the key `2` now adds `4`.

### Expire entries that stop showing up

Give the table a write timeout in its context file:

contexts/active-indicators.yaml

```yaml
type: lookup-table
write-timeout: 7d
```

Every update of a key resets its timeout, so an indicator that the feed stops reporting expires a week after its last update:

```tql
from {indicator: "malicious.example", source: "ThreatFeed"}
context_update "active-indicators", key=indicator, value={source: source}
```

### Add keys to a Bloom filter

Declare a Bloom filter in the configuration:

contexts/seen-hashes.yaml

```yaml
type: bloom-filter
capacity: 1000000
fp-probability: 0.01
```

Add keys without a value:

```tql
from {sha256: "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
context_update "seen-hashes", key=sha256
```

## See Also

* [`context_enrich`](context_enrich.md)
* [Contexts](../contexts.md)
* [Declare contexts](../../guides/enrich/declare-contexts.md)
* [Use lookup tables](../../guides/enrich/use-lookup-tables.md)
* [Enrich with threat intel](../../guides/enrich/enrich-with-threat-intel.md)
* [Enrich with asset inventory](../../guides/enrich/enrich-with-asset-inventory.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)
* [Enrichment](../../explanations/enrichment.md)
