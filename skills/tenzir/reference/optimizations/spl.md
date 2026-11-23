---
title: "SPL"
canonical: https://tenzir.com/docs/reference/optimizations/spl
source: https://tenzir.com/docs/reference/optimizations/spl.md
section: "Docs"
---

# SPL

> This page documents which operators and functions fromsplunk transpiles to Splunk Search Processing Language (SPL and SPL2), and how Splunk’s semantics differ from TQL. See our explanation of transpilation for shared planning rules and our optimizations overview for cross-target matrices.

This page documents which operators and functions [`from_splunk`](../operators/from_splunk.md) transpiles to Splunk Search Processing Language (SPL and SPL2), and how Splunk’s semantics differ from TQL. See our explanation of [transpilation](../../explanations/transpilation.md) for shared planning rules and our [optimizations overview](../optimizations.md) for cross-target matrices.

## When it applies

The operator searches in one of three ways:

* **With `index`**, Tenzir writes the search for the events of the indexes, such as `search index="main"`, and appends the operators that follow.
* **With `search`**, the operator runs your search, prepending the `search` command where Splunk Web does, and appends the operators that follow, each on a new line. The appended stages apply to the results of your search, so they also work after transforming commands such as `stats`.
* **With `spl2`**, the operator runs your SPL2 search and appends the operators that follow, as [SPL2](spl.md#spl2) describes.

The operator takes over no operator if your search does not end where stages may follow, such as a search that ends in `|` or has an unterminated string, comment, or subsearch, or if it may format its values with `fieldformat` or a macro. It also takes over nothing with `options`, which may change how Splunk runs the search, and with `pushdown=false`, which runs every operator in Tenzir with TQL semantics. The search then still returns only the fields that the pipeline uses.

### SPL2

The `spl2` argument of [`from_splunk`](../operators/from_splunk.md) runs an SPL2 search. Splunk takes over the same operators as for `search`, appended to your search as SPL2 stages, and [Splunk semantics](spl.md#splunk-semantics) apply too. SPL2 spells a few things differently:

* Fields in commands are single-quoted, as in `'user'`.
* SPL2 has a `null` literal, and `stats` counts with `count()` and `count(if(p, 1, null))`.
* There is no `fields *`. The operator asks Splunk to extract all fields instead, and appends a `fields` stage only to keep the fields that the pipeline reads.
* Comments are `//` and `/* */`, raw strings start with `@"`, and a `;` ends the search so that no stage may follow.

The operator never treats an SPL2 search as plain, because a search may redefine `_time`. Comparisons of `_time` and the operators after them run in Tenzir, and the bounds `earliest` and `latest` never narrow. The pipeline

```tql
from_splunk "https://splunk.example.com:8089",
  spl2=r#"from main where sourcetype == "linux_secure""#,
  earliest="-1h",
  latest="now",
  headers={Authorization: secret("splunk-rest-authorization")}
where user != "root"
summarize user, attempts=count()
sort -attempts
head 20
```

dispatches this search:

```text
from main where sourcetype == "linux_secure"
| where ('user' != "root")
| stats count() as tenzir_column_0 by 'user'
| sort 20 -'tenzir_column_0'
| head 20
| appendpipe [stats count() as tenzir_groups_0]
```

## Operators that Splunk takes over

Splunk takes over the [longest run of operators](../../explanations/transpilation.md#the-run-of-operators-after-the-source) directly after the source that SPL can spell:

* [`where`](../operators/where.md), as the [filters and functions](spl.md#filters-and-functions) section describes.
* [`select`](../operators/select.md) of top-level fields, including renames, which becomes `fields`.
* [`drop`](../operators/drop.md) of top-level fields, which becomes `fields -`.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](spl.md#summaries) section lists, which becomes `stats … by`. The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../../explanations/transpilation.md#summaries-and-computed-expressions) describes.
* [`sort`](../operators/sort.md) by fields, which becomes `sort` with an explicit count: the count of the [`head`](../operators/head.md) after it, or `0` for all results, since `sort` keeps only 10,000 results by default.
* [`head`](../operators/head.md), which becomes `head`, and [`top`](../operators/top.md) or [`rare`](../operators/rare.md) followed by [`head`](../operators/head.md). A search with a command that has side effects, such as `outputlookup` or `collect`, or with a macro, which may hide one, runs the limit in Tenzir.

For example, the pipeline

```tql
from_splunk "https://splunk.example.com:8089",
  index="main",
  earliest="-1h",
  latest="now",
  headers={Authorization: secret("splunk-rest-authorization")}
where source == "auth" and user != "root"
summarize user, events=count()
where events > 1
sort -events
head 3
```

sends this search:

```text
search index="main" source="auth"
| where ('user' != "root")
| stats count as tenzir_column_0 by user
| where ('tenzir_column_0' > 1)
| sort 3 -tenzir_column_0
| head 3
| fields user, tenzir_column_0
| appendpipe [stats count as tenzir_groups_0]
```

Tenzir arranges the result fields into the fields of the pipeline, such as `events`. A search with a summary ends with an `appendpipe` that adds a row counting the results. Splunk returns no results and no error when an expression in a search with `stats` fails, so the operator fails the pipeline when that row is missing. The error reads `Splunk search ended without its last result`, with a note that Splunk computed the stages that the operator took over with its own semantics, and a hint to use `pushdown=false`.

Without an operator that enumerates the fields, the search ends with a `fields` stage that keeps the fields that the pipeline reads, or with `fields *`, since Splunk’s export endpoint otherwise returns only the fields that the search references.

## Summaries

Splunk computes these aggregation functions of a [`summarize`](../operators/summarize.md):

🟢 runs in Splunk, 🟡 runs in Splunk conditionally or approximately, and ⚪ runs in Tenzir.

| TQL                   | Status | SPL                                            | Notes                                                                                                |
| --------------------- | ------ | ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `count()`             | 🟢     | `count`                                        | SPL2 spells it `count()`                                                                             |
| `count(x)`            | 🟢     | `count(x)`                                     | Counts each value of a multivalue field                                                              |
| `min(x)`              | 🟢     | `min(x)`                                       | Compares numbers numerically and other values as text                                                |
| `max(x)`              | 🟢     | `max(x)`                                       | Compares numbers numerically and other values as text                                                |
| `count_if(x, v => p)` | 🟢     | `count(eval(p))`                               | Skips events without a value; `count(if(p, 1, null))` in SPL2                                        |
| `count_distinct(x)`   | 🟢     | `dc(x)`                                        | Exact, unlike `estdc`                                                                                |
| `sum(x)`              | 🟢     | `sum(x)`                                       |                                                                                                      |
| `mean(x)`             | 🟢     | `avg(x)`                                       |                                                                                                      |
| `stddev(x)`           | 🟢     | `stdevp(x)`                                    |                                                                                                      |
| `variance(x)`         | 🟢     | `varp(x)`                                      |                                                                                                      |
| `all(x)`              | 🟢     | `min(eval(case(x=="true", 1, x=="false", 0)))` | Decoded as a boolean; skips `null` values and yields `null` without values; `min(case(...))` in SPL2 |
| `any(x)`              | 🟢     | `max(eval(case(x=="true", 1, x=="false", 0)))` | Decoded as a boolean; skips `null` values and yields `null` without values; `max(case(...))` in SPL2 |

Splunk returns every value as a string, so the operator reads counts as integers, and sums, means, deviations, and variances as numbers.

Group keys and aggregate arguments can be computed values, such as values that a [`set`](../operators/set.md) before the summary assigns. Splunk computes them with `eval` before `stats`:

```tql
from_splunk "https://splunk:8089", index="main", earliest="-1h", latest="now"
kind = action.to_upper()
summarize kind, events=count()
```

The search computes the key with `| eval tenzir_column_0=upper('action')`. An assignment that the summary reads may call a function that SPL spells, and Splunk computes it with its own semantics. An assignment that the summary doesn’t read must be infallible, as the rules for [computed keys and arguments](../../explanations/transpilation.md#summaries-and-computed-expressions) explain.

A time bucket, such as `hour = floor(_time, 1h)` before a

[`summarize`](../operators/summarize.md), also runs in Splunk:

| Width                                  | Status | SPL                                                                                  |
| -------------------------------------- | ------ | ------------------------------------------------------------------------------------ |
| Whole seconds, such as `1h`            | 🟢     | Runs as `strftime(floor(x / w) * w, "%Y-%m-%dT%H:%M:%S%z")`, which arrives as a time |
| Fractions of a second, such as `250ms` | ⚪      | Runs in Tenzir                                                                       |
| Multiples of a week or a month         | ⚪      | Runs in Tenzir, since TQL aligns them to the calendar                                |

## Filters and functions

With `index`, the conjuncts of the filters right after the operator extend the base `search` command where it can spell them, which lets Splunk use its indexes:

* `==` of a field with a string, a number, a boolean, or an IP address, and `<`, `<=`, `>`, and `>=` with a number.
* Comparisons of `_time` with a time, in epoch seconds.
* `in` with a list, which becomes `IN`, and `in` with a subnet, which becomes a CIDR match.
* `!= null`, which becomes `field=*`.
* `starts_with` and `ends_with`, and `"x" in field`, which become wildcards.
* `and` and `or` of such terms.

All other filters become `where` stages. They consist of top-level fields, literals (numbers, strings, booleans, `null`, times compared with `_time`, and IP addresses), comparisons, `in` with a list, arithmetic, `and`, `or`, `not`, and the functions marked 🟢 or 🟡 in the following table:

| Kind    | TQL                       | Status | SPL                                            | Notes                                                                                                              |
| ------- | ------------------------- | ------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Strings | `x.starts_with(y)`        | 🟢     | `substr(x, 1, len(y))==y`                      | As a value, wrapped in `if(p, "true", "false")` and decoded as a boolean (`null` becomes `false`)                  |
| Strings | `x.ends_with(y)`          | 🟢     | `substr(x, len(x)-len(y)+1)==y`                | As a value, wrapped in `if(p, "true", "false")` and decoded as a boolean (`null` becomes `false`)                  |
| Strings | `x.match_regex(y)`        | 🟢     | `match(x, y)`                                  | As a value, wrapped in `if(p, "true", "false")` and decoded as a boolean (`null` becomes `false`)                  |
| Strings | `x.length_bytes()`        | ⚪      | —                                              |                                                                                                                    |
| Strings | `x.length_chars()`        | 🟢     | `len(x)`                                       |                                                                                                                    |
| Strings | `x.to_lower()`            | 🟢     | `lower(x)`                                     |                                                                                                                    |
| Strings | `x.to_upper()`            | 🟢     | `upper(x)`                                     |                                                                                                                    |
| Strings | `x.capitalize()`          | 🟢     | `upper(substr(x, 1, 1)) + lower(substr(x, 2))` | Yields `null` for an empty string                                                                                  |
| Strings | `x.trim()`                | 🟢     | `trim(x)`                                      |                                                                                                                    |
| Strings | `x.trim_start()`          | 🟢     | `ltrim(x)`                                     |                                                                                                                    |
| Strings | `x.trim_end()`            | 🟢     | `rtrim(x)`                                     |                                                                                                                    |
| Strings | `x.replace(y, z)`         | 🟡     | `replace(x, y, z)`                             | With a constant string `y`, regex-escaped for Splunk's PCRE matcher                                                |
| Strings | `x.is_empty()`            | 🟢     | `len(x)==0`                                    | As a value, wrapped in `if(p, "true", "false")` and decoded as a boolean (`null` becomes `false`)                  |
| Strings | `x.slice(begin=b, end=e)` | 🟡     | `if(e > b, substr(x, b + 1, e - b), "")`       | With constant `begin` and `end` that are not negative; uses `substr(x, b + 1)` or `substr(x, 1, e)` with one bound |
| Hashes  | `x.hash_md5()`            | 🟢     | `md5(x)`                                       |                                                                                                                    |
| Hashes  | `x.hash_sha1()`           | 🟢     | `sha1(x)`                                      |                                                                                                                    |
| Hashes  | `x.hash_sha256()`         | 🟢     | `sha256(x)`                                    |                                                                                                                    |
| Numbers | `x.abs()`                 | 🟢     | `abs(x)`                                       |                                                                                                                    |
| Numbers | `x.ceil()`                | 🟢     | `ceiling(x)`                                   |                                                                                                                    |
| Numbers | `x.floor()`               | 🟢     | `floor(x)`                                     |                                                                                                                    |
| Numbers | `x.round()`               | 🟢     | `round(x)`                                     |                                                                                                                    |
| Numbers | `x.sqrt()`                | 🟢     | `sqrt(x)`                                      |                                                                                                                    |
| Numbers | `x.exp()`                 | 🟢     | `exp(x)`                                       |                                                                                                                    |
| Numbers | `x.log()`, `x.log(base)`  | 🟢     | `ln(x)`, `log(x, base)`                        |                                                                                                                    |
| Times   | `x.year()`                | 🟢     | `tonumber(strftime(x, "%Y"))`                  | Uses Splunk's configured time zone                                                                                 |
| Times   | `x.month()`               | 🟢     | `tonumber(strftime(x, "%m"))`                  | Uses Splunk's configured time zone                                                                                 |
| Times   | `x.day()`                 | 🟢     | `tonumber(strftime(x, "%d"))`                  | Uses Splunk's configured time zone                                                                                 |
| Times   | `x.hour()`                | 🟢     | `tonumber(strftime(x, "%H"))`                  | Uses Splunk's configured time zone                                                                                 |
| Times   | `x.minute()`              | 🟢     | `tonumber(strftime(x, "%M"))`                  | Uses Splunk's configured time zone                                                                                 |
| Times   | `x.second()`              | 🟢     | `tonumber(strftime(x, "%S.%6N"))`              | Microsecond precision                                                                                              |
| Times   | `x.since_epoch()`         | ⚪      | —                                              | Splunk has no durations                                                                                            |

The same functions compute group keys and aggregate arguments with `eval`. Predicates used as values are wrapped in `if(p, "true", "false")` and decoded back as booleans (`null` predicates become `false`). They follow Splunk’s semantics, such as how `round` rounds halves, how `trim` delimits whitespace, and Splunk’s configured time zone for `strftime`.

Nested field paths, subnets outside the base search, times compared with fields other than Splunk’s own `_time`, such as `_time` after `select _time=event_time` or after a `search` that runs more than a single `search` command, such as `| rename event* AS _*`, bare boolean fields such as `where flag`, fields whose names start with `__`, which Splunk treats as internal, named arguments such as `ignore_case`, and optional fields such as `x?` run in Tenzir.

## Splunk semantics

The operators that Splunk takes over run as Splunk runs them, which can differ from TQL:

* Terms of the base `search` command match strings without regard to case, so `user == "root"` also matches `Root`. A string with `*` becomes a `where` stage instead, so that `*` is no wildcard.
* A `where` stage compares strings exactly. The filter `x != "a"` drops results without `x`, and a comparison with a multivalue field holds if any of its values matches.
* Splunk returns every value as a string. A comparison with an IP address compares the text of the address, such as `198.51.100.24`.
* The `stats` command drops results whose group key is `null`, and puts a result with a multivalue key into the group of each of its values.
* A summary value that Splunk leaves out, such as `min` over no values, is missing from the result rather than `null`.
* Counts are integers also with `raw=true`. Other values follow `raw`.
* A `where` stage whose expression fails, outside a search with `stats`, makes Splunk return an empty result without an error.
* When Splunk reports an error or a warning, the diagnostic shows the search as the operator sent it, including the appended stages.

### Time window

With `index`, comparisons of `_time` in the filters before any summary, limit, or sort also narrow `earliest` and `latest`, rounded outward to whole seconds, when both are absolute. A strict bound excludes its time, so `where _time < 2025-01-01T00:02:00Z` requests `latest_time=1735689720`. A relative bound, such as `-15m`, resolves on the server, so the operator keeps both bounds as they are. It also keeps them when the narrowed bounds would cross, since Splunk rejects crossing bounds. The comparisons stay in the search in every case. With `search`, the bounds never narrow, since a `_time` field in your search’s results may stem from an aggregation or a computation.
