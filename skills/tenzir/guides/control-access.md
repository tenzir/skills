---
title: "Control access"
description: "Invite members and give them the roles they need, limit what scripts and AI agents may do, protect production branches, and remove access you no longer trust."
canonical: https://tenzir.com/docs/guides/control-access
source: https://tenzir.com/docs/guides/control-access.md
section: "Docs"
---

# Control access

> Invite members and give them the roles they need, limit what scripts and AI agents may do, protect production branches, and remove access you no longer trust.

Everyone and everything that works with your deployments goes through the platform: people in the app, scripts through the API and the CLI, and AI agents via MCP. All of them act as a member of your organization, with the permissions of that member’s roles. Controlling access therefore comes down to the members you let in, the roles you give them, the limits you put on API keys, and the access you take back. This guide walks through each, from the first invitation to removing a member.

Before you begin

* Managing members and roles takes the built-in **Owner** role, or a custom role with **People** → **Invite & Remove** and **Roles** → **Write**.
* Protecting branches takes **Protected Branches** → **Change Protection**.
* Our [IAM reference](../reference/iam.md) lists every permission and the actions behind it.

## Invite a member

An invitation is a link that adds whoever redeems it to your organization. The platform sends no email, so you share the link yourself:

* MCP

  Ask your agent:

  ```prompt
  Invite Jane Doe to acme and give me the invitation link.
  ```

* App

  1. Open **Settings** → **IAM** → **People**.
  2. Select **Invite member**, enter an **Invitation label** that tells you who the link is for, such as `Jane Doe`, and select **Create invitation**.
  3. Copy the **Redeem link** and send it to the person.

* CLI

  ```sh
  tenzir platform organization member invite 'Jane Doe' --org acme
  ```

  The command prints the link that admits the invitee.

* API

  ```sh
  curl -X POST -H "x-tenzir-api-key: $TENZIR_API_KEY" \
    -H 'content-type: application/json' \
    -d '{"label":"Jane Doe"}' \
    https://platform.tenzir.com/api/organizations/acme/invitations
  ```

  The answer holds the new member’s `memberId`, the `invitation` with its `id`, and the `secret`, which the platform shows only once. The link to share is `https://platform.tenzir.com/invitations/<org-id>/<invitation-id>#secret=<secret>`.

The link admits whoever opens it first, once, so send it to the invitee only. The invited member appears under **People** with **Pending invitation** right away, and holds no role until you give it one. You can assign roles before the person joins, so that they find what they need on their first visit.

## Give members the roles they need

Each member has one or more roles. The built-in **Owner** role, with the id `org.owner`, may do everything, including managing members, billing, and protected branches. The built-in **Member** role, `org.member`, may work with the organization’s workspaces and deployments, but not manage people or write protected branches. A custom role grants exactly the permissions you choose, such as reading configurations but not deploying them.

This example creates a role that may only read the configurations of every workspace, the permissions **Workspaces** → **Read** and **Configuration** → **Read** in the app, and gives it to a member:

* MCP

  Ask your agent:

  ```prompt
  Create a role "Auditor" in acme with only Workspaces → Read and Configuration → Read, and assign it to jane@example.com.
  ```

* App

  1. Open **Settings** → **IAM** → **Roles** and select **New role**.
  2. Name the role `Auditor`, create it, and select **Workspaces** → **Read** and **Configuration** → **Read**.
  3. Open **People**, select the member, and add the role with **Add**.

