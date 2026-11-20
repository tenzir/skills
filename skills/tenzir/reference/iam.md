---
title: "IAM"
canonical: https://tenzir.com/docs/reference/iam
source: https://tenzir.com/docs/reference/iam.md
section: "Docs"
---

# IAM

> The platform decides every request with role-based access control: a member’s roles grant actions on resources, an API key’s policy narrows its member’s actions, and an agent connected via MCP acts with its user’s actions. This page lists the roles, the permissions that the app offers, the actions behind them, and the policy format that roles and API keys share. Our guide on controlling access puts them to use.

The platform decides every request with role-based access control: a member’s roles grant actions on resources, an API key’s policy narrows its member’s actions, and an agent connected via MCP acts with its user’s actions. This page lists the roles, the permissions that the app offers, the actions behind them, and the policy format that roles and API keys share. Our guide on [controlling access](../guides/control-access.md) puts them to use.

## Principals

Every request acts as a principal, whose permissions come from these sources:

| Principal            | Permissions                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A member             | The union of the member’s roles in each organization, limited to that organization’s resources.                                                        |
| An API key           | The intersection of its member’s permissions and the key’s [policy](iam.md#policies). It never exceeds the member’s. |
| An agent via MCP     | Exactly the permissions of the user who signed it in.                                                                                                  |
| Every signed-in user | The [baseline](iam.md#baseline) on the user’s own account, independent of roles.                                     |

A permission that a member loses also leaves every API key and agent of that member at once.

### Baseline

Every signed-in user may, without a role:

* Create organizations, read our documentation, use the Tenzir Assistant, and send feedback.
* Redeem invitations and deployment key links.
* List, create, rename, revoke, and set the policy of their own API keys.
* List and revoke their browser sessions and agent sessions.
* Leave an organization, which removes their own membership.
* Read and change their preferences, and delete their account.

## Roles

A member has one or more roles in an organization. A role is a [policy](iam.md#policies) with a label and a color.

| Role        | Id           | Grants                                                                                                                                                                                                          |
| ----------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owner       | `org.owner`  | Every permission in the organization, including members, roles, billing, protected branches, and deleting the organization. Like the Member role, it reaches only the ad-hoc pipelines that its member started. |
| Member      | `org.member` | Work with workspaces, configurations, deployments, pipelines, secrets, and ingest endpoints. The [next table](iam.md#built-in-roles) lists what it lacks.                     |
| Custom role | a UUID       | Exactly the permissions you choose.                                                                                                                                                                             |

The built-in roles are read-only, and a member may hold several roles at once. A custom role limits ad-hoc pipelines to the ones its member started only if its rule for the `AdhocPipeline` actions carries the [relationship](iam.md#relationships) `owner`; without it, the role reaches every member’s ad-hoc pipelines.

### Built-in roles

In terms of the [permissions in the app](iam.md#permissions-in-the-app), the built-in roles grant these levels:

| Area               | Owner                       | Member                      |
| ------------------ | --------------------------- | --------------------------- |
| Organization       | Delete                      | Read                        |
| Workspaces         | Write                       | Write                       |
| Deployments        | Resilience                  | Resilience                  |
| Configuration      | Deploy                      | Deploy                      |
| Protected Branches | Change Protection           | none                        |
| Secrets            | Write                       | Write                       |
| Pipelines          | Run                         | Run                         |
| Contexts           | Inspect                     | Inspect                     |
| Ingest Endpoints   | Manage                      | Manage                      |
| Adhoc Pipelines    | Create, Run, and View Owned | Create, Run, and View Owned |
| Audit Logs         | Read                        | Read                        |
| People             | Invite & Remove             | Read                        |
| Roles              | Write                       | Read                        |
| Usage              | Read                        | none                        |
| Billing            | Change plan                 | none                        |

### Recovery access

The platform refuses a change to roles, assignments, or members that would leave no member able to recover the organization. At least one member with a user account must keep these actions:

| Target             | Actions                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `Organization`     | `Organization.read`, `Organization.readUsageState`, `Organization.listRoles`, `Organization.createRole`, `Organization.listMembers` |
| `OrganizationRole` | `OrganizationRole.read`, `OrganizationRole.update`, `OrganizationRole.assignToMember`                                               |

### Manage roles

| Task                       | App                                        | CLI                                                               | MCP                  | API                |
| -------------------------- | ------------------------------------------ | ----------------------------------------------------------------- | -------------------- | ------------------ |
| List roles                 | **Settings** → **IAM** → **Roles**         | `tenzir organization role list`                                   | `list_roles`         | `listRoles`        |
| Read a role’s policy       | Select the role                            | `tenzir organization role get <role>`                             | `read_role`          | `readRole`         |
| Create a role              | **New role**                               | `tenzir organization role create --label <label> --policy <json>` | `create_role`        | `createRole`       |
| Change a role              | Select the role and change its permissions | `tenzir organization role update <role>`                          | `update_role`        | `updateRole`       |
| Delete a role              | Select the role, then **Delete role**      | `tenzir organization role delete <role>`                          | `delete_role`        | `deleteRole`       |
| List members and their ids | **Settings** → **IAM** → **People**        | `tenzir organization member list`                                 | `list_members`       | `listMembers`      |
| Assign a role              | Select the member, then **Add**            | `tenzir organization role assign <role> <member>`                 | `assign_member_role` | `assignMemberRole` |
| Revoke a role              | Select the member and remove the role      | `tenzir organization role revoke <role> <member>`                 | `revoke_member_role` | `revokeMemberRole` |

A role goes by its id, `org.owner`, `org.member`, or a custom role’s UUID. A member goes by its member id, a UUID that also identifies an invited member who hasn’t joined yet. It is not the user’s id: take it from `tenzir organization member list`, `list_members`, `listMembers`, or the address of the member’s page in the app.

## Permissions in the app

The app groups actions into areas, each with levels, under **Settings** → **IAM** → **Roles** and on an API key’s page. The levels of an area build on each other: selecting a level also selects every level before it, and clearing a level also clears every level after it. Selecting or clearing **Roles** → **Assign** or **Roles** → **Write** asks you to confirm.

| Area               | Level                       | Actions                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Organization       | Read                        | `Organization.read`, `Organization.readUsageState`                                                                                                                                                                                                                                                                                                                                             |
|                    | Update                      | `Organization.update`                                                                                                                                                                                                                                                                                                                                                                          |
|                    | Delete                      | `Organization.delete`                                                                                                                                                                                                                                                                                                                                                                          |
| Workspaces         | Read                        | `Organization.listWorkspaces`, `Workspace.read`, `Workspace.listDeploymentTypes`, `Workspace.readMetrics`, `Workspace.streamMetrics`                                                                                                                                                                                                                                                           |
|                    | Write                       | `Organization.createWorkspace`, `Workspace.update`, `Workspace.delete`                                                                                                                                                                                                                                                                                                                         |
| Deployments        | Read                        | `Workspace.listDeployments`, `Workspace.streamDeployments`, `Deployment.read`, `Deployment.readTracker`, `Deployment.readConfigurationStatus`, `Deployment.readResilience`, `Deployment.redeemKeyLink`                                                                                                                                                                                         |
|                    | Diagnose                    | `Deployment.diagnose`, which also reads the deployment’s logs                                                                                                                                                                                                                                                                                                                                  |
|                    | Write                       | `Workspace.createDeployment`, `Workspace.createHostedDeployment`, `Deployment.issueKeyLink`, `Deployment.rotateKey`, `Deployment.changeType`, `Deployment.update`, `Deployment.resume`, `Deployment.rename`, `Deployment.delete`                                                                                                                                                               |
|                    | Resilience                  | `Deployment.changeResilience`. Buffering secrets stores every secret a deployment can read on its storage.                                                                                                                                                                                                                                                                                     |
| Configuration      | Read                        | `Workspace.readGitRemote`, `Workspace.readBranches`, `Workspace.readFileTree`, `Workspace.readCommits`, `Workspace.readCommit`, `Workspace.readCommitDiff`, `Workspace.readFile`, `Workspace.readConfiguredPipelines`, `Workspace.readConfiguredContexts`, `Workspace.readPackages`, `Workspace.readPackageLibrary`, `Workspace.fetchGit`, `Workspace.listDrafts`, `WorkspaceBranch.readDraft` |
|                    | Write                       | `Workspace.pushGit`; on every branch `WorkspaceBranch.createDraft`, `WorkspaceBranch.saveDraft`, `WorkspaceBranch.discardDraft`, `WorkspaceBranch.createRevertDraft`, `WorkspaceBranch.changeDraftPackages`; on unprotected branches `WorkspaceBranch.create`, `WorkspaceBranch.push`, `WorkspaceBranch.commitDraft`                                                                           |
|                    | Deploy                      | `Deployment.deployConfiguration`, `Deployment.changeTracker`                                                                                                                                                                                                                                                                                                                                   |
| Protected Branches | Write                       | On protected branches `WorkspaceBranch.create`, `WorkspaceBranch.push`, `WorkspaceBranch.commitDraft`                                                                                                                                                                                                                                                                                          |
|                    | Change Protection           | `Workspace.setBranchProtection`, which can lift the protection of any branch                                                                                                                                                                                                                                                                                                                   |
| Secrets            | View                        | `Organization.listSecrets`, `Workspace.listSecrets`, `Deployment.listSecrets`                                                                                                                                                                                                                                                                                                                  |
|                    | Write                       | `Organization.createSecret`, `Workspace.createSecret`, `Deployment.createSecret`, and `update` and `delete` on `OrgSecret`, `WorkspaceSecret`, and `DeploymentSecret`                                                                                                                                                                                                                          |
| Pipelines          | Read                        | `Deployment.listPipelines`, `Deployment.streamPipelines`, `Deployment.readPipelineMetrics`, `Deployment.readLoad`, `Deployment.streamPipelineMetrics`                                                                                                                                                                                                                                          |
|                    | Inspect Graph & Sources     | `Deployment.streamPipelineGraph`, which includes the complete pipeline and package source text                                                                                                                                                                                                                                                                                                 |
|                    | Inspect Events              | `Deployment.streamPipelineEvents`                                                                                                                                                                                                                                                                                                                                                              |
|                    | Diagnose                    | `Deployment.readPipelineDiagnostics`                                                                                                                                                                                                                                                                                                                                                           |
|                    | Run                         | `Deployment.startPipeline`, `Deployment.stopPipeline`                                                                                                                                                                                                                                                                                                                                          |
| Contexts           | Inspect                     | `Deployment.inspectContexts`                                                                                                                                                                                                                                                                                                                                                                   |
| Ingest Endpoints   | View                        | `Organization.listIngestEndpoints`, `Organization.readIngestMetrics`, `Organization.listIngestConsumers`, `IngestEndpoint.read`, `IngestEndpoint.readMetrics`, `IngestEndpoint.readBuffer`                                                                                                                                                                                                     |
|                    | Manage                      | `Organization.createIngestEndpoint`, `IngestEndpoint.update`, `IngestEndpoint.delete`, `IngestEndpoint.sendTestEvent`, `IngestEndpoint.readToken`, `IngestEndpoint.rotateToken`                                                                                                                                                                                                                |
| Adhoc Pipelines    | Create, Run, and View Owned | `Deployment.startAdhocPipeline`; on ad-hoc pipelines that you started, `AdhocPipeline.read`, `AdhocPipeline.readEvents`, `AdhocPipeline.stream`, `AdhocPipeline.stop`                                                                                                                                                                                                                          |
| Audit Logs         | Read                        | `Organization.listAuditEvents`, `Organization.exportAuditEvents`                                                                                                                                                                                                                                                                                                                               |
| People             | Read                        | `Organization.listMembers`                                                                                                                                                                                                                                                                                                                                                                     |
|                    | Invite & Remove             | `Organization.inviteMember`, `OrganizationMember.remove`                                                                                                                                                                                                                                                                                                                                       |
| Roles              | Read                        | `Organization.listRoles`, `OrganizationRole.read`                                                                                                                                                                                                                                                                                                                                              |
|                    | Assign                      | `OrganizationRole.assignToMember`, `OrganizationRole.revokeFromMember`, which allow assigning the role to any member, yourself included                                                                                                                                                                                                                                                        |
|                    | Write                       | `Organization.createRole`, `OrganizationRole.update`, `OrganizationRole.delete`                                                                                                                                                                                                                                                                                                                |
| Usage              | Read                        | `Organization.readUsage`                                                                                                                                                                                                                                                                                                                                                                       |
| Billing            | Read                        | `Organization.readBilling`, `Organization.readCost`, `Organization.listCreditGrants`, `Organization.quoteCredits`                                                                                                                                                                                                                                                                              |
|                    | Set budget                  | `Organization.setBudget`                                                                                                                                                                                                                                                                                                                                                                       |
|                    | Buy credits                 | `Organization.purchaseCredits`                                                                                                                                                                                                                                                                                                                                                                 |
|                    | Change plan                 | `Organization.changePlan`                                                                                                                                                                                                                                                                                                                                                                      |

The operations of the [API](api.md#permissions) and the tools of the [MCP server](mcp.md#permissions) name the action they require.

## Policies

Roles and API keys share one policy format: a JSON array of rules, each a pair of constraints and actions.

```json
[
  [
    { "target": { "_tag": "Workspace", "workspaceId": "<workspace-id>" }, "relationships": [] },
    ["Workspace.listDeployments", "Workspace.readFile"]
  ],
  [
    { "target": { "_tag": "WorkspaceBranch", "protected": false }, "relationships": [] },
    ["WorkspaceBranch.commitDraft"]
  ]
]
```

| Part            | Format                                                                                        | Meaning                                                                        |
| --------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Rule            | `[constraints, actions]`                                                                      | Allows the actions on every resource that the constraints match.               |
| `target`        | An object with `_tag` and optional [fields](iam.md#targets) | Matches resources of that kind. Every field you give must match exactly.       |
| `relationships` | An array of [relationships](iam.md#relationships)           | Matches only when the principal has every listed relationship to the resource. |
| Actions         | A non-empty array of action names                                                             | Matched by exact name, such as `Deployment.startPipeline`.                     |

These rules decide a request:

* A request is allowed when at least one rule matches its action and its resource. A policy grants nothing else, so the empty policy `[]` denies every action. An API key with `[]` can still read its own account.
* A role grants only within its organization, whatever its rules select.
* An API key’s policy can only narrow: it allows an action only when its member is allowed it as well.
* Creating an API key or changing its policy takes holding every action that the policy grants.

## Targets

A target names the kind of resource that a rule applies to. A field that you leave out matches every value.

| `_tag`                  | Fields                                                   | Covers                                                        |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------- |
| `Organization`          | `orgId`                                                  | An organization and what it lists, creates, and bills.        |
| `OrganizationMember`    | `orgId`, `memberId`, `userId`                            | A member or invited member.                                   |
| `OrganizationRole`      | `orgId`, `roleId`                                        | A role and its assignments.                                   |
| `Invitation`            | `orgId`, `invitationId`                                  | A pending invitation.                                         |
| `Workspace`             | `orgId`, `workspaceId`                                   | A workspace, its configuration repository, and its secrets.   |
| `WorkspaceBranch`       | `orgId`, `workspaceId`, `branch`, `protected`            | A branch of a configuration and your drafts of it.            |
| `Deployment`            | `orgId`, `deploymentId`                                  | A deployment, its configuration status, and its pipelines.    |
| `AdhocPipeline`         | `orgId`, `deploymentId`, `pipelineId`, `ownerId`         | An ad-hoc pipeline.                                           |
| `OrgSecret`             | `orgId`, `secretId`, `name`, `restricted`                | A secret of an organization.                                  |
| `WorkspaceSecret`       | `orgId`, `workspaceId`, `secretId`, `name`, `restricted` | A secret of a workspace.                                      |
| `DeploymentSecret`      | `orgId`, `deploymentId`, `secretId`, `name`              | A secret of a deployment.                                     |
| `IngestEndpoint`        | `orgId`, `endpointId`, `name`                            | An ingest endpoint.                                           |
| `User`                  | `userId`                                                 | A user account, its API keys, and its sessions.               |
| `ApiKey`                | `apiKeyId`, `owner`                                      | An API key. The `owner` is a `User` or `Organization` target. |
| `AssistantConversation` | `conversationId`, `ownerId`                              | A conversation with the Tenzir Assistant.                     |

The `protected` field of a `WorkspaceBranch` tells whether one of the workspace’s protection patterns matches the branch. The `restricted` field of a secret tells whether only some workspaces or deployments may read it.

## Relationships

A relationship ties the principal to a resource. Rules that list one match only the resources that the principal has that relationship to:

| Relationship | Holds when…                                                | Used with                                          |
| ------------ | ---------------------------------------------------------- | -------------------------------------------------- |
| `self`       | The resource is the principal’s own account or membership. | `User`, `OrganizationMember`                       |
| `other`      | The resource is another user’s account or membership.      | `User`, `OrganizationMember`                       |
| `owner`      | The principal created the resource.                        | `ApiKey`, `AdhocPipeline`, `AssistantConversation` |

The relationships `parent`, `child`, and `consumer` tie deployments to their own resources, and member policies don’t use them.

## See also

* [Control access](../guides/control-access.md)
* [API](api.md)
* [MCP](mcp.md)
