---
title: "CloudWatch Logs"
canonical: https://tenzir.com/docs/reference/optimizations/cloudwatch
source: https://tenzir.com/docs/reference/optimizations/cloudwatch.md
section: "Docs"
---

# CloudWatch Logs

> The CloudWatch source fromamazoncloudwatch hands CloudWatch Logs the operators that follow it, as far as its request parameters can express them: a filter pattern, a time range, log stream names, and a limit. CloudWatch takes over those operators, which leave the pipeline and run in CloudWatch with CloudWatch’s semantics, and the rest of the pipeline runs in Tenzir. This page describes which operators CloudWatch takes over and how its results can differ from Tenzir’s. Our optimizations overview compares the targets and describes the rules that all sources share.

The CloudWatch source [`from_amazon_cloudwatch`](../operators/from_amazon_cloudwatch.md) hands CloudWatch Logs the operators that follow it, as far as its request parameters can express them: a filter pattern, a time range, log stream names, and a limit. CloudWatch takes over those operators, which leave the pipeline and run in CloudWatch with CloudWatch’s semantics, and the rest of the pipeline runs in Tenzir. This page describes which operators CloudWatch takes over and how its results can differ from Tenzir’s. Our [optimizations overview](../optimizations.md) compares the targets and describes the rules that all sources share.

## When it applies

What CloudWatch takes over depends on the mode:

* **`mode="search"`** (`FilterLogEvents`) takes over filter patterns, time ranges, log stream names, and limits.
* **`mode="replay"`** (`GetLogEvents`) reads a single stream, and takes over time ranges and limits.
* **`mode="live"`** (`StartLiveTail`) never ends, so it takes over filter patterns only.

With `count`, only a [`head`](../operators/head.md) directly after the operator goes to CloudWatch, since `count` limits the events before the operators that follow. With `pushdown=false`, every operator runs in Tenzir with TQL semantics.

## Operators that CloudWatch takes over

CloudWatch takes over the [longest run of operators](../optimizations.md#the-run-of-operators-after-the-source) directly after the source that it can express:

* [`where`](../operators/where.md) with phrases in `message`, which become a filter pattern, as the [filter patterns](cloudwatch.md#filter-patterns) section describes, if you set no `filter`.
* [`where`](../operators/where.md) that compares `timestamp` with a time, which narrows the time range of the request.
* [`where`](../operators/where.md) that compares `log_stream` with up to 100 names of at most 512 characters, which selects those log streams in `mode="search"`, if you set no `stream` or `stream_prefix`.
* [`head`](../operators/head.md), which limits the request in `mode="search"` and `mode="replay"`.

For example, the pipeline

```tql
from_amazon_cloudwatch "/aws/lambda/api", mode="search"
where "ERROR" in message
where not ("healthcheck" in message)
where timestamp >= 2024-01-01
where timestamp < 2024-01-02
head 100
```

sends a `FilterLogEvents` request with these parameters:

```json
{
  "logGroupName": "/aws/lambda/api",
  "startTime": 1704067200000,
  "endTime": 1704153599999,
  "filterPattern": "\"ERROR\" -\"healthcheck\"",
  "limit": 100
}
```

## Summaries

CloudWatch computes no summaries: a [`summarize`](../operators/summarize.md) and everything after it run in Tenzir.

## Filters and functions

CloudWatch takes over filters as filter patterns, time ranges, and log stream names. It computes no functions.

### Filter patterns

A [`where`](../operators/where.md) with `"x" in message` becomes the phrase `"x"` of a filter pattern:

| TQL                                               | Filter pattern |
| ------------------------------------------------- | -------------- |
| `"ERROR" in message`                              | `"ERROR"`      |
| `"a b" in message and "c" in message`             | `"a b" "c"`    |
| `not ("d" in message)`, next to a required phrase | `-"d"`         |
| `"a" in message or "b" in message`                | `?"a" ?"b"`    |

CloudWatch ignores optional phrases next to required or excluded ones, so an `or` of phrases goes to CloudWatch only on its own, and an excluded phrase only next to a required one. Phrases with a quote, a backslash, a control character, or only whitespace, other fields, and other functions, such as `message.starts_with("x")`, run in Tenzir. So does a filter that would make the pattern longer than the 1,024 characters that CloudWatch accepts.

### Time ranges

A comparison of `timestamp` with a time narrows the time range of the request in milliseconds, which CloudWatch’s timestamps have. `mode="search"` includes both ends of the range and `mode="replay"` excludes its end, so the operator converts each comparison exactly: `timestamp > 2024-01-01` starts the range one millisecond later. The comparison then holds exactly through the range, and never widens `start` and `end`. A range without events completes without a request, such as for a strict comparison beyond the range of a time, which no event satisfies.

## CloudWatch semantics

The operators that CloudWatch takes over run as CloudWatch runs them, which can differ from TQL:

* Filter patterns match words and phrases case-sensitively, not arbitrary substrings like TQL’s `in`, so a message with `"ERROR"` inside a longer word may not match `"ERROR" in message`.
* A limit counts the events that CloudWatch returns for the request.
* Live Tail may sample the matching events when they arrive too fast, which the operator reports as a warning.
* A request that CloudWatch rejects fails the pipeline with the error of CloudWatch, as the overview’s [diagnostics](../optimizations.md#diagnostics) describe.

## Verify an optimization

To see which operators CloudWatch takes over in a pipeline, print the optimized pipeline, as the overview’s section on [verifying an optimization](../optimizations.md#verify-an-optimization) shows.
