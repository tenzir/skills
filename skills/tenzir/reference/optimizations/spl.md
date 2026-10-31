---
title: "SPL"
canonical: https://tenzir.com/docs/reference/optimizations/spl
source: https://tenzir.com/docs/reference/optimizations/spl.md
section: "Docs"
---

# SPL

> The Splunk source fromsplunk uses the where, select, and head operators that follow it to extend the Splunk Search Processing Language (SPL) search that it sends, so that Splunk returns fewer results and fields. This page describes how the search changes, which filters reach Splunk, and what stays in Tenzir. Our optimizations overview explains how Tenzir optimizes pipelines in general.

The Splunk source [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) uses the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators that follow it to extend the Splunk Search Processing Language (SPL) search that it sends, so that Splunk returns fewer results and fields. This page describes how the search changes, which filters reach Splunk, and what stays in Tenzir. Our [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## How the search changes

The operator extends the search in one of two ways, depending on whether you pass `search` or `index`.

### Searches that you write

With `search`, the operator first prepends the `search` command unless your search begins with `search` or with `|`, as Splunk Web does. Leading whitespace and comments don’t count for this check. It then sends your search as you wrote it and appends up to three stages, each on a new line, in this order:

1. A `search` stage with the [prefilters](spl.md#filters-are-prefilters) of the [`where`](https://tenzir.com/docs/reference/operators/where.md) operators that follow the source.
2. A `fields` stage with the top-level fields that the pipeline reads.
3. A `head` stage with the limit of a [`head`](https://tenzir.com/docs/reference/operators/head.md), if no [`where`](https://tenzir.com/docs/reference/operators/where.md) precedes it.

Without a projection, the `fields` stage is `fields *`, as [Fields](spl.md#fields) explains, so a search that only a [`head`](https://tenzir.com/docs/reference/operators/head.md) follows ends in `| fields *` and `| head N`. For example, the pipeline

```tql
from_splunk "https://splunk.example.com:8089",
  search="index=main sourcetype=linux_secure",
  earliest="-15m",
  latest="now",
  headers={Authorization: secret("splunk-rest-authorization")}
where status >= 500 and user.starts_with("adm")
select _time, user, status
```

sends this search:

```text
search index=main sourcetype=linux_secure
| search status>=500 user="adm*"
| fields status, user, _time
```

The stages apply to the results of your search, so they work with any search that returns results, including one with transforming commands such as `stats`. In that case, the prefilters apply to the statistics rows.

### Searches for indexes

With `index`, Tenzir writes the search itself. The search consists of a `search` command for the indexes, and the prefilters extend this command instead of following in a stage of their own. The `fields` and `head` stages follow as before. For example, the pipeline

```tql
from_splunk "https://splunk.example.com:8089",
  index="main",
  earliest="-1h",
  latest="now",
  headers={Authorization: secret("splunk-rest-authorization")}
where sourcetype == "linux_secure" and user == "root"
select _time, user, src_ip
```

sends this search:

```text
search index="main" sourcetype="linux_secure" user="root"
| fields src_ip, user, _time, sourcetype
```

A list of indexes, such as `index=["main", "web_*"]`, starts the search with `search index IN ("main", "web_*")`.

## Filters are prefilters

Splunk returns every field value as a string, and [`from_splunk`](https://tenzir.com/docs/reference/operators/from_splunk.md) infers numbers, booleans, IP addresses, and timestamps from these strings. The prefilters use the terms of Splunk’s `search` command, which compare values differently from TQL:

* A comparison such as `user="alice"` matches case-insensitively, so it also matches `Alice`.
* A `*` in a value is a wildcard, even in quotes, so `user="a*b"` also matches `axb`.
* A comparison with a number compares numerically when the value looks like a number, so `n>6` matches `"50"` and `"007"`.
* A term such as `action=*` matches every value, including the empty string, but not a missing field.

A pushed predicate therefore only preselects candidates: it keeps every result that the predicate could keep, and possibly more. Tenzir then evaluates every original predicate locally, including those that the operator sent, so that it removes the extra results.

Splunk and Tenzir can still disagree in rare cases. They may parse different strings as numbers, such as values with surrounding whitespace, `inf`, or `NaN`, and they may fold the case of non-ASCII characters differently. In such cases, a prefilter can drop a result that Tenzir alone would keep. If you need different semantics, write the filter in SPL in your `search`.

A predicate splits at `and`: the parts that translate go into the search, and the rest runs only in Tenzir. An `or` goes into the search only if all of its operands translate. For example, `where (n > 6 or user.match_regex("^a")) and user == "alice"` appends a prefilter for `user == "alice"` only.

### Filters that Splunk evaluates

These predicates on top-level fields go into the search:

* Comparisons with `==`, `<`, `<=`, `>`, and `>=` between a field and a number, with the number on either side.
* Equality between a field and a string or a boolean, including a bare boolean field, as in `where flag`.
* Comparisons of `_time` with a [timestamp](spl.md#timestamps).
* Membership with `in` and a list of string, number, or boolean literals.
* `starts_with`, `ends_with`, and substring search with `"needle" in haystack`, including `ignore_case=true` with an ASCII string literal.
* Equality and list membership after `to_lower()` or `to_upper()`, with ASCII string literals.
* Presence checks with `!= null`.
* The boolean operators `and` and `or` of these predicates.

Predicates on `_time` and on fields named like Splunk search modifiers follow [stricter rules](spl.md#filters-that-stay-in-tenzir). The following table shows how the predicates translate:

| TQL predicate              | SPL term                   |
| -------------------------- | -------------------------- |
| `n > 6`                    | `n>6`                      |
| `n == 7`                   | `n=7`                      |
| `user == "alice"`          | `user="alice"`             |
| `flag`                     | `flag=true`                |
| `user in ["alice", "bob"]` | `user IN ("alice", "bob")` |
| `n in [5, 7]`              | `n IN (5, 7)`              |
| `user.starts_with("al")`   | `user="al*"`               |
| `user.ends_with("ce")`     | `user="*ce"`               |
| `"lic" in user`            | `user="*lic*"`             |
| `action != null`           | `action=*`                 |
| `n > 6 or user == "bob"`   | `(n>6 OR user="bob")`      |

The `search` command combines terms separated by spaces with `AND`, so the prefilters of several predicates follow each other on one line.

Numbers go into the search without an exponent, so a floating-point literal that needs one, such as `0.0000001`, stays local. Integer literals from −2^53 through 2^53 are supported. At either endpoint, a strict `<` or `>` becomes `<=` or `>=` in the prefilter, and Tenzir still evaluates the original strict comparison locally.

Field names that aren’t plain identifiers, or that are keywords of the `search` command such as `AND`, `OR`, `NOT`, `IN`, `TERM`, and `CASE`, go into the search in double quotes, as in `"weird field"="x"`. Strings escape `"` and `\` with a backslash.

### Timestamps

Splunk holds `_time` as epoch seconds, so a comparison of `_time` with a timestamp goes into the search as whole seconds, rounded outwards so that the prefilter keeps every candidate:

| TQL predicate                     | SPL term                                |
| --------------------------------- | --------------------------------------- |
| `_time >= 2025-01-01T00:00:30.5Z` | `_time>=1735689630`                     |
| `_time < 2025-01-01T00:00:30.5Z`  | `_time<=1735689631`                     |
| `_time == 2025-01-01T00:00:30.5Z` | `(_time>=1735689630 _time<=1735689631)` |

A `>` becomes `>=`, and a `<` becomes `<=`. Tenzir still evaluates the exact original comparison, so subsecond boundaries and half-open intervals keep their local semantics.

With `index`, Tenzir writes the search, so `_time` always holds Splunk’s event time, and these comparisons always extend the base search. For example, `index="main"` followed by `where _time >= 2025-01-01T00:01:00Z` sends:

```text
search index="main" _time>=1735689660
| fields *
```

With `search`, your search may change `_time`, for example with `eval _time=strftime(_time, "%FT%T.%Q%:z")`, `rename`, or `fields - _time`. The operator therefore pushes comparisons of `_time` with timestamps only if your search doesn’t contain the text `_time` anywhere, not even inside another word, a string, or a comment. Otherwise, these comparisons stay in Tenzir, which compares the `_time` values that it receives. The `!= null` check still becomes `_time=*`.

Splunk holds other fields with timestamps as text, which the `search` command can’t order, so comparisons of these fields with timestamps stay local.

### Filters that stay in Tenzir

Everything else runs only in Tenzir, with the same result. This includes:

* Negation with `not`, inequality with `!=` against a value, and `== null`.
* Ordering comparisons with strings.
* Comparisons of fields other than `_time` with timestamps.
* Comparisons of `_time` with timestamps when your `search` contains the text `_time`, as [Timestamps](spl.md#timestamps) explains.
* Predicates on `_time` other than comparisons with a timestamp and `!= null`, such as string equality, `in` lists, `starts_with`, `ends_with`, substring search, and comparisons with numbers. Splunk holds `_time` as epoch seconds, while Tenzir receives a formatted string.
* Predicates on fields named like Splunk search modifiers, such as `earliest`, `latest`, `starttime`, `hosttag`, or `savedsearch`, since `name=value` would act as a modifier instead of a comparison. The names compare case-insensitively, so `Latest` counts as well. A `fields` stage still names these fields.
* Regular expressions, IP address comparisons, and subnet membership.
* Recursive string search with the `search` function.
* Case-insensitive string matching with non-ASCII literals.
* Arithmetic, comparisons between two fields, and function calls outside the supported patterns.
* Nested field paths, such as `obj.k`. Splunk field names are flat, so use `this["obj.k"]` to refer to a field named `obj.k`.
* Field names that contain `*`, `"`, `\`, or control characters, and string literals with control characters.
* Integer literals beyond ±2^53 and floating-point literals that need an exponent.

Prefilters that would make the appended text exceed 16 KiB also stay local.

## Fields

Splunk’s export endpoint returns only the fields that a search references, plus default fields such as `_raw`, `_time`, `host`, `source`, `sourcetype`, `index`, `splunk_server`, and `linecount`. A plain search such as `index=main` would thus return few of the fields that Splunk extracts. When no [projection](spl.md#projections) names the fields that the pipeline needs, the operator therefore appends `fields *`, so that every result carries all of its fields, including those that only a local predicate reads.

The `fields *` stage can’t bring back fields that an earlier command removed, such as `fields - user`, and has no effect after a transforming command such as `stats` or `table`, whose results already consist of the fields that the command produces.

## Projections

The `fields` stage keeps the top-level fields that [`select`](https://tenzir.com/docs/reference/operators/select.md) and later operators read, plus every field that a predicate reads, since Tenzir evaluates the predicates on the results. A selected nested field, such as `src.ip`, keeps its top-level field `src`. Splunk’s `fields` command keeps internal fields such as `_raw` and `_time` in the results, and the local [`select`](https://tenzir.com/docs/reference/operators/select.md) removes them. When the pipeline reads the whole event, such as with `this`, the operator appends `fields *` instead.

## Limits

A [`head`](https://tenzir.com/docs/reference/operators/head.md) becomes a `head` stage only if no [`where`](https://tenzir.com/docs/reference/operators/where.md) precedes it. Since every predicate runs locally after the search, a `head` stage would otherwise cut off results before Tenzir filters them. Tenzir enforces the limit locally in every case, and the operator stops reading results once it reaches the limit.

A search that contains a command with side effects never gets a `head` stage, since the stage could stop the command early. These commands are `collect`, `dbxoutput`, `delete`, `map`, `mcollect`, `meventcollect`, `outputcsv`, `outputlookup`, `outputtext`, `run`, `script`, `sendalert`, `sendemail`, and `tscollect`. The same holds for a search with a macro in backticks, which can hide such a command. For example, the pipeline

```tql
from_splunk "https://splunk.example.com:8089",
  search="search index=main | outputlookup users.csv",
  earliest="-15m",
  latest="now",
  headers={Authorization: secret("splunk-rest-authorization")}
head 1
select user
```

sends this search, without a `head` stage:

```text
search index=main | outputlookup users.csv
| fields user
```

The search can still end early. Once the [`head`](https://tenzir.com/docs/reference/operators/head.md) has enough events, or another operator ends the pipeline, the operator closes the export request, which may end the Splunk search, including its side effects. Don’t follow a search with side effects by [`head`](https://tenzir.com/docs/reference/operators/head.md) if the side effects must complete.

With `index`, the operator writes the search itself, so a [`head`](https://tenzir.com/docs/reference/operators/head.md) without a preceding [`where`](https://tenzir.com/docs/reference/operators/where.md) always becomes a `head` stage. For example, `index=["main", "web_*"]` followed by `head 1` and `select user` sends:

```text
search index IN ("main", "web_*")
| fields user
| head 1
```

## Time window

The operator never narrows the `earliest` and `latest` window based on a predicate. A `_time` field in your search’s results may stem from an aggregation, a rename, or a computation, so a predicate on it doesn’t reliably refer to the time that the window selects. A comparison of `_time` goes into the search as a [prefilter](spl.md#timestamps) instead. Use `earliest` and `latest` to bound the request.

## Searches that stay unchanged

The operator sends the search unchanged, without any appended stage, if a stage might break the search or not apply to its results. Tenzir then runs every operator locally, and the results carry only the fields that the search references, plus the default fields. This is the case for:

* Searches that the operator can’t tokenize, such as one with an unterminated double-quoted string, single-quoted field name, macro, comment, or subsearch, or with a `]` that closes no subsearch.
* Searches that end in `|`.
* Searches that contain only comments and whitespace. The operator rejects a search that is empty or contains only whitespace.

A single apostrophe counts as an unterminated single-quoted field name, so a search such as `index=main user=O'Brien` stays unchanged. Write `user="O'Brien"` to keep the stages. Words in strings and comments don’t count, so `msg="| outputlookup x"` neither prevents the `head` stage nor leaves the search unchanged.

## Verify an optimization

Print the optimized pipeline to see which hints the source received:

```sh
tenzir --dump-opt-ir 'from_splunk "https://splunk.example.com:8089", index="main", earliest="-1h", latest="now", headers={Authorization: secret("splunk-rest-authorization")} | where user == "root" | head 10'
```

The source shows the predicates as `filter`, the limit as `limit`, and the fields as `projection`, and the [`where`](https://tenzir.com/docs/reference/operators/where.md) that it took over no longer appears. The [compilation output guide](../../guides/troubleshooting/inspect-compilation-output.md) explains the format. The output doesn’t show the appended SPL stages, which follow the rules on this page. When Splunk reports an error or a warning, the diagnostic shows the search as the operator sent it, including the appended stages.
