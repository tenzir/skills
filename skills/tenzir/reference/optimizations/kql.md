---
title: "KQL"
canonical: https://tenzir.com/docs/reference/optimizations/kql
source: https://tenzir.com/docs/reference/optimizations/kql.md
section: "Docs"
---

# KQL

> This page documents which operators and functions frommicrosoftdefender and fromazureloganalytics transpile to Kusto Query Language (KQL) stages, and how KQL’s semantics differ from TQL. See our explanation of transpilation for shared planning rules and our optimizations overview for cross-target matrices.

This page documents which operators and functions [`from_microsoft_defender`](../operators/from_microsoft_defender.md) and [`from_azure_log_analytics`](../operators/from_azure_log_analytics.md) transpile to Kusto Query Language (KQL) stages, and how KQL’s semantics differ from TQL. See our explanation of [transpilation](../../explanations/transpilation.md) for shared planning rules and our [optimizations overview](../optimizations.md) for cross-target matrices.

## When it applies

The operator sends your query and appends the operators that follow as further stages, each on a new line, so that they apply to the table that your query returns, also after joins and aggregations. Your query text stays as is. The operator takes over no operator, and sends your query as you wrote it, if an appended stage might not apply to your query’s result or might change how it parses:

* Management commands, which start with a `.`.
* Queries that use `render`, `fork`, or `facet`, since `render` must end a query and the others return several tables.
* Queries with a `set` statement, such as `set notruncation`, which can change how the service limits a result.
* Queries with several tabular statements separated by `;`, since the service returns a table for each of them. Statements with `let`, `declare`, or `alias` before the final one are fine.
* Queries that end in `;` or `|`, that contain only whitespace and comments, or that the operator can’t tokenize, such as one with an unterminated string.

