---
title: "CLI"
canonical: https://tenzir.com/docs/reference/cli
source: https://tenzir.com/docs/reference/cli.md
section: "Docs"
---

# CLI

> The tenzir command runs pipelines on your machine and on your deployments, runs a deployment on your machine, and does everything the platform offers from a terminal, under the same permissions as the app, the API, and the MCP server. This page lists its settings and commands. Our guide on connecting to Tenzir installs it.

The `tenzir` command runs pipelines on your machine and on your deployments, runs a deployment on your machine, and does everything the [platform](../explanations/platform.md) offers from a terminal, under the same permissions as the app, the [API](api.md), and the [MCP server](mcp.md). This page lists its settings and commands. Our guide on [connecting to Tenzir](../guides/connect-to-tenzir.md) installs it.

Run `tenzir` without arguments for the commands most people start with, `tenzir help --all` for every command, and `tenzir help <command>` for the subcommands, flags, and examples of one. Agents learn the command the same way.

## Settings

Every command that talks to the platform reads these settings:

| Setting      | Flag             | Environment           | Default                       |
| ------------ | ---------------- | --------------------- | ----------------------------- |
| Platform URL | `--url`          | `TENZIR_PLATFORM_URL` | `https://platform.tenzir.com` |
| API key      | `--api-key-file` | `TENZIR_API_KEY`      | none                          |
| Bearer token | `--token`        | `TENZIR_TOKEN`        | the saved sign-in             |
| Target       | none             | `TENZIR_TARGET`       | what `tenzir use` selected    |

An API key or a token that you pass explicitly wins over the saved sign-in, and `tenzir auth logout` doesn’t clear credentials from the environment. Keep an API key in a file or an environment variable, so that it doesn’t end up in your shell history.

These flags work with every command:

| Flag        | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| `--json`    | Print what the platform answered as JSON instead of a table. |
| `--verbose` | Show technical details for errors.                           |
| `--refresh` | Ask the platform again what it publishes about itself.       |

The command keeps your sign-in and selection under `$XDG_STATE_HOME/tenzir/platform`, by default `~/.local/state`.

## Targets

Most commands act on an organization, a workspace, or a deployment. Select one with `tenzir use`, and the commands fall back to it when you leave off `--org`, `--workspace`, `--deployment`, `--on`, or the deployment name of a `tenzir deployment` command:

```sh
# Select a workspace and a deployment in it.
tenzir use acme/prod/edge-1
# Switch to another deployment of the same workspace.
tenzir use edge-2
# Show the selection, the sign-in, and the deployments on this machine.
tenzir status
```

A deployment goes by its id, its slug, or its name when only one carries it. A name or a flag always wins over the selection, and `tenzir use --` clears it.

To act on another target in one shell or script without changing the selection, set `TENZIR_TARGET` to `<org>/<workspace>` or `<org>/<workspace>/<deployment>`. It takes precedence over what `tenzir use` selected, so a command acts on what it names, else on `TENZIR_TARGET`, else on the selection. `tenzir use` and `tenzir status` say when the target comes from `TENZIR_TARGET`:

```sh
TENZIR_TARGET=acme/staging/canary tenzir deployment info
```

## Commands

A bare `tenzir` shows the commands most people start with:

```text
Get started
  auth login                              Sign in to the Tenzir Platform
  up -d [<name>]                          Run a deployment in the background
  ask '<question>'                        Ask the Tenzir Assistant


Run on this machine
  run [-f <file>] <tql> ...               Run a pipeline locally
  config clone [<workspace>]              Clone a workspace's configuration
  package add <id>[@<versions>]           Use a package in the clone, and lock it


Work with the platform
  use [<org>/<workspace>[/<deployment>]]  Select the deployment to work with
  pipeline list                           List the pipelines of the selected deployment
  run -r [-f <file>] <tql> ...            Run on the selected deployment


More commands
  run  up  down  config  package  pipeline  ask  auth  use  status  deployment  platform
```

The top-level commands are for daily work: running pipelines and deployments, the clone of a configuration, and the deployments and pipelines on the platform. The `tenzir platform` commands set up an account and an organization, and work with the history and branches of a configuration on the platform.

### Run pipelines

