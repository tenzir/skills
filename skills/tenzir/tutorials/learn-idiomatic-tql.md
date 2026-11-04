---
title: "Learn idiomatic TQL"
canonical: https://tenzir.com/docs/tutorials/learn-idiomatic-tql
source: https://tenzir.com/docs/tutorials/learn-idiomatic-tql.md
section: "Docs"
---

# Learn idiomatic TQL

> This tutorial teaches you to write TQL that is clear, efficient, and maintainable. It assumes you already know basic TQL syntax and operators, and shows you how experienced TQL developers approach common patterns.

This tutorial teaches you to write TQL that is clear, efficient, and maintainable. It assumes you already know basic TQL syntax and operators, and shows you how experienced TQL developers approach common patterns.

Understanding TQL First

If you’re new to TQL or want to understand its design philosophy and architecture, read the [TQL language explanation](../explanations/language.md) first. This tutorial focuses on practical patterns, while the explanation covers the conceptual foundations.

## What makes TQL idiomatic?

Idiomatic TQL follows consistent patterns that leverage the language’s strengths:

* **Vertical clarity**: Pipelines flow top-to-bottom for readability
* **Explicit data contracts**: Clear about what data should vs. might exist
* **Domain-aware types**: Uses IP addresses, not strings; durations, not integers
* **Composition over complexity**: Small, focused operators that combine well
* **Performance-conscious**: Filters early, aggregates late

This tutorial shows you these patterns through concrete examples, comparing idiomatic approaches with common pitfalls.

## Pipeline structure

### Vertical vs horizontal: choosing the right style

TQL offers two ways to chain statements: a newline `\n` (vertical) or pipe `|` (horizontal). While both are valid, each has its place.

#### Always use vertical structure in files

✅ Idiomatic vertical structure:

```tql
let $ports = [22, 443]


from_file "/tmp/logs.json"
where port in $ports
select src_ip, dst_ip, bytes
summarize src_ip, total=sum(bytes)
```

Benefits of vertical structure:

* **Readability**: Easy to scan and understand data flow
* **Debugging**: Simple to comment out individual operators
* **Modification**: Easy to insert or remove pipeline stages
* **Version Control**: Clear diffs when pipelines change

#### Use horizontal structure only for command-line

✅ Appropriate for one-liners:

```tql
tenzir 'from_file "logs.json" | where severity == "high" | summarize count()'
```

The horizontal approach is ideal for:

* **Command-line usage**: Quick ad-hoc queries in the terminal
* **API requests**: Single-line strings in JSON payloads
* **Shell scripts**: Embedding TQL in bash scripts
* **Interactive exploration**: Building pipelines in a REPL

#### Never mix styles

❌ Avoid hybrid approaches:

```tql
let $ports = [22, 443]


from_file "/tmp/logs.json"
| where port in $ports
| select src_ip, dst_ip, bytes
| summarize src_ip, total=sum(bytes)
```

This Kusto-like style makes code harder to read and maintain, especially with nested pipelines that increase indentation.

Quick rule

* **In files**: Always use newlines (vertical)

* **On command-line**: Use pipes (horizontal)

* **Never**: Mix both styles

### Trailing commas in vertical structures

When writing vertical structures, use trailing commas consistently to improve maintainability.

#### Lists and records

✅ Vertical structures with trailing commas:

```tql
let $ports = [
  22,
  80,
  443,
  3306,
]


let $config = {
  threshold: 100,
  timeout: 30s,
  enabled: true,
}
```

Benefits:

* Add new items without modifying existing lines
* Reorder items without worrying about comma placement
* Get cleaner diffs in version control
* Avoid syntax errors when adding/removing items

✅ Horizontal structures without trailing commas:

```tql
let $ports = [22, 80, 443, 3306]
let $config = {threshold: 100, timeout: 30s}
```

❌ Never use trailing commas horizontally:

```tql
let $ports = [22, 80, 443, 3306,]  // Wrong!
let $config = {threshold: 100, timeout: 30s,}  // Wrong!
```

❌ No trailing comma after an operator argument sequence:

```tql
from {status: 200, path: "/api"},
     {status: 404, path: "/missing"}  // No comma here
```

```tql
{
  status: 200,
  path: "/api",
}
{
  status: 404,
  path: "/missing",
}
```

Quick rule

Trailing commas are only allowed in contexts with parentheses (‘()’), brackets (‘\[]’), or braces (‘’).

### Line continuation in operator arguments

When writing operators with multiple arguments across lines, you must explicitly signal that the statement continues. This is a common source of errors.

✅ Trailing comma signals continuation:

```tql
select uid,
       src,
       dst
```

✅ Backslash for explicit continuation:

```tql
select \
  uid,
  src,
  dst
```

❌ Invalid - newline ends the statement:

```tql
select
  uid,
  src,
  dst
```

The rule is simple: **a newline after an operator name (with no arguments) ends the statement**. Either put the first argument on the same line (with a trailing comma) or use a backslash to continue.

Quick rule

