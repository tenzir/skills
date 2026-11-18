---
title: "Declare contexts"
description: "Declare lookup tables, Bloom filters, and GeoIP databases in a deployment's configuration"
canonical: https://tenzir.com/docs/guides/enrich/declare-contexts
source: https://tenzir.com/docs/guides/enrich/declare-contexts.md
section: "Docs"
---

# Declare contexts

> Declare lookup tables, Bloom filters, and GeoIP databases in a deployment's configuration

A [context](../../explanations/enrichment.md) holds the reference data that pipelines enrich events with. Your deployment’s configuration declares which contexts exist, pipelines keep them filled, and other pipelines enrich events with them. This guide walks through that lifecycle for a threat intelligence lookup table, from declaring it to removing it.

Before you begin

* You need a deployment and a configuration in its workspace.
* Your role needs **Configuration** → **Write** and **Deploy** to change and deploy the configuration, **Contexts** → **Inspect** to see the contexts a deployment runs, and **Adhoc Pipelines** → **Create**, **Run**, and **View Owned** to look up a key. Our [IAM reference](../../reference/iam.md) lists the details.

## Declare a context

Every context is one YAML file in the `contexts/` folder of your configuration:

* contexts/

  * threat-indicators.yaml

* pipelines/

  * update-threat-indicators.tql
  * enrich-network-events.tql

The file names the type of context and its settings:

contexts/threat-indicators.yaml

```yaml
type: lookup-table
persist-interval: 5min
write-timeout: 7d
```

The context takes its name from the file, here `threat-indicators`. Set `name` in the file when you want another one, for example with spaces. The `persist-interval` keeps the table across restarts, and the `write-timeout` drops an indicator that the feed hasn’t reported for a week.

Tenzir has three types of context:

| Type           | Holds                                    | Filled by                                                                         |
| -------------- | ---------------------------------------- | --------------------------------------------------------------------------------- |
| `lookup-table` | Values under keys, including subnet keys | [`context_update`](../../reference/operators/context_update.md) |
| `bloom-filter` | A set of keys, in fixed space            | [`context_update`](../../reference/operators/context_update.md) |
| `geoip`        | A MaxMind database                       | Its own download from `url`                                                       |

Our reference for [context files](../../reference/contexts.md) lists the settings of each type.

Add the file to your configuration:

* MCP

  Ask your agent for the context:

  ```prompt
  Add a lookup table context named threat-indicators to my configuration on main. Persist it every 5 minutes and drop entries that the feed hasn't reported for 7 days. Commit it.
  ```

  The agent writes `contexts/threat-indicators.yaml` into your personal draft of the branch and commits it.

* App

  1. Open **Contexts** with the deployment selected.
  2. Select **Add context**.
  3. Enter the name `threat-indicators`, select **Lookup table**, and set the **Persist interval** to `5min` and **Expire after last write** to `7d`.
  4. Confirm the dialog. It writes the file into your draft of the branch, and the list marks the context as **not committed**.
  5. Commit the draft from the top bar.

* CLI

  Clone the configuration, add the file, then commit and push:

  ```sh
  tenzir config clone prod
  cd tenzir-workspace
  # Write contexts/threat-indicators.yaml with your editor.
  tenzir config apply -m 'Add the threat-indicators context'
  ```

The platform checks context files while you edit them, so that a deploy doesn’t fail on a typo.