| Command                                   | Description                                                 |
| ----------------------------------------- | ----------------------------------------------------------- |
| `tenzir run [-f <file>] <tql>`            | Runs a pipeline on this machine.                            |
| `tenzir run -r [--on <deployment>] <tql>` | Runs a pipeline once on a deployment and prints its events. |

#### `tenzir run`

Without `-r`, the pipeline runs in the `tenzir` process itself and needs no deployment and no sign-in. The command completes an open pipeline with standard input and standard output:

* A pipeline that starts with a source and ends with a sink runs as written.
* A pipeline without a source reads JSON events from standard input.
* A pipeline that starts with a parser, such as `read_yaml`, reads bytes from standard input.
* A pipeline without a sink writes its events to standard output as TQL, or as bytes when it ends with a printer, such as `write_csv`.

```sh
tenzir run 'from_file "events.json" { read_json } | to_file "events.csv" { write_csv }'
echo '{"x":1}' | tenzir run 'select x | head'
cat input.yaml | tenzir run 'read_yaml | select x | write_csv'
tenzir run -f pipeline.tql
```

A pipeline on your machine can call the packages of the configuration in the current directory once `tenzir package fetch` downloaded them.

#### `tenzir run -r`

With `-r`, the pipeline runs once on a deployment as an ad-hoc pipeline, and the command prints its events as JSON, one per line, until it ends. Ctrl-C stops it. The pipeline starts with a source and has no sink, because its events go to you. It runs on the selected deployment unless `--on` names another.

```sh
tenzir run -r 'demo::suricata | where event_type == "alert" | head 100'
tenzir run -r --on acme/prod/edge-1 -f query.tql | jq .
```