* First argument on same line with trailing comma: `select uid,`
* Or use backslash: `select \`
* Inside `()`, `[]`, `{}`: newlines don’t end the statement

### Extract bulky arguments before subpipelines

Operators that take a subpipeline often also take record or list arguments. When those arguments span multiple lines, the record braces and subpipeline braces can be hard to distinguish. Move bulky configuration values into `let` bindings so the operator call stays compact and the subpipeline remains visually clear. This pattern is common with [`from_http`](https://tenzir.com/docs/reference/operators/from_http.md), where request records can sit directly before a parsing subpipeline such as [`read_json`](https://tenzir.com/docs/reference/operators/read_json.md).

❌ Hard to scan:

```tql
from_http "https://api.example.com/search",
  headers={
    "Authorization": f"Bearer {secret("API_TOKEN")}",
    "Content-Type": "application/json",
  },
  body={
    query: "severity:high",
    limit: 100,
  } {
  read_json
}
```

✅ Clear separation between configuration and parsing:

```tql
let $headers = {
  "Authorization": f"Bearer {secret("API_TOKEN")}",
  "Content-Type": "application/json",
}
let $body = {
  query: "severity:high",
  limit: 100,
}


from_http "https://api.example.com/search", headers=$headers, body=$body {
  read_json
}
```

Use this pattern for readability, even when you don’t reuse the value. Keep short scalar arguments inline, but extract multi-line records or lists when they would otherwise sit directly before `{ ... }`.

## Expression style

### Avoid unnecessary parentheses

TQL’s `if` and `where` don’t require parentheses around conditions. Adding them creates visual noise without any benefit.

✅ Clean:

```tql
if @name == "suricata.dns" {
  // ...
}


where severity == "critical"
```

❌ Noisy:

```tql
if (@name == "suricata.dns") {
  // ...
}


where (severity == "critical")
```

Use parentheses only when they clarify precedence in complex expressions:

```tql
where (a > 1 and b < 2) or c == 3
```

### Use format strings for string composition

Use format strings (f-strings) when embedding values in a larger string. They keep separators, literals, and conversions in one template.

✅ Readable string composition:

```tql
message = f"{status} - {ratio * 100}%"
endpoint = f"{host}:{port}"
```

F-strings also work with secrets. When a format string contains a secret, the result is a secret:

```tql
let $headers = {
  "Authorization": f"Bearer {secret("API_TOKEN")}",
}
```

❌ Avoid building formatted strings with `+`:

```tql
message = status.string() + " - " + (ratio * 100).string() + "%"
endpoint = string(host) + ":" + port.string()
```

### Use inline ternary for simple binary choices

TQL supports `value if condition else other` as an inline expression. Use it when a field takes exactly one of two values based on a single boolean.

✅ Clean and self-documenting:

```tql
connection = {
  direction: 2 if initiated else 1,   // Outbound / Inbound
  protocol_ver: 6 if is_ipv6 else 4,  // IPv6 / IPv4
  status: 1 if success else 2,        // Success / Failure
}
```

❌ Unnecessarily verbose for a binary choice:

```tql
connection = {
  direction: 1,  // default
  ...
}
if initiated {
  connection.direction = 2
}
```

When the source field is only needed as the condition and not used elsewhere, wrap a `move` in parentheses to consume and test it in a single expression - no separate `drop` required:

```tql
connection_info = {
  direction_id: 2 if (move raw.initiated) else 1,
  protocol_ver_id: 6 if (move raw.is_ipv6) else 4,
}
// raw.initiated and raw.is_ipv6 are already consumed  -  no drop needed
```

The ternary form is appropriate *only for genuinely binary choices*. The moment you need a third branch, switch to `match` for branch pipelines or a [record constant lookup](learn-idiomatic-tql.md#use-record-constants-for-value-mappings) for pure value mappings:

```tql
// Three or more enum-like outcomes → record constant
let $protocols = { tcp: 6, udp: 17, icmp: 1 }
protocol_num = $protocols[proto]? else 255
```

### Use match for finite case branching

Use `match` when you route events by comparing one value against a finite set of cases. This keeps dispatching logic close to the field it depends on, and the final `_` arm makes the fallback explicit.

✅ Select different transformations for different event kinds:

```tql
from {kind: "process", command: "whoami"},
     {kind: "file", path: "/etc/hosts"},
     {kind: "other", description: "Session started"}
match kind {
  "process" => {
    process = {cmd_line: move command}
  }
  "file" => {
    file = {path: move path}
  }
  _ => {
    message = move description?
  }
}
```

```tql
{
  kind: "process",
  process: {cmd_line: "whoami"},
}
{
  kind: "file",
  file: {path: "/etc/hosts"},
}
{
  kind: "other",
  message: "Session started",
}
```

Each branch consumes different source fields and builds a different object. The source discriminator `kind` remains available to downstream consumers. For repetitive mappings from exact string keys to constant values, prefer a [record lookup](learn-idiomatic-tql.md#use-record-constants-for-value-mappings). A short `match` can still make the recognized cases and fallback clearer. Keep `match` for ranges, guards, and composite patterns, even when the result is a label.

Match arms should describe values or ranges of the expression after `match`. Use a [guard](../reference/statements.md#guards) when the case also depends on another field, and let one guard cover every pattern it applies to instead of repeating an `if` in each arm:

```tql
from {status: 503, retries: 1},
     {status: 503, retries: 0},
     {status: 429, retries: 1},
     {status: 429, retries: 0},
     {status: 404, retries: 0}
