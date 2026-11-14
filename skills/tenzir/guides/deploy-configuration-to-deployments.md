---
title: "Deploy configuration to deployments"
description: "Choose a tracked branch, deploy a configuration revision, and verify that a deployment accepted it."
canonical: https://tenzir.com/docs/guides/deploy-configuration-to-deployments
source: https://tenzir.com/docs/guides/deploy-configuration-to-deployments.md
section: "Docs"
---

# Deploy configuration to deployments

> Choose a tracked branch, deploy a configuration revision, and verify that a deployment accepted it.

A workspace stores its configuration in Git. Each deployment follows a branch and can either deploy new commits automatically or wait for you to deploy a revision. This guide shows you how to choose that behavior, deploy a commit, and verify that the deployment accepted it.

## Before you begin

You need a deployment and a committed configuration in its workspace. Select the organization, workspace, and deployment you intend to change in the platform.

Your organization role needs Deployments → Read, Configuration → Read, and Configuration → Deploy for the target workspace and deployment.

The CLI examples use the `tenzir` platform commands. Sign in with `tenzir auth login`, then select a target with `tenzir use <org>/<workspace>/<deployment>`. Replace `<deployment>` in the examples with a deployment ID, slug, or name in the selected workspace, or use a full `<org>/<workspace>/<deployment>` reference.

## Choose a deployment tracker

A **deployment tracker** selects the branch a deployment follows and whether Auto deploy is on. It belongs to the deployment, not to the branch you happen to be editing. Two deployments can follow different branches of the same workspace.

1. Open the deployment’s page.
2. In the Configuration card, select the branch to follow.
3. Turn Auto deploy on to deploy new commits automatically, or off to deploy only when you choose to.

Enabling automatic deployment, or changing the tracked branch while it is enabled, schedules deployment of the selected branch’s latest commit. Saving the tracker is not confirmation that the deployment accepted that configuration. Turning automatic deployment off keeps the accepted configuration, including when the deployment reconnects.

### Use the CLI or MCP

Read or update the tracker with:

```sh
tenzir deployment tracker get <deployment>
tenzir deployment tracker set <deployment> --branch main --auto-deploy true
```

You can pass `--branch`, `--auto-deploy true|false`, or both. An omitted setting stays unchanged. Invalid configurations or missing branches leave the previous tracker unchanged when you enable automatic deployment or change its branch while it is enabled.

With MCP, use `read_deployment_tracker` or `change_deployment_tracker`. Both take `org`, `workspace`, and `deployment`. The change tool accepts `branch`, `autoDeploy`, or both; omitted settings stay unchanged.

## Deploy the latest commit

With Auto deploy on, commits to the tracked branch deploy automatically. You can still deploy manually, for example to retry a failed attempt.

1. Check the selected deployment and its tracked branch.
2. In the deployment’s Configuration card, click Deploy.
3. Wait for the message “The deployment accepted the configuration.”

When Auto deploy is off, the topbar also offers Deploy once the tracked branch has commits that the deployment does not run yet. It shows a count when the platform knows how many, such as Deploy 3. This deploys the latest commit on the selected deployment’s tracked branch, not uncommitted edits or necessarily the branch open in your editor. It does not deploy each pending commit in sequence.

When Auto deploy is on, the topbar leaves deploying to the deployment and shows a notification instead. “Deployed” means that the deployment accepted the latest commit. “Not deployed” means that it refused the latest commit and names the reason. Until the next commit, the topbar keeps a Not deployed link to the deployment’s page.

Deploying the latest commit manually does not turn automatic deployment off.

## Deploy a revision from history

Use history to deploy a particular configuration without moving a branch or creating a revert commit.

1. Select the target deployment.
2. Open History and select the commit to deploy.
3. Click “Deploy this revision…”.
4. Read the confirmation dialog, then click “Deploy to …”, which names the selected deployment.

If automatic deployment is on and you choose a revision other than the latest commit on the tracked branch, the dialog turns automatic deployment off before deploying. This prevents new commits from replacing your chosen revision. If you choose the latest commit instead, automatic deployment stays on.

To resume following new commits, turn Auto deploy on again. This schedules the current branch tip, which may differ from the revision you deployed.

### Deploy a commit with the CLI

First read the current status:

```sh
tenzir deployment configuration status <deployment> --json
```

Copy the full commit SHA you want to deploy and the generation from the `deployed` revision, then run:

```sh
tenzir deployment configuration deploy <deployment> \
  --commit <full-commit-sha> \
  --expected-deployed-generation <generation>
```

Both flags are required. Use generation `0` if no configuration has been deployed. The expected generation prevents you from overwriting a concurrent deployment without noticing. On a conflict, read the status again and decide whether to retry with the new generation.

The commit must exist in the workspace repository, but does not need to belong to the tracked branch. The command waits for acceptance; with `--json`, it returns `{generation, commit, digest}`.

Unlike the history dialog, the CLI deploy command does not change the tracker. To keep a previous revision deployed, turn automatic deployment off first:

```sh
tenzir deployment tracker set <deployment> --auto-deploy false
```

## Verify the deployed configuration

The deployment’s Configuration card shows two revisions:

* Latest is the latest committed revision on the tracked branch.
* Deployed is the last configuration whose acceptance the platform confirmed.

The browser status updates live. A difference between these revisions can be intentional when automatic deployment is off, or can indicate a pending or failed deployment.

Inspect revision metadata with:

```sh
tenzir deployment configuration status <deployment>
```

Add `--json` for the `tracker`, `latest`, `deployed`, and `refused` fields. An absent revision is `null`. The deployed revision includes:

* The commit, which identifies the workspace revision.
* The generation, which identifies a configuration proposal. Failed proposals can leave gaps in generation numbers.
* The digest, which identifies the configuration’s contents.

Acceptance is not pipeline health

An accepted configuration does not confirm that its pipelines are running. Inspect pipeline status and diagnostics separately, as described in our guide to [inspecting a node](observability/inspect-a-node.md).
