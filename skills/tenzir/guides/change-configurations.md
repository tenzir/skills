---
title: "Change configurations"
description: "Change what your deployments run, review the change, take it to a deployment automatically or by hand, try it on a staging branch, and roll it back when it goes wrong."
canonical: https://tenzir.com/docs/guides/change-configurations
source: https://tenzir.com/docs/guides/change-configurations.md
section: "Docs"
---

# Change configurations

> Change what your deployments run, review the change, take it to a deployment automatically or by hand, try it on a staging branch, and roll it back when it goes wrong.

Every pipeline that runs in production started as a change to a configuration. Because a configuration is a Git repository, each change is a commit that you can review before it ships, deploy when you choose, and undo when it misbehaves. This guide walks a change through its whole life: write it, review it, deploy it, try it on a staging branch first, fix a refused deploy, roll it back, and check what the deployment runs.

Before you begin

* You need a [deployment](add-a-deployment.md). A new one follows the branch `main` with **Auto deploy** on, so every commit to `main` reaches it.
* The built-in **Member** role grants every step except writing a protected branch. Our [IAM reference](../reference/iam.md#permissions-in-the-app) lists the permission behind each step.
* For the CLI steps, sign in with `tenzir auth login` and select a target with `tenzir use <org>/<workspace>/<deployment>`.

## Change the configuration

Every change to a configuration ends as a commit on a branch of its repository. In the app and via MCP, you first collect your edits in your personal **draft** of the branch, which nobody else sees and which changes nothing until you commit it:

* MCP

  Ask your agent for the change:

  ```prompt
  Write a pipeline that keeps only Suricata alerts with severity 1 and publishes them to the topic "alerts". Add it to my configuration on main, but don't commit it yet.
  ```

  The agent writes the change into your draft of the branch, so that you can review it in the next step.

* App

  1. Use the path picker in the top bar (available on every page) to select a deployment or a branch. The picker lists each configuration with the deployments that run it beneath, followed by other branches (each showing `off <origin>` when made from a configuration) and **New branch…**.
  2. Open **Files** under **Configuration** in the sidebar.
  3. Edit a file, or select **Create file** to add one, such as `pipelines/alerts.tql`. The editor saves your changes into your draft of the branch as you type.
  4. To throw the draft away, select **Discard** in the top bar.

  When you select a branch without a deployment, runtime pages under **Deployment** stay clickable and tell you they need a deployment. The **Pipelines** page shows each pipeline’s **Pipeline** name, its **File** path, and (when the branch has an origin) a **Changes** column marking pipelines **Added**, **Modified**, or **Deleted** compared with the origin configuration, including your uncommitted edits. Pipelines that merging the branch would delete appear struck through below the branch’s pipelines.

* CLI

  Clone the configuration to edit it with your own editor and Git:

  ```sh
  tenzir config clone prod
  cd tenzir-workspace
  ```

  * tenzir-workspace/

    * pipelines/

      * onboard-suricata.tql

    * contexts/

      * …

    * package.yaml

    * package.lock

  Add or edit files, and add the packages that your pipelines use with `tenzir package add`, as our guide on [managing packages](manage-packages.md) shows. Nothing leaves your machine until you apply the change.

Our reference on the [directory layout](../reference/directory-layout.md) lists every file a configuration may contain.

## Review and commit the change

Look at the change before it becomes a commit, and once more before it reaches a deployment:

* MCP

  Ask your agent:

  ```prompt
  Show me what my draft on main changes, then commit it with the message "Publish severe Suricata alerts".
  ```

  For a commit that exists already, ask for its diff, such as “What changed in the last commit on main?”.

* App

  1. Open **History**. Your draft appears at the top, marked **Draft**, above the branch’s commit graph.
  2. Select the draft or a commit to see the files it changes, each with its diff.
  3. Select **Commit** in the top bar to open the commit review.
  4. When you have permission to write the branch, your draft commits directly to it by default. On a configuration, you can instead select **Commit to a new branch** to commit your draft to a new working branch made from that configuration (which runs nowhere until merged back). When you may not write the configuration, such as a protected branch, committing to a new branch is the only option.

* CLI

  Review the change with Git, then commit and push it:

  ```sh
  git diff
  tenzir config apply -m 'Publish severe Suricata alerts'
  ```

  The `config apply` command commits every change in the clone and pushes it to the branch the workspace serves, or the one that `--branch` names. To review a commit that someone else pushed, read its changed files and the diff of one of them:

  ```sh
  git pull
  git log --format='%H %s' -5
  tenzir platform config log --commit <full-commit-sha>
  tenzir platform config log --commit <full-commit-sha> --path pipelines/alerts.tql
  ```

With **Auto deploy** on, the commit now goes to every deployment that follows the branch. The next sections show how to choose that.

## Choose what the deployment follows

A **deployment tracker** selects the branch that a deployment follows and whether **Auto deploy** is on. It belongs to the deployment, not to the branch you edit, so two deployments can follow different branches of the same workspace:

* MCP

  Ask your agent:

  ```prompt
  Make edge-1 follow the branch main and deploy new commits automatically.
  ```

* App

  1. Open the deployment’s page.
  2. In the **Configuration** card, select the branch to follow.
  3. Turn **Auto deploy** on to deploy new commits automatically, or off to deploy only when you choose to.

* CLI

  ```sh
  tenzir deployment info <deployment>
  tenzir deployment configuration follow <deployment> --branch main
  ```

  Add `--manual` to follow the branch with **Auto deploy** off.

Turning **Auto deploy** on, or changing the branch while it is on, deploys the branch’s latest commit. Turning it off keeps what the deployment runs. Our CLI reference lists [every rule of the tracker](../reference/cli.md#deployment-trackers).

## Deploy the latest commit

With **Auto deploy** on, every commit to the tracked branch deploys automatically. With it off, or to retry a failed attempt, deploy by hand:

* MCP

  Ask your agent:

  ```prompt
  Deploy the latest commit of main to edge-1.
  ```

  The platform asks you to confirm before the agent deploys.

* App

  1. Open the deployment’s page and check its tracked branch.
  2. In the **Configuration** card, select **Deploy**.
  3. Wait for the message “The deployment accepted the configuration.”

  With **Auto deploy** off, the top bar also offers **Deploy** once the tracked branch has commits that the deployment doesn’t run yet, with a count when the platform knows how many, such as **Deploy 3**. **Deploy** only appears on a deployment with **Auto deploy** off that is behind its branch; on a working branch selected alone, the top bar offers **Merge** instead. **Deploy** delivers the latest commit of the selected deployment’s tracked branch, not uncommitted edits, and not each pending commit in turn.

  With **Auto deploy** on, the top bar shows a notification instead: *Deployed* means that the deployment accepted the latest commit, and *Not deployed* means that it refused it and names the reason.

* CLI

  Deploy the latest commit of the tracked branch:

  ```sh
  tenzir deployment configuration deploy <deployment>
  ```

  The command refuses a deployment with **Auto deploy** on. It returns once the deployment accepted the configuration. If another deploy happened in between, it fails with a conflict: read the status with `tenzir deployment configuration status <deployment>` and retry.

Deploying the latest commit by hand doesn’t turn **Auto deploy** off.

## Try a change on a staging branch

To test a change on one deployment before production sees it, give the test deployment a branch of its own. Production keeps following `main` while you iterate on the branch:

* MCP

  Ask your agent:

  ```prompt
  Create a branch staging from main in the workspace prod, and make the deployment edge-staging follow it with auto deploy on.
  ```

  Then ask for changes on `staging` as on any other branch.

* App

  1. Open the test deployment’s page.
  2. In the **Configuration** card, open the branch list and select **New branch…**.
  3. Name the branch, such as `staging`, pick `main` as its **Base**, and create it. The deployment follows the new branch from then on.
  4. Select `staging` in the top bar and change files as before.

* CLI

  Create the branch and point the test deployment at it:

  ```sh
  tenzir platform config branch create staging --base main
  tenzir deployment configuration follow edge-staging --branch staging
  ```

  Switch your clone to the branch, then change and apply as before:

  ```sh
  git fetch origin
  git switch staging
  tenzir config apply --branch staging -m 'Try the new alert filter'
  ```

Once the change works on the test deployment, bring it to `main` by merging the branch in the app (see [Merge a branch into a configuration](change-configurations.md#merge-a-branch-into-a-configuration)) or with Git, such as `git switch main`, `git merge staging`, and `tenzir config apply` in your clone. If `main` is protected, merging into it takes **Protected Branches** → **Write**, as our guide on [protecting production branches](control-access.md#protect-production-branches) explains.

## Merge a branch into a configuration

When you commit changes to a working branch (such as one created via **Commit to a new branch** or pushed with Git), merge it into a configuration to ship those commits:

* MCP

  Ask your agent:

  ```prompt
  Merge my branch alice/main into its configuration in the workspace prod.
  ```

  The `merge_workspace_configuration_branch` tool defaults the target to the branch’s recorded origin when you don’t name one, asks you to confirm when deployments follow the target automatically, and returns the merge commit along with which deployments run the target branch and whether each deploys it automatically.

* App

  1. Select the working branch in the top-bar picker.

  2. Select **Merge** in the top bar to open the **Merge into …** dialog.

     * If the branch was made from a configuration, that origin configuration is preselected.
     * If the branch has no recorded origin (for example, a branch pushed with Git), choose the target configuration from the list.

  3. Review the commits the merge brings, and select **Show diff** to inspect all their changes together against the target configuration.

  4. If you still have uncommitted edits on the branch, commit them first: only commits merge.

  5. Check the summary of which deployments will deploy the merge automatically and which require **Deploy** by hand, and decide whether to keep **Delete `<branch>` once merged** selected (enabled by default; the branch is kept if someone committed to it in the meantime).

  6. Select **Merge**.

* CLI

  Merge into the branch’s recorded origin and delete the merged branch afterward:

  ```sh
  tenzir platform config branch merge alice/main --delete
  ```

  Pass `--into <branch>` when the branch has no recorded origin (for example, a branch pushed with Git), `-m <message>` to customize the merge commit message, or `--expected <commit-sha>` to pin a specific reviewed tip. Without `--expected`, the command pins the merge (and `--delete`) to the tip it reads before merging so unseen commits aren’t merged or deleted.

Merging requires `WorkspaceBranch.merge` on the target branch (included in **Configuration** → **Write** for unprotected branches and **Protected Branches** → **Write** for protected branches). Merging updates the configuration branch; whether each deployment tracking that branch deploys the result automatically or waits for **Deploy** depends on its **Auto deploy** setting.

## Manage branches

View, rename, and delete workspace branches from the **Branches** page, the CLI, or MCP:

* MCP

  Ask your agent:

  ```prompt
  Rename the branch alice/main to alice/suricata-alerts in the workspace prod.
  ```

  You can also ask your agent to list, create, merge, or delete branches.

* App

  1. Open **Branches** under **Platform** in the sidebar. The table lists each configuration with the deployments that run it and the branches made from it nested beneath, followed by **Other branches**.
  2. To rename a branch, select the rename (pencil) button on its row, enter the new name, and select **Rename branch**. Renaming keeps the branch’s commits, its origin, any branches made from it (which then point to the new name), and every user’s saved draft on it. If you have unsaved edits on that branch or edits kept only in your browser, save or resolve them before renaming.
  3. To delete a branch, select the delete button on its row and confirm. Deleting a branch also removes every user’s draft on it.

  Both renaming and deleting are refused while any deployment tracks the branch: point those deployments at another branch first.

* CLI

  ```sh
  tenzir platform config branch create alice/suricata-alerts --base main
  tenzir platform config branch rename alice/suricata-alerts alice/suricata-v2
  tenzir platform config branch merge alice/suricata-v2 --delete
  tenzir platform config branch delete alice/suricata-v2
  ```

When someone renames a branch (through the app, REST API, MCP, or CLI), the platform remembers the rename and forwards the old name to the new one, including across chained renames. Other open browser tabs and saved links holding the old name follow the rename automatically to the same page on the new branch. Saved drafts move with the branch. Edits that a browser hasn’t saved yet stay with the old name, which is why the app waits to rename a branch until your own edits on it are saved. Forwarding ends once another branch is created or pushed with the old name, or once the renamed branch is deleted.

Renaming a branch requires `WorkspaceBranch.rename` on the branch and `WorkspaceBranch.create` on the new name, both subject to branch protection. Deleting a branch requires `WorkspaceBranch.delete`, also subject to branch protection.

## Fix a refused deploy

A deployment refuses a configuration as a whole when a file can’t become a configuration, such as a malformed context or a lock that doesn’t fit the manifest. It then keeps running what it ran before, and the status names the reason:

* MCP

  Ask your agent:

  ```prompt
  Why didn't the latest commit deploy to edge-1? Fix it on main.
  ```

* App

  The top bar shows *Not deployed* with the reason, and the deployment’s **Configuration** card shows the revision it still runs.

* CLI

  ```sh
  tenzir deployment configuration status <deployment>
  ```

  The output ends with `refused` and the reason when the latest commit didn’t deploy.

Fix the cause in a new commit on the tracked branch. With **Auto deploy** on, that commit deploys on its own. Otherwise, deploy it as the section on [deploying the latest commit](change-configurations.md#deploy-the-latest-commit) shows. A refusal concerns only the latest commit: once the branch moves on, the status drops it. A lost connection is no refusal, and the platform retries by itself.

## Deploy a revision from history

Deploy an older revision to roll back fast, without moving a branch or creating a revert commit:

* MCP

  Ask your agent:

  ```prompt
  Show me the last five commits of main, then deploy the one before my last change to edge-1, and turn auto deploy off.
  ```

* App

  1. Select the target deployment.
  2. Open **History** and select the commit to deploy.
  3. Select **Deploy this revision…**.
  4. Read the confirmation dialog, then select **Deploy to …**, which names the selected deployment.

  If **Auto deploy** is on and you choose a revision other than the latest commit of the tracked branch, the dialog turns **Auto deploy** off, so that new commits don’t replace your chosen revision.

* CLI

  Find the full SHA of the commit in your clone, then turn **Auto deploy** off and deploy it:

  ```sh
  git log --format='%H %s' -10
  tenzir deployment configuration follow <deployment> --branch <branch> --manual
  tenzir deployment configuration deploy <deployment> --commit <full-commit-sha>
  ```

  Unlike the history dialog, the deploy command doesn’t change the tracker, and it refuses a deployment with **Auto deploy** on, so turn **Auto deploy** off first.

The commit must exist in the workspace’s repository, but needn’t belong to the tracked branch. To resume following new commits, turn **Auto deploy** on again, which deploys the branch’s latest commit.

## Revert a change

A deployed revision from history is a stopgap: the branch still holds the change, and the next deploy brings it back. To undo the change for good, revert its commit on the branch:

* MCP

  Ask your agent:

  ```prompt
  Revert the commit "Publish severe Suricata alerts" on main, show me the draft, and commit it once I agree.
  ```

* App

  1. Open **History** and select the commit.
  2. Select **Revert…**, then **Create revert draft**. The app opens your draft of the branch with the change undone.
  3. Review the draft and commit it from the top bar.

  For a commit that a draft can’t revert, a merge commit or the branch’s first commit, the dialog shows the Git commands instead.

* CLI

  In your clone, on the branch that holds the commit:

  ```sh
  git pull
  git revert <full-commit-sha>
  tenzir config apply
  ```

The revert is a new commit, so **Auto deploy** delivers it like any other. If you deployed a revision from history and turned **Auto deploy** off, turn it on again after the revert.

What a deploy does to pipelines

When a deployment accepts a configuration, it starts every pipeline in the configuration’s `pipelines/` folder that isn’t [`disabled`](../reference/directory-layout.md#pipelines), and stops the pipelines that the configuration no longer contains.

A later deploy runs a pipeline again only when it compiles to something else, because you edited it or a package that it uses changed. It then restarts a running or failed pipeline with the new definition. A pipeline that finished or that you stopped stays that way and takes the new definition for its next start. Our explanation of [what a deploy guarantees](../explanations/configuration.md#what-a-deploy-guarantees) covers the details.

## Start and stop a pipeline

Start or stop a pipeline of the configuration without changing the configuration:

* MCP

  Ask your agent:

  ```prompt
  Stop the pipeline pipelines/onboard-suricata.tql on edge-1.
  ```

  If a stop doesn’t finish, ask the agent to force it.

* App

  Select **Start**, **Stop**, or **Force stop** on the deployment’s pipeline list or on the pipeline’s page.

* CLI

  ```sh
  tenzir pipeline start pipelines/onboard-suricata.tql --deployment <deployment>
  tenzir pipeline stop pipelines/onboard-suricata.tql --deployment <deployment>
  tenzir pipeline stop pipelines/onboard-suricata.tql --deployment <deployment> --force
  ```

A start runs the deployed definition, not pending changes on the branch. A stop lets the pipeline drain its events, and a forced stop ends it at once, also one that is stopping already, losing the events in flight. To keep a pipeline from starting with the next deploy, mark it [`disabled`](../reference/directory-layout.md#pipelines) in the configuration instead.

## Verify the deployed configuration

Check that the deployment runs what you expect, and that its pipelines are healthy:

* MCP

  Ask your agent:

  ```prompt
  Which commit does edge-1 run, is it behind main, and do any of its pipelines report errors?
  ```

* App

  The deployment’s **Configuration** card shows two revisions:

  * **Latest** is the latest commit of the tracked branch.
  * **Deployed** is the last configuration whose acceptance the platform confirmed.

  The deployment’s pipeline list shows each pipeline’s state and errors.

* CLI

  ```sh
  tenzir deployment configuration status <deployment>
  tenzir pipeline list --deployment <deployment>
  tenzir pipeline diagnostics pipelines/alerts.tql --deployment <deployment>
  ```

A difference between the latest and the deployed revision is intentional when **Auto deploy** is off, and otherwise points to a pending or refused deploy. An accepted configuration doesn’t confirm that its pipelines run: a pipeline that doesn’t compile fails on its own while the rest of the configuration runs. Our CLI reference describes [every field of the status](../reference/cli.md#configuration-status).

## Next steps

Your pipelines can now reach production safely. Most of them call operators from packages, which our guide on [managing packages](manage-packages.md) adds, updates, and pins.

* [Manage packages](manage-packages.md)
* [Configuration](../explanations/configuration.md)
* [CLI](../reference/cli.md)
