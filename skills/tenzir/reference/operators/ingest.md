---
title: "ingest"
canonical: https://tenzir.com/docs/reference/operators/ingest
source: https://tenzir.com/docs/reference/operators/ingest.md
section: "Docs"
---

# ingest

> Reads the events that an ingest endpoint received.

Reads the events that an ingest endpoint received.

```tql
ingest name:string
```

## Description

The `ingest` operator reads the requests that senders sent to an [ingest endpoint](../../explanations/ingest-endpoints.md). The endpoint must allow the deployment to read it.

Tenzir-hosted deployments only

For now, only [Tenzir-hosted deployments](../../guides/add-a-deployment.md) in `europe-west3` can read ingest endpoints. On a self-hosted deployment, the operator fails with an error that says so. A node outside a deployment does not offer the operator at all.

Each request becomes one event:

```tql
{
  received_at: time,
  method: string,
  path: string,
  query: record,
  headers: record,
  body: string,
}
```

The `method` is in lowercase, and `headers` leaves out the `authorization` header. Parse the `body` in the pipeline that follows, for example with [`parse_json`](../functions/parse_json.md).

Every pipeline that reads an endpoint receives every event. A deployed pipeline resumes where it left off when it restarts, and starts with the events that arrive from then on the first time it runs or after you rename its file. An ad-hoc pipeline, such as one in the Explorer, reads only the events that arrive while it runs.

### `name: string`

The name of the ingest endpoint.

## Examples

### Parse JSON webhooks

```tql
ingest "app-events"
where method == "post"
this = body.parse_json()
```

### Route requests by their path

```tql
ingest "alerts"
where path == "/firewall"
this = body.parse_json()
publish "firewall-alerts"
```

## See Also

* [`accept_http`](accept_http.md)
* [Ingest endpoints](../../explanations/ingest-endpoints.md)
* [Receive events with ingest endpoints](../../guides/collect/receive-events-with-ingest-endpoints.md)