The pipeline can call the operators of every package in the deployment’s configuration. The command exits non-zero unless the pipeline ran out of events. Our explanation of [where pipelines run](../explanations/pipeline.md#where-pipelines-run) lists when an ad-hoc pipeline ends.

### Manage a configuration

| Command                                                | Description                                                                                                             |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `tenzir config clone [<workspace>] [--branch <name>]`  | Clones a workspace’s configuration, by default into `tenzir-workspace`.                                                 |
| `tenzir config apply [-m <message>] [--branch <name>]` | Commits every change in the working copy and pushes it to the branch the workspace serves, or the one `--branch` names. |
| `tenzir package <command>`                             | Adds, updates, and removes [packages](cli.md#packages).                               |

The `config apply` command refuses a push that isn’t a fast-forward. Named no workspace, it pushes to the one the working copy was cloned from. With `--branch`, it pushes to that branch and creates it if the workspace has none of that name. After the push, it names the deployments that deploy it by themselves. With auto deploy on, a push to the tracked branch deploys, as the section on [deploying](cli.md#deploying) and our guide on [changing configurations](../guides/change-configurations.md) show. The [`tenzir platform config`](cli.md#manage-the-platform) commands work with the history and branches of a configuration without a clone.

### Run a deployment on this machine

| Command                      | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| `tenzir up [<deployment>]`   | Runs a deployment in the foreground until you interrupt it.  |
| `tenzir up -d`               | Runs it in the background.                                   |
| `tenzir up --init <link>`    | Runs the deployment that a key link from the platform names. |
| `tenzir down [<deployment>]` | Stops a deployment that runs in the background.              |

Without an argument, `tenzir up` runs the selected deployment, or with nothing selected, the only deployment that has state on this machine. A name that no deployment of the selected workspace carries creates a new one. The command fetches the deployment’s key on first start and keeps it, with the deployment’s state, readable by you alone:

| Condition                       | State directory                                                                        |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| systemd sets `$STATE_DIRECTORY` | `$STATE_DIRECTORY/deployments/`                                                        |
| otherwise                       | `$XDG_STATE_HOME/tenzir/deployments/`, by default `~/.local/state/tenzir/deployments/` |

Each deployment has a folder there with its `key`, its `store/`, and, while it runs in the background, its `pid` and `log`. The command mints a new key only when it has none or the platform refuses the stored one.

A key link needs no sign-in: the platform issues it for one deployment, and it works once, within 15 minutes. The first Ctrl-C or `SIGTERM` lets the pipelines finish, and a second one stops the deployment at once. The `tenzir down` command waits up to ten seconds for the pipelines to finish. Our guide on [adding a deployment](../guides/add-a-deployment.md) runs one and keeps it running across reboots.

### Manage pipelines

The `tenzir pipeline` commands act on the selected deployment, or on the one that `--deployment` names.

| Command                                                  | Description                                                                                                                             |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `tenzir pipeline list`                                   | Lists the pipelines with their state and run, which counts up on every start. With only a workspace selected, lists every deployment’s. |
| `tenzir pipeline start <pipeline>`                       | Starts the deployed definition of a pipeline, such as `pipelines/ingest.tql`.                                                           |
| `tenzir pipeline stop <pipeline> [--force]`              | Stops a pipeline and lets it drain. With `--force`, ends it at once and loses the events in flight.                                     |
| `tenzir pipeline diagnostics <pipeline>`                 | Shows why a pipeline misbehaves.                                                                                                        |
| `tenzir pipeline metrics <pipeline>`                     | Shows what a pipeline read and wrote, by default over the last 24 hours.                                                                |
| `tenzir pipeline inspect channels <pipeline>`            | Shows the channels of a running pipeline.                                                                                               |
| `tenzir pipeline inspect events <pipeline> <channel>...` | Prints the events that flow through channels of a running pipeline.                                                                     |

Starting and stopping a pipeline doesn’t change the configuration.

### Manage deployments

| Command                                                       | Description                                                                                                                                             |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deployment list`                                             | Lists the deployments with their version, whether an update is available, whether they’re reachable, and when each was last seen.                       |
| `deployment info [<deployment>]`                              | Shows a deployment’s details, load, CPU and memory, and the branch it follows.                                                                          |
| `deployment create [<name>]`                                  | Registers a deployment that you run yourself. With `--hosted`, Tenzir runs it, in `--type` and `--region`.                                              |
| `deployment types`                                            | Lists the types and regions of Tenzir-hosted deployments, with vCPUs, memory, and rates.                                                                |
| `deployment resize [<deployment>] --type <type>`              | Runs a Tenzir-hosted deployment as another type, which restarts it.                                                                                     |
| `deployment update [<deployment>] [--version <v>] [-d]`       | Runs a Tenzir-hosted deployment on the version the platform offers, which restarts it.                                                                  |
| `deployment resume [<deployment>]`                            | Resumes a deployment that the usage limit suspended, once the limit allows it.                                                                          |
| `deployment settings [<deployment>]`                          | Shows the name, the slug, and whether the deployment buffers secrets. `--name`, `--slug`, and `--resilience on\|off` change them.                       |
| `deployment rotate-token [<deployment>]`                      | Mints a new key and stops the current one at once.                                                                                                      |
| `deployment delete <deployment>`                              | Deletes a deployment and its metrics. A self-hosted installation stays on its host.                                                                     |
| `deployment diagnose [<deployment>]`                          | Shows whether the deployment answers, its uptime, and whether log retrieval works.                                                                      |
| `deployment logs [<deployment>]`                              | Reads the deployment’s logs, newest first, by default the latest 10.                                                                                    |
| `deployment contexts [<deployment>]`                          | Lists the contexts on a deployment.                                                                                                                     |
| `deployment configuration status [<deployment>]`              | Reads the [configuration status](cli.md#configuration-status).                                                        |
| `deployment configuration follow [<deployment>] --branch <b>` | Changes the branch that the deployment [follows](cli.md#deployment-trackers). With `--manual`, turns auto deploy off. |
| `deployment configuration deploy [<deployment>]`              | [Deploys](cli.md#deploys) the tip of the followed branch, or with `--commit` any commit.                              |

The `deployment` commands that act on one deployment take it the way `tenzir use` does, and act on the selected deployment when you leave it off. `deployment delete` is the exception and always needs the deployment named.

The `deployment update` command reads the version the platform offers the deployment, as `deployment list` shows it, and updates to that version. It fails without changing anything when no update is on offer. With `--version <version>`, it updates to that version without reading the deployment first, which needs only the `Deployment.update` permission together with `-d`.

The `deployment logs` command takes `--source application`, the default, or `kubernetes` and `pod` for a Tenzir-hosted deployment, and filters with `--from`, `--to`, `--levels` (`trace`, `debug`, `info`, `warning`, `error`, `critical`), `--search`, and `--limit`. It needs `Deployment.diagnose`.

### Manage the platform

| Command                               | Subcommands                                                                                                              |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `tenzir auth`                         | `login`, `logout`                                                                                                        |
| `tenzir platform account`             | `sessions`, `delete`                                                                                                     |
| `tenzir platform organization`        | `list`, `memberships`, `create`, `update`, `leave`, `delete`, `audit-log`, `usage`, `cost`, `plan`, `credits`, `budget`  |
| `tenzir platform organization role`   | `list`, `get`, `create`, `update`, `delete`, `assign`, `revoke`                                                          |
| `tenzir platform organization member` | `list`, `invite`, `remove`                                                                                               |
| `tenzir platform workspace`           | `list`, `create`, `update`, `delete`, `metrics`                                                                          |
| `tenzir platform api-key`             | `list`, `create`, `update`, `revoke`                                                                                     |
| `tenzir platform secret`              | `list`, `set`, `delete`                                                                                                  |
| `tenzir platform endpoint`            | `list`, `get`, `create`, `update`, `delete`, `rotate-token`, `token`, `test`, `resume`, `metrics`, `buffer`, `consumers` |
| `tenzir platform config`              | `log`, `branch`                                                                                                          |

The `auth login` command prints a URL to sign in with, which also works when the browser runs on another machine. The `platform api-key create` and `deployment rotate-token` commands print a secret once, and nothing reads it back. The `platform api-key create --policy <json>` flag sets the key’s [policy](iam.md#policies), and without it, the key may only read its own account.

The `platform organization member list` command shows each member’s id, which `platform organization member remove`, `platform organization role assign`, and `platform organization role revoke` take. The `platform organization member invite <label>` command prints the link that admits the invitee, once.

The `platform config` commands work on a workspace’s configuration on the platform, without a clone:

| Command                                                                     | Description                                                                                                                                                                                                                                |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `tenzir platform config log [--branch <branch>]`                            | Lists the commits of a branch, by default `main`, newest first.                                                                                                                                                                            |
| `tenzir platform config log --commit <commit> [--path <path>]`              | Shows a commit and the files it changes, compared with its first parent, or with `--path` the patch of one file.                                                                                                                           |
| `tenzir platform config branch create <name>`                               | Creates a branch from the tip of `--base <branch>`, or with `--empty` from an empty commit.                                                                                                                                                |
| `tenzir platform config branch rename <name> <new-name>`                    | Renames a branch, keeping its commits, its origin, branches made from it, and every draft on it, and forwards the old name to the new name. Refused while a deployment tracks the branch.                                                  |
| `tenzir platform config branch merge <branch> [--into <branch>] [--delete]` | Merges a branch into a configuration branch, defaulting `--into` to its recorded origin. With `--expected <sha>`, merges only if the branch is at that commit. With `--delete`, deletes the merged branch afterward unless it moved since. |
| `tenzir platform config branch delete <name>`                               | Deletes a branch and every draft on it. Refused while a deployment tracks the branch.                                                                                                                                                      |
| `tenzir platform config branch protection set [<pattern>…]`                 | Replaces the patterns of the protected branches. No pattern protects no branch.                                                                                                                                                            |

The `platform config log --commit` flag takes a full commit SHA. Creating a branch never changes a deployment’s tracker. The `platform config branch merge` command also accepts `-m <message>` (`--message`) to customize the merge commit message; when `--delete` is passed and deleting the branch fails afterward (for example, because another commit landed on it), the merge stands and the output notes why the branch was kept.

### Use with AI

| Command                   | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `tenzir ask '<question>'` | Asks the Tenzir Assistant and prints its answer. |

## Deploying

A deploy takes a commit of a workspace’s configuration to one deployment. Our explanation of [what a deploy guarantees](../explanations/configuration.md#what-a-deploy-guarantees) describes what the deployment does with it.

### Deployment trackers

Each deployment has a tracker, which `deployment info` and `deployment configuration status` show and `deployment configuration follow --branch <branch> [--manual]` changes:

| Field       | JSON key     | Default for a new deployment | Meaning                                                      |
| ----------- | ------------ | ---------------------------- | ------------------------------------------------------------ |
| Branch      | `branch`     | `main`                       | The branch of the workspace’s configuration that it follows. |
| Auto deploy | `autoDeploy` | `true`                       | Whether each new commit on the branch deploys automatically. |

These rules apply:

* Without `--manual`, auto deploy is on.
* Turning auto deploy on, or changing the branch while it is on, deploys the branch’s latest commit.
* Turning auto deploy off keeps the configuration that the deployment runs, also when it reconnects.
* When a deployment with auto deploy on connects and runs something other than its branch’s latest commit, the platform deploys that commit.
* Saving the tracker confirms the setting, not that the deployment accepted a configuration.
* An invalid configuration or a missing branch leaves the previous tracker unchanged.

### Configuration status

The `deployment configuration status` command shows what a deployment follows and runs. With `--json`, it prints these keys:

| Key                   | Content                                                                                                                                                          |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tracker`             | The [tracker](cli.md#deployment-trackers): `branch` and `autoDeploy`.                                                          |
| `latest`              | The full SHA of the tracked branch’s latest commit, or `null`.                                                                                                   |
| `deployed`            | The last revision whose acceptance the platform confirmed, or `null` if none.                                                                                    |
| `deployed.commit`     | The commit of that revision.                                                                                                                                     |
| `deployed.generation` | The number of the deploy that delivered it. It grows with every deploy, and failed attempts leave gaps.                                                          |
| `deployed.digest`     | The identity of the revision’s contents.                                                                                                                         |
| `deployed.behind`     | The number of commits on the tracked branch since the deployed one. Absent when the deployed commit isn’t an ancestor of the latest, such as after a force-push. |
| `refused`             | Why the latest commit didn’t deploy, absent otherwise: `commit`, `message`, and `refusedAt`.                                                                     |

A refusal means that the commit’s files can’t become a configuration, or that the deployment rejected the configuration they made. It concerns only the latest commit and disappears once the branch moves on. A lost connection is no refusal, because the platform retries. The deployed revision stays until the deployment accepts another one. The table output shows the same fields, including the refusal’s message.

### Deploys

The `deployment configuration deploy` command deploys a commit by hand:

| Flag                                          | Description                                                                                                                |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `--commit <sha>`                              | The full SHA of any commit in the workspace’s repository, on any branch. Defaults to the tip of the followed branch.       |
| `--expected-deployed-generation <generation>` | The `deployed.generation` from the status, or `0` if nothing was deployed. Defaults to the generation the deployment runs. |

These rules apply:

* The command returns once the deployment accepted the configuration, and fails when the deployment refuses it or doesn’t confirm it.
* When the deployed generation is no longer the expected one, because another deploy happened in between, the command fails with a conflict. If the deployment has accepted the same commit in the meantime, the command returns that revision instead.
* Unless you pass both flags, the command refuses a deployment with auto deploy on, so follow its branch with `--manual` first. It changes neither the tracker nor the branch. Deploying an older commit with auto deploy on lasts only until the next commit on the branch.
* Every deploy gets a higher generation, and a deployment takes only a configuration with a higher generation than the one it runs, so a delayed or repeated delivery never rolls it back.

## Packages

The `tenzir package` commands add, update, and remove the packages that a configuration or a package uses. They edit the [manifest](manifest.md), write the [lock](lock.md), and fill the package cache that `tenzir run` reads. Our guides on [installing a package](../guides/manage-packages.md#install-a-package) and [updating packages](../guides/manage-packages.md#update-packages) put them to use.

| Command                                                                            | Description                                                 |
| ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [`package list`](cli.md#tenzir-package-list)     | Lists the locked packages.                                  |
| [`package add`](cli.md#tenzir-package-add)       | Declares a package and locks it.                            |
| [`package remove`](cli.md#tenzir-package-remove) | Drops a package from the manifest and the lock.             |
| [`package update`](cli.md#tenzir-package-update) | Moves packages to their newest accepted versions.           |
| [`package lock`](cli.md#tenzir-package-lock)     | Brings the lock in line with a manifest edited by hand.     |
| [`package fetch`](cli.md#tenzir-package-fetch)   | Downloads the locked packages into the cache.               |
| [`package search`](cli.md#tenzir-package-search) | Searches the packages of our library or another repository. |

The commands take a package by its [id](manifest.md#the-id).

### Where the package commands work

The commands change only the files in your working copy. They commit and push nothing: [`tenzir config apply`](../explanations/configuration.md#every-change-is-a-commit) takes the changes to the configuration, and the next deploy ships them. The help text of the commands calls a configuration a *workspace*.

Every command but `package search` works on a manifest and a lock:

* **The manifest** is the nearest `package.yaml` at or above the current directory, or the directory that `--directory` names. That is a configuration’s manifest, or a package’s, as our reference on the [package manifest](manifest.md#package-or-configuration) tells them apart.
* **The root**, which holds `package.lock`, is the configuration when the manifest is the configuration’s own, or that of a package directly under the configuration’s `packages/`. Any other package is a root of its own, with its `package.lock` next to its `package.yaml`.

| You run the command in…               | It edits…                      | It locks in…                        |
| ------------------------------------- | ------------------------------ | ----------------------------------- |
| a configuration                       | `package.yaml`                 | `package.lock`                      |
| `packages/myteam/` of a configuration | `packages/myteam/package.yaml` | `package.lock` of the configuration |
| a package of its own                  | the package’s `package.yaml`   | the package’s `package.lock`        |

Without a `package.yaml` at or above the directory, the commands stop. To start a configuration that uses packages, write a `package.yaml` that holds `dependencies:`. The commands refuse to write through a symbolic link, so `package.yaml`, `package.lock`, `packages/`, and every folder on the way to the manifest must be no links.

Every command that writes `package.lock` resolves the requirements first, as our reference on [package dependencies](dependencies.md#resolution) describes, and fills the package cache afterwards. It writes `package.yaml` only when it changes what the manifest declares, and keeps the file’s comments and layout.

### Common flags

| Flag                      | Commands         | Description                                                       |
| ------------------------- | ---------------- | ----------------------------------------------------------------- |
| `--directory <directory>` | all but `search` | Work in this directory instead of the current one. It must exist. |
| `--json`                  | all              | Print the result as JSON instead of a table.                      |

With `--json`, the commands that print locked packages print a JSON array of [lock entries](lock.md#entries), with the same keys as in `package.lock`.

### Package commands

#### `tenzir package list`

```text
tenzir package list [--directory <directory>] [--json]
```

Lists the packages that `package.lock` pins: the dependencies and what they need in turn. For each, it prints the id, the version, the source, which is `library` for our library and the URL otherwise, and the commit, shortened to 12 characters. The command reads only the lock and needs no network.

```text
$ tenzir package list
ID        VERSION  SOURCE   COMMIT
suricata  0.2.0    library  e8956fbbbc70
```

#### `tenzir package add`

```text
tenzir package add <id>[@<requirement>] [--git <url>] [--rev <rev>] [--path <path>]
                   [--directory <directory>] [--json]
```

Declares a package under `dependencies` in the manifest and locks it, with everything it needs, in `package.lock`. It copies nothing into the configuration.

| Argument or flag | Description                                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `<id>`           | The package id, such as `suricata`.                                                                                                        |
| `@<requirement>` | The [version requirement](dependencies.md#version-requirements) to accept, such as `suricata@^0.2`.      |
| `--git <url>`    | The repository to take the package from, such as `https://…`, or `file:///…` on your machine. Defaults to our library.                     |
| `--rev <rev>`    | A commit, tag, or branch to [pin the package to](dependencies.md#pinned-revisions) instead of a release. |
| `--path <path>`  | A package of the configuration under `packages/`, relative to the manifest that names it.                                                  |

What the command writes depends on what you give it:

* Without a requirement, `--rev`, or `--path`, it accepts the newest release that is no pre-release and the later ones compatible with it: a caret on that version, such as `^0.2.0`. A package without such a release fails, and the message suggests `--rev`.
* With a requirement, it writes that requirement. For a package that the manifest declares already, this changes which versions it accepts, and the lock moves only if the locked version no longer fits.
* With `--rev`, it writes `git` and `rev`, and the requirement only if you give one.
* With `--path`, it writes only `path`, which takes no requirement, `--git`, or `--rev`. A package of its own, outside a configuration, can’t use `--path`.

A package that the manifest declares already fails without a requirement, `--git`, `--rev`, or `--path`, and the message suggests `package update` or `package add <id>@<versions>`. With one of them, the new entry replaces the old one.

```sh
# The newest release of our library.
tenzir package add suricata
# Accept 0.1.x, or move to it.
tenzir package add suricata@^0.1
# A release from another repository.
tenzir package add acme_firewall --git https://github.com/acme/tenzir-packages.git
# A branch instead of a release.
tenzir package add suricata --git https://github.com/tenzir/library.git --rev main
# A package of the configuration.
tenzir package add myteam --path packages/myteam
```

The command resolves in [lock mode](dependencies.md#modes) and prints the entry that it locked for the package.

#### `tenzir package remove`

```text
tenzir package remove <id> [--directory <directory>] [--json]
```

Drops the package from the manifest’s `dependencies`, and from `package.lock` together with the packages that only it needed. The manifest must declare the package. Other locked versions stay as they are. The command prints the remaining locked packages.

```sh
tenzir package remove suricata
```

#### `tenzir package update`

```text
tenzir package update [<id>] [--latest] [--directory <directory>] [--json]
```

Moves every package, or the named one and the packages it needs, to the newest version that the requirements accept. The id must be declared in the manifest or locked, so you can update a package that only another package uses. Without `--latest`, only `package.lock` changes. A package [pinned to a branch](dependencies.md#pinned-revisions) moves to the branch’s latest commit.

With `--latest`, the command also moves a package to its newest stable release when the requirement in `package.yaml` accepts only older ones, such as `^0.0.1` or the pin `=1.0.0`. It then rewrites the requirement to `^<newest>`, which accepts the newest release and compatible ones after it, edits `package.yaml`, and resolves the lock. Without an id, `--latest` leaves packages pinned with `=` as they are, as Cargo does. Naming a package lifts its pin. You can also change a requirement yourself with `package add <id>@<requirement>`.

```sh
# Every package.
tenzir package update
# Only suricata and what it needs.
tenzir package update suricata
# Newest stable release, even past the requirement.
tenzir package update suricata --latest
```

The command resolves in [update mode](dependencies.md#modes) and prints the locked packages.

#### `tenzir package lock`

```text
tenzir package lock [--directory <directory>] [--json]
```

Locks what the manifests ask for after you edited `package.yaml` by hand, keeping every locked version that still fits. It also writes a lock that the platform refused as [stale](lock.md#stale-locks). The manifests stay as they are.

```sh
tenzir package lock
```

#### `tenzir package fetch`

```text
tenzir package fetch [--locked] [--directory <directory>] [--json]
```

Downloads every package that `package.lock` pins into the [package cache](lock.md#package-cache) that `tenzir run` reads, and checks each against its hash. Packages that the cache holds already, with files that match their hash, aren’t fetched again.

| Flag       | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| `--locked` | Fail when `package.lock` is stale, instead of locking anew. |

Without `--locked`, a stale lock is locked anew in lock mode, as with `package lock`, before the packages are fetched. With `--locked`, the command changes no file, which suits CI and a fresh clone of a configuration:

```sh
tenzir package fetch --locked
```

#### `tenzir package search`

```text
tenzir package search [<query>] [--git <url>] [--rev <rev>] [--json]
```

Searches the packages of our library, or of another repository, that a configuration can use. It needs no manifest.

| Argument or flag | Description                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------------------ |
| `<query>`        | Words to look for in the id, name, description, and categories. Without it, the command lists every package. |
| `--git <url>`    | The repository to search. Defaults to our library.                                                           |
| `--rev <rev>`    | A commit, tag, or branch to list the packages at, released or not.                                           |

A package matches when every word of the query appears in its id, name, description, or categories, ignoring case. Without `--rev`, the command lists the packages with a release, as of their newest release. With `--rev`, it lists the packages in the repository’s top-level folders and at its root at that revision. For each, it prints the id, the name, the newest release that is no pre-release, or else the newest pre-release, and the categories. With `--json`, it prints an array of objects with the keys `id`, `name`, `latest`, and `categories`.

```sh
# Every package of our library.
tenzir package search
# Packages about OCSF.
tenzir package search ocsf
# The packages on the main branch of our library, released or not.
tenzir package search --rev main
```

### Packages in the app

The **Packages** page of the app makes the same changes as `package add`, `package update`, `package remove`, and `package lock`, in your draft of the selected branch, which you then review and commit. Picking a package’s latest version writes a caret requirement, and picking an older one writes an exact requirement with `=`. Our guide on [installing a package](../guides/manage-packages.md#add-a-package) shows the page.
