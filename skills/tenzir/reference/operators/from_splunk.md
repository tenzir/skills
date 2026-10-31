---
title: "from_splunk"
canonical: https://tenzir.com/docs/reference/operators/from_splunk
source: https://tenzir.com/docs/reference/operators/from_splunk.md
section: "Docs"
---

# from_splunk

> Runs a Splunk search and returns its results as events.

Runs a Splunk search and returns its results as events.

```tql
from_splunk url:string, [search=string], [index=string|list<string>],
            earliest=string|time, latest=string|time, headers=record,
            [options=record, tls=record, timeout=duration,
            connection_timeout=duration, max_retry_count=int,
            retry_delay=duration, raw=bool]
```

## Description

The `from_splunk` operator sends one search request to a Splunk Search Head and returns every search result as a Tenzir event. Tenzir initiates the connection to Splunk. Splunk doesn’t need outbound network access to Tenzir.

Pass exactly one of `index` and `search`. With `index`, Tenzir writes the search for the events of one or more indexes, and you filter the events in TQL. With `search`, Tenzir runs your Splunk Search Processing Language (SPL) search. In both cases, the operator adds the work of the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators that follow it to the search, so that Splunk returns fewer results, as [Optimizations](from_splunk.md#optimizations) describes.

For each invocation, the operator sends a form-encoded `POST` request to the Splunk management API endpoint `/services/search/v2/jobs/export`. It requests final JSON results and streams them into the pipeline without buffering the complete response. The export endpoint returns one streamed HTTP response, so the operator doesn’t issue pagination requests.

Splunk `ERROR` and `FATAL` response messages fail the pipeline. The diagnostic includes Splunk’s message and the search as Tenzir sent it, including the stages that Tenzir appended. Splunk `WARN` messages produce Tenzir warnings without discarding valid search results.

### Result fields

The operator preserves the fields inside each Splunk `result` record and assigns the schema name `tenzir.splunk` to the resulting events. It removes Splunk’s `preview`, `offset`, and `lastrow` export-envelope fields.

Splunk’s export endpoint returns only the fields that a search references, plus default fields such as `_raw`, `_time`, `host`, `source`, `sourcetype`, `index`, `splunk_server`, and `linecount`. To return every extracted field, the operator appends `| fields *` to the search. When an operator that follows, such as [`select`](https://tenzir.com/docs/reference/operators/select.md), names the fields that the pipeline needs, the operator appends a `fields` stage with these fields instead.

The appended `fields *` doesn’t bring back fields that an earlier `fields - <field>` command in your search removed. After a transforming command such as `stats` or `table`, it has no effect. Splunk result fields such as `_raw`, `_bkt`, and `_indextime` are available unless the search removes them.

Splunk field names are flat. The operator keeps a name such as `obj.k` or `tags{}` as a single top-level field, so refer to it as `this["obj.k"]` in TQL. The operator doesn’t normalize field names and doesn’t parse the event text in `_raw` into fields.

### Result types

Splunk returns every field value as a string. The operator infers numbers, booleans, IP addresses, subnets, timestamps, and durations from these strings, so that you can compare the values like other typed values, as in `where status >= 500`. Strings that don’t spell one of these types remain strings. Splunk returns multivalue fields as lists, and the operator infers the types of their elements in the same way.

Inference can change how a value reads. For example, the string `"007"` becomes the number `7`. Set [`raw=true`](https://tenzir.com/docs/reference/operators/from_splunk.md#raw--bool-optional) to keep every value as the string that Splunk returns.

Splunk renders `_time` as a string in the search user’s time zone. Tenzir infers a `time` value when the string uses a supported timestamp format. This includes timestamps with `GMT`, `UTC`, `UT`, `Z`, or a numeric UTC offset.

Tenzir currently doesn’t parse named non-zero-offset zones such as `PDT`, `EST`, or `CET`. These abbreviations can be ambiguous, so `_time` remains a string when Splunk returns one of them. Format `_time` with a numeric offset in the search to get a `time` value regardless of the search user’s time zone:

```tql
search=r#"index=main | eval _time=strftime(_time, "%FT%T.%Q%:z")"#
```

For example, Splunk formats a UTC timestamp as `2025-01-01T00:00:00.000+00:00`, which Tenzir infers as a `time` value.

Tenzir sends a comparison of `_time` with a timestamp to Splunk in epoch seconds, which matches Splunk’s own `_time` values. Since a search like this one changes `_time`, the operator keeps such comparisons in Tenzir whenever your `search` contains the text `_time`, so a [`where`](https://tenzir.com/docs/reference/operators/where.md) on `_time` still works after the `eval`.

### `url: string`

The Splunk Search Head management URL. Splunk Enterprise uses port `8089` for the management API by default.

For Splunk Cloud Platform, use `https://<deployment-name>.splunkcloud.com:8089`. Your deployment must permit REST API access from the Tenzir egress IP address. You can configure the search API IP allowlist through the Admin Config Service or ask Splunk Support to open port `8089`. Splunk Cloud Platform free trials don’t provide REST API access. See the [Splunk Cloud Platform REST API requirements](https://help.splunk.com/en-gb/splunk-enterprise/leverage-rest-apis/rest-api-tutorials/9.1/rest-api-tutorials/access-requirements-and-limitations-for-the-splunk-cloud-platform-rest-api).

### `search = string`

The SPL search to run. Use exactly one of `search` and `index`.

The Splunk account must have permission to run the search and read every index that the search accesses.

Write the search as you would type it in Splunk Web, such as `index=main sourcetype=linux_secure`. The REST API requires a search to begin with a command, so Tenzir prepends the `search` command unless your search already begins with `search` or with `|`, as generating commands such as `| makeresults` or `| tstats` do. Leading whitespace and comments don’t count for this check. The search must contain more than whitespace.

The operator appends stages to your search for the operators that follow it, as [Optimizations](from_splunk.md#optimizations) describes. To read events without writing SPL, use `index` and filter the events in TQL.

Use a [raw string](../expressions.md#string) when the search contains quotes:

```tql
search=r#"index=main user="Jane Doe" | eval label="login event""#
```

Use a [format string](../expressions.md#format-strings-f-strings) to include TQL variables in the search. Escape quotes that belong to the resulting SPL search:

```tql
let $index = "main"
let $user = "Jane Doe"


from_splunk "https://splunk-search-head.example.com:8089",
  search=f"index={$index} user=\"{$user}\"",
  earliest="-15m",
  latest="-5m",
  headers={
    Authorization: secret("splunk-rest-authorization"),
  }
```

### `index = string|list<string>`

The Splunk indexes to read. Use exactly one of `search` and `index`.

Tenzir writes the search for you. A single index, such as `index="main"`, becomes the search `search index="main"`. A list, such as `index=["main", "web_*"]`, becomes `search index IN ("main", "web_*")`. Index names can contain the `*` wildcard. Tenzir adds the filters of the [`where`](https://tenzir.com/docs/reference/operators/where.md) operators that follow to this search, so you can filter the events in TQL instead of SPL.

Each index name must be a nonempty string, and a list must contain at least one name. The Splunk account must have permission to read every index.

### `earliest = string|time`

The inclusive lower time boundary for the search. Tenzir sends this value as Splunk’s `earliest_time` form field.

Pass a `time` value for an absolute UTC timestamp. For a string, you can use a UTC timestamp, a UNIX timestamp, or a [Splunk relative time expression](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.2/specify-time-ranges/specify-time-modifiers-in-your-search) such as `-15m` or `@d`.

### `latest = string|time`

The exclusive upper time boundary for the search. Tenzir sends this value as Splunk’s `latest_time` form field. It accepts the same values as `earliest`.

Specify both `earliest` and `latest` for every invocation. This prevents a recurring pipeline from accidentally running an unbounded search.

The operator rejects real-time bounds such as `rt`, `rt-5m`, and `rt@h`.

### `headers = record`

The HTTP headers to send with the request. The record must contain an `Authorization` header.

Store the complete header value as a Tenzir secret:

```tql
headers={
  Authorization: secret("splunk-rest-authorization"),
}
```

Set the secret to one of the authentication values that the Splunk management REST API accepts:

| Authentication              | Complete header value                |
| --------------------------- | ------------------------------------ |
| Splunk authentication token | `Bearer <authentication-token>`      |
| Splunk session key          | `Splunk <session-key>`               |
| HTTP Basic authentication   | `Basic <base64-encoded-credentials>` |

A Splunk HTTP Event Collector (HEC) token authenticates ingestion requests. It doesn’t authenticate search requests to the management REST API. See [Splunk REST API authentication](https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-user-manual/9.0/rest-api-user-manual/basic-concepts-about-the-splunk-platform-rest-api) for details.

### `options = record (optional)`

Additional form parameters for Splunk’s [`search/v2/jobs/export` endpoint](https://help.splunk.com/en/splunk-cloud-platform/leverage-rest-apis/rest-api-reference/10.3.2512/search-endpoints/search-endpoint-descriptions#search-v2-jobs-export). Use a flat record. Tenzir form-encodes each field and includes it in the search request.

Common parameters include:

| Field            | Purpose                                                                               |
| ---------------- | ------------------------------------------------------------------------------------- |
| `namespace`      | Selects the application namespace for macros, lookups, and other knowledge objects.   |
| `index_earliest` | Sets the inclusive lower boundary based on index time.                                |
| `index_latest`   | Sets the exclusive upper boundary based on index time.                                |
| `now`            | Anchors relative time expressions to one absolute time.                               |
| `max_time`       | Limits the Splunk search runtime in seconds. Use a positive value for a finite limit. |
| `enable_lookups` | Enables or disables lookup application.                                               |
| `rf`             | Adds one required field to the search.                                                |

Each option must contain one value. Tenzir rejects list values because the record-based `options` parameter can’t represent repeated form fields. For example, pass `rf: "host"` rather than `rf: ["host", "source"]`.

The `index_earliest` and `index_latest` fields accept the same absolute and relative time expressions as `earliest` and `latest`.

Tenzir owns `search`, `earliest_time`, `latest_time`, `output_mode`, and `preview`. The operator rejects these fields in `options`. It also rejects real-time settings, including `search_mode="realtime"`, `indexedRealtime`, and parameters whose names begin with `rt_`.

### `timeout = duration (optional)`

The timeout for the complete request.

Defaults to `90s`.

### `connection_timeout = duration (optional)`

The timeout for establishing the connection.

Defaults to `5s`.

### `max_retry_count = int (optional)`

The maximum number of retry attempts. Tenzir retries transient transport failures and HTTP `429` and `5xx` responses.

Defaults to `5`.

### `retry_delay = duration (optional)`

The base delay between retry attempts. The operator uses the same retry behavior as [`from_http`](https://tenzir.com/docs/reference/operators/from_http.md): exponential backoff capped at `16 * retry_delay`. A `Retry-After` response header overrides the delay.

Defaults to `1s`.

### `raw = bool (optional)`

Whether to keep every field value as the string that Splunk returns instead of inferring types, as [Result types](from_splunk.md#result-types) describes.

Defaults to `false`. With `raw=true`, filters compare strings, as in `where status == "500"`.

### `tls = record (optional)`

TLS configuration. Provide an empty record (`tls={}`) to enable TLS with defaults or set fields to customize it.

```tql
{
  skip_peer_verification: bool, // skip certificate verification.
  cacert: string,               // CA bundle to verify peers.
  certfile: string,             // client certificate to present.
  keyfile: string,              // private key for the client certificate.
  min_version: string,          // minimum TLS version (`"1.0"`, `"1.1"`, `"1.2"`, "1.3"`).
  ciphers: string,              // OpenSSL cipher list string.
  client_ca: string,            // CA to validate client certificates.
  require_client_cert: bool,    // require clients to present a certificate.
}
```

The `client_ca` and `require_client_cert` options are only valid for operators that accept incoming client connections.

Any value not specified in the record will either be picked up from the configuration or if not configured will not be used by the operator.

See the [Node TLS Setup guide](../../guides/node-setup/configure-tls.md) for more details.

To trust a private certificate authority, set `tls.cacert` to its CA bundle:

```tql
tls={cacert: "/etc/tenzir/splunk-ca.pem"}
```

## Optimizations

The operator adds SPL to the search for the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators that follow it, so that Splunk returns fewer results and fields. With `search`, the operator appends `search`, `fields`, and `head` stages to your search, each on a new line. With `index`, the prefilters extend the search that Tenzir writes. For example, the pipeline in [Filter the events of an index](from_splunk.md#filter-the-events-of-an-index) sends this search:

```text
search index="main" source="tenzir-docs-auth" outcome="fail*"
| fields outcome, src_ip, user, _time, source
```

* **Filters** become prefilters that keep every result that could match. Splunk’s `search` command matches strings case-insensitively and reads `*` as a wildcard, so Tenzir still evaluates every predicate locally. Comparisons of top-level fields with numbers, strings, and booleans, comparisons of `_time` with timestamps unless your `search` contains `_time`, `in` lists, `starts_with`, `ends_with`, substring tests, and `!= null` reach Splunk. Negation, `!=` against a value, `== null`, regular expressions, IP comparisons, nested field paths, and arithmetic stay local, as do other predicates on `_time` and predicates on fields named like search modifiers, such as `earliest` or `latest`.
* **Projections** become a `fields` stage with the fields that the pipeline reads, including those of local predicates. Without a projection, the operator appends `fields *`.
* **Limits** become a `head` stage only if no [`where`](https://tenzir.com/docs/reference/operators/where.md) precedes the [`head`](https://tenzir.com/docs/reference/operators/head.md). Searches with commands that have side effects, such as `outputlookup` or `collect`, or with macros never get a `head` stage. The operator stops reading results once it reaches the limit, which can still end such a search early, as [Limitations](from_splunk.md#limitations) describes.

Splunk and Tenzir can disagree on what parses as a number and on case folding beyond ASCII. In such rare cases, a prefilter can drop a result that Tenzir alone would keep.

The operator never narrows the `earliest` and `latest` window. It sends a search unchanged, without `fields *`, if it can’t tokenize the search, such as one with an unterminated string or a lone apostrophe as in `user=O'Brien`, or if the search ends in `|`. The page on [SPL optimizations](../optimizations/spl.md) describes the rules in detail.

## Examples

### Filter the events of an index

Assume the `main` index in Splunk contains three authentication events under the source `tenzir-docs-auth`:

Events in Splunk

```tql
{_time: 2025-01-01T00:00:00Z, user: "alice", action: "login", src_ip: "192.0.2.10", outcome: "success"}
{_time: 2025-01-01T00:01:00Z, user: "bob", action: "login", src_ip: "198.51.100.24", outcome: "failure"}
{_time: 2025-01-01T00:02:00Z, user: "alice", action: "logout", src_ip: "192.0.2.10", outcome: "success"}
```

Read the failed attempts and select the fields that the pipeline needs:

```tql
from_splunk "https://splunk-search-head.example.com:8089",
  index="main",
  earliest="1735689599",
  latest="1735689780",
  headers={
    Authorization: secret("splunk-rest-authorization"),
  }
where source == "tenzir-docs-auth" and outcome.starts_with("fail")
select _time, user, src_ip, outcome
```

```tql
{_time: 2025-01-01T00:01:00Z, user: "bob", src_ip: 198.51.100.24, outcome: "failure"}
```

The filter reaches Splunk as part of the search, as [Optimizations](from_splunk.md#optimizations) shows, and Tenzir infers the `time` and `ip` values from the strings that Splunk returns. Pass a list, such as `index=["main", "web_*"]`, to read several indexes.

### Run an SPL search

Use `search` to run SPL, such as a statistics search over the same events:

```tql
from_splunk "https://splunk-search-head.example.com:8089",
  search=r#"index=main source="tenzir-docs-auth" | stats count by user"#,
  earliest="1735689599",
  latest="1735689780",
  headers={
    Authorization: secret("splunk-rest-authorization"),
  }
where count > 1
```

```tql
{user: "alice", count: 2}
```

Splunk counts the events, and the filter applies to the statistics rows in Splunk and again in Tenzir. Splunk receives this search:

```text
search index=main source="tenzir-docs-auth" | stats count by user
| search count>1
| fields *
```

### Use Tenzir times as search boundaries

Pass `time` values directly when another part of the pipeline computes the search window. Tenzir serializes them as UTC strings for Splunk:

```tql
let $start = 2026-07-14T08:00:00Z
let $end = 2026-07-14T09:00:00Z


from_splunk "https://splunk-search-head.example.com:8089",
  search="index=main sourcetype=linux_secure",
  earliest=$start,
  latest=$end,
  headers={
    Authorization: secret("splunk-rest-authorization"),
  }
```

### Collect recurring results by index time

Use Splunk index-time bounds to collect events that arrived late. This example runs every five minutes, accepts events with timestamps up to one day old, and uses a five-minute overlap between index-time windows:

```tql
every 5m {
  from_splunk "https://splunk-search-head.example.com:8089",
    search="index=main sourcetype=linux_secure",
    earliest="-24h",
    latest="-5m",
    options={
      now: now().since_epoch().count_seconds().int(),
      index_earliest: "-15m",
      index_latest: "-5m",
      max_time: 60,
    },
    headers={
      Authorization: secret("splunk-rest-authorization"),
    }
}
publish "splunk-results"
```

The `now` parameter gives every relative boundary in one invocation the same anchor, including retries. Adjust the event-time window to the maximum delay that you accept. Overlapping index-time windows can return an event more than once. [Deduplicate events](../../guides/optimize/deduplicate-events.md) by a stable identifier when duplicates aren’t acceptable.

## Limitations

The operator runs one finite export request per invocation. It rejects real-time bounds and search parameters before sending the request. It doesn’t create search jobs, poll search IDs, manage saved searches, schedule requests, persist checkpoints, or deduplicate results. Scheduling and stateful processing belong in the surrounding pipeline.

When the pipeline ends early, for example because a [`head`](https://tenzir.com/docs/reference/operators/head.md) has enough events, the operator closes the export request, which may end the Splunk search before its side effects complete. Don’t follow a search with commands such as `outputlookup` or `collect` by [`head`](https://tenzir.com/docs/reference/operators/head.md) if the side effects must complete.

## See also

* [`every`](https://tenzir.com/docs/reference/operators/every.md)
* [`from_http`](https://tenzir.com/docs/reference/operators/from_http.md)
* [`to_splunk`](https://tenzir.com/docs/reference/operators/to_splunk.md)
* [Splunk](../../integrations/splunk.md)