match status {
  499..600 | 429 if retries > 0 => {
    action = "retry"
  }
  499..600 => {
    action = "page"
  }
  429 => {
    action = "throttle"
  }
  _ => {
    action = "ignore"
  }
}
```

```tql
{
  status: 503,
  retries: 1,
  action: "retry",
}
{
  status: 503,
  retries: 0,
  action: "page",
}
{
  status: 429,
  retries: 1,
  action: "retry",
}
{
  status: 429,
  retries: 0,
  action: "throttle",
}
{
  status: 404,
  retries: 0,
  action: "ignore",
}
```

TQL range patterns exclude both endpoints. The pattern `499..600` therefore matches numeric values greater than `499` and less than `600`. For integer HTTP status codes, `199..300` covers `200` through `299`, `399..500` covers `400` through `499`, and `499..600` covers `500` through `599`.

A guard belongs to an arm that still matches on a value. Once the pattern is a wildcard, the guard carries the whole decision and `match` degenerates into an `if` ladder.

❌ Wildcard guards:

```tql
match event_code {
  _ if event_code.starts_with("user.") => {
    category = "user"
  }
  _ if event_code.starts_with("group.") => {
    category = "group"
  }
  _ => {
    category = "unknown"
  }
}
```

Reach for `if` and `else if` when the branches depend on predicates such as `search`, `starts_with`, regular-expression matches, field presence, or a combination of fields.

✅ Predicate ladder:

```tql
if event_code.starts_with("user.") {
  category = "user"
} else if event_code.starts_with("group.") {
  category = "group"
} else {
  category = "unknown"
}
```

If the source value has a documented structure, extract its categorical part and match that value instead. This short dispatch makes the recognized categories and the fallback explicit. Match the runtime expression directly, because `let` only binds constants.

✅ Match on the extracted category:

```tql
match event_code.split(".")[0] {
  "user" => {
    category = "user"
  }
  "group" => {
    category = "group"
  }
  _ => {
    category = "unknown"
  }
}
```

When several fields form a category, a `match` expression can be a list. This expresses composite patterns directly without constructing string keys:

```tql
match [src_role, dst_role] {
  ["lan", "wan"] => {
    direction = "outbound"
  }
  ["wan", "lan"] => {
    direction = "inbound"
  }
  _ => {
    direction = "unknown"
  }
}
```

List patterns compare element by element, so a `null` in either field falls through to `_`.

Keep `if` for predicates and binary control flow that select different work. Don’t introduce a branch merely because a field might be null. Our section on [streamlining transformations](learn-idiomatic-tql.md#streamline-transformations-instead-of-branching) shows how optional access, fallbacks, and lookups replace those guards.

### Use `in` for multi-value membership tests

When a condition checks whether a field matches one of several values, `in` with a list is cleaner than a chain of `or` comparisons. This works anywhere you write a condition, such as `where` or `if`.

✅ Idiomatic:

```tql
if event_code in ["4624", "4625", "4648"] {
  // ...
}
```

When the list grows, move it to a named constant:

```tql
let $logon_eids = ["4624", "4625", "4648"]
if event_code in $logon_eids {
  // ...
}
```

❌ Verbose:

```tql
if event_code == "4624" or event_code == "4625" or event_code == "4648" {
  // ...
}
```

### Prefer spread when combining records and lists

Use the spread operator `...` when you build a record or list from other records or lists. Spread keeps the resulting shape visible where you construct it, and lets you mix existing fragments with literals or computed fields.

✅ Clear construction:

```tql
from {
  defaults: {host: "localhost", port: 80},
  overrides: {port: 443},
  base_tags: ["prod"],
  extra_tags: ["api"],
}


service = {
  ...defaults,
  ...overrides,
  tls: true,
}
tags = [
  ...base_tags,
  "monitored",
  ...extra_tags,
]
```

```tql
{
  defaults: {host: "localhost", port: 80},
  overrides: {port: 443},
  base_tags: ["prod"],
  extra_tags: ["api"],
  service: {host: "localhost", port: 443, tls: true},
  tags: ["prod", "monitored", "api"]
}
```

For records, later fields overwrite earlier fields. Put defaults first and overrides last.

❌ Nested function calls hide the target shape:

```tql
from {
  defaults: {host: "localhost", port: 80},
  overrides: {port: 443},
  base_tags: ["prod"],
  extra_tags: ["api"],
}


