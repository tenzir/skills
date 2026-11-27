---
title: "Read ingest endpoint metrics"
description: "What one ingest endpoint accepted over a range, at a step the server picks so that a day has hourly points, with the totals and when it last accepted a request."
canonical: https://tenzir.com/docs/reference/api/ingest-endpoints/read-ingest-endpoint-metrics
source: https://tenzir.com/docs/reference/api/ingest-endpoints/read-ingest-endpoint-metrics.md
section: "Docs"
---

# Read ingest endpoint metrics

> What one ingest endpoint accepted over a range, at a step the server picks so that a day has hourly points, with the totals and when it last accepted a request.

`GET /api/organizations/{org}/ingest-endpoints/{endpointId}/metrics`

What one ingest endpoint accepted over a range, at a step the server picks so that a day has hourly points, with the totals and when it last accepted a request. Requires IngestEndpoint.readMetrics.

Authentication: `bearer` + `session` + `apiKey`.

## Path parameters

* `org` (`Id / Slug`, required): An organization identified by its ID or slug

  Any of:

  * **Id** (`string`)
  * **Slug** (`string`)

* `endpointId` (`string`, required): A UUID

## Query parameters

* `from` (`string`, required)
* `to` (`string`, optional)

## Responses

### `200`: What one endpoint accepted over a range

Media type: `application/json`

* `from` (`string`, required)

* `to` (`string`, required)

* `step` (`number / enum`, required)

  Any of:

  * **Option 1** (`number`)
  * **Option 2** (`enum`)

* `total` (`Ingest Endpoint Traffic`, required)

  * `events` (`number / enum`, required)

    Any of:

    * **Option 1** (`number`)
    * **Option 2** (`enum`)

  * `bytes` (`number / enum`, required)

    Any of:

    * **Option 1** (`number`)
    * **Option 2** (`enum`)

* `lastEventAt` (`string | null`, optional)

* `points` (`array<Ingest Endpoint Traffic Point>`, required): Steps without traffic are left out

  Array items:

  * `at` (`string`, required)

  * `events` (`number / enum`, required)

    Any of:

    * **Option 1** (`number`)
    * **Option 2** (`enum`)

  * `bytes` (`number / enum`, required)

    Any of:

    * **Option 1** (`number`)
    * **Option 2** (`enum`)

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
