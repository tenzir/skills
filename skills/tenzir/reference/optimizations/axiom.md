---
title: "Axiom"
canonical: https://tenzir.com/docs/reference/optimizations/axiom
source: https://tenzir.com/docs/reference/optimizations/axiom.md
section: "Docs"
---

# Axiom

> This page documents which operators and functions fromaxiom transpiles to Axiom Processing Language (APL) stages, and how APL’s semantics differ from TQL. See our explanation of transpilation for shared planning rules and our optimizations overview for cross-target matrices.

This page documents which operators and functions [`from_axiom`](../operators/from_axiom.md) transpiles to Axiom Processing Language (APL) stages, and how APL’s semantics differ from TQL. See our explanation of [transpilation](../../explanations/transpilation.md) for shared planning rules and our [optimizations overview](../optimizations.md) for cross-target matrices.

## When it applies

In dataset mode (`from_axiom "my-logs", …`), the base query is `['my-logs']`, which always accepts trailing APL stages. In raw query mode (`from_axiom query="…", …`), `from_axiom` uses the same trailing-stage check as [KQL](kql.md#when-it-applies): management commands, `render`/`fork`/`facet`, `set`, multiple tabular statements separated by `;`, and queries ending in `;` or `|` stay untouched.

With `pushdown=false`, Axiom takes over no operator and every operator runs in Tenzir with TQL semantics. The query still appends a `project` with `column_ifexists` for implicit projections of the top-level fields downstream reads.

## Operators that Axiom takes over

Axiom takes over the [longest run of operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after `from_axiom` that APL can spell:

* [`where`](../operators/where.md), as [Filters and functions](axiom.md#filters-and-functions) describes.
* [`select`](../operators/select.md) of top-level fields, including renames, which becomes `project`.
* [`drop`](../operators/drop.md) of top-level fields, which becomes `project-away`.
* [`summarize`](../operators/summarize.md) with group keys and the functions in [Summaries](axiom.md#summaries), which becomes `summarize … by` (or two `summarize` stages for exact `count_distinct`). This includes [`top`](../operators/top.md) and [`rare`](../operators/rare.md), and may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments as [summaries and computed expressions](../../explanations/transpilation.md#summaries-and-computed-expressions) describes.
* [`sort`](../operators/sort.md) by fields, which becomes `sort by` with an explicit direction.
* [`head`](../operators/head.md) with a positive count (`count > 0`), which becomes `take`. Axiom rejects `take 0`, so `head 0` runs in Tenzir.

An operator that would grow the appended stages beyond 16 KiB ends the run. For example, the pipeline

```tql
from_axiom "test",
  token=secret("axiom_token"),
  start=2026-11-21T00:00:00Z,
  end=2026-11-22T00:00:00Z
where status >= 400 and uri.starts_with("/api/")
bucket = _time.floor(5min)
summarize bucket, method, errors = count(), unique_ips = count_distinct(src_ip)
sort -errors, bucket, method
head 10
```

sends this APL query:

```kusto
['test']
| where (['status'] >= 400)
| where (['uri'] startswith_cs "/api/")
| extend ['__tenzir_column_0'] = bin(['_time'], timespan(300000000000ns))
| summarize ['__tenzir_part_0'] = count() by ['__tenzir_column_0'], ['method'], ['src_ip']
| summarize ['__tenzir_column_1'] = sum(['__tenzir_part_0']), ['__tenzir_column_2'] = countif(isnotnull(['src_ip'])) by ['__tenzir_column_0'], ['method']
| sort by ['__tenzir_column_1'] desc, ['__tenzir_column_0'] asc, ['method'] asc
| take 10
```

Without an operator that enumerates output fields, the query ends with a `project` using `column_ifexists(…, dynamic(null))` for the top-level fields downstream reads.

## Summaries

The table shows which aggregation functions run in Axiom and which run in Tenzir:

🟢 runs in Axiom, 🟡 runs in Axiom conditionally or approximately, and ⚪ runs in Tenzir.

| TQL                   | Status | APL                                                                            | Notes                                                                                                                                       |
| --------------------- | ------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `count()`             | 🟢     | `count()`                                                                      |                                                                                                                                             |
| `count(x)`            | 🟢     | `countif(isnotnull(x))`                                                        | Counts empty strings; skips `null`                                                                                                          |
| `min(x)`              | 🟢     | `min(x)`                                                                       |                                                                                                                                             |
| `max(x)`              | 🟢     | `max(x)`                                                                       |                                                                                                                                             |
| `count_if(x, v => p)` | 🟢     | `countif(p)`                                                                   | Skips `null` values                                                                                                                         |
| `count_distinct(x)`   | 🟡     | `summarize … by …, x \| summarize countif(isnotnull(x)) by …`                  | Exact via two `summarize` stages when siblings recompose; runs in Tenzir alongside a second distinct field, `mean`, `stddev`, or `variance` |
| `sum(x)`              | 🟢     | `sum(x)`                                                                       | Yields `0` without values                                                                                                                   |
| `mean(x)`             | 🟢     | `avg(x)`                                                                       |                                                                                                                                             |
| `stddev(x)`           | 🟢     | `stdev(x) * sqrt(todouble(countif(isnotnull(x)) - 1) / countif(isnotnull(x)))` | Rescales sample `stdev` to population form; yields `null` for `n <= 1`                                                                      |
| `variance(x)`         | 🟢     | `variance(x) * (todouble(countif(isnotnull(x)) - 1) / countif(isnotnull(x)))`  | Rescales sample `variance` to population form; yields `null` for `n <= 1`                                                                   |
| `all(x)`              | 🟢     | `countif(x == false) == 0`                                                     | Skips `null` values                                                                                                                         |
| `any(x)`              | 🟢     | `countif(x == true) > 0`                                                       | Skips `null` values                                                                                                                         |

APL has no single-stage exact `count_distinct` (only approximate `dcount`). When a summary contains a single `count_distinct(x)` alongside decomposable siblings (`count`, `count_if`, `sum`, `min`, `max`, `all`, `any`), Tenzir rewrites it into two exact `summarize` stages: stage 1 groups by the summary keys plus `x` and computes partial aggregates, and stage 2 computes `countif(isnotnull(x))` and recomposes the siblings. Summaries with a second distinct field, `mean`, `stddev`, or `variance` alongside `count_distinct` run in Tenzir instead of falling back to `dcount`.

Because APL provides sample `stdev` and `variance`, Tenzir rescales both to population values using `countif(isnotnull(x))`.

Computed keys and arguments run in an `extend` stage before `summarize`. Time buckets such as `bucket = _time.floor(5min)` run as `bin`:

| Width                                  | Status | Axiom                                                 |
| -------------------------------------- | ------ | ----------------------------------------------------- |
| Whole seconds, such as `1h`            | 🟢     | Runs as `bin(x, w)`                                   |
| Fractions of a second, such as `250ms` | 🟢     | Runs as `bin(x, w)`                                   |
| Multiples of a week or a month         | ⚪      | Runs in Tenzir, since TQL aligns them to the calendar |

Unlike KQL, APL aligns `bin` to the Unix epoch (`1970-01-01`) and accepts any positive nanosecond width.

## Filters and functions

Filters become `where` stages using top-level fields, literals, comparisons, `in` with a list, arithmetic, `and`, `or`, `not`, and these special forms:

| TQL                      | APL                                 |
| ------------------------ | ----------------------------------- |
| `x == null`, `x != null` | `isnull(x)`, `isnotnull(x)`         |
| `"a" in x`               | `x contains_cs "a"`                 |
| `x in 10.0.0.0/8`        | `ipv4_is_in_range(x, "10.0.0.0/8")` |

Literals support nanosecond `datetime(…)` and `timespan(Nns)` (except the minimum signed 64-bit duration). Filters, group keys, and aggregate arguments can call these functions:

| Kind    | TQL                       | Status | APL                                                                 | Notes                                                 |
| ------- | ------------------------- | ------ | ------------------------------------------------------------------- | ----------------------------------------------------- |
| Strings | `x.starts_with(y)`        | 🟢     | `x startswith_cs y`                                                 |                                                       |
| Strings | `x.ends_with(y)`          | 🟢     | `x endswith_cs y`                                                   |                                                       |
| Strings | `x.match_regex(y)`        | 🟢     | `x matches regex y`                                                 | Go RE2                                                |
| Strings | `x.length_bytes()`        | 🟢     | `string_size(x)`                                                    |                                                       |
| Strings | `x.length_chars()`        | 🟢     | `strlen(x)`                                                         |                                                       |
| Strings | `x.to_lower()`            | 🟢     | `tolower(x)`                                                        |                                                       |
| Strings | `x.to_upper()`            | 🟢     | `toupper(x)`                                                        |                                                       |
| Strings | `x.capitalize()`          | 🟢     | `strcat(toupper(substring(x, 0, 1)), tolower(substring(x, 1)))`     |                                                       |
| Strings | `x.trim()`                | 🟢     | `trim_regex(@"\s+", x)`                                             |                                                       |
| Strings | `x.trim_start()`          | 🟢     | `trim_start_regex(@"\s+", x)`                                       |                                                       |
| Strings | `x.trim_end()`            | 🟢     | `trim_end_regex(@"\s+", x)`                                         |                                                       |
| Strings | `x.replace(y, z)`         | 🟢     | `replace_string(y, z, x)`                                           |                                                       |
| Strings | `x.is_empty()`            | 🟢     | `isempty(x)`                                                        | Yields `true` for `null`                              |
| Strings | `x.slice(begin=b, end=e)` | 🟡     | `substring(x, b, e - b)`                                            | With constant `begin` and `end` that are not negative |
| Hashes  | `x.hash_md5()`            | 🟢     | `hash_md5(x)`                                                       |                                                       |
| Hashes  | `x.hash_sha1()`           | 🟢     | `hash_sha1(x)`                                                      |                                                       |
| Hashes  | `x.hash_sha256()`         | 🟢     | `hash_sha256(x)`                                                    |                                                       |
| Numbers | `x.abs()`                 | 🟢     | `abs(x)`                                                            |                                                       |
| Numbers | `x.ceil()`                | 🟢     | `tolong(ceiling(x))`                                                |                                                       |
| Numbers | `x.floor()`               | 🟢     | `tolong(floor(x))`                                                  |                                                       |
| Numbers | `x.round()`               | 🟢     | `tolong(round(x))`                                                  |                                                       |
| Numbers | `x.sqrt()`                | 🟢     | `sqrt(x)`                                                           |                                                       |
| Numbers | `x.exp()`                 | 🟢     | `exp(x)`                                                            |                                                       |
| Numbers | `x.log()`, `x.log(base)`  | 🟢     | `log(x)`, `(log(x) / log(base))`                                    |                                                       |
| Times   | `x.year()`                | 🟢     | `getyear(x)`                                                        |                                                       |
| Times   | `x.month()`               | 🟢     | `getmonth(x)`                                                       |                                                       |
| Times   | `x.day()`                 | 🟢     | `dayofmonth(x)`                                                     |                                                       |
| Times   | `x.hour()`                | 🟢     | `datetime_part("hour", x)`                                          |                                                       |
| Times   | `x.minute()`              | 🟢     | `datetime_part("minute", x)`                                        |                                                       |
| Times   | `x.second()`              | 🟢     | `datetime_part("second", x) + datetime_part("nanosecond", x) / 1e9` |                                                       |
| Times   | `x.since_epoch()`         | 🟢     | `x - datetime(1970-01-01)`                                          |                                                       |

Ordering comparisons with a string, nested field paths (use flat `this["geo.country"]` for Axiom’s flattened dotted columns), field names with `*`, `null` outside a comparison, non-finite numbers, named arguments such as `ignore_case`, and optional fields such as `x?` run in Tenzir.

## APL semantics

Operators that Axiom takes over run with APL’s native semantics:

* Strings can be `null` in APL, and `isempty(string(null))` yields `true`.
* Regular expressions use Go’s RE2 engine.
* Population `stddev` and `variance` yield `null` for single-element groups (`n == 1`) because APL’s `stdev` and `variance` return `null` for `n <= 1`.
* Nested JSON objects ingested into Axiom are flattened into dotted top-level column names (`['geo.country']`). Map-field sub-access (`['a']['b']`) stays in Tenzir.
* Pre-1970 timestamps in `bin` truncate toward the Unix epoch.
* A query that Axiom rejects fails the pipeline with Axiom’s error, as our explanation of [plan-time diagnostics](../../explanations/transpilation.md#plan-time-decisions-and-diagnostics) describes.

### Result cap

Every query sends `defaultLimit: 50000` (Axiom’s base single-query row cap). The operator warns on `isPartial`, `isEstimate`, `default_limit_warning`, `license_limit_for_query_warning`, and unexpected `max_limit_warning`. Narrow `_time` or aggregate with [`summarize`](../operators/summarize.md) to stay within the cap.

### Time window

The `start` and `end` options are sent in the request body as `startTime` and `endTime`. A pushed `where _time` filter that is disjoint with `start` and `end` fails with Axiom’s HTTP `400` error.
