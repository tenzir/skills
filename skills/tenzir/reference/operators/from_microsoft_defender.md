---
title: "from_microsoft_defender"
canonical: https://tenzir.com/docs/reference/operators/from_microsoft_defender
source: https://tenzir.com/docs/reference/operators/from_microsoft_defender.md
section: "Docs"
---

# from_microsoft_defender

> Runs a Microsoft Defender advanced hunting query and reads its results.

Runs a Microsoft Defender advanced hunting query and reads its results.

```tql
from_microsoft_defender query:string, azure_auth=record, [start=time, end=time, tls=bool|record]
```

## Description

The `from_microsoft_defender` operator is a finite source that sends a `POST` request to Microsoft Graph [`/v1.0/security/runHuntingQuery`](https://learn.microsoft.com/en-us/graph/api/security-security-runhuntingquery?view=graph-rest-1.0). It passes your Kusto Query Language (KQL) string, with [appended stages](from_microsoft_defender.md#optimizations) for downstream operators, and emits the returned rows, not the Graph response envelope. It doesn’t normalize events to OCSF.

The operator validates the entire response before emitting any rows. Empty results succeed without emitting events. Invalid schemas, incompatible values, service errors, and unexpected envelope fields (including partial-result or continuation metadata) fail the pipeline. Diagnostics omit response bodies and result values. HTTP failures and invalid responses include a request ID when the service provides a safe identifier. Query errors point to `query`, while authorization errors point to `azure_auth` and provide status-specific setup hints.

The operator uses the same Entra client-credentials token provider, TLS settings, and bounded HTTP retry policy as [`from_microsoft_graph`](https://tenzir.com/docs/reference/operators/from_microsoft_graph.md). Transient failures and throttling honor `Retry-After`; exhausted retries fail the pipeline. The operator checks token freshness before each attempt and refreshes it when needed, including after a retry delay. Retries preserve the original query and explicit time range. Permanent client and authorization failures aren’t retried.

There is no pagination, automatic time-window splitting, persistent cursor, or deduplication guarantee. Restarting the pipeline reruns the query. The Microsoft Graph v1.0 [advanced-hunting quotas](https://learn.microsoft.com/en-us/graph/api/resources/security-api-overview?view=graph-rest-1.0#quotas-and-resource-allocation) limit results to 100,000 rows and 50 MB per query. These limits are documented for Microsoft Graph, not inferred from the older Defender hunting API or the interactive portal. The [`huntingQueryResults` response type](https://learn.microsoft.com/en-us/graph/api/resources/security-huntingqueryresults?view=graph-rest-1.0) doesn’t document a truncation indicator. A successful response doesn’t guarantee extraction completeness. Bound queries with appropriate time predicates and projections, and check your tenant’s service quotas and data availability.

### Result types

Column names and capitalization are preserved. The response schema controls conversion. Microsoft Graph reports the KQL types with these names:

| Graph type       | KQL type         | Tenzir type                                                  |
| ---------------- | ---------------- | ------------------------------------------------------------ |
| `DateTime`       | `datetime`       | `time`                                                       |
| `Int32`, `Int64` | `int`, `long`    | `int64`                                                      |
| `Double`         | `real`           | `double`                                                     |
| `SByte`          | `bool`           | `bool`                                                       |
| `String`, `Guid` | `string`, `guid` | `string`                                                     |
| `SqlDecimal`     | `decimal`        | `string` with the exact digits                               |
| `TimeSpan`       | `timespan`       | `duration`                                                   |
| `Object`         | `dynamic`        | Records, lists, or scalar values according to the JSON value |

The KQL type names and the older names `Long`, `Real`, `Boolean`, `Bool`, and `Dynamic` are also accepted. Null values remain null. KQL strings have no null value and arrive as empty strings. Integers must fit signed 64-bit range and aren’t converted through floating point. Ordinary string columns stay strings even when they look like timestamps, IP addresses, numbers, or durations. A dynamic string stays a string, even when it looks like a number or holds JSON, and nested strings don’t undergo timestamp or IP inference. Microsoft Graph fails with an internal server error for dynamic lists that mix types, such as `dynamic([1, "x"])`, so convert such values in your query, for example with `tostring()`. Graph also sends objects inside dynamic lists as JSON text, so `dynamic([{"x": 1}])` arrives as a list with the string `{"x":1}`, which you can decode with `parse_json`. Graph treats keys of dynamic objects that contain `@odata.`, such as `x@odata.type`, as its own metadata: it drops them or fails the query. The operator asks Graph to omit OData type annotations, and removes them if Graph sends them anyway.

### `query: string`

The required, arbitrary KQL query. You can select tables, filter events, join available tables, aggregate, and project computed columns. Tenzir keeps your query text as is and only appends stages after it, as [Optimizations](from_microsoft_defender.md#optimizations) describes.

### `azure_auth = record`

Required Microsoft Entra application credentials:

| Field           | Type                 | Description                                                   |
| --------------- | -------------------- | ------------------------------------------------------------- |
| `tenant_id`     | `string` or `secret` | Tenant ID or domain.                                          |
| `client_id`     | `string` or `secret` | Application client ID.                                        |
| `client_secret` | `string` or `secret` | Application client secret.                                    |
| `scope`         | `string` or `secret` | Optional; defaults to `https://graph.microsoft.com/.default`. |
| `authority`     | `string` or `secret` | Optional; defaults to `https://login.microsoftonline.com`.    |

The default endpoint and audience target Azure public cloud. Delegated tokens and web identity assertions aren’t supported.

To configure access:

1. Register an application in Microsoft Entra ID.
2. Add the Microsoft Graph **application** permission `ThreatHunting.Read.All`.
3. Grant tenant administrator consent.
4. Create a client secret and store it in your Tenzir secret store.
5. Confirm that your tenant has the Defender product licenses and table access needed by your specific query. API permission alone doesn’t provide licenses or make uncollected data available.

### `start = time`, `end = time` (optional)

Specify both arguments or neither. The start must be earlier than the end. The arguments are evaluated once for the operator invocation and sent as a single ISO 8601 `Timespan` interval. Retries reuse that interval. Tenzir doesn’t inject a `Timestamp` predicate into your KQL.

When you omit both arguments, the request omits `Timespan`. The Graph service currently documents a default lookback of 30 days. This isn’t a retention promise: availability depends on the table, retention configuration, licenses, and tenant. Time filters in the KQL query still apply; Microsoft documents that the shorter range applies when both the query and request constrain time.

### `tls = bool | record` (optional)

TLS configuration, with the same behavior as [`from_microsoft_graph`](https://tenzir.com/docs/reference/operators/from_microsoft_graph.md#tls--bool--record-optional). HTTPS and certificate verification are enabled by default.

## Optimizations

The operator appends KQL `where`, `project`, and `take` stages to your query for the [`where`](https://tenzir.com/docs/reference/operators/where.md), [`select`](https://tenzir.com/docs/reference/operators/select.md), and [`head`](https://tenzir.com/docs/reference/operators/head.md) operators that follow it, so that Defender returns fewer rows and columns. The stages apply to the rows that your query returns, and your query text stays as is:

* **Filters** become prefilters that keep every row that could match. Tenzir still evaluates every predicate locally, so the result stays the same. Supported predicates include top-level comparisons, string hunts with `starts_with`, `ends_with`, and recursive `search`, and ASCII-literal case-insensitive matching. Equality and list membership after `to_lower()` or `to_upper()`, plus IP equality and subnet membership with `ip()`, also produce prefilters. Conservative guards retain Unicode, structured values, and address spellings that need local evaluation. Use `ip()` to compare a string field with an IP literal; equality doesn’t implicitly parse strings. Timestamp comparisons with `==`, `<`, `<=`, `>`, and `>=` also produce [prefilters](../optimizations/kql.md#timestamp-intervals), with widened bounds to preserve decoding precision. They apply to query-output timestamps, including renamed, computed, or aggregated columns, without changing the request’s `start` and `end` window. Negation, regular expressions, timestamp list membership, nested field references, and unsupported function calls stay local. A `take 100000` stage precedes the prefilters to preserve the documented Microsoft Graph result cap, so that they never reveal rows beyond it.
* **Projections** keep the fields that the pipeline reads, including those of local predicates. A field that your query doesn’t return becomes `null`.
* **Limits** become a `take` stage only if no [`where`](https://tenzir.com/docs/reference/operators/where.md) precedes the [`head`](https://tenzir.com/docs/reference/operators/head.md).

The operator never narrows the `start` and `end` window, and sends queries that use `render`, `fork`, `facet`, or a `set` statement, or that end in `;` or `|`, unchanged. The page on [KQL optimizations](../optimizations/kql.md) describes the rules in detail.

## Examples

### Read native Defender events

```tql
from_microsoft_defender "DeviceProcessEvents | project Timestamp, DeviceName, FileName | take 100",
  azure_auth={
    tenant_id: secret("AZURE_TENANT_ID"),
    client_id: secret("AZURE_CLIENT_ID"),
    client_secret: secret("AZURE_CLIENT_SECRET"),
  }
```

### Query a bounded interval

```tql
from_microsoft_defender "DeviceEvents | summarize Count=count() by ActionType",
  azure_auth={
    tenant_id: secret("AZURE_TENANT_ID"),
    client_id: secret("AZURE_CLIENT_ID"),
    client_secret: secret("AZURE_CLIENT_SECRET"),
  },
  start=2026-01-01,
  end=2026-01-02
```

## Defender and Sentinel

Native Defender advanced hunting doesn’t require a Sentinel or Log Analytics workspace. It queries the Defender data available to your tenant and application. Copies ingested into a Log Analytics workspace are separate datasets with their own retention and ingestion configuration; they aren’t interchangeable with native Defender tables.

Microsoft also describes [advanced hunting with connected Sentinel data](https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-microsoft-defender). This operator doesn’t expose `workspace_id` or select a Sentinel workspace. Workspace targeting and acceptance testing against connected Sentinel are outside this version’s scope. Validate licensing, table access, and expected query results in your own tenant before relying on the pipeline in production.

## See also

[Microsoft Defender](../../integrations/microsoft/defender.md)