service = merge(merge(defaults, overrides), {tls: true})
tags = concatenate(concatenate(base_tags, ["monitored"]), extra_tags)
```

```tql
{
  defaults: {host: "localhost", port: 80},
  overrides: {port: 443},
  base_tags: ["prod"],
  extra_tags: ["api"],
  service: {host: "localhost", port: 443, tls: true},
  tags: ["prod", "monitored", "api"]
}
```

When a fragment may be missing, use optional access such as `...profile?` or `...custom_tags?`.

Keep [`merge`](https://tenzir.com/docs/reference/functions/merge.md) and [`concatenate`](https://tenzir.com/docs/reference/functions/concatenate.md) in mind when you read existing code or need an explicit two-argument function. For new transformations, prefer spread when you are constructing the resulting record or list.

## Streamline transformations instead of branching

Start with the record you want to produce, not a list of conditions under which you might assign each field. A field whose value is `null` is usually a useful representation of missing information. It does not need its own branch.

Statement-level branches can add routing and execution overhead, and repeated guards make the transformation harder to inspect. Prefer direct expressions when they express the same contract. This is not a rule to remove every condition: keep branches that select different work or protect a real precondition. Measure representative pipelines before claiming a speedup.

Use this order when choosing a construct:

| Need                                         | Prefer                                            |
| -------------------------------------------- | ------------------------------------------------- |
| Copy or convert an optional value            | Optional access and a null-propagating expression |
| Pick the first non-null value                | An `else` fallback chain                          |
| Choose between two values                    | One inline `if … else` expression                 |
| Map a finite key to values                   | A constant record or list lookup                  |
| Execute different pipelines for finite cases | A `match` statement                               |
| Gate work on a predicate                     | An `if` statement                                 |

### Build records with nullable fields

Suppose a source record can contain a hostname, a user ID, and a session ID. Don’t turn each optional field into a separate control-flow decision.

❌ A branch for every field:

```tql
normalized = {}
if raw.host? != null {
  normalized.device.hostname = move raw.host
}
if raw.user_id? != null {
  normalized.user.uid = move raw.user_id
}
if raw.session_id? != null {
  normalized.session_uid = move raw.session_id
}
```

✅ One record that shows the target shape:

```tql
normalized = {
  device: {hostname: move raw.host?},
  user: {uid: move raw.user_id?},
  session_uid: move raw.session_id?,
}
```

The streamlined version deliberately retains null fields. A user record with a null UID is not the same shape as an absent user record. Use this form when that distinction does not matter to the consumer; keep a presence guard when the existence of the object itself carries meaning.

### Let conversions propagate null

A null check before a null-propagating function repeats the function’s work. For example, [`time`](https://tenzir.com/docs/reference/functions/time.md) and [`to_lower`](https://tenzir.com/docs/reference/functions/to_lower.md) accept null input and return null.

❌ Guarded assignments with explicit null defaults:

```tql
first_seen = null
if raw.first_seen? != null {
  first_seen = time(move raw.first_seen)
}
tool_name = null
if raw.tool?.name? != null {
  tool_name = raw.tool.name.to_lower()
}
```

✅ Direct conversions:

```tql
first_seen = time(move raw.first_seen?)
tool_name = raw.tool?.name?.to_lower()
```

The conversion already handles null, so neither a statement-level guard nor an inline conditional is needed.

Optional access permits absence, not malformed values. An invalid non-null timestamp still produces a warning. With `move`, the original value is consumed even when conversion fails. Omit `move` if you need to retain that value for investigation or preserve it under `unmapped`.

Keep required fields non-optional. Check or test a function’s null behavior before applying this pattern; not every function reference documents it.

### Use fallbacks instead of presence ladders

When several fields can supply the same value, express their priority with `else`.

❌ Repeating the assignment for each candidate:

```tql
if raw.file_path? != null {
  path = raw.file_path
} else if raw.path? != null {
  path = raw.path
} else if raw.target_file? != null {
  path = raw.target_file
} else {
  path = null
}
```

✅ Read the preference order from left to right:

```tql
path = raw.file_path? else raw.path? else raw.target_file?
```

If every candidate is absent or null, the result is null. Don’t add `else ""` unless an empty string is actually the desired result. The fallback operator does not treat `""`, `0`, or `false` as missing. Normalize source-specific placeholders with [`replace`](https://tenzir.com/docs/reference/operators/replace.md) when the source contract calls for it.

### Don’t guard predicates against null

In a predicate position, null is falsy: the event skips the `if` body, taking `else` if present, and fails a `where` filter, without a warning. Only `true` enters the `if` body or passes the filter. Don’t replace null with an empty string merely to call a string predicate.

❌ Checking presence before a null-propagating predicate:

```tql
if raw.reason? != null and (raw.reason? else "").starts_with("policy:") {
  policy_name = raw.reason.split(":")[1]
}
```

✅ Keep the meaningful condition:

```tql
if raw.reason?.starts_with("policy:") {
  policy_name = raw.reason.split(":")[1]
}
```

The same applies to filtering:

```tql
where raw.reason?.starts_with("policy:")
```

That filter intentionally removes events with missing reasons. It is not a replacement for an assignment when you need to retain every event.

### Map nullable lists without special cases

The [`map`](https://tenzir.com/docs/reference/functions/map.md) function returns null for a null input list without evaluating its lambda. An empty list stays empty.

❌ Separate paths for absent, empty, and populated lists:

```tql
related_events = null
if raw.event_ids? != null {
  if raw.event_ids.length() > 0 {
    related_events = raw.event_ids.map(id => {uid: id})
  } else {
    related_events = []
  }
}
```

✅ Express the element transformation once:

```tql
related_events = raw.event_ids?.map(id => {uid: id})
```

Use `raw.event_ids?.map(id => {uid: id}) else []` only if the consumer requires an empty list rather than null. When constructing a list with spread, no fallback is needed: spreading null contributes no elements.

```tql
related_events = [
  ...raw.event_ids?.map(id => {uid: id}),
  ...raw.parent_ids?.map(id => {uid: id}),
]
```

Here the result is an empty list if both source lists are absent.

### Classify once and look up the presentation

Don’t repeat the same outcome conditions to produce a status, a label, and a message. Map related values together, or compute one outcome key in the branch that already decides the event’s meaning.

❌ Parallel conditional chains that can drift apart:

```tql
status_id = 1 if outcome == "success" else 2 if outcome == "denied" else 0
label = "completed" if outcome == "success" else "blocked" if outcome == "denied" else "pending"
message = f"Tool {tool} completed" if outcome == "success" else
          f"Tool {tool} blocked" if outcome == "denied" else
          f"Tool {tool} pending"
```

✅ One lookup, then one format string:

```tql
let $outcomes = {
  success: {status_id: 1, label: "completed"},
  denied: {status_id: 2, label: "blocked"},
}