Deploy the configuration to create the context, as our guide on [deploying configurations](../change-configurations.md#deploy-the-latest-commit) shows. With **Auto deploy** on, the commit deploys by itself. The context starts empty.

## Fill the context

Add a pipeline that keeps the context current. This one fetches a feed every hour and stores each indicator:

pipelines/update-threat-indicators.tql

```tql
every 1h {
  from_http "https://feeds.example.com/indicators.json"
}
context_update "threat-indicators", key=indicator
```

The `key` parameter selects the enrichment key. Without `value`, the whole event becomes the value stored under the key. Commit and deploy the pipeline the same way as the context file.

A GeoIP context needs no such pipeline, because it downloads its database itself:

contexts/geo.yaml

```yaml
type: geoip
url: https://example.com/GeoLite2-City.mmdb
reload-interval: 1d
persist: true
```

## Verify the context

Once the deploy went through, check that the deployment runs the context and that it holds what the feed delivered:

* MCP

  Ask your agent:

  ```prompt
  Run an ad-hoc pipeline on edge-1 that enriches {dst_ip: 203.0.113.7} with the context threat-indicators, and tell me whether the key is in it.
  ```

  The agent runs the pipeline with `start_adhoc_pipeline` and reads its events.

* App

  1. Open **Contexts** with the deployment selected.
  2. Find `threat-indicators` in the list. The **Details** column shows how many entries the table holds, such as `1,204 entries`.

  A context that the configuration declares but the deployment doesn’t run yet shows **pending deployment**, and one with settings that the next deploy changes shows **pending update**.

  To look up a key, run an ad-hoc pipeline in the **Explorer**:

  ```tql
  from {dst_ip: 203.0.113.7}
  context_enrich "threat-indicators", key=dst_ip, into=threat
  ```

* CLI

  Run an ad-hoc pipeline on the deployment that looks up a key:

  ```sh
  tenzir run -r 'from {dst_ip: 203.0.113.7}
  context_enrich "threat-indicators", key=dst_ip, into=threat'
  ```

* API

  List the contexts that the deployment runs, with what each holds:

  ```sh
  curl -H "x-tenzir-api-key: $TENZIR_API_KEY" \
    https://platform.tenzir.com/api/organizations/<org>/workspaces/<workspace>/deployments/<deployment>/contexts
  ```

  Each context has a `name`, a `type`, and `details` that depend on the type, such as `num_entries` for a lookup table.

When the table holds the key, the `threat` field holds the stored value, and `null` otherwise. A GeoIP context that failed to load its database shows the error in its details.

## Enrich events

Enrich events with [`context_enrich`](../../reference/operators/context_enrich.md) in any other pipeline:

pipelines/enrich-network-events.tql

```tql
subscribe "network-events"
context_enrich "threat-indicators", key=dst_ip, into=threat
where threat != null
publish "alerts"
```

When the context holds the key, the `into` field holds the stored value. Our guide on [using lookup tables](use-lookup-tables.md) shows where results belong in OCSF events.

## Change a context

Edit the context file the same way as you added it, and deploy again. The context keeps its content when it can take the new settings, and starts over empty when it can’t:

* A lookup table takes any change. New timeouts apply to the entries it holds already.
* A Bloom filter starts over when its `capacity` or `fp-probability` changes, because it cannot be resized.
* A GeoIP context starts over when its `url` changes, and loads from the new source right away.
* Any context starts over when its `type` changes.

Renaming a file without setting `name` renames the context, which also starts it over. Pipelines that use the context keep running when it starts over with the same type. Before you deploy, the app’s **Contexts** page marks a context that the deploy changes with **pending update**.

A file that the deployment can’t read refuses the whole configuration, and the running contexts stay as they are.

## Remove a context

Delete the context file and deploy. The deployment removes the context together with what it persisted, and the app’s **Contexts** page marks it with **pending removal** until you deploy. Pipelines that still use it fail, so remove or change them in the same deploy.

To empty a lookup table, you can’t change a setting, because the table takes every change in place. Only a rename or a change of its `type` empties it, and a rename also changes the name that pipelines use. A Bloom filter empties when its `capacity` or `fp-probability` changes, and a GeoIP context loads again when its `url` changes. To drop entries that stop arriving instead, give a lookup table a short `write-timeout`.

## See Also

* [Contexts](../../reference/contexts.md)
* [Change configurations](../change-configurations.md)
* [Use lookup tables](use-lookup-tables.md)
* [Enrich with threat intel](enrich-with-threat-intel.md)
* [Add enrichment contexts](../../tutorials/add-enrichment-contexts.md)
* [Deployment](../../explanations/deployment.md)
* [Enrichment](../../explanations/enrichment.md)
