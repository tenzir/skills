---
title: "Ingest endpoints"
description: "Understand how ingest endpoints accept events over HTTPS, buffer them on the platform, and hand them to the pipelines of your deployments."
canonical: https://tenzir.com/docs/explanations/ingest-endpoints
source: https://tenzir.com/docs/explanations/ingest-endpoints.md
section: "Docs"
---

# Ingest endpoints

> Understand how ingest endpoints accept events over HTTPS, buffer them on the platform, and hand them to the pipelines of your deployments.

An **ingest endpoint** is an HTTPS address on the platform that turns every request it receives into an event. Webhooks, SaaS integrations, and your own applications can push events to Tenzir without you opening a port or managing a certificate. Your [deployments](deployment.md) read the events with the [`ingest`](../reference/operators/ingest.md) operator.

A deployment dials out to the [platform](platform.md), so nothing on the internet can reach it, including a sender that can only push. Ingest endpoints close that gap: senders push to the platform, and deployments pull from it over the connection they already have. This makes ingest endpoints the one place where the platform holds your events themselves.

## How an event travels

Every endpoint has a name that is unique in your organization, such as `app-events`, a URL, and a secret token:

1. A sender sends an HTTP request to the URL, with the token in an `Authorization: Bearer` header.
2. The platform checks the token, appends the request to the endpoint’s buffer, and answers `202 Accepted`.
3. A pipeline on a deployment that may read the endpoint runs `ingest "app-events"` and receives each request as one event, with its method, path, query, headers, and body.

The endpoint accepts any method and any path below its URL, so a sender can encode where an event comes from in the path. The token never reaches a pipeline.

## Buffering and positions

Each endpoint buffers events for up to 24 hours and up to 10 GB, whichever comes first. Beyond either limit, the oldest events go first. A deployment can restart or a pipeline can fail, and the events wait until the pipeline reads them again.

Every pipeline that runs `ingest` receives every event of the endpoint, so two pipelines can archive and analyze the same events without taking them away from each other:

* A deployed pipeline remembers how far it has read and resumes there when it restarts. The first time it runs, it starts with the events that arrive from then on, not with what the endpoint already buffers. Its file path identifies it, so renaming the file starts over.
* An ad-hoc pipeline, such as one in the Explorer, remembers nothing. Every time it runs, it reads only the events that arrive while it runs.

If a pipeline falls so far behind that the endpoint drops events it has not read yet, the pipeline skips ahead to the events that arrive next.

When a deployment loses access to an endpoint or you delete the deployment, the platform discards the positions of its pipelines.

## Who may send and who may read

* **The token** decides who may send. Treat it like a password. Rotating it invalidates the old token within seconds. Tokens start with `tzi_`, which makes a leaked one easy to spot in logs and secret scanners.
* **Readers** decide which deployments may read: every deployment of the organization, or only the workspaces and deployments you list. A deployment that loses access stops reading.

Managing endpoints takes the **Ingest Endpoints** permission, as our [IAM reference](../reference/iam.md) lists.

## Limits

| Status | Reason                                                       |
| ------ | ------------------------------------------------------------ |
| `202`  | The platform accepted the event.                             |
| `401`  | The request has no token, or the token is unknown.           |
| `413`  | The request body is larger than 1 MB.                        |
| `415`  | The request body is not valid UTF-8 text.                    |
| `503`  | The buffer is unavailable for the moment. Retry the request. |

A sender that retries on `503` and on network errors loses no events. The endpoint does not detect duplicates, so a retried request may arrive twice.

## See also

* [Receive events with ingest endpoints](../guides/collect/receive-events-with-ingest-endpoints.md)
* [Platform](platform.md)
* [Deployment](deployment.md)
* [IAM](../reference/iam.md)