result = $outcomes[outcome]? else {status_id: 0, label: "pending"}
status_id = result.status_id
label = result.label
message = f"Tool {tool} {result.label}"
drop result
```

This also works when the key comes from a necessary branch: assign a key such as `"approved"`, `"rejected"`, or `"inferred"` there, then look up the wording. Don’t reconstruct the decision from several status fields downstream.

Keep static mappings in `let` bindings. A runtime record evaluates every field; selecting one field does not make the others lazy. For example, this emits a division-by-zero warning even though the selected field is `fallback`:

```tql
from {total: 0, key: "fallback"}
result = {ratio: 1 / total, fallback: 0}[key]
```

Look up static fragments and format once, or use `match` when the alternatives perform different work.

### Don’t branch just to tidy the output

After moving fields, a source record can be empty or contain only nulls. That is not, by itself, a reason to add another branch to every event.

❌ Cleanup after every transfer:

```tql
agent_name = move raw.agent.name
if raw.agent.skill_id? == null {
  drop raw.agent
}
if raw.action?.is_empty() {
  drop raw.action
}
```

✅ Move what you map and retain the rest:

```tql
agent_name = move raw.agent.name
```

The first version can lose data: a null skill ID says nothing about other attributes in `raw.agent`. Preserve those attributes for downstream consumers or under `unmapped`. Empty records and null fields can remain in the pipeline.

If a destination requires null fields to be omitted, use [`drop_null_fields`](https://tenzir.com/docs/reference/operators/drop_null_fields.md) at that boundary rather than individual presence checks throughout the mapping. It removes null fields, not empty records. Don’t add cleanup merely to make an intermediate event look shorter.

### Keep conditions that protect meaning or validity

Streamlined TQL still needs conditions. Keep them when they do one of the following:

* Choose different parsers, event classes, enrichments, or destinations.
* Prevent an invalid operation, such as division by zero.
* Avoid an external request or other expensive work for inapplicable events.
* Distinguish an absent entity from an entity with unknown attributes.

For example, this ratio is meaningful only for a positive total:

```tql
ratio = failures / total if total > 0 else null
```

The inline conditional evaluates only the selected branch. At zero, it returns null without attempting division. Unguarded division also returns null at zero, but emits a warning. Keep this guard when a zero total is expected, so the warning channel remains useful for unexpected input.

A missing user ID, by contrast, usually needs only `user.uid = raw.user_id?`. Ask whether a guard protects a semantic distinction or merely avoids writing null. Remove the guard in the latter case.

## Field management

### Use `move` expressions to prevent field duplication

✅ Clean field transfers with move:

```tql
// Moving fields during transformation
normalized.src_ip = move raw.source_address
normalized.dst_port = move raw.destination.port
normalized.severity = move alert.level
```

❌ Avoid copy-then-drop pattern:

```tql
normalized.src_ip = raw.source_address
normalized.dst_port = raw.destination.port
normalized.severity = alert.level
drop raw.source_address, raw.destination.port, alert.level
```

### Be intentional about field preservation

✅ Move fields that are transformed:

```tql
ocsf.activity_id = move http_methods[method]? else 99
```

✅ Drop only static metadata fields:

```tql
drop event_kind  // Same across all events
```

❌ Don’t leave transformed data in original location:

```tql
ocsf.src_ip = original.ip  // Bad: original.ip still exists
```

When normalizing data (e.g., to OCSF format):

* Use `move` for fields being transformed to prevent duplication
* Ensure transformed values don’t appear in both old and new locations
* Only drop fields you’re certain are constant across events
* Verify no critical data ends up in `unmapped` fields
* Treat all input-derived values as dynamic, not constants
* Don’t hardcode field values based on example data

### Use `replace` to normalize placeholder values

When dealing with data that uses placeholder values like `"-"`, `"N/A"`, or empty strings to represent null, use the [`replace`](https://tenzir.com/docs/reference/operators/replace.md) operator to normalize them instead of writing conditional logic.

✅ Clear and composable approach:

```tql
from {content: {field: null}},
     {content: {field: "-"}},
     {content: {field: "value"}}
replace content.field, what="-", with=null
drop_null_fields content
```

```tql
{
  content: {},
}
{
  content: {},
}
{
  content: {
    field: "value",
  },
}
```

❌ Complex conditional logic:

```tql
from {content: {field: null}},
     {content: {field: "-"}},
     {content: {field: "value"}}
if content.has("field") {
  if content.field == "-" or content.field == null {
    drop content.field
  }
}
```

```tql
{
  content: {},
}
{
  content: {},
}
{
  content: {
    field: "value",
  },
}
```

Benefits of using `replace`:

* **Clear intent**: The operator name explicitly states what you’re doing
* **No branching**: Avoid nested conditionals that are hard to follow
* **Composable**: Add `drop_null_fields` if the destination requires omission
* **Maintainable**: Easy to add more placeholder values if needed

Apply placeholder replacement only to fields where the source defines those values as missing. Keep null fields during transformation; add cleanup at the destination only when needed.

✅ Handling multiple placeholders for a source whose `user` and `referrer` fields use them to mean missing:

```tql
replace raw.user, raw.referrer, what="-", with=null
replace raw.user, raw.referrer, what="N/A", with=null
replace raw.user, raw.referrer, what="", with=null
```

The selected placeholders become null. Other fields keep their values, including empty strings.

Operator vs. function

Don’t confuse the [`replace`](https://tenzir.com/docs/reference/operators/replace.md) operator with the [`replace`](https://tenzir.com/docs/reference/functions/replace.md) function:

* **Operator**: Replaces entire values in the selected fields, or across the event if no fields are specified.
* **Function**: Replaces substrings within a string (e.g., `"hello".replace("l", "r")` → `"herro"`)

### Use meaningful names for computed fields

✅ Clear intent:

```tql
summarize \
  src_ip,
  total_traffic=sum(bytes),
  avg_response=mean(response_time),
  error_rate=count(status >= 400) / count()
