# Microsoft Graph


Microsoft Graph is the unified API for Microsoft 365, Microsoft Entra ID, and other Microsoft cloud services.

Use [`from_microsoft_graph`](/reference/operators/from_microsoft_graph.md) to read events and inventory data from Microsoft Graph collection resources. The operator handles Microsoft Entra client-credentials authentication, emits each object from the OData `value` array, and follows `@odata.nextLink` pagination.

Common security use cases include collecting Microsoft Entra audit and sign-in logs, reading users and groups for enrichment, and extracting inventory from Microsoft 365 services that expose collection resources through Microsoft Graph.

Prerequisites

Create a Microsoft Entra application registration, grant the application permissions required by the Microsoft Graph resource that you want to read, and create a client secret. For example, reading `auditLogs/signIns` requires an application permission such as `AuditLog.Read.All`.

## Prepare Microsoft Graph access

Before you run a pipeline, prepare the Microsoft Entra application and verify that it can read the Microsoft Graph resource you want to collect:

1. [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in Microsoft Entra ID and record the **Application (client) ID** and tenant ID.
2. [Create a client secret](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials?tabs=client-secret) for the application and record the secret value.
3. [Add Microsoft Graph application permissions](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-configure-app-access-web-apis#application-permission-to-microsoft-graph) for the API calls you plan to make. The `from_microsoft_graph` operator uses application permissions because it authenticates without a signed-in user.
4. [Grant administrator consent](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent) for those application permissions.
5. Look up the required permissions in the [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference) or on the reference page for the resource.

Useful Microsoft Graph reference pages:

* [Use the Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api)
* [Get access without a user](https://learn.microsoft.com/en-us/graph/auth-v2-service)
* [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference)
* [Sign-ins API](https://learn.microsoft.com/en-us/graph/api/signin-list)
* [Directory audits API](https://learn.microsoft.com/en-us/graph/api/directoryaudit-list)
* [Users API](https://learn.microsoft.com/en-us/graph/api/user-list)
* [Groups API](https://learn.microsoft.com/en-us/graph/api/group-list)

## Read sign-in logs

The following pipeline reads Microsoft Entra sign-in logs and requests only a subset of fields:

```tql
from_microsoft_graph "auditLogs/signIns",
  auth={
    tenant_id: "contoso.onmicrosoft.com",
    client_id: "00000000-0000-0000-0000-000000000000",
    client_secret: secret("ms-graph-client-secret"),
  },
  odata={
    filter: "createdDateTime ge 2026-04-24T00:00:00Z",
    select: ["id", "createdDateTime", "userPrincipalName", "status"],
    top: 1000,
  }
```

## Read directory objects

You can read users, groups, or other directory collections for enrichment and inventory workflows:

```tql
from_microsoft_graph "users",
  auth={
    tenant_id: secret("ms-graph-tenant-id"),
    client_id: secret("ms-graph-client-id"),
    client_secret: secret("ms-graph-client-secret"),
  },
  odata={
    select: ["id", "displayName", "userPrincipalName"],
  }
```

Use `version="beta"` to read Microsoft Graph beta collections:

```tql
from_microsoft_graph "users",
  version="beta",
  auth={
    tenant_id: secret("ms-graph-tenant-id"),
    client_id: secret("ms-graph-client-id"),
    client_secret: secret("ms-graph-client-secret"),
  },
  odata={
    select: ["id", "displayName", "signInActivity"],
  }
```

## See Also

* [`from_microsoft_graph`](/reference/operators/from_microsoft_graph.md)
* [`from_http`](/reference/operators/from_http.md)
* [Defender](defender.md)
* [Sentinel & Log Analytics](sentinel-log-analytics.md)