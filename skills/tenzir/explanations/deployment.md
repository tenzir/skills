---
title: "Deployment"
description: "Understand what a deployment runs, which states its pipelines go through, how it survives restarts, and how it keeps working when the platform is unreachable."
canonical: https://tenzir.com/docs/explanations/deployment
source: https://tenzir.com/docs/explanations/deployment.md
section: "Docs"
---

# Deployment

> Understand what a deployment runs, which states its pipelines go through, how it survives restarts, and how it keeps working when the platform is unreachable.

A **deployment** runs the pipelines and contexts of one [configuration](configuration.md). It belongs to a workspace on the [platform](platform.md), which delivers the configuration and shows what the deployment does, while your events stay on the deployment. Tenzir hosts it for you, or you run it yourself on a server, in a container, or on your machine with `tenzir up`. Either way it is the same program.

Sources send data into a deployment’s pipelines. A deployment runs configured pipelines, which write to your destinations, and ad-hoc pipelines, which return their results to the platform. Contexts serve both. The platform deploys the configuration to the deployment, which reports metrics and status back, and its Explorer runs ad-hoc pipelines. The deployment keeps its state in an object store, the pipeline states and the persisted contexts, and restores it from there after a restart. You and your agent reach the platform.

## What a deployment runs

A deployment runs three kinds of things:

* **Configured pipelines** come from the `pipelines/` folder of the configuration. They keep running across restarts and change only through a new configuration.
* **Contexts** come from the `contexts/` folder and hold reference data that pipelines [enrich](enrichment.md) events with. Their content lives in the deployment, and a new configuration keeps every context that it still declares, with its content.
* **Ad-hoc pipelines** run once, for looking at data, from the Explorer or `tenzir run -r`. Our explanation of [where pipelines run](pipeline.md#where-pipelines-run) compares them with configured pipelines.

## Pipeline states

Every configured pipeline is in one of five states:

| State      | Meaning                                                         |
| ---------- | --------------------------------------------------------------- |
| `running`  | The pipeline processes events.                                  |
| `stopping` | The pipeline was asked to stop and drains its open work.        |
| `finished` | The pipeline ran out of input and ended on its own.             |
| `failed`   | The pipeline ended with an error, which its state records.      |
| `stopped`  | Someone stopped the pipeline, or the configuration disables it. |

You can start and stop a configured pipeline without changing the configuration, with **Start** and **Stop** in the app or with `tenzir deployment start-pipeline` and `stop-pipeline`. A stop is graceful: the pipeline finishes the events it holds before it ends. The deployment never restarts a failed pipeline on its own, so it stays failed until you start it again or a new configuration changes it.

The platform can also suspend a whole deployment, for example when an organization reaches its usage limit. A suspended deployment runs no pipelines but remembers their states, and resuming it starts the ones that were running.

## State survives restarts

A deployment keeps everything that must survive a restart in one object store: a local directory, Amazon S3, Google Cloud Storage, or Azure Blob Storage. It needs no database and no other disk. The store holds the configurations the deployment accepted, the state of each pipeline, and the content of persisted contexts. The deployment updates it atomically, so a crash never leaves half-written state.

A deployment that restarts, or a new instance on the same store, therefore picks up where the last one left off. It starts every pipeline that was running and restores the persisted contexts.

## When the platform is unreachable

A deployment needs the platform to receive new configurations, but not to run the one it has. When its [connection](platform.md#how-deployments-connect) drops, it keeps running its pipelines and reconnects in the background.

Secrets are the exception. Pipelines resolve them through the platform, so a pipeline that starts during an outage, for example after a restart, cannot get its secrets. A deployment that [buffers secrets](secrets.md#resolution) receives them ahead of time and starts its pipelines without the platform.

## See also

* [Configuration](configuration.md)
* [Platform](platform.md)
* [Secrets](secrets.md)
* [Quickstart](../guides/quickstart.md)
* [Add a deployment](../guides/add-a-deployment.md)
* [Contexts](../reference/contexts.md)