```

❌ Unclear:

```tql
summarize src_ip, sum(bytes), mean(response_time)
```

## Type awareness

### Leverage TQL’s domain-specific types

✅ Use native types:

```tql
let $timestamp = now()
let $weekend = $timestamp.day_of_week() in ["Saturday", "Sunday"]


where src_ip in 10.0.0.0/8
where duration > 5min
```

⚠️ Less expressive and error-prone:

```tql
let $timestamp = now()
let $weekend = $timestamp_day in [0, 6]  // What do 0 and 6 mean?


where src_ip.string().starts_with("10.")
where duration_ms > 300000
```

### Use method chaining for time conversions

When converting numeric values to timestamps or durations, prefer method chaining over multiplication with duration units.

✅ Idiomatic method chaining:

```tql
// Convert Unix epoch seconds to timestamp
timestamp = epoch_secs.seconds().from_epoch()


// Convert to duration
timeout = timeout_secs.seconds()


// Chain multiple conversions
duration_ms = (end_time - start_time).milliseconds()
```

❌ Less readable multiplication:

```tql
// Multiplication obscures intent
timestamp = from_epoch(epoch_secs * 1s)


// What unit is this? Seconds? Milliseconds?
timeout = timeout_value * 1s


// Hard to parse at a glance
duration_ms = count_milliseconds(from_epoch(end * 1s) - from_epoch(start * 1s))
```

Method chaining reads naturally left-to-right: “take epoch seconds, interpret as seconds, convert from epoch.” The multiplication style requires understanding that `* 1s` converts a number to a duration, which is less intuitive.

## Performance considerations

### Place filters early in pipelines

✅ Filter first, reduce data volume:

```tql
from_file "large_dataset.json"
where severity == "critical"     // Reduce early
where timestamp > now() - 1h     // Further reduction
select relevant_fields           // Drop unnecessary data
summarize ...                    // Aggregate reduced dataset
```

❌ Process everything, then filter:

```tql
from_file "large_dataset.json"
select all_fields
summarize ...
where result > threshold        // Filter after expensive operation
```

### Put the stream clock outside keyed aggregations

When you aggregate keys inside event-time windows, put [`window`](https://tenzir.com/docs/reference/operators/window.md) outside [`group`](https://tenzir.com/docs/reference/operators/group.md) if one stream-wide event-time clock should close all buckets. This keeps sparse keys from holding their own windows open until another event for the same key arrives, `idle_timeout` fires, or the input ends.

✅ Prefer a single window clock for stream-wide detections:

```tql
from {ts: 2024-01-01T10:00:00, user: "alice"},
     {ts: 2024-01-01T10:01:00, user: "alice"},
     {ts: 2024-01-01T10:02:00, user: "bob"}
window size=5min, on=ts {
  group user {
    summarize failures=count()
    user = $group
    start = $window.start
  }
}
```

❌ Avoid independent clocks unless each key should advance on its own:

```tql
from {ts: 2024-01-01T10:00:00, user: "alice"},
     {ts: 2024-01-01T10:01:00, user: "alice"},
     {ts: 2024-01-01T10:02:00, user: "bob"}
group user {
  window size=5min, on=ts {
    summarize failures=count()
    user = $group
    start = $window.start
  }
}
```

Use [`group`](https://tenzir.com/docs/reference/operators/group.md) around [`window`](https://tenzir.com/docs/reference/operators/window.md) only when each key needs an independent event-time clock or independent trailing history. For fixed windows that share one stream clock, put [`window`](https://tenzir.com/docs/reference/operators/window.md) outside [`group`](https://tenzir.com/docs/reference/operators/group.md) so state closes more predictably.

## Composition patterns

### Use constants for reusable values

✅ Maintainable and self-documenting:

```tql
let $internal_net = 10.0.0.0/8
let $critical_ports = [22, 3389, 5432]  // SSH, RDP, PostgreSQL
let $high_risk_threshold = 0.8


where src_ip in $internal_net
where dst_port in $critical_ports
where risk_score > $high_risk_threshold
```

❌ Magic numbers scattered throughout:

```tql
where src_ip in 10.0.0.0/8
where dst_port in [22, 3389, 5432]
where risk_score > 0.8          // What does 0.8 mean?
```

## Record constants and mappings

### Use record constants for value mappings

✅ Clean record-based mappings with else fallback:

```tql
let $http_methods = {
  CONNECT: 1,
  DELETE: 2,
  GET: 3,
  HEAD: 4,
  OPTIONS: 5,
  POST: 6,
  PUT: 7,
  TRACE: 8,
  PATCH: 9,
}


let $activity_names = [
  "Unknown",
  "Connect",
  "Delete",
  "Get",
  "Head",
  "Options",
  "Post",
  "Put",
  "Trace",
  "Patch",
]


let $dispositions = {
  OBSERVED: {id: 15, name: "Detected"},
  LOGGED: {id: 17, name: "Logged"},
  ALLOWED: {id: 1, name: "Allowed"},
  BLOCKED: {id: 2, name: "Blocked"},
  DENIED: {id: 2, name: "Blocked"},
}


// Use record indexing with else for fallback values
activity_id = $http_methods[method]? else 99
activity_name = $activity_names[activity_id]? else "Other"
disposition = $dispositions[action]? else {id: 0, name: "Unknown"}
```

❌ Complex if-else chains:

```tql
// Hard to maintain and extend
if method == "GET" {
  activity_id = 3
} else if method == "POST" {
  activity_id = 6
} else if method == "PUT" {
  activity_id = 7
} else if method == "DELETE" {
  activity_id = 2
} else {
  activity_id = 99
}


