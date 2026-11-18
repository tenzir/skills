---
title: "Platform"
description: "Understand how the platform organizes organizations, workspaces, and deployments, how deployments connect to it, and which data it sees."
canonical: https://tenzir.com/docs/explanations/platform
source: https://tenzir.com/docs/explanations/platform.md
section: "Docs"
---

# Platform

> Understand how the platform organizes organizations, workspaces, and deployments, how deployments connect to it, and which data it sees.

The **platform** is where you manage Tenzir. It stores the [configuration](configuration.md) of every workspace, delivers it to your [deployments](deployment.md), and shows what they do. Your events never pass through it: they flow from your sources through a deployment straight to your destinations.

The platform deploys configurations to the deployments in the data plane, which report metrics and status back. In the platform, an organization has members, roles, and billing, and holds workspaces with their configuration, deployments, secrets, ingest endpoints, access rules, and library. You and your agent reach the platform through the app, MCP, the CLI, and the API.

You reach the platform through four interfaces:

* The **app** in your browser, at [platform.tenzir.com](https://platform.tenzir.com).
* The **CLI**, the `tenzir` command on your machine, for working with a configuration as files and for shell scripts.
* The **API** for your own scripts, CI jobs, and services.
* The **MCP server** for your AI agent.

All four offer the same operations under the same permissions. Our guide on [connecting to Tenzir](../guides/connect-to-tenzir.md) sets up each of them.

## Organizations

An **organization** is the top level. It owns the workspaces and deployments, the subscription and its billing, and the list of its **members**, who join by invitation or through your company’s identity provider.

Each member has one or more roles. The built-in **Owner** role may do everything, the built-in **Member** role may work with the workspaces, and custom roles grant exactly the actions you choose. An API key acts for the member who created it and can narrow, but never widen, what that member may do. Our [IAM reference](../reference/iam.md) lists every role and action.

## Workspaces

A **workspace** groups deployments that share a purpose, such as production and staging for one team. It holds a configuration repository, the deployments that run it, and secrets. Secrets can also belong to the whole organization or to a single deployment, as our explanation of [secret owners](secrets.md#owners-and-readers) describes.

## Deployments

Every [deployment](deployment.md) belongs to exactly one workspace. Tenzir hosts it for you, in a size and region you pick, or you run it yourself in your own network. The platform shows each deployment’s pipelines with their state, throughput, and diagnostics, and which commit of the configuration it runs.

## How deployments connect

A deployment always opens the connection, so it needs no inbound port and no public address. It dials the platform’s gateway over a WebSocket and authenticates with its **deployment key**, which the platform issues and `tenzir up` keeps for you. This works behind firewalls and NAT, as long as the deployment reaches the platform over HTTPS.

The platform sends its requests back through this connection. Each request carries a short-lived token that the platform signs for this deployment and this request, so a deployment acts only on requests from its own platform.

The platform sees what it needs to manage your deployments, and little else:

* **Configurations** flow to the deployment, along with requests to start and stop pipelines.
* **Secrets** flow to the deployment when a pipeline asks for one, encrypted for that request.
* **Telemetry** flows to the platform: how many events and bytes each pipeline reads and writes, when a pipeline starts, finishes, or fails, and the diagnostics that pipelines report.
* **Events of ad-hoc pipelines** flow to the platform, which holds only the most recent ones, so that the Explorer and `tenzir run -r` can show them.

When the connection drops, the deployment keeps running its pipelines and reconnects, as our explanation of [deployments without the platform](deployment.md#when-the-platform-is-unreachable) describes.

## See also

* [Configuration](configuration.md)
* [Deployment](deployment.md)
* [Quickstart](../guides/quickstart.md)
* [Control access](../guides/control-access.md)
* [IAM](../reference/iam.md)
