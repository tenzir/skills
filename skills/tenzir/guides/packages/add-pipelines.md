---
title: "Add pipelines"
canonical: https://tenzir.com/docs/guides/packages/add-pipelines
source: https://tenzir.com/docs/guides/packages/add-pipelines.md
section: "Docs"
---

# Add pipelines

> This guide shows you how to add deployable pipelines to your package. You’ll learn about pipeline frontmatter options and when to use pipelines versus operators.

This guide shows you how to add deployable pipelines to your package. You’ll learn about pipeline frontmatter options and when to use pipelines versus operators.

Prefer operators

Ship reusable [user-defined operators](add-operators.md) and let users write the pipelines around them. A packaged pipeline hard-codes one deployment’s sources, destinations, and schedule, which users then have to configure through installation inputs instead of operator arguments. Add a pipeline when the package must own a running workflow, such as keeping a context current.

## Create a pipeline

The `pipelines` directory contains fully deployable TQL pipelines. Unlike [user-defined operators (UDOs)](add-operators.md), pipelines are complete units that must begin with an input operator and end with an output operator.

Pipelines typically use source operators to fetch and parse data, then call UDOs from the same package to transform the parsed events:

pipelines/fetch-and-normalize.tql

```tql
every 1h {
  from_http "https://api.example.com/events" {
    read_json
  }
}
vendor::ocsf::map
ocsf_derive
ocsf_cast
publish "normalized-events"
```

When you install the package, the node automatically runs any enabled pipelines. The source operator handles collection and may already decode data into events, while the package UDO handles the product’s remaining parsing, cleanup, mapping, and other reusable transformation logic. Use enabled pipelines only when the package should take action as soon as it is installed. Ship optional operational workflows as disabled templates unless automatic execution is the package’s core behavior.

Public mapping UDOs should default to mapping the current event, so `vendor::ocsf::map` works when the source operator already emits parsed source events. Use the paved-road normalizer for the product’s complete standard procedure. This example starts with raw lines, so normalization includes parsing and provenance:

pipelines/fetch-raw-and-normalize.tql

```tql
every 1h {
  from_http "https://api.example.com/events" {
    read_lines
  }
}
vendor::ocsf::normalize line
ocsf_derive
ocsf_cast
publish "normalized-events"
```

If collection already produces structured product events, the pipeline calls the mapper instead, because the normalizer always starts from a raw payload:

pipelines/fetch-json-and-map.tql

```tql
every 1h {
  from_http "https://api.example.com/events" {
    read_json
  }
}
vendor::ocsf::map
ocsf_derive
ocsf_cast
publish "normalized-events"
```

Use the composable parser and mapper when the pipeline must inspect or modify the structured source event between stages:

pipelines/fetch-raw-and-customize.tql

```tql
every 1h {
  from_http "https://api.example.com/events" {
    read_lines
  }
}
vendor::parse line, into=event
event.tenant = "production"
vendor::ocsf::map event, into=ocsf
this = {
  ...ocsf,
  raw_data: line,
  raw_data_size: line.length_bytes(),
}
ocsf_derive
ocsf_cast
publish "normalized-events"
```

## Configure pipeline behavior

Configure pipelines using YAML frontmatter at the beginning of the TQL file. The following options are available:

### `name` and `description`

Add metadata to identify the pipeline in the UI:

pipelines/update-context.tql

```tql
---
name: Update Threat Intel
description: >
  Fetches threat intelligence hourly and updates the lookup table.
---


every 1h {
  from_http "https://feeds.example.com/iocs.json" {
    read_json
  }
}
context_update "threat-intel", key=indicator
```

### `restart-on-error`

Configure automatic restart behavior when the pipeline encounters an error. By default, pipelines stop running and show an error state.

pipelines/resilient-fetch.tql

```tql
---
restart-on-error: 5m  # Restart after 5 minutes on failure
---


every 1h {
  from_http "https://api.example.com/data"
}
publish "raw-data"
```

Options:

* Omit the option, or set it to `null` or `false` to disable automatic restarts
* Set it to `true` to enable restarts with a default delay of 1 minute
* Set it to a valid duration (for example, `5m`, `1h`) to enable restarts with a custom delay

### `disabled`

Set to `true` to disable the pipeline. Disabled pipelines don’t run when the package is installed, but users can enable them manually.

pipelines/notify-webhook.tql

```tql
---
name: Notify Webhook
description: >
  Sends selected security events to a webhook. Enable manually if needed.
disabled: true
---


subscribe "security-events"
where severity_id >= 3
to_http "https://hooks.example.com/security-events"
```

Ship disabled by default

For opt-in operation, add `disabled: true` to pipeline frontmatter. This ships the pipeline as a template that users must explicitly enable, combining the convenience of ready-made pipelines with predictable installation behavior.

### `unstoppable`

Set to `true` to make the pipeline run automatically and indefinitely. You cannot pause or stop unstoppable pipelines manually. If they complete, they end up in a failed state. If you enable `restart-on-error`, they restart after the specified duration.

pipelines/critical-router.tql

```tql
---
unstoppable: true
restart-on-error: 1m
---


from_kafka "critical-events"
publish "critical-events"
```

### Complete example

Combine multiple options:

pipelines/publish-as-ocsf.tql

```tql
---
name: Publish as OCSF
description: >
  Fetches threat intel hourly and publishes OCSF events to the `ocsf` topic.
disabled: true
restart-on-error: 5m
---


every 1h {
  from_http "https://api.example.com/events" {
    read_lines
  }
}
vendor::ocsf::normalize line
publish "ocsf"
```

## Operators versus pipelines

Understanding when to use operators versus pipelines helps you design packages that are both powerful and flexible.

| Aspect        | Operators                      | Pipelines                            |
| ------------- | ------------------------------ | ------------------------------------ |
| **Purpose**   | Reusable building blocks       | Complete workflows                   |
| **Execution** | Called explicitly by other TQL | Run automatically on install         |
| **Structure** | No input/output restrictions   | Must have input and output operators |
| **Testing**   | Test with sample data          | Test with fixtures or mocks          |

**Use operators when:**

* You want to provide reusable transformations
* The logic should be composable with other operations
* Users decide when and how to invoke the functionality

**Use pipelines when:**

* You need background tasks like periodic data fetching
* The workflow is complete and self-contained
* The package should take action upon installation

For flexible packages, consider shipping both: operators that provide reusable capabilities and disabled pipelines that demonstrate how to compose them.

## See also

* [Create a package](create-a-package.md)
* [Add operators](add-operators.md)
* [Add contexts](add-contexts.md)
* [Onboard a data source](../../tutorials/onboard-a-data-source.md)
* [Packages](../../explanations/packages.md)