// Error-prone string building
if activity_id == 1 {
  activity_name = "Connect"
} else if activity_id == 2 {
  activity_name = "Delete"
} else if activity_id == 3 {
  activity_name = "Get"
} // ... many more conditions
```

❌ Inline nested if-else expressions are especially problematic:

```tql
// TERRIBLE: Unreadable chain of inline conditionals
activity_id = 3 if method == "GET" else 6 if method == "POST" else 7 if method == "PUT" else 2 if method == "DELETE" else 99


// AWFUL: Complex nested logic impossible to follow
severity_level = "critical" if score > 90 else "high" if score > 70 else "medium" if score > 50 else "low" if score > 30 else "info"


// UNMAINTAINABLE: Mixed logic with nested conditions
result = "blocked" if is_malicious else "allowed" if is_trusted else "quarantine" if risk > 0.8 else "review" if risk > 0.5 else "log"
```

When you see an `if`/`else if` ladder over one field, first ask whether it maps values or selects different work. Prefer a record constant for repetitive value mappings, including mappings that produce several related fields. Use `match` for different pipelines, or when a small set of explicit cases reads more clearly. The goal is to remove redundant decisions, not every branch.

Nested inline chains are a serious anti-pattern because:

* **Unreadable**: Eyes can’t parse the logic flow easily
* **Error-prone**: Easy to mix up conditions and values
* **Unmaintainable**: Adding/removing conditions requires rewriting the entire expression
* **Hard to inspect**: You can’t see each case as a separate branch
* **Wrong abstraction**: Static value lookups belong in records, and branch pipelines belong in `match`

✅ Use record constants for pure value lookup:

```tql
// Clean, maintainable lookups with record indexing
activity_id = $http_methods[method]? else 99
activity_name = $activity_names[activity_id]? else "Other"
disposition = $dispositions[action]? else {id: 0, name: "Unknown"}
```

The `else` keyword provides a fallback value when its left operand is null, including these cases:

* A field doesn’t exist (`field? else default`)
* An array index is out of bounds (`array[index]? else default`)
* A record key doesn’t exist (`record[key]? else default`)

This pattern is particularly powerful for:

* Normalizing data to standard formats (like OCSF)
* Mapping between different naming conventions
* Providing sensible defaults for missing data
* Creating reusable transformation logic

For branches that consume different source fields or run different operators, use [finite case branching](learn-idiomatic-tql.md#use-match-for-finite-case-branching) instead.

## Writing comments

Good comments explain the reasoning, business logic, or non-obvious decisions behind code. The code itself should show what it does; comments should explain why it does it.

❌ Bad; explains what (redundant):

```tql
// Increment counter by 1
set counter = counter + 1
```

✅ Good; Explains why:

```tql
/*
 * Binary field curves are deprecated due to:
 * 1. Weak reduction polynomials in some cases
 * 2. Complex implementation leading to side-channel vulnerabilities
 * 3. Patent concerns that historically limited adoption
 * 4. Generally slower performance compared to prime field curves
 * 5. Less scrutiny from cryptographic community
 * RFC 8422 deprecates these for TLS 1.3.
 */
let $weak_prime_curves = [
  "secp160k1", // 160-bit curves
  "secp160r1",
  "secp160r2",
  "secp192k1", // 192-bit curves
  "secp224k1", // 224-bit curves
  "secp224r1", // NIST P-224
]
```

Why you should comment your code

Don’t be skimpy with your comments - here’s why:

* **Prevent “improvements” that break things**: Future developers won’t accidentally “fix” your intentional design choices.
* **Save investigation time**: Document your research so others don’t repeat the same Stack Overflow searches.
* **Explain business constraints**: Code reviews can’t capture why you chose the “worse” technical solution for valid business reasons.
* **Help your future self**: You’ll forget your own reasoning faster than you think.
* **Speed up onboarding**: New team members understand decisions instead of guessing at intent.

Remember: well-named fields and clear structure communicate *what* your code does - comments explain *why* you chose to do it that way.

## Data quality

TQL’s diagnostic system helps you maintain data quality by distinguishing between expected variations and genuine problems. Understanding how to work with warnings intentionally is key to building robust pipelines.

In TQL, warnings are not annoyances to suppress - they’re signals about your data’s health. The language provides tools to express your expectations clearly:

* **No `?`**: Field should exist; warning indicates a problem
* **With `?`**: Field naturally varies; absence is normal
* **`assert`**: Enforce invariants with warnings
* **`strict`**: Escalate warnings to errors when quality matters

### Be deliberate about optional field access

The `?` operator controls whether missing fields trigger warnings. Use it to express your data contract clearly.

✅ Clear data expectations in transformations:

```tql
// Required field - warning if missing
result = {id: event_id, severity: severity}


// Optional field - no warning if missing
result = {id: event_id, customer: customer_id?}
```

✅ Express expectations in selections:

```tql
// Required field - warning if missing
select event_id, timestamp


// Mix required and optional fields
select event_id, customer_id?
```

❌ Suppressing warnings on required fields:

```tql
// Bad: This hides data quality problems
select event_id?  // Should warn if missing!
```

Tip

The `?` operator expresses your data contract. Use it to distinguish between “this field should exist” and “this field naturally varies.”

### Enforce invariants with `assert`

Use `assert` when specific conditions must be true for your pipeline to work correctly. Unlike `where`, which silently filters, `assert` emits warnings when invariants are violated.

✅ Use `assert` for data quality checks:

```tql
// Ensure critical field has valid values
assert severity in ["low", "medium", "high", "critical"]


