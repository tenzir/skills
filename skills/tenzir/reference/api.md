---
title: "API"
canonical: https://tenzir.com/docs/reference/api
source: https://tenzir.com/docs/reference/api.md
section: "Docs"
---

# API

> The platform’s REST API offers everything that the app, the CLI, and the MCP server do, under the same permissions, for your own scripts and tools. This page lists where the API lives, how a request authenticates, and what it can do. Our guide on connecting to Tenzir makes a first request.

The platform’s REST API offers everything that the app, the [CLI](cli.md), and the [MCP server](mcp.md) do, under the same permissions, for your own scripts and tools. This page lists where the API lives, how a request authenticates, and what it can do. Our guide on [connecting to Tenzir](../guides/connect-to-tenzir.md) makes a first request.

## Endpoint

The API lives under `/api` on the platform:

```text
https://platform.tenzir.com/api
```

The platform describes every operation in an OpenAPI document, and renders it as interactive documentation:

| Path                | Content                                           |
| ------------------- | ------------------------------------------------- |
| `/api/openapi.json` | The OpenAPI document, for clients and generators. |
| `/api/docs`         | The interactive documentation in your browser.    |

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

You create an API key in the app under **Settings** → **API keys**, or with `tenzir api-key create`. The platform shows its secret once, and nothing reads it back. A lost key must be revoked and replaced.

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

The operations cover every area of the platform:

| Area             | What you can do                                                                                                    | Examples                                                                                                                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Account          | Read your account, and manage your API keys and sessions.                                                          | `readAccount`, `createApiKey`, `setApiKeyPolicy`, `revokeApiKey`                                                                                |
| Organizations    | Invite and remove members, manage roles, and read usage, billing, and budgets.                                     | `listMembers`, `inviteMember`, `removeMember`, `createRole`, `assignMemberRole`, `revokeMemberRole`                                             |
| Workspaces       | Create, update, and delete workspaces.                                                                             | `createWorkspace`, `updateWorkspace`, `deleteWorkspace`                                                                                         |
| Configuration    | Read and write the configuration repository: branches, commits, files, drafts, and reverts.                        | `readCommits`, `readCommitDiff`, `saveDraft`, `commitDraft`, `createRevertDraft`, `createBranch`, `setBranchProtection`                         |
| Packages         | Read the packages of a configuration and of our library, and add, update, remove, and re-lock packages in a draft. | `readPackages`, `readPackageLibrary`, `addDraftPackage`, `updateDraftPackage`, `updateDraftPackages`, `removeDraftPackage`, `syncDraftPackages` |
| Deployments      | Create, update, upgrade, change the type of, resume, and delete deployments, and diagnose them.                    | `createHostedDeployment`, `changeDeploymentType`, `upgradeDeployment`, `deleteDeployment`, `diagnoseDeployment`                                 |
| Deploying        | Read and change a deployment’s tracker, read its configuration status, and deploy a commit.                        | `readDeploymentTracker`, `changeDeploymentTracker`, `readDeploymentConfigurationStatus`, `deployDeploymentConfiguration`                        |
| Pipelines        | List pipelines, start and stop them, and read their diagnostics and metrics.                                       | `listPipelines`, `startPipeline`, `stopPipeline`, `readPipelineDiagnostics`                                                                     |
| Ad-hoc pipelines | Run a pipeline once on a deployment and read its events.                                                           | `startAdhocPipeline`, `readAdhocPipeline`, `stopAdhocPipeline`                                                                                  |
| Contexts         | Read the contexts that a configuration declares, and inspect the contexts of a deployment.                         | `readConfiguredContexts`, `inspectContexts`                                                                                                     |
| Secrets          | Create, list, update, and delete secrets.                                                                          | `createWorkspaceSecret`, `listDeploymentSecrets`, `deleteOrganizationSecret`                                                                    |
| Ingest endpoints | Create and manage ingest endpoints, and read their metrics.                                                        | `createIngestEndpoint`, `readIngestEndpointMetrics`, `rotateIngestToken`                                                                        |
| Deployment logs  | Read what a deployment logged.                                                                                     | `readLogs`                                                                                                                                      |
| Audit log        | List and export the organization’s audit events.                                                                   | `listAuditEvents`, `exportAuditEvents`                                                                                                          |

Changing packages in a draft takes `WorkspaceBranch.changeDraftPackages`, and inspecting a deployment’s contexts takes `Deployment.inspectContexts`. The rules of trackers, the fields of the configuration status, and the generation that a deploy expects are the same as for the CLI, whose reference describes [deploying](cli.md#deploying).

The configuration repository is also a Git remote: `tenzir config clone` and any Git client work with it directly, as our explanation of [configurations](../explanations/configuration.md#every-change-is-a-commit) describes.

## Errors

A failed request answers with an HTTP status and a JSON body that names the error:

| Status | Meaning                                                                 |
| ------ | ----------------------------------------------------------------------- |
| `401`  | The request carries no credential, or one that the platform refuses.    |
| `403`  | The credential is valid, but its permissions don’t allow the action.    |
| `404`  | The resource doesn’t exist, or the credential may not see it.           |
| `409`  | The request conflicts with the current state, such as a stale revision. |