* CLI

  Save the role’s [policy](../reference/iam.md#policies) as `auditor.json`:

  auditor.json

  ```json
  [
    [
      { "target": { "_tag": "Organization" }, "relationships": [] },
      ["Organization.listWorkspaces"]
    ],
    [
      { "target": { "_tag": "Workspace" }, "relationships": [] },
      [
        "Workspace.read",
        "Workspace.listDeploymentTypes",
        "Workspace.readMetrics",
        "Workspace.streamMetrics",
        "Workspace.readGitRemote",
        "Workspace.readBranches",
        "Workspace.readFileTree",
        "Workspace.readCommits",
        "Workspace.readCommit",
        "Workspace.readCommitDiff",
        "Workspace.readFile",
        "Workspace.readConfiguredPipelines",
        "Workspace.readConfiguredContexts",
        "Workspace.readPackages",
        "Workspace.readPackageLibrary",
        "Workspace.fetchGit",
        "Workspace.listDrafts"
      ]
    ],
    [
      { "target": { "_tag": "WorkspaceBranch" }, "relationships": [] },
      ["WorkspaceBranch.readDraft"]
    ]
  ]
  ```

  Create the role, which prints its id, and assign it:

  ```sh
  tenzir platform organization role create --org acme --label Auditor \
    --policy "$(cat auditor.json)"
  tenzir platform organization role assign <role-id> <member-id> --org acme
  ```

  The `<member-id>` is the member’s id, not the user’s, as `tenzir platform organization member list --org acme` shows it. A built-in role goes by `org.owner` or `org.member` instead of a UUID.

* API

  List the members to find the member’s id:

  ```sh
  curl -H "x-tenzir-api-key: $TENZIR_API_KEY" \
    https://platform.tenzir.com/api/organizations/acme/members
  ```

  Each entry carries the member’s `id`, its `user` with name and email once the person joined, and its `roles`. The `createRole` and `assignMemberRole` operations create and assign the role, as the interactive documentation at `https://platform.tenzir.com/api/docs` shows.

The platform refuses a change that would leave no member able to recover the organization, so give another member that access before you take it from yourself. Our IAM reference lists the [actions that recovery needs](../reference/iam.md#recovery-access).

## Limit what a script may do

An API key acts on behalf of the member who created it, and its **policy** narrows that member’s permissions to what the script needs. A key never exceeds its member’s permissions, so removing a role from a member also takes it from every key of that member. A key without a policy may only read its own account.

A policy is a list of rules, each pairing the resources that it applies to with the actions that it allows. This policy lets a key list the deployments of every workspace its member can see, and nothing else:

```json
[
  [
    { "target": { "_tag": "Workspace" }, "relationships": [] },
    ["Workspace.listDeployments"]
  ]
]
```

Create a key with that policy, or give an existing key a new one:

* MCP

  Agents don’t create API keys, so that a key’s secret never passes through an agent. Create the key in the app or with the CLI, then ask your agent to narrow it:

  ```prompt
  Limit my API key ci to listing the deployments of my workspaces.
  ```

* App

  1. Open **Settings** → **API keys** and select **Create API key**.
  2. Name the key, such as `ci`, and copy the secret that the dialog shows.
  3. Open the key’s page and choose the permissions that it allows.

* CLI

  ```sh
  tenzir platform api-key create --name ci \
    --policy '[[{"target":{"_tag":"Workspace"},"relationships":[]},["Workspace.listDeployments"]]]'
  ```

  The command prints the secret once. To change the policy of an existing key:

  ```sh
  tenzir platform api-key update ci \
    --policy '[[{"target":{"_tag":"Workspace"},"relationships":[]},["Workspace.listDeployments"]]]'
  ```

Give each script its own key with the smallest policy that works. A request that the policy doesn’t allow fails with `403`, and the operation in the [API reference](../reference/api.md#permissions) names the action it requires. A policy may grant only actions that you hold yourself.

Agents act as you

An agent that you connect via MCP acts as you, with exactly your permissions. Every connected agent appears under **Settings** → **Sessions** → **Agent sessions**, with when it connected and when it was last active.

Two safeguards apply to every agent. Before an agent deploys a configuration, the platform asks you to confirm, as a form in your client or in the conversation if your client can’t show forms. And secrets never pass through an agent: create them in the app or with `tenzir platform secret set`.

## Protect production branches

A deployment runs what its tracked branch holds, so whoever may write that branch decides what runs in production. Protect the branches that production deployments follow, so that committing, merging, pushing, renaming, or deleting them takes **Protected Branches** → **Write**:

* MCP

  Ask your agent:

  ```prompt
  Protect the branches main and release/* in the workspace prod.
  ```

* App

  Open the workspace’s settings, and add the patterns under **Protected branches** on the **General** page.

* CLI

  ```sh
  tenzir platform config branch protection set main 'release/*' --org acme --workspace prod
  ```

  The command replaces every pattern, so list all of them. Without a pattern, it lifts the protection from every branch.

A pattern’s `*` matches any characters but `/`, and `**` matches any characters. The built-in **Member** role can’t write protected branches, but can still draft changes on them and commit the draft to a new working branch made from the protected configuration, ready for someone with **Protected Branches** → **Write** to review and merge. Setting the patterns takes **Protected Branches** → **Change Protection**, which can lift any protection, so grant it as sparingly as **Owner**.

## Remove a member

Removing a member ends the membership and every role assignment at once, including those of a pending invitation, and with them the permissions of the member’s API keys and agents in your organization:

* MCP

  Ask your agent:

  ```prompt
  Remove jane@example.com from acme.
  ```

* App

  1. Open **Settings** → **IAM** → **People** and select the member.
  2. Select **Remove from organization**, or **Revoke invitation** for a pending one, and confirm.

* CLI

  ```sh
  tenzir platform organization member list --org acme
  tenzir platform organization member remove <member-id> --org acme
  ```

  The `list` command shows each member’s id, also for pending invitations.

* API

  ```sh
  curl -X DELETE -H "x-tenzir-api-key: $TENZIR_API_KEY" \
    https://platform.tenzir.com/api/organizations/acme/members/<member-id>
  ```

The same recovery rule applies: the platform refuses to remove the last member who can recover the organization. Any member may leave an organization on their own.

## Revoke access

Revoke access as soon as you no longer trust it:

| To revoke…           | Do this                                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| A member             | [Remove the member](control-access.md#remove-a-member) from the organization.                                       |
| A member’s role      | Remove the role on the member’s page under **Settings** → **IAM** → **People**, or run `tenzir platform organization role revoke <role> <member>`. |
| An agent             | Select **Disconnect** under **Settings** → **Sessions** → **Agent sessions**.                                                                      |
| Every agent of yours | Select **Disconnect all** in the same place.                                                                                                       |
| An API key           | Select **Revoke** on the key’s page under **Settings** → **API keys**, or run `tenzir platform api-key revoke <key>`.                              |
| A browser session    | Sign it out under **Settings** → **Sessions** → **User sessions**.                                                                                 |

A revoked agent or key fails on its next request.

## Next steps

Your organization now lets in exactly the people, scripts, and agents it should. Our IAM reference holds every permission for when you fine-tune a role, and our explanation of the platform shows how organizations, workspaces, and deployments fit together.

* [IAM](../reference/iam.md)
* [Platform](../explanations/platform.md)
* [Connect to Tenzir](connect-to-tenzir.md)
