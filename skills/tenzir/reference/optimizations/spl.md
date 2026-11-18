---
title: "SPL"
canonical: https://tenzir.com/docs/reference/optimizations/spl
source: https://tenzir.com/docs/reference/optimizations/spl.md
section: "Docs"
---

# SPL

> The Splunk source fromsplunk hands Splunk the operators that follow it by appending stages in the Splunk Search Processing Language (SPL) to the search that it sends, so that Splunk returns only what the pipeline keeps. Those operators leave the pipeline and run in Splunk, with Splunk’s semantics. This page describes which operators Splunk takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our optimizations overview explains how Tenzir optimizes pipelines in general.

The Splunk source [`from_splunk`](../operators/from_splunk.md) hands Splunk the operators that follow it by appending stages in the Splunk Search Processing Language (SPL) to the search that it sends, so that Splunk returns only what the pipeline keeps. Those operators leave the pipeline and run in Splunk, with Splunk’s semantics. This page describes which operators Splunk takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator searches in one of three ways:

* **With `index`**, Tenzir writes the search for the events of the indexes, such as `search index="main"`, and appends the operators that follow.
* **With `search`**, the operator runs your search, prepending the `search` command where Splunk Web does, and appends the operators that follow, each on a new line. The appended stages apply to the results of your search, so they also work after transforming commands such as `stats`.
* **With `spl2`**, the operator runs your SPL2 search and appends the operators that follow, as [SPL2](spl.md#spl2) describes.

The operator takes over no operator if your search does not end where stages may follow, such as a search that ends in `|` or has an unterminated string, comment, or subsearch, or if it may format its values with `fieldformat` or a macro. It also takes over nothing with `options`, which may change how Splunk runs the search, and with `pushdown=false`, which keeps every operator in Tenzir with TQL semantics. The search then still returns only the fields that the pipeline uses.

## Operators that Splunk takes over

The operator takes over the longest run of operators directly after it that SPL can spell:

* [`where`](../operators/where.md), as the [filters](spl.md#filters) section describes.
* [`select`](../operators/select.md) of top-level fields, including renames, which becomes `fields`.
* [`drop`](../operators/drop.md) of top-level fields, which becomes `fields -`.
* [`summarize`](../operators/summarize.md) with group keys and the functions that the [summaries](spl.md#summaries) section lists, which becomes `stats … by`. The summary may follow [`select`](../operators/select.md), [`drop`](../operators/drop.md), and assignments, as [Aggregations in the source](../optimizations.md#aggregations-in-the-source) describes.
* [`sort`](../operators/sort.md) by fields, which becomes `sort` with an explicit count: the count of the [`head`](../operators/head.md) after it, or `0` for all results, since `sort` keeps only 10,000 results by default.
* [`head`](../operators/head.md), which becomes `head`, and [`top`](../operators/top.md) or [`rare`](../operators/rare.md) followed by [`head`](../operators/head.md). A search with a command that has side effects, such as `outputlookup` or `collect`, or with a macro, which may hide one, keeps the limit in Tenzir.

The first operator that SPL cannot spell ends the run. That operator and everything after it run in Tenzir. Tenzir splits a [`where`](../operators/where.md) at `and`, so Splunk can still take over the conjuncts that it spells. For example, the pipeline

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

| TQL                   | SPL                                                  |
| --------------------- | ---------------------------------------------------- |
| `count()`             | `count`                                              |
| `count(x)`            | `count(x)`                                           |
| `min(x)`, `max(x)`    | `min(x)`, `max(x)`                                   |
| `count_if(x, v => p)` | `count(eval(p))`, which skips events without a value |
| `count_distinct(x)`   | `dc(x)`, which counts exactly, unlike `estdc`        |
| `sum(x)`              | `sum(x)`                                             |
| `mean(x)`             | `avg(x)`                                             |

Splunk returns every value as a string, so the operator reads counts as integers and sums and means as numbers.

Group keys and aggregate arguments can be computed values, such as values that a [`set`](../operators/set.md) before the summary assigns. Splunk computes them with `eval` before `stats`:

```tql
from_splunk "https://splunk:8089", index="main", earliest="-1h", latest="now"
kind = action.to_upper()
summarize kind, events=count()
```

The search computes the key with `| eval tenzir_column_0=upper('action')`. An assignment that the summary reads may call a function that SPL spells, and Splunk computes it with its own semantics. An assignment that the summary doesn’t read, including one that a later assignment shadows, must be infallible. See [Computed keys and arguments](../optimizations.md#computed-keys-and-arguments).

A `floor` of a time stays in Tenzir.

## Filters

With `index`, the conjuncts of the filters right after the operator extend the base `search` command where it can spell them, which lets Splunk use its indexes:

* `==` of a field with a string, a number, a boolean, or an IP address, and `<`, `<=`, `>`, and `>=` with a number.
* Comparisons of `_time` with a time, in epoch seconds.
* `in` with a list, which becomes `IN`, and `in` with a subnet, which becomes a CIDR match.
* `!= null`, which becomes `field=*`.
* `starts_with` and `ends_with`, and `"x" in field`, which become wildcards.
* `and` and `or` of such terms.

All other filters become `where` stages. They consist of top-level fields, literals (numbers, strings, booleans, `null`, times compared with `_time`, and IP addresses), comparisons, `in` with a list, arithmetic, `and`, `or`, `not`, and the functions `starts_with`, `ends_with`, `match_regex`, `length_chars`, `to_lower`, `to_upper`, `trim`, and `abs`, without named arguments such as `ignore_case`.

Nested field paths, subnets outside the base search, times compared with fields other than Splunk’s own `_time`, such as `_time` after `select _time=event_time` or after a `search` that runs more than a single `search` command, such as `| rename event* AS _*`, bare boolean fields such as `where flag`, fields whose names start with `__`, which Splunk treats as internal, and optional fields such as `x?` stay in Tenzir.

## Splunk semantics

The operators that Splunk takes over run as Splunk runs them, which can differ from TQL:

* Terms of the base `search` command match strings without regard to case, so `user == "root"` also matches `Root`. A string with `*` becomes a `where` stage instead, so that `*` is no wildcard.
* `where` compares strings exactly. `x != "a"` drops results without `x`, and a comparison with a multivalue field holds if any of its values matches.
* Splunk returns every value as a string. A comparison with an IP address compares the text of the address, such as `198.51.100.24`.
* `stats` drops results whose group key is `null`, puts a result with a multivalue key into the group of each of its values, and counts each value of a multivalue field in `count(field)`. `min` and `max` compare numbers numerically and other values as text.
* A summary value that Splunk leaves out, such as `min` over no values, is missing from the result rather than `null`.
* Counts are integers also with `raw=true`. Other values follow `raw`.
* A `where` stage whose expression fails, outside a search with `stats`, makes Splunk return an empty result without an error.

## Time window

With `index`, comparisons of `_time` in the filters before any summary, limit, or sort also narrow `earliest` and `latest`, rounded outward to whole seconds, when both are absolute. A strict bound excludes its time, so `where _time < 2025-01-01T00:02:00Z` requests `latest_time=1735689720`. A relative bound, such as `-15m`, resolves on the server, so the operator keeps both bounds as they are. It also keeps them when the narrowed bounds would cross, since Splunk rejects crossing bounds. The comparisons stay in the search in every case. With `search`, the bounds never narrow, since a `_time` field in your search’s results may stem from an aggregation or a computation.

## SPL2

The `spl2` argument of [`from_splunk`](../operators/from_splunk.md) runs an SPL2 search. The operator takes over the same operators as for `search`, appended to your search as SPL2 stages, and [Splunk semantics](spl.md#splunk-semantics) apply too. SPL2 spells a few things differently:

* Fields in commands are single-quoted, as in `'user'`.
* `null` is a literal, and `stats` counts with `count()` and `count(if(p, 1, null))`.
* There is no `fields *`. The operator asks Splunk to extract all fields instead, and appends a `fields` stage only to keep the fields that the pipeline reads.
* Comments are `//` and `/* */`, raw strings start with `@"`, and a `;` ends the search so that no stage may follow.

The operator never treats an SPL2 search as plain, because a search may redefine `_time`. Comparisons of `_time` and the operators after them stay in Tenzir, and the bounds `earliest` and `latest` never narrow. The pipeline

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

## Verify an optimization

To see the operators that Splunk takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_splunk "https://splunk.example.com:8089", index="main", earliest="-1h", latest="now", headers={Authorization: secret("splunk-rest-authorization")} | where user == "root" | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`. When Splunk reports an error or a warning, the diagnostic shows the search as the operator sent it, including the appended stages.
