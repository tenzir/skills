---
title: "Receive events with ingest endpoints"
description: "Give webhooks and applications an HTTPS address to push events to, and read them in the pipelines of your deployments."
canonical: https://tenzir.com/docs/guides/collect/receive-events-with-ingest-endpoints
source: https://tenzir.com/docs/guides/collect/receive-events-with-ingest-endpoints.md
section: "Docs"
---

# Receive events with ingest endpoints

> Give webhooks and applications an HTTPS address to push events to, and read them in the pipelines of your deployments.

This guide sets up an [ingest endpoint](../../explanations/ingest-endpoints.md), watches a first event arrive, and deploys a pipeline that reads the endpoint with the [`ingest`](../../reference/operators/ingest.md) operator.

Before you begin

You need a [Tenzir-hosted deployment](../add-a-deployment.md) in `europe-west3` and a configuration in its workspace. Self-hosted deployments cannot read ingest endpoints yet. Your role needs **Ingest Endpoints** → **Manage**, **Configuration** → **Write** and **Deploy**, and **Adhoc Pipelines** → **Create** and **Run**. Our [IAM reference](../../reference/iam.md) lists the details.

## Create an endpoint

Open **Ingest Endpoints** in the app and select **New ingest endpoint**:

1. Enter a name, such as `app-events`. It must be unique in your organization and consist of 3 to 21 lowercase letters, digits, and single dashes.
2. Describe what sends events here.
3. Choose which deployments may read the endpoint.

The endpoint’s page shows the URL and the token that senders need.

## Watch for events

Select **View in Explorer** on the endpoint’s page. The Explorer runs this pipeline and shows each event as it arrives:

```tql
ingest "app-events"
where method == "post"
this = body.parse_json()
```

The pipeline reads only the events that arrive while it runs, so keep the Explorer open while you send the first one. The `where` keeps only `POST` requests. If your sender uses another method, such as `PUT`, change or remove it, because the pipeline otherwise drops those events. [`parse_json`](../../reference/functions/parse_json.md) turns the body into the event that the sender meant.

## Send a first event

The endpoint’s page shows a `curl` command with the endpoint’s URL, and its copy button includes the token. Run it, or fill in the placeholders yourself:

```sh
curl --fail-with-body -X POST "<url>" \
  -H "Authorization: Bearer <token>" \
  -d '{"message": "hello from curl", "severity": "info"}'
```

The endpoint answers `202 Accepted` once it holds the event, and the event shows up in the Explorer. **Send test event** on the endpoint’s page does the same without a shell.

Configure your sender the same way: it must set the `Authorization` header. It may add a path or a query to the URL, such as `/audit?service=billing`, which reaches your pipeline in the `path` and `query` fields.

## Deploy a pipeline

Add the pipeline to the `pipelines/` folder of your configuration and send the events on:

* pipelines/

  * app-events.tql

pipelines/app-events.tql

```tql
ingest "app-events"
where method == "post"
this = body.parse_json()
publish "app-events"
```

[Deploy the configuration](../change-configurations.md). The pipeline starts with the events that arrive after you deploy it, so it does not receive what senders pushed before, such as your first event. When it restarts, it resumes where it left off. Other pipelines that read the endpoint receive every event too.

## Keep the endpoint safe

* **Rotate token** when the token leaks. The old token stops working within seconds, so update your senders right away.
* **Edit** next to **Readable by** changes which deployments may read.
* **Delete** removes the endpoint along with the events it still buffers.

## See also

* [Ingest endpoints](../../explanations/ingest-endpoints.md)
* [Fetch via HTTP and APIs](fetch-via-http-and-apis.md)
* [IAM](../../reference/iam.md)
