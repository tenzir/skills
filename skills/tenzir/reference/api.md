---
title: "Overview"
canonical: https://tenzir.com/docs/reference/api
source: https://tenzir.com/docs/reference/api.md
section: "Docs"
---

# Overview

> The platform’s REST API offers everything that the app, the MCP server, and the CLI do, under the same permissions, for your own scripts and tools. This page lists where the API lives, how a request authenticates, and what it can do. Our guide on connecting to Tenzir makes a first request.

The [platform](../explanations/platform.md)’s REST API offers everything that the app, the [MCP server](mcp.md), and the [CLI](cli.md) do, under the same permissions, for your own scripts and tools. This page lists where the API lives, how a request authenticates, and what it can do. Our guide on [connecting to Tenzir](../guides/connect-to-tenzir.md) makes a first request.

## Endpoint

All REST API requests use `https://platform.tenzir.com/api` as their base URL. You can browse and test operations directly in the platform’s [interactive API documentation](https://platform.tenzir.com/api/docs), or fetch the live [OpenAPI 3.1 specification](https://platform.tenzir.com/api/openapi.json):

| Resource                                                              | Purpose                                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `https://platform.tenzir.com/api`                                     | Base URL for all REST API requests.                                                                                                  |
| [Interactive API docs](https://platform.tenzir.com/api/docs)          | Browse and test endpoints in your browser.                                                                                           |
| [OpenAPI specification](https://platform.tenzir.com/api/openapi.json) | Live OpenAPI 3.1 JSON for clients and generators (mirrored at [`/openapi/platform.json`](https://tenzir.com/openapi/platform.json)). |

Requests and responses carry JSON. A path names an organization, a workspace, or a deployment by its slug or its id, such as `/api/organizations/acme/workspaces/prod/deployments`.

## Authentication

A request authenticates with one of two credentials:

| Credential   | Header                          | Use                                                 |
| ------------ | ------------------------------- | --------------------------------------------------- |
| API key      | `x-tenzir-api-key: <key>`       | Scripts, CI jobs, and services that run unattended. |
| Bearer token | `Authorization: Bearer <token>` | Tools that sign you in with your identity provider. |

```sh
curl -H "x-tenzir-api-key: $TENZIR_API_KEY" \
  https://platform.tenzir.com/api/account
```

You create an API key in the app under **Settings** → **API keys**, or with `tenzir platform api-key create`. The platform shows its secret once, and nothing reads it back. A lost key must be revoked and replaced.

## Permissions

An API key acts on behalf of the member who created it. Its **policy** can narrow what that member may do, but never widen it, and the key loses every permission that the member loses later.

A policy is a list of rules, each pairing the resources it applies to with the actions it allows:

```json
[
  [
    { "target": { "_tag": "User" }, "relationships": ["self"] },
    ["User.listApiKeys"]
  ]
]
```

The empty policy `[]` allows only reading the key’s own account. Actions have names such as `Deployment.startAdhocPipeline` or `Workspace.readFileTree`, and each operation in the OpenAPI document names the action it requires. Creating a key or changing its policy takes holding every action that the policy grants. Our [IAM reference](iam.md) lists the roles, the actions behind each permission in the app, and the [policy format](iam.md#policies).

## Operations

The operations are grouped by resource area in the sidebar, with one reference page per endpoint:

| Area             | What you can do                                                                                           | Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account          | Read your account, and manage API keys, sessions, agent sessions, and preferences.                        | [`readAccount`](api/account/read-account.md), [`createApiKey`](api/account/create-api-key.md), [`setApiKeyPolicy`](api/account/set-api-key-policy.md), [`listSessions`](api/account/list-sessions.md)                                                                                                                                                            |
| Organizations    | Manage organizations, members, invitations, custom roles, and audit logs.                                 | [`listOrganizations`](api/organizations/list-organizations.md), [`inviteMember`](api/organizations/invite-member.md), [`createRole`](api/organizations/create-role.md), [`listAuditEvents`](api/organizations/list-audit-events.md)                                                                                                                              |
| Billing          | Read billing plans, cost, credit grants, and usage state, and set budgets.                                | [`readBilling`](api/billing/read-billing.md), [`readCost`](api/billing/read-cost.md), [`setBudget`](api/billing/set-budget.md), [`readUsageState`](api/billing/read-usage-state.md)                                                                                                                                                                              |
| Workspaces       | Manage workspaces and their Git configuration repository: branches, commits, diffs, drafts, and packages. | [`createWorkspace`](api/workspaces/create-workspace.md), [`readBranches`](api/workspaces/read-branches.md), [`saveDraft`](api/workspaces/save-draft.md), [`commitDraft`](api/workspaces/commit-draft.md), [`addDraftPackage`](api/workspaces/add-draft-package.md)                                                             |
| Deployments      | Create, update, resize, and deploy configurations to deployments, and inspect their contexts and logs.    | [`listDeployments`](api/deployments/list-deployments.md), [`createHostedDeployment`](api/deployments/create-hosted-deployment.md), [`deployDeploymentConfiguration`](api/deployments/deploy-deployment-configuration.md), [`inspectContexts`](api/deployments/inspect-contexts.md), [`readLogs`](api/deployments/read-logs.md) |
| Pipelines        | Start, stop, and diagnose pipelines, run ad-hoc pipelines, and read throughput metrics.                   | [`listPipelines`](api/pipelines/list-pipelines.md), [`startPipeline`](api/pipelines/start-pipeline.md), [`startAdhocPipeline`](api/pipelines/start-adhoc-pipeline.md), [`readWorkspaceMetrics`](api/pipelines/read-workspace-metrics.md)                                                                                                                         |
| Secrets          | Create, list, update, and delete organization, workspace, and deployment secrets.                         | [`createOrganizationSecret`](api/secrets/create-organization-secret.md), [`setWorkspaceSecret`](api/secrets/set-workspace-secret.md), [`listDeploymentSecrets`](api/secrets/list-deployment-secrets.md)                                                                                                                                                                                            |
| Ingest Endpoints | Create and manage ingest endpoints, rotate tokens, and inspect buffer and throughput metrics.             | [`createIngestEndpoint`](api/ingest-endpoints/create-ingest-endpoint.md), [`rotateIngestToken`](api/ingest-endpoints/rotate-ingest-token.md), [`readIngestEndpointMetrics`](api/ingest-endpoints/read-ingest-endpoint-metrics.md)                                                                                                                                                                  |
| Assistant        | Check assistant availability, manage conversations, and send feedback.                                    | [`readAssistant`](api/assistant/read-assistant.md), [`createConversation`](api/assistant/create-conversation.md), [`askConversation`](api/assistant/ask-conversation.md)                                                                                                                                                                                                                           |
| Platform         | Sign in via OIDC or CLI flows, check health and build info, and discover platform and MCP metadata.       | [`readHealth`](api/platform/read-health.md), [`readPlatformConfiguration`](api/platform/read-platform-configuration.md), [`getProtectedResourceMetadata`](api/platform/get-protected-resource-metadata.md)                                                                                                                                                                                         |

Updating a deployment names the version it updates to, as `listDeployments` offers it in the deployment’s `update.version`: `updateDeployment` takes the body `{"version": "7.0.1"}`. The platform refuses any other version, and any while it offers no update, with `VersionNotOffered`, and a body without a version with `Validation`.

Changing packages in a draft takes `WorkspaceBranch.changeDraftPackages`, and inspecting a deployment’s contexts takes `Deployment.inspectContexts`. Branch management operations follow the same branch protection rules:

* `GET /organizations/:org/workspaces/:workspace/branches` (`readBranches`) returns the workspace’s `branches`, the recorded `origins` of branches made from another, and active `forwards` (`{"from": "...", "to": "..."}`) mapping renamed branch names to their current names. Chained renames resolve directly to the latest name, creating or pushing a branch of the old name stops forwarding it, and deleting the target branch drops every forward pointing to it.
* `POST /organizations/:org/workspaces/:workspace/branches/:branch/merge` (`mergeBranch`) merges another branch into `:branch` with a merge commit and requires `WorkspaceBranch.merge` on the target branch. Pass `expected` to refuse the merge if the source branch moved since review.
* `POST /organizations/:org/workspaces/:workspace/branches/:branch/rename` (`renameBranch`, body `{"name": "..."}`) renames `:branch`, keeping its commits, its origin, branches made from it, and every user’s draft on it, and records a forward from the old name to the new name. It requires `WorkspaceBranch.rename` on the branch and `WorkspaceBranch.create` on the new name, and is refused while a deployment tracks the branch.
* `POST /organizations/:org/workspaces/:workspace/branches/:branch/delete` (`deleteBranch`) takes an optional `expectedHead` query parameter to refuse deletion if the branch moved past that commit, and is refused while a deployment tracks the branch.
* `POST /organizations/:org/workspaces/:workspace/branches` (`createBranch`) also accepts a `draft` base to create a new branch starting from the caller’s personal draft on another branch, recording that branch as its origin.
* `GET /organizations/:org/workspaces/:workspace/commits` (`readCommits`) accepts an `exclude` query parameter to list only commits not yet on another branch, and `readCommit` and `readCommitDiff` accept `into` to compare a commit against where its history meets the target branch.

The rules of trackers, the fields of the configuration status, and the generation that a deploy expects are the same as for the CLI, whose reference describes [deploying](cli.md#deploying).

The configuration repository is also a Git remote: `tenzir config clone` and any Git client work with it directly, as our explanation of [configurations](../explanations/configuration.md#every-change-is-a-commit) describes.

## Errors

A failed request answers with an HTTP status and a JSON body that names the error:

| Status | Meaning                                                                 |
| ------ | ----------------------------------------------------------------------- |
| `401`  | The request carries no credential, or one that the platform refuses.    |
| `403`  | The credential is valid, but its permissions don’t allow the action.    |
| `404`  | The resource doesn’t exist, or the credential may not see it.           |
| `409`  | The request conflicts with the current state, such as a stale revision. |