Words in string literals and comments don’t count, so `where Action == "render"` still receives stages. With `pushdown=false`, the operator takes over nothing, and every operator runs in Tenzir with TQL semantics. The operator then still appends the `project` of the fields that the pipeline reads, as [Operators that the service takes over](kql.md#operators-that-the-service-takes-over) describes, but no other stage.

## Operators that the service takes over

The service takes over the [longest run of operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after the source that KQL can spell:

* [`where`](../operators/where.md), as the [filters and functions](kql.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of top-level fields, including renames, which becomes `project`.
* [`drop`](../operators/drop.md) of top-level fields, which becomes `project-away`.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](kql.md#summaries) section lists, which becomes `summarize … by`. This includes [`top`](../operators/top.md) and [`rare`](../operators/rare.md). The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../../explanations/transpilation.md#summaries-and-computed-expressions) describes.
* [`sort`](../operators/sort.md) by fields, which becomes `sort by` with an explicit direction.
* [`head`](../operators/head.md), which becomes `take`.

An operator that would make the appended stages longer than 16 KiB also ends the run, since both services limit the size of a query. For example, the pipeline

```tql
from_microsoft_defender "DeviceNetworkEvents",
  azure_auth={
    tenant_id: secret("AZURE_TENANT_ID"),
    client_id: secret("AZURE_CLIENT_ID"),
    client_secret: secret("AZURE_CLIENT_SECRET"),
  }
where RemotePort != null
summarize Allowed, events=count()
sort -events
head 2
```

sends this query:

```text
DeviceNetworkEvents
| where isnotnull(['RemotePort'])
| summarize ['__tenzir_column_0'] = count() by ['Allowed']
| sort by ['__tenzir_column_0'] desc
| take 2
```

Tenzir arranges the result columns into the fields of the pipeline, such as `events`. Without an operator that enumerates the fields, the query ends with a `project` of the top-level fields that the pipeline reads, each as `column_ifexists(…)`, which keeps the type of a column that your query returns and yields `null` for one that it doesn’t. With `pushdown=false`, the query ends in this `project` too, for the fields that the operators in Tenzir read:

```text
| project ['Id'] = column_ifexists('Id', dynamic(null)), ['DeviceName'] = column_ifexists('DeviceName', dynamic(null))
```

Tenzir leaves out a projection that would exceed the 16 KiB.

## Summaries

The service computes these aggregation functions of a [`summarize`](../operators/summarize.md):

🟢 runs in the service, 🟡 runs in the service conditionally or approximately, and ⚪ runs in Tenzir.

| TQL                   | Status | KQL                        | Notes                                                                      |
| --------------------- | ------ | -------------------------- | -------------------------------------------------------------------------- |
| `count()`             | 🟢     | `count()`                  |                                                                            |
| `count(x)`            | 🟢     | `countif(isnotnull(x))`    | Counts empty strings                                                       |
| `min(x)`              | 🟢     | `min(x)`                   |                                                                            |
| `max(x)`              | 🟢     | `max(x)`                   |                                                                            |
| `count_if(x, v => p)` | 🟢     | `countif(p)`               | Skips `null` values                                                        |
| `count_distinct(x)`   | 🟢     | `count_distinct(x)`        | Exact; counts empty strings and fails beyond 100 million values in a group |
| `sum(x)`              | 🟢     | `sum(x)`                   | Yields `0` without values                                                  |
| `mean(x)`             | 🟢     | `avg(x)`                   | Yields `NaN` without values                                                |
| `stddev(x)`           | 🟢     | `stdevp(x)`                | Yields `0` without values                                                  |
| `variance(x)`         | 🟢     | `variancep(x)`             | Yields `0` without values                                                  |
| `all(x)`              | 🟢     | `countif(x == false) == 0` | Skips `null` values                                                        |
| `any(x)`              | 🟢     | `countif(x == true) > 0`   | Skips `null` values                                                        |

Without values, `all` holds and `any` does not, as in TQL, but both skip `null` values, where TQL’s `all(true, null)` is `null`. A summary keeps a group for `null` keys.

Group keys and aggregate arguments can be computed values, such as values that a [`set`](../operators/set.md) before the summary assigns. The service computes them with `extend` before `summarize`:

```tql
from_microsoft_defender "DeviceEvents", azure_auth={…}
kind = ActionType.to_upper()
summarize kind, events=count()
```

An assignment that the summary reads may call a function that KQL spells, and the service computes it with KQL’s semantics. An assignment that the summary doesn’t read must be infallible, as the rules for [computed keys and arguments](../../explanations/transpilation.md#summaries-and-computed-expressions) explain.

A time bucket, such as `hour = floor(TimeGenerated, 1h)` before a `summarize hour, events=count()`, runs in the service for these widths:

| Width                                  | Status | KQL                                                                                                               |
| -------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------- |
| Whole seconds, such as `1h`            | 🟡     | Runs as `bin(x, w)`. Widths that divide the time from 0001-01-01 to the epoch, such as those that divide two days |
| Fractions of a second, such as `250ms` | 🟡     | Runs as `bin(x, w)`. Whole multiples of 100 nanoseconds that divide the time from 0001-01-01 to the epoch         |
| Multiples of a week or a month         | ⚪      | Runs in Tenzir, since TQL aligns them to the calendar                                                             |

KQL’s `bin` counts from 0001-01-01 rather than from the epoch, which agrees with TQL only for widths that divide the time between the two, so other widths run in Tenzir. For example, `1h` becomes `bin(TimeGenerated, timespan(36000000000tick))`.

## Filters and functions

Filters become `where` stages. They consist of top-level fields, literals, comparisons, `in` with a list, arithmetic, `and`, `or`, and `not`, and these special forms:

| TQL                      | KQL                                 |
| ------------------------ | ----------------------------------- |
| `x == null`, `x != null` | `isnull(x)`, `isnotnull(x)`         |
| `"a" in x`               | `x contains_cs "a"`                 |
| `x in 10.0.0.0/8`        | `ipv4_is_in_range(x, "10.0.0.0/8")` |

Literals are strings, numbers, booleans, times as `datetime(…)` and durations as `timespan(…)`, both in whole multiples of 100 nanoseconds, and IP addresses as their canonical text. Filters, group keys, and aggregate arguments can also call these functions:

| Kind    | TQL                       | Status | KQL                                                                 | Notes                                                 |
| ------- | ------------------------- | ------ | ------------------------------------------------------------------- | ----------------------------------------------------- |
| Strings | `x.starts_with(y)`        | 🟢     | `x startswith_cs y`                                                 |                                                       |
| Strings | `x.ends_with(y)`          | 🟢     | `x endswith_cs y`                                                   |                                                       |
| Strings | `x.match_regex(y)`        | 🟢     | `x matches regex y`                                                 |                                                       |
| Strings | `x.length_bytes()`        | 🟢     | `string_size(x)`                                                    |                                                       |
| Strings | `x.length_chars()`        | 🟢     | `strlen(x)`                                                         |                                                       |
| Strings | `x.to_lower()`            | 🟢     | `tolower(x)`                                                        |                                                       |
| Strings | `x.to_upper()`            | 🟢     | `toupper(x)`                                                        |                                                       |
| Strings | `x.capitalize()`          | 🟢     | `strcat(toupper(substring(x, 0, 1)), tolower(substring(x, 1)))`     |                                                       |
| Strings | `x.trim()`                | 🟢     | `trim(@"\s+", x)`                                                   |                                                       |
| Strings | `x.trim_start()`          | 🟢     | `trim_start(@"\s+", x)`                                             |                                                       |
| Strings | `x.trim_end()`            | 🟢     | `trim_end(@"\s+", x)`                                               |                                                       |
| Strings | `x.replace(y, z)`         | 🟢     | `replace_string(x, y, z)`                                           |                                                       |
| Strings | `x.is_empty()`            | 🟢     | `isempty(x)`                                                        |                                                       |
| Strings | `x.slice(begin=b, end=e)` | 🟡     | `substring(x, b, e - b)`                                            | With constant `begin` and `end` that are not negative |
| Hashes  | `x.hash_md5()`            | 🟢     | `hash_md5(x)`                                                       |                                                       |
| Hashes  | `x.hash_sha1()`           | 🟢     | `hash_sha1(x)`                                                      |                                                       |
| Hashes  | `x.hash_sha256()`         | 🟢     | `hash_sha256(x)`                                                    |                                                       |
| Numbers | `x.abs()`                 | 🟢     | `abs(x)`                                                            |                                                       |
| Numbers | `x.ceil()`                | 🟢     | `tolong(ceiling(x))`                                                |                                                       |
| Numbers | `x.floor()`               | 🟢     | `tolong(floor(x, 1))`                                               |                                                       |
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

Ordering comparisons with a string, nested fields such as `Process.Name`, field names with `*`, the literal `null` outside a comparison, non-finite numbers, named arguments such as `ignore_case`, and optional fields such as `x?` run in Tenzir.

## KQL semantics

The operators that the service takes over run as KQL runs them, which can differ from TQL:

* KQL is statically typed. A field that your query doesn’t return, `sum` of a string, and `summarize` or `sort` by a `dynamic` column fail the query with the service’s error. Comparing a string column with a number matches no rows, and comparing a number column with a string converts the string.
* Strings are never `null` in KQL: a missing string is the empty string. The comparison `x == null` doesn’t match it, but `count(x)`, which becomes `countif(isnotnull(x))`, counts it.
* IP addresses compare as text, so `RemoteIP == 2001:db8::1` doesn’t match another spelling of the same address. Subnet membership parses addresses.
* Integer division truncates, and arithmetic follows KQL’s types.
* KQL’s `sort` puts `null` first in ascending and last in descending order, and compares strings by their characters.
* A name that a `let` statement of your query binds shadows a column of the same name in an appended stage.
* A query that the service rejects fails the pipeline with the error of the service, as our explanation of [plan-time diagnostics](../../explanations/transpilation.md#plan-time-decisions-and-diagnostics) describes.

### Result cap

Defender returns at most 100,000 rows of a query without reporting a truncation, so [`from_microsoft_defender`](../operators/from_microsoft_defender.md) warns when a result has exactly that many rows, unless a [`head`](../operators/head.md) that the service took over explains it. Narrow the query or its time range to get the complete result.

Log Analytics returns at most 500,000 rows and about 100 MiB of data, and reports a result beyond either limit as a partial failure, which [`from_azure_log_analytics`](../operators/from_azure_log_analytics.md) rejects with an error. Operators that the service takes over make the result smaller and may thus avoid such an error.

### Time window

The operator never narrows the `start` and `end` window based on an operator. A time field in your query’s output, such as `Timestamp` or `TimeGenerated`, may stem from an aggregation, a rename, or a computation, so a filter on it doesn’t reliably refer to the time that the window selects. Such filters still run in the service. Use `start` and `end`, or a time filter in your query, to bound the request.
