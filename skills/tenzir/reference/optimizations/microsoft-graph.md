---
title: "Microsoft Graph"
canonical: https://tenzir.com/docs/v6.23.0/reference/optimizations/microsoft-graph
source: https://tenzir.com/docs/v6.23.0/reference/optimizations/microsoft-graph.md
section: "Docs"
---

# Microsoft Graph

> The Microsoft Graph source frommicrosoftgraph hands Microsoft Graph the operators that follow it as OData query parameters: $filter, $select, and $top. Those operators leave the pipeline and run in Graph, with Graph’s semantics. This page describes which operators Graph takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our optimizations overview explains how Tenzir optimizes pipelines in general.

The Microsoft Graph source [`from_microsoft_graph`](https://tenzir.com/docs/v6.23.0/reference/operators/from_microsoft_graph.md) hands Microsoft Graph the operators that follow it as OData query parameters: `$filter`, `$select`, and `$top`. Those operators leave the pipeline and run in Graph, with Graph’s semantics. This page describes which operators Graph takes over, how its results can differ from Tenzir’s, and how to keep operators in Tenzir. Our [optimizations overview](../optimizations.md) explains how Tenzir optimizes pipelines in general.

## When it applies

The operator hands Graph the operators that follow it when it reads a collection once, as in `from_microsoft_graph "users"`. It takes over nothing with `delta=true`, which polls for changes, with a `resource` that has its own query string, such as `"users?$select=id"`, and for a query parameter that your `odata` options already set. With `pushdown=false`, every operator stays in Tenzir and runs with TQL semantics.

## Operators that Graph takes over

The operator takes over the longest run of operators directly after it that Graph can express:

* [`where`](https://tenzir.com/docs/v6.23.0/reference/operators/where.md), which becomes a `$filter` for the resources and properties that the [filters](microsoft-graph.md#filters) section lists.
* [`select`](https://tenzir.com/docs/v6.23.0/reference/operators/select.md) of top-level properties, including renames, which becomes a `$select` for any resource.
* [`head`](https://tenzir.com/docs/v6.23.0/reference/operators/head.md), which stops paging once the operator has enough events, and sets the page size with `$top` where Graph documents a maximum page size: 999 for `users` and `groups`, and 1,000 for `auditLogs/signIns`. A limit of zero sends no request at all.

A [`sort`](https://tenzir.com/docs/v6.23.0/reference/operators/sort.md), a [`drop`](https://tenzir.com/docs/v6.23.0/reference/operators/drop.md), a [`summarize`](https://tenzir.com/docs/v6.23.0/reference/operators/summarize.md), and every operator after a [`head`](https://tenzir.com/docs/v6.23.0/reference/operators/head.md) stay in Tenzir, since Graph may ignore `$orderby` without an error and counts only with advanced queries. For example, the pipeline

```tql
from_microsoft_graph "users",
  auth={
    tenant_id: secret("ms-graph-tenant-id"),
    client_id: secret("ms-graph-client-id"),
    client_secret: secret("ms-graph-client-secret"),
  }
where department == "Security"
where accountEnabled == true
select id, displayName, mail
head 10
```

requests a single page:

```text
/v1.0/users?$filter=(department eq 'Security') and (accountEnabled eq true)&$select=id,displayName,mail&$top=10
```

## Filters

Graph may silently ignore a query parameter that it does not support, and then returns rows that the filter would have dropped. The operator therefore takes over a [`where`](https://tenzir.com/docs/v6.23.0/reference/operators/where.md) only for the `v1.0` resources and properties for which Microsoft documents `$filter` support without [advanced queries](https://learn.microsoft.com/graph/aad-advanced-queries):

| Resource                    | `==` and `in`                                                                                                                                                                                                     | `starts_with`                                                                                                                                                                                | `>=` and `<=`                                   | `or` |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- | ---- |
| `users`                     | `accountEnabled`, `creationType`, `employeeId`, `externalUserState`, `onPremisesImmutableId`, `onPremisesSecurityIdentifier`, `onPremisesSyncEnabled`, `state`, `userType`, and the `starts_with` properties      | `city`, `country`, `department`, `displayName`, `givenName`, `jobTitle`, `mail`, `mailNickname`, `surname`, `usageLocation`, `userPrincipalName`                                             | `createdDateTime`, `onPremisesLastSyncDateTime` | Yes  |
| `groups`                    | `hasMembersWithLicenseErrors`, `isAssignableToRole`, `mailEnabled`, `membershipRuleProcessingState`, `onPremisesSecurityIdentifier`, `onPremisesSyncEnabled`, `securityEnabled`, and the `starts_with` properties | `classification`, `displayName`, `mail`, `mailNickname`, `membershipRule`, `uniqueName`                                                                                                      | `onPremisesLastSyncDateTime`, `renewedDateTime` | Yes  |
| `auditLogs/signIns`         | `==` only: `appId`, `clientAppUsed`, `correlationId`, `id`, `resourceDisplayName`, `resourceId`, `status.errorCode`, `userId`, and the `starts_with` properties                                                   | `appDisplayName`, `deviceDetail.browser`, `deviceDetail.operatingSystem`, `ipAddress`, `location.city`, `location.state`, `location.countryOrRegion`, `userDisplayName`, `userPrincipalName` | `createdDateTime`                               | No   |
| `auditLogs/directoryAudits` | `==` only: `id`, `loggedByService`, `initiatedBy.app.appId`, `initiatedBy.app.displayName`, `initiatedBy.user.id`, `initiatedBy.user.displayName`, and the `starts_with` properties                               | `activityDisplayName`, `initiatedBy.user.userPrincipalName`                                                                                                                                  | `activityDateTime`                              | No   |

Several [`where`](https://tenzir.com/docs/v6.23.0/reference/operators/where.md) operators combine with `and`. Strings become `'…'`, with a quote doubled, and times become `2024-01-02T00:00:00Z`. Strings longer than 120 characters, filters with more than 15 terms, `!=`, `not`, `<` and `>`, `ends_with`, `null`, other properties, and other resources stay in Tenzir.

## Graph semantics

The operators that Graph takes over run as Graph runs them, which can differ from TQL:

* Graph compares many directory strings without regard to case, so `displayName == "alice"` also matches `Alice`.
* `$top` sets the size of a page, not the number of results. The operator counts the events itself and stops paging once the [`head`](https://tenzir.com/docs/v6.23.0/reference/operators/head.md) has enough.
* A request that Graph rejects fails the pipeline with a hint to use `pushdown=false`.

## Verify an optimization

To see the operators that Graph takes over, print the optimized pipeline:

```sh
tenzir --dump-opt-ir 'from_microsoft_graph "users", auth={tenant_id: secret("t"), client_id: secret("c"), client_secret: secret("s")} | where displayName == "Ada" | head 10'
```

The operator lists the operators that it took over as `plan`, and the reason why it took over no more as `declined`.
