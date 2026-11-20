---
title: "MCP"
canonical: https://tenzir.com/docs/reference/mcp
source: https://tenzir.com/docs/reference/mcp.md
section: "Docs"
---

# MCP

> The platform’s MCP server lets an AI agent do what you do in the app, with your permissions: run pipelines, read diagnostics, change the configuration, and manage deployments. It speaks the Model Context Protocol, so any agent that supports remote MCP servers can connect. This page lists the endpoint, how an agent signs in, and the tools it gets. Our guide on connecting to Tenzir sets up a client.

The platform’s MCP server lets an AI agent do what you do in the app, with your permissions: run pipelines, read diagnostics, change the configuration, and manage deployments. It speaks the [Model Context Protocol](https://modelcontextprotocol.io), so any agent that supports remote MCP servers can connect. This page lists the endpoint, how an agent signs in, and the tools it gets. Our guide on [connecting to Tenzir](../guides/connect-to-tenzir.md) sets up a client.

## Endpoint

The server lives at `/mcp` on the platform and uses the streamable HTTP transport:

```text
https://platform.tenzir.com/mcp
```

## Authentication

The server signs agents in with OAuth. The first time an agent connects, it opens your browser, you sign in to the platform as usual, and the agent receives a token that acts on your behalf. The agent discovers how to sign in from the server’s metadata at `/.well-known/oauth-protected-resource/mcp`, so a client needs nothing but the endpoint’s URL.

The server accepts only these tokens. API keys work with the [API](api.md) and the [CLI](cli.md), not with MCP.

## Permissions

An agent acts as you, with exactly the permissions of your roles in each organization. What you may not do, the agent may not do either, and a tool that needs a permission you lack fails with a message that names it. Each tool’s description names the action it requires, and our [IAM reference](iam.md#permissions-in-the-app) lists which permission of a role grants that action.

Every agent you connect appears in the app under **Settings** → **Sessions** → **Agent sessions**, with its client’s name, when it connected, and when it was last active. Disconnect one there to revoke its token, or select **Disconnect all**.

## Confirmations

A tool that deploys a configuration asks you to confirm before it acts. The server shows the question as a form in your client, if the client can show forms. Otherwise the tool’s description tells the agent to confirm with you in the conversation first.

Secrets never pass through an agent: create them in the app or with `tenzir secret set`. The agent can list which secrets a deployment reaches and delete them, but not read or set their values. For the same reason, an agent can’t create API keys, whose secret the platform shows once.

## Tools

Each tool describes what it does and which permission it requires, and marks whether it only reads, and whether it can destroy something, so that your client can ask before it calls a tool that changes state.

| Area          | Tools                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account       | `whoami`, `list_api_keys`, `rename_api_key`, `set_api_key_policy`, `revoke_api_key`                                                                                                                                                                                                                                                                                                             |
| Organizations | `create_organization`, `update_organization`, `delete_organization`, `list_members`, `invite_member`, `remove_member`, `list_roles`, `create_role`, `read_role`, `update_role`, `delete_role`, `assign_member_role`, `revoke_member_role`                                                                                                                                                       |
| Billing       | `read_usage`, `read_usage_state`, `read_billing`, `read_cost`, `read_budget`, `set_budget`, `list_credit_grants`, `quote_credits`                                                                                                                                                                                                                                                               |
| Workspaces    | `create_workspace`, `update_workspace`, `delete_workspace`                                                                                                                                                                                                                                                                                                                                      |
| Deployments   | `list_deployments`, `list_deployment_types`, `create_deployment`, `create_hosted_deployment`, `change_deployment_type`, `rename_deployment`, `update_deployment`, `resume_deployment`, `delete_deployment`, `rotate_deployment_key`, `diagnose_deployment`, `read_deployment_logs`, `read_deployment_resilience`, `change_deployment_resilience`, `inspect_deployment_contexts`                 |
| Secrets       | `list_secrets`, `delete_secret`                                                                                                                                                                                                                                                                                                                                                                 |
| Pipelines     | `list_pipelines`, `start_pipeline`, `stop_pipeline`, `read_pipeline_diagnostics`, `start_adhoc_pipeline`, `read_adhoc_pipeline`, `stop_adhoc_pipeline`                                                                                                                                                                                                                                          |
| Configuration | `list_workspace_configuration_branches`, `create_workspace_configuration_branch`, `set_workspace_branch_protection`, `list_workspace_configuration`, `read_workspace_configuration_file`, `list_workspace_configuration_commits`, `read_workspace_configuration_commit`, `read_workspace_configuration_diff`, `list_workspace_configuration_pipelines`, `list_workspace_configuration_contexts` |
| Drafts        | `list_workspace_configuration_drafts`, `read_workspace_configuration_draft`, `create_workspace_configuration_draft`, `save_workspace_configuration_draft`, `commit_workspace_configuration_draft`, `discard_workspace_configuration_draft`                                                                                                                                                      |
| Packages      | `read_workspace_packages`, `list_package_library`, `add_draft_package`, `remove_draft_package`, `update_draft_packages`, `sync_draft_packages`                                                                                                                                                                                                                                                  |
| Deploying     | `read_deployment_tracker`, `change_deployment_tracker`, `read_deployment_configuration_status`, `deploy_deployment_configuration`                                                                                                                                                                                                                                                               |
| Help          | `read_docs`, `send_feedback`                                                                                                                                                                                                                                                                                                                                                                    |

### Deployments

`update_deployment` takes the `version` that `list_deployments` offers in the deployment’s `update`, and refuses any other version, and any while no update is on offer.

### Packages

The package tools change the packages of your personal draft of a branch, as the app’s **Packages** page does: they edit `package.yaml` and lock the result in `package.lock`, so a commit of the draft deploys. Editing `package.yaml` through `save_workspace_configuration_draft` leaves the lock stale; `sync_draft_packages` brings it in line.

### Drafts

An agent changes a configuration through your personal **draft** of a branch, the same draft that the app’s configuration editor keeps. You can review its changes in the app before you or the agent commit them. Our explanation of [configurations](../explanations/configuration.md#every-change-is-a-commit) describes drafts and commits.

### Deploying

The `read_deployment_tracker`, `change_deployment_tracker`, `read_deployment_configuration_status`, and `deploy_deployment_configuration` tools follow the same rules and return the same fields as the CLI, whose reference describes [deploying](cli.md#deploying). A deploy takes the full SHA of a commit and the generation of the deployed revision, `0` if none.

### Ad-hoc pipelines

The `start_adhoc_pipeline` tool runs a pipeline once on a deployment, and `read_adhoc_pipeline` returns its events and diagnostics. With the built-in roles, only you and your agents read and stop the pipelines you start. Our explanation of [where pipelines run](../explanations/pipeline.md#where-pipelines-run) lists when an ad-hoc pipeline ends.

### Documentation

The `read_docs` tool serves our documentation, laid out for agents, and the schema references of our [agent skills](../guides/set-up-your-agent.md), such as OCSF:

* The `skill` parameter selects the skill: `tenzir` by default, or a schema skill such as `tenzir-ocsf`.
* The `version` parameter selects the docs of a deployment’s Tenzir release, as `list_deployments` reports it. A version between releases reads the newest release before it, and without a version, the tool reads the latest Tenzir 7 release. The result names the release that answered.
* A `query` searches the docs, or a single long page when you also give one.

An agent connected via MCP therefore needs no skills installed.

### Feedback

The `send_feedback` tool sends the Tenzir team an anonymous report about what worked and what didn’t. Your client shows you the report to edit or decline before it goes out.
