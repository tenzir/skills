---
title: "Read workspace metrics"
description: "Throughput of every pipeline in a workspace over a range: totals, the range before for trends, the current rate, a sparkline and diagnostic counts."
canonical: https://tenzir.com/docs/reference/api/pipelines/read-workspace-metrics
source: https://tenzir.com/docs/reference/api/pipelines/read-workspace-metrics.md
section: "Docs"
---

# Read workspace metrics

> Throughput of every pipeline in a workspace over a range: totals, the range before for trends, the current rate, a sparkline and diagnostic counts.

`GET /api/organizations/{org}/workspaces/{workspace}/metrics`

Throughput of every pipeline in a workspace over a range: totals, the range before for trends, the current rate, a sparkline and diagnostic counts. Only deployments the caller may read metrics of are included

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `workspace` (`Id / Slug`, required): A workspace identified by its ID or slug within an organization

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

## Query parameters

* `from` (`string`, required)
* `to` (`string`, optional)
* `deployment` (`string`, optional): Only this deployment of the workspace; all by default
* `diagnostics` (`enum`, optional): Include counts per pipeline run: with run, over all that is retained of each run; with runInRange, over the part of each run within the range. Range-based counts are always included. Allowed values: `range`, `run`, `runInRange`.
* `runs` (`string<json>`, optional)
* `points` (`string`, optional)

## Responses

### `200`: Tenzir.Telemetry.WorkspaceMetrics

Media type: `application/json`

* `from` (`string`, required)

* `to` (`string`, required)

* `step` (`integer`, required): The step the server used, in seconds. Range: `>= 0, <= 9007199254740991`.

* `settled` (`string`, required)

* `pipelines` (`array<Workspace Pipeline>`, required)

  Array items:

  * `deploymentId` (`string`, required): A UUID

  * `pipelineId` (`string`, required): An identifier that may be a path

  * `sources` (`array<Connector Flow>`, required): Totals over the range, per source connector type

    Array items:

    * `connector` (`string`, required): The connector type, such as `kafka`
    * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

  * `sinks` (`array<Connector Flow>`, required): Totals over the range, per sink connector type

    Array items:

    * `connector` (`string`, required): The connector type, such as `kafka`
    * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

  * `total` (`Ingress and Egress`, required): Over the range

    * `ingress` (`Flow`, required): What passed one point of a pipeline in a window. Counters cover that window alone and are never running totals

      * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

    * `egress` (`Flow`, required): What passed one point of a pipeline in a window. Counters cover that window alone and are never running totals

      * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

  * `previous` (`Ingress and Egress`, required): Over the range of the same length before it

    * `ingress` (`Flow`, required): What passed one point of a pipeline in a window. Counters cover that window alone and are never running totals

      * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

    * `egress` (`Flow`, required): What passed one point of a pipeline in a window. Counters cover that window alone and are never running totals

      * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
      * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

  * `rate` (`object`, required): Ingress, and egress in the egress fields, per second over the last settled minute

    * `events` (`number / enum`, required)

      Any of:

      * **Option 1** (`number`)
      * **Option 2** (`enum`)

    * `bytes` (`number / enum`, required)

      Any of:

      * **Option 1** (`number`)
      * **Option 2** (`enum`)

    * `egressEvents` (`number / enum`, required)

      Any of:

      * **Option 1** (`number`)
      * **Option 2** (`enum`)

    * `egressBytes` (`number / enum`, required)

      Any of:

      * **Option 1** (`number`)
      * **Option 2** (`enum`)

  * `points` (`array<Spark Point>`, required)

    Array items:

    * `at` (`string`, required)
    * `events` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `bytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `egressEvents` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `egressBytes` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
    * `activity` (`integer`, required): Events all its sources read and all its sinks wrote in the step, external and internal alike. Zero where the deployment does not measure it. Range: `>= 0, <= 9007199254740991`.

  * `warnings` (`integer`, required): Over the part of the range within the last 30 days. Range: `>= 0, <= 9007199254740991`.

  * `errors` (`integer`, required): Over the part of the range within the last 30 days. Range: `>= 0, <= 9007199254740991`.

* `runDiagnostics` (`array<Run Diagnostic Counts>`, optional)

  Array items:

  * `deploymentId` (`string`, required): A UUID
  * `pipelineId` (`string`, required): An identifier that may be a path
  * `run` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
  * `errors` (`integer`, required) Range: `>= 0, <= 9007199254740991`.
  * `warnings` (`integer`, required) Range: `>= 0, <= 9007199254740991`.

### `400`: InvalidRange | CredentialConflict | Validation

Media type: `application/json`

Any of:

* **InvalidRange** (`InvalidRange`)

  * `_tag` (`"InvalidRange"`, required)
  * `message` (`string`, required)

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

### `500`: InternalServerError

Media type: `application/json`

* `_tag` (`"InternalServerError"`, required)

### `503`: ServiceUnavailable

Media type: `application/json`

* `_tag` (`"ServiceUnavailable"`, required)
