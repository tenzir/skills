---
title: "Start pipeline"
description: "Starts another run of the persisted deployed definition, not pending branch changes."
canonical: https://tenzir.com/docs/reference/api/pipelines/start-pipeline
source: https://tenzir.com/docs/reference/api/pipelines/start-pipeline.md
section: "Docs"
---

# Start pipeline

> Starts another run of the persisted deployed definition, not pending branch changes.

`POST /api/organizations/{org}/workspaces/{workspace}/deployments/{deploymentId}/pipelines/{pipelineId}/start`

Starts another run of the persisted deployed definition, not pending branch changes. Already running is a no-op. Does not change configuration. Requires Deployment.startPipeline

Authentication: `bearer` + `session` + `apiKey` + `key`.

## Path parameters

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

* `pipelineId` (`string`, required): An identifier that may be a path

## Responses

### `204`: \<No Content>

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

### `404`: PipelineNotFound | NotFound

Media type: `application/json`

Any of:

* **PipelineNotFound** (`PipelineNotFound`)

  * `_tag` (`"PipelineNotFound"`, required)
  * `message` (`string`, required)

* **NotFound** (`NotFound`)
  * `_tag` (`"NotFound"`, required)

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)

### `503`: ServiceUnavailable

Media type: `application/json`

* `_tag` (`"ServiceUnavailable"`, required)

### `504`: DeploymentTimeout

Media type: `application/json`

* `_tag` (`"DeploymentTimeout"`, required)
* `message` (`string`, required)
