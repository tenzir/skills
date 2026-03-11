# context::inspect


Resets a context.

```tql
context::inspect name:string
```

## Description

The `context::inspect` operator shows details about a specified context.

### `name: string`

The name of the context to inspect.

## Examples

### Inspect a context

Add data to the lookup table:

```tql
from {x:1, y:"a"},
     {x:2, y:"b"}
context::update "ctx", key=x, value=y
```

Retrieve the lookup table contents:

```tql
context::inspect "ctx"
```

```tql
{key: 2, value: "b"}
{key: 1, value: "a"}
```

## See Also

* [`context::create_bloom_filter`](/reference/operators/context/create_bloom_filter.md)
* [`context::create_geoip`](/reference/operators/context/create_geoip.md)
* [`context::create_lookup_table`](/reference/operators/context/create_lookup_table.md)
* [`context::enrich`](/reference/operators/context/enrich.md)
* [`context::erase`](/reference/operators/context/erase.md)
* [`context::list`](/reference/operators/context/list.md)
* [`context::load`](/reference/operators/context/load.md)
* [`context::remove`](/reference/operators/context/remove.md)
* [`context::reset`](/reference/operators/context/reset.md)
* [`context::save`](/reference/operators/context/save.md)
* [`context::update`](/reference/operators/context/update.md)
* [Work with lookup tables](../../../guides/enrichment/work-with-lookup-tables.md)