// Verify schema expectations
subscribe "ocsf"
assert @name == "ocsf.network_activity"  // Wrong event type = warning
```

✅ Combine `assert` with filtering:

```tql
// First assert invariant (with warning)
assert src_ip != null


// Then filter normally (silent)
where src_ip.is_private()
```

❌ Don’t use `assert` for normal filtering:

```tql
// Wrong: This creates unnecessary warnings
assert severity == "critical"


// Right: Use where for filtering
where severity == "critical"
```

Performance

`where` is faster than `assert` due to optimizations like predicate pushdown. Only use `assert` when you specifically want warnings for violated conditions.

### Treat warnings as errors with `strict`

The [`strict`](https://tenzir.com/docs/reference/operators/strict.md) operator escalates all warnings to errors within its scope, stopping the pipeline when data quality issues occur.

✅ Use `strict` for critical data processing:

```tql
// Stop pipeline if any required field is missing
strict {
  select transaction_id  // Warning → Error if missing
}
```

✅ Combine with `assert` for comprehensive checks:

```tql
strict {
  // Assertion becomes fatal if violated
  assert amount > 0


  // Missing field also becomes fatal
  select customer_id
}
```

Quick rule

By default, trust the operator to accurately distinguish between warnings and errors. Only use `strict` when warnings should halt the pipeline, and when data loss is less important than data correctness.

### Choose the right quality control

| Tool         | Use When             | Behavior           |
| ------------ | -------------------- | ------------------ |
| `field`      | Field must exist     | Warning if missing |
| `field?`     | Field is optional    | Silent if missing  |
| `where`      | Filtering data       | Silent filter      |
| `assert`     | Enforcing invariants | Warning + filter   |
| `strict { }` | Zero tolerance       | Warnings → Errors  |

✅ Production pipeline with layered quality control:

```tql
// Constants for validation
let $valid_severities = ["low", "medium", "high", "critical"]
let $required_fields = ["event_id", "timestamp", "source"]


// Strict mode for critical path
strict {
  subscribe "prod"


  // Assertions for data integrity
  assert severity in $valid_severities
  assert timestamp > 2024-01-01


  // Required field access (warnings → errors)
  where event_id != null and source != null


  // Normal processing
  context_enrich "geo", key=source
}


// Optional enrichment (outside strict)
where geo?.country? == "US"  // No warning if geo missing
```

This layered approach ensures critical data meets requirements while allowing flexibility for optional enrichments.

## OCSF mapping best practices

### Work with record-based mappings

✅ Drive dispatching with clear maps:

```tql
let $severities = {
  critical: 5,
  high: 4,
  medium: 3,
  low: 2,
  none: 0,
}
ocsf.severity_id = $severities[source.severity]? else 0
```

❌ Don’t use `if-else` chains for this.

### Use range checks to map status codes

✅ Derive `status_id` from status codes, e.g., HTTP:

```tql
from {http_status: 200},
     {http_status: 302},
     {http_status: 404},
     {http_status: 503},
     {http_status: 100}
match http_status {
  199..400 => {
    ocsf.status_id = 1  // Success
  }
  399..600 => {
    ocsf.status_id = 2  // Failure
  }
  _ => {
    ocsf.status_id = 0  // Unknown
  }
}
```

```tql
{
  http_status: 200,
  ocsf: {
    status_id: 1,
  },
}
{
  http_status: 302,
  ocsf: {
    status_id: 1,
  },
}
{
  http_status: 404,
  ocsf: {
    status_id: 2,
  },
}
{
  http_status: 503,
  ocsf: {
    status_id: 2,
  },
}
{
  http_status: 100,
  ocsf: {
    status_id: 0,
  },
}
```

❌ Don’t use `record` mapping when status codes are partitioned into ranges.

✅ Use `status_detail` for human-readable status messages.

✅ Use `status_code` for the raw status code (as `string`).

### OCSF Profile: Network Proxy

✅ For proxy logs, identify which endpoint is the proxy itself:

* `src_endpoint`: The client machine initiating the request
* `dst_endpoint`: The destination server being accessed
* `proxy_endpoint`: The proxy/gateway infrastructure

### OCSF Profile: Security Control

✅ Set `is_alert` to `true` if the event represents an alert.

### Only add profiles when necessary

OCSF profiles extend the base event class with additional fields. Only declare a profile in `metadata.profiles` when your source data contains fields that:

1. Map naturally to profile-specific OCSF fields
2. Would otherwise end up in `unmapped` without a proper home

✅ Add a profile when you have data for its fields:

```tql
// Source has cloud-specific fields like account_id, region, zone
ocsf.metadata.profiles = ["cloud"]
ocsf.cloud.account.uid = move source.account_id
ocsf.cloud.region = move source.region
```

❌ Don’t add profiles “just in case” or for redundant fields:

```tql
// Wrong: datetime profile adds *_dt variants of time fields,
// but TQL timestamps already serialize as ISO 8601 datetimes
ocsf.metadata.profiles = ["cloud", "datetime"]  // datetime is redundant
ocsf.start_time = source.start.seconds().from_epoch()
ocsf.start_time_dt = ocsf.start_time  // Same value, no benefit
```

The datetime profile is particularly prone to misuse - it adds `time_dt`, `start_time_dt`, and `end_time_dt` fields that duplicate the base timestamp fields. Since TQL’s `time` type already serializes as ISO 8601 datetimes, these `_dt` variants provide no additional value.
