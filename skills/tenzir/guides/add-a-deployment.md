---
title: "Add a deployment"
description: "Add a deployment that runs your pipelines, hosted by Tenzir or on your own machine or server, keep it running and up to date, find out why it doesn't connect, and delete it when you no longer need it."
canonical: https://tenzir.com/docs/guides/add-a-deployment
source: https://tenzir.com/docs/guides/add-a-deployment.md
section: "Docs"
---

# Add a deployment

> Add a deployment that runs your pipelines, hosted by Tenzir or on your own machine or server, keep it running and up to date, find out why it doesn't connect, and delete it when you no longer need it.

A [deployment](../explanations/deployment.md) is where your pipelines run. Tenzir can host it for you, so you have one running within minutes, or you run it yourself, next to your data, on a server, in a container, or on your laptop. Either way it is the same program, and the platform manages it the same way. This guide adds both kinds, checks that they connect, keeps them running and up to date, and deletes them when their job is done.

Before you begin

* Your role needs **Deployments** → **Write** to add, change, and delete deployments, and **Deployments** → **Diagnose** to troubleshoot them. The built-in **Member** role grants both.
* For the CLI steps, [install Tenzir](installation.md), sign in with `tenzir auth login`, and select a workspace with `tenzir use <org>/<workspace>`.

## Choose where it runs

Pick where your deployment runs:

| Aspect      | Tenzir-hosted                                     | Self-hosted                                   |
| ----------- | ------------------------------------------------- | --------------------------------------------- |
| Who runs it | Tenzir, in the type and cloud region you pick     | you, on any machine that reaches the platform |
| Data access | sources and destinations reachable from the cloud | everything in your network                    |
| Edition     | Enterprise                                        | every edition                                 |
| Start       | one step, it connects on its own                  | `tenzir up` or Docker on your machine         |
| Updates     | one step in the app, the CLI, or via MCP          | where it runs                                 |
| Ingest      | reads ingest endpoints, in `europe-west3`         | cannot read ingest endpoints yet              |

A self-hosted deployment only dials out to the platform, so it needs no inbound ports. Every new deployment follows the branch `main` of its workspace’s configuration and deploys each new commit automatically.

## Add a Tenzir-hosted deployment

* MCP

  Ask your agent:

  ```prompt
  Create a Tenzir-hosted deployment named edge-1 in my workspace prod. Show me the available types and regions first.
  ```

  The agent lists the types with their vCPUs, memory, and rates, and creates the deployment once you choose.

* App

  1. Open **Deployments** and select **New deployment**.
  2. Select **Tenzir-hosted**, then pick a name, a type, and a region.
  3. Select **Start deployment**.

* CLI

  List the types and regions, then create the deployment:

  ```sh
  tenzir deployment types
  tenzir deployment create edge-1 --hosted --type small --region europe-west3
  ```

  Without `--type`, the deployment takes the default type that `deployment types` marks, and without `--region`, the first region.

The deployment starts right away and connects to the platform within a minute or two. It runs until you delete it, and on Enterprise it accrues the credits per hour of its type while it runs.

## Run a deployment on your machine

The `tenzir` command runs a deployment on your machine and connects it to the platform. Start a deployment by name. A name that no deployment of the workspace carries creates a new one:

```sh
tenzir up laptop
```

The deployment runs in the foreground and prints its log until you press Ctrl-C, which lets its pipelines finish. A second Ctrl-C stops it at once. To keep it running in the background, add `-d`, and stop it later with `tenzir down`:

```sh
tenzir up laptop -d
tenzir down laptop
```

The command fetches the deployment’s key on the first start and keeps it, with the deployment’s state, under `~/.local/state/tenzir/deployments/`. A later `tenzir up laptop` continues where the deployment left off.

## Run a deployment on a server

On a server, you may not want to sign in with your own account. Create the deployment in the app instead, and let the server redeem a one-time key link:

1. Open **Deployments**, select **New deployment**, then **Self-hosted**, pick a name, and select **Continue**.

2. In the install dialog, choose how the server runs the deployment:

   * **Install with Docker** shows a `curl … | sh` command that writes a `tenzir/docker-compose.yaml` in the current directory and starts the deployment in a container.
   * **Already installed** shows a `tenzir up --init '<link>'` command for a server with the `tenzir` command installed.

3. Run the command on the server within 15 minutes.

The link works once. The deployment keeps the key it redeems, so later starts need no link.

## Keep it running across reboots

A deployment that Tenzir hosts restarts on its own. For a self-hosted one, let the server’s service manager start it:

* **Docker:** the container restarts unless you stop it, so it comes back whenever the Docker daemon starts. Enable the daemon at boot, such as with `systemctl enable docker`.
* **`tenzir up`:** run it as a systemd service. When systemd sets `$STATE_DIRECTORY`, as `StateDirectory=` does, the command keeps the key and the state under `$STATE_DIRECTORY/deployments/` instead of your home directory.

For the systemd service, redeem the key link into the service’s state directory once, and stop the deployment with Ctrl-C once it connects:

```sh
sudo env STATE_DIRECTORY=/var/lib/tenzir "$(which tenzir)" up --init '<link>'
```

