---
title: "Configuration"
description: "Understand how a workspace keeps its pipelines, contexts, and packages in a Git repository, and what a deploy guarantees when a commit reaches a deployment."
canonical: https://tenzir.com/docs/explanations/configuration
source: https://tenzir.com/docs/explanations/configuration.md
section: "Docs"
---

# Configuration

> Understand how a workspace keeps its pipelines, contexts, and packages in a Git repository, and what a deploy guarantees when a commit reaches a deployment.

A **configuration** is the set of files that a [deployment](deployment.md) runs: its pipelines, its contexts, and the packages those pipelines use. Each workspace keeps its configuration in a Git repository on the [platform](platform.md), so every change is a commit, and a deploy brings a commit to a deployment.

## What a configuration contains

A configuration is a folder of plain files:

* pipelines/

  * onboard-suricata.tql

  * routing/

    * to-splunk.tql

* contexts/

  * threat-indicators.yaml

* packages/

  * acme/ a package written in this repository

    * …

* package.yaml

* package.lock

- **Pipelines** live in `pipelines/`, one `.tql` file per pipeline, in subfolders if you like. The path of the file identifies the pipeline. An optional [frontmatter](../reference/directory-layout.md#pipelines) sets the name the platform shows and whether the pipeline starts at all.
- **Contexts** live in `contexts/`, one YAML file per context, as the [contexts reference](../reference/contexts.md) describes.
- **Packages** provide operators and constants that the pipelines call. The repository’s `package.yaml` lists the packages it depends on, and `package.lock` pins the exact version of each. A package you write yourself lives under `packages/`. Our explanation of [packages in a configuration](packages.md#packages-in-a-configuration) covers how the two files work together.

Our reference on the [directory layout](../reference/directory-layout.md) lists every file a configuration may contain.

## Every change is a commit

Because the configuration is a Git repository, its history is the history of everything your deployments run. You see who changed what and when, compare commits, and review a change before it reaches production. Every way to change a configuration ends in a commit:

* In the app, the configuration editor keeps a personal **draft** for each branch. It saves as you type and changes nothing until you commit it. When you have permission to write a configuration, you commit to it directly by default, or choose **Commit to a new branch** in the commit review. When you may not write a configuration, such as a protected branch, committing to a new branch is the only option.
* On your machine, `tenzir config clone` clones the repository, and `tenzir config apply` commits your changes and pushes them back. Any Git client works as well.
* An AI agent [connected via MCP](../guides/connect-to-tenzir.md) writes drafts for you to review and commit.

## Branches and deployments

Each deployment **tracks** one branch of the repository, `main` by default. A branch that one or more deployments track is a **configuration**; other branches are working branches that run nowhere on their own.

With **auto deploy** on, every new commit on a tracked branch deploys right away, and a deployment that reconnects while behind its branch gets the latest commit as well. With auto deploy off, the deployment keeps what it runs until you deploy a commit by hand.

Several deployments can track the same branch, or different ones, for example `staging` for a test deployment and `main` for production. A workspace can **protect** branches by name pattern, so that only members with the right permission can commit, merge, push, rename, or delete them.

When you create a working branch from a configuration, the repository records that configuration as the branch’s **origin** (shown as `<branch> off <origin>` in the top bar). Once your changes on the working branch are committed, you merge it back into its origin configuration, and the deployments tracking that configuration pick up the merge commit according to their auto deploy setting.

In the app, **Branches** under **Platform** lists every configuration with the deployments that run it and the working branches made from it, followed by other branches. **History** displays the branch’s commit graph so merged branches appear alongside the main line.

## What a deploy guarantees

A deploy brings one commit to one deployment. The platform bundles the commit’s files with the packages that its lock pins, and the deployment checks the result before it changes anything. This makes every deploy safe in four ways:

In the platform, a commit on a tracked branch starts a deploy: the platform checks the files and the lock and builds an archive with the locked packages and a manifest. It deploys that configuration to the deployment, which validates it and keeps the previous configuration if it is not valid. Otherwise the deployment stores the archive and applies it by starting, restarting, and stopping pipelines.

* **All or nothing.** A configuration with any problem, such as a malformed context or a lock that doesn’t fit `package.yaml`, is refused as a whole, and the deployment keeps running the previous one unchanged. The one exception is a pipeline that doesn’t compile: the deploy goes through, and only that pipeline fails with the error.
* **Never backward.** Every deploy gets a higher **generation** number, and a deployment takes only a configuration newer than the one it runs. A delayed or repeated delivery therefore cannot roll it back.
* **Only what changed restarts.** The deployment compares what each pipeline compiles to, including the package operators it calls and the secrets it buffers, with the running one. New pipelines start, removed ones stop, and changed ones restart. A change that compiles to the same pipeline, such as a new comment, restarts nothing. A pipeline that finished or that you stopped takes its new definition when it next starts.
* **No events lost between pipelines.** New subscribers attach before old pipelines stop, and old pipelines stop from upstream to downstream, so the events that a stopping [`publish`](../reference/operators/publish.md) still sends reach their [`subscribe`](../reference/operators/subscribe.md).

Acceptance means that the deployment runs the new configuration, not that every pipeline in it is healthy. The pipeline list shows each pipeline’s state and error.

A rollback is a deploy like any other. Deploy an older commit, and it gets a new generation, so the deployment takes it while the branch stays as it is. To undo a change on the branch itself, revert the commit, and auto deploy delivers the revert. Our guide on [changing configurations](../guides/change-configurations.md#revert-a-change) shows both.

## See also

* [Deployment](deployment.md)
* [Packages](packages.md)
* [Quickstart](../guides/quickstart.md)
* [Change configurations](../guides/change-configurations.md)
* [Declare contexts](../guides/enrich/declare-contexts.md)
* [Directory Layout](../reference/directory-layout.md)
