---
title: "Start adhoc pipeline"
description: "Runs a pipeline once on a deployment, to look at the events it produces."
canonical: https://tenzir.com/docs/reference/api/pipelines/start-adhoc-pipeline
source: https://tenzir.com/docs/reference/api/pipelines/start-adhoc-pipeline.md
section: "Docs"
---

# Start adhoc pipeline

> Runs a pipeline once on a deployment, to look at the events it produces.

`POST /api/users/{userId}/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/adhoc-pipelines`

Runs a pipeline once on a deployment, to look at the events it produces. The pipeline begins with a source and has no sink. It ends when it runs out of events, when it produces more than an ad-hoc pipeline may, when it is stopped, or when nobody has read it for a minute. The user named in the path owns it and its start allowance. Requires DeploymentUser.startAdhocPipeline for that deployment and user. Requesting operator sources also requires Deployment.streamPipelineGraph on the deployment. Reading and stopping it require their own permissions; built-in organization roles restrict these to its owner.

Authentication: `bearer` + `session` + `apiKey` + `key`.

## Path parameters

* `userId` (`string<uuid>`, required): The platform's own identifier for a user. Pattern: `^([0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}|00000000-0000-0000-0000-000000000000|[fF]{8}-[fF]{4}-[fF]{4}-[fF]{4}-[fF]{12})$`.

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `workspace` (`Id / Slug`, required): A workspace identified by its ID or slug within an organization

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `deploymentId` (`Id / Slug`, required): A deployment identified by its ID or slug within a workspace

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Request body (`application/json`, required)

* `includeSources` (`boolean`, optional): Include operator source files in the response. Requires Deployment.streamPipelineGraph.
* `definition` (`string`, required): The pipeline in TQL. It has to begin with a source and produce events: no sink, and no writer that turns them into bytes

## Responses

### `201`: Tenzir.AdhocPipeline.StartedAdhocPipeline

Media type: `application/json`

* `adhocPipelineId` (`string`, required): The id the platform gave an ad-hoc pipeline when it started it

* `sources` (`Sources`, optional): What the pipeline compiled from: the definition, and each user-defined operator it calls. Absent when the deployment does not send them

  * `sources` (`array<SourceFile>`, required)

    Array items:

    * `id` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.
    * `origin` (`string`, required)
    * `text` (`string`, required)

  * `callSites` (`array<CallSite>`, required): Call site IDs are one-based indices into this array; zero means top-level

    Array items:

    * `begin` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `end` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `sourceIndex` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `callsiteIndex` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `calleeIndex` (`integer`, optional): The id of the source the call expands into: the definition of the operator it calls. Absent from a deployment that predates it. Range: `>= 0, <= 9007199254740991`.

### `400`: InvalidPipeline | CredentialConflict | Validation

Media type: `application/json`

Any of:

* **InvalidPipeline** (`InvalidPipeline`)

  * `_tag` (`"InvalidPipeline"`, required)

  * `message` (`string`, required)

  * `diagnostics` (`array<Ad-hoc Pipeline Diagnostic>`, optional)

    Array items:

    * `severity` (`enum`, required) Allowed values: `note`, `warning`, `error`.

    * `message` (`string`, required)

    * `rendered` (`string`, required): The diagnostic as the engine prints it, source excerpt included

    * `notes` (`array<Diagnostic Note>`, required)

      Array items:

      * `kind` (`string`, required)
      * `message` (`string`, required)

    * `annotations` (`array<Diagnostic Annotation>`, required): Byte offsets into the definition, or into the user-defined operators it calls, that the diagnostic points at

      Array items:

      * `primary` (`boolean`, required)
      * `text` (`string`, required)
      * `begin` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.
      * `end` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.
      * `callsiteIndex` (`integer`, optional): The call of a user-defined operator the span is in, as an index into the call sites the pipeline compiled to, so that `begin` and `end` count from the start of the operator's definition. Zero, or absent, when the span is in the definition itself. Range: `>= 0, <= 9007199254740991`.

  * `sources` (`Sources`, optional): The text a compiled pipeline comes from: its own, and the definition of each user-defined operator it calls, with every call between them

    * `sources` (`array<SourceFile>`, required)

      Array items:

      * `id` (`integer`, required) Range: `>= -9007199254740991, <= 9007199254740991`.
      * `origin` (`string`, required)
      * `text` (`string`, required)

    * `callSites` (`array<CallSite>`, required): Call site IDs are one-based indices into this array; zero means top-level

      Array items:

      * `begin` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `end` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `sourceIndex` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `callsiteIndex` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `calleeIndex` (`integer`, optional): The id of the source the call expands into: the definition of the operator it calls. Absent from a deployment that predates it. Range: `>= 0, <= 9007199254740991`.

* **CredentialConflict** (`CredentialConflict`)

  * `_tag` (`"CredentialConflict"`, required)
  * `message` (`string`, required)

* **Validation** (`Validation`)

  * `_tag` (`"Validation"`, required)
  * `message` (`string`, required)

### `401`: Unauthenticated

Media type: `application/json`

* `_tag` (`"Unauthenticated"`, required)
* `message` (`string`, required)

### `403`: Unauthorized

Media type: `application/json`

* `_tag` (`"Unauthorized"`, required)
* `message` (`string`, required)

### `404`: NotFound

Media type: `application/json`

* `_tag` (`"NotFound"`, required)

### `409`: UsageRestricted | DeploymentSuspended

Media type: `application/json`

Any of:

* **UsageRestricted** (`UsageRestricted`)

  * `_tag` (`"UsageRestricted"`, required)
  * `message` (`string`, required)
  * `resolution` (`string`, required)
  * `state` (`enum`, required): The state of a deployment, from least to most restricted. `locked`: its pipelines keep running, but no configuration change reaches it, which includes starting, stopping, pausing and deleting pipelines, no ad-hoc pipeline starts on it, and it cannot run as a larger type; deleting it and downsizing it still work. It ends on its own once usage is back within limits. `suspended`: what a locked deployment refuses, and it runs no pipelines, and a Tenzir-hosted one does not run at all. It ends only when the deployment is resumed, which the usage limit allows once usage is back within limits. Allowed values: `active`, `locked`, `suspended`.
  * `operation` (`enum`, required): What the state of a deployment admits or refuses on it: delivering a configuration to it, changing the branch it follows, starting an ad-hoc pipeline on it, creating it, running it as a larger type, and resuming it from a suspension. Allowed values: `deliverConfiguration`, `changeTracker`, `startAdhocPipeline`, `createDeployment`, `upsize`, `resume`.

* **DeploymentSuspended** (`DeploymentSuspended`)

  * `_tag` (`"DeploymentSuspended"`, required)
  * `message` (`string`, required)

### `429`: Busy

Media type: `application/json`

* `_tag` (`"Busy"`, required)
* `message` (`string`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)

### `503`: ServiceUnavailable

Media type: `application/json`

* `_tag` (`"ServiceUnavailable"`, required)