Then add a unit that runs the deployment. Use the absolute path that `which tenzir` prints:

/etc/systemd/system/tenzir.service

```ini
[Unit]
Description=Tenzir deployment
Wants=network-online.target
After=network-online.target


[Service]
ExecStart=/usr/local/bin/tenzir up
StateDirectory=tenzir
Restart=on-failure
TimeoutStopSec=60


[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl enable --now tenzir
```

Without an argument and without a selected workspace, `tenzir up` runs the only deployment that has state in the directory. On a stop, systemd sends `SIGTERM`, which lets the pipelines finish like the first Ctrl-C.

## Check that it connects

* MCP

  Ask your agent:

  ```prompt
  List the deployments of my workspace prod and when each was last seen.
  ```

* App

  Open **Deployments**. The **Last seen** field of each deployment reads *now* while it is connected.

* CLI

  ```sh
  tenzir deployment list
  tenzir status
  ```

  A connected deployment reads `yes` under `REACHABLE`. The `status` command also shows the deployments that run on this machine.

Once it connects, the deployment runs the configuration of its workspace.

## Find out why it doesn’t connect

A deployment that never shows up, or that drops off, tells you why in its diagnosis and its logs:

* MCP

  Ask your agent:

  ```prompt
  Diagnose the deployment edge-1 and show me its latest error logs.
  ```

* App

  Open the deployment’s page. The **Diagnosis** card shows whether the deployment answers, and its **Latest logs** show what it logged.

* CLI

  ```sh
  tenzir deployment diagnose edge-1
  tenzir deployment logs edge-1 --levels error,warning
  ```

  For a Tenzir-hosted deployment, `--source kubernetes` and `--source pod` read the events and the output of its container instead.

On your own machine, `tenzir up` in the foreground prints the same log as it runs, and `tenzir up -d` appends it to the file `log` in the deployment’s state directory. A deployment needs to reach the platform over HTTPS, so check proxies and firewalls first. An install command or key link that expired or was used already needs a new one: on the deployment’s page, select **Install** or **Reinstall**, then **Show install command** or **Issue install command**.

## Change or update a Tenzir-hosted deployment

Change the type of a Tenzir-hosted deployment when it needs more or less capacity, and update it when the platform offers a newer version. Both restart the deployment:

* MCP

  Ask your agent:

  ```prompt
  Change edge-1 to the type medium, then update it if it runs an older version.
  ```

* App

  On the deployment’s page, select **Change type** and pick the new type. Select **Update available** when the page offers it.

* CLI

  ```sh
  tenzir deployment change-type edge-1 medium
  tenzir deployment update edge-1
  ```

  The `update` command follows the restart until the deployment is back. Add `-d` to return right away.

On Enterprise, the deployment accrues the rate of its new type from the change. A deployment that the organization’s usage limit suspended resumes only when you resume it, with **Resume deployment** on its page or `tenzir deployment resume edge-1`.

## Update a self-hosted deployment

A self-hosted deployment is updated where it runs, the same way you installed it. When the platform offers a newer version, the deployment’s page shows **Update available**, and its dialog names the current and the available version. Update to the available version, then restart the deployment:

* Docker

  In the directory where you ran the install command, set the `image` of the `deployment` service in `tenzir/docker-compose.yaml` to the available version, such as `ghcr.io/tenzir/tenzir:v7.0.1-slim`, then restart it:

  ```sh
  docker compose --file tenzir/docker-compose.yaml up --detach
  ```

  The deployment keeps its key and its state in the `state` volume.

* Homebrew

  ```sh
  brew upgrade --cask tenzir
  tenzir down && tenzir up -d
  ```

* Debian and RPM

  Install the newer package as our guide on [installing Tenzir](installation.md#install-a-system-package) shows, then restart the deployment, such as with `sudo systemctl restart <unit>` for a systemd service.

* uv

  ```sh
  uv tool upgrade tenzir
  tenzir down && tenzir up -d
  ```

* Kubernetes

  Set the image of the deployment’s container to the available version where you define the workload, such as in your manifest or Helm values, and roll it out as usual.

A deployment in the foreground restarts with Ctrl-C and another `tenzir up`. The deployment’s page shows when it runs the new version.

## Delete a deployment

Deleting a deployment removes it and its metrics from the platform. A connected deployment stops and removes its pipelines first:

* MCP

  Ask your agent:

  ```prompt
  Delete the deployment laptop.
  ```

* App

  1. Open the deployment’s page.
  2. In the **Delete deployment** card, select **Delete**, then confirm with **Delete deployment**.

* CLI

  ```sh
  tenzir deployment delete laptop
  ```

The platform stops a deployment that it hosts. A self-hosted installation stays on its host but can no longer connect, so remove it there: run `tenzir down laptop` and delete its folder under `~/.local/state/tenzir/deployments/`, or for Docker, run `docker compose down --volumes` in its `tenzir` directory. Deleting can’t be undone.

## Next steps

Your deployment is running. Give it something to do: our guide on [changing configurations](change-configurations.md) takes your first pipeline to it and keeps it current.

* [Change configurations](change-configurations.md)
* [Deployment](../explanations/deployment.md)
* [CLI](../reference/cli.md)
