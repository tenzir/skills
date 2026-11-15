---
name: tenzir
description: >-
  Answer questions using the documentation of Tenzir 6.22.0. Use whenever the
  user asks about TQL syntax, pipeline operators, functions, data parsing or
  transformation, normalization, OCSF mapping, enrichment, lookup tables,
  contexts, packages, nodes, platform setup, deployment, configuration,
  integrations with tools like Splunk, Kafka, S3, Elasticsearch, or any other
  Tenzir feature. Also use when the user asks how to collect, route, filter,
  aggregate, or export security data with Tenzir, or needs help writing or
  debugging TQL pipelines, even if they don't mention 'Tenzir' explicitly but
  are clearly working in a Tenzir context. Also use for questions about Tenzir
  the company or product, release notes and changelog, blog posts, and
  solution use cases.
---

# Tenzir Documentation Map

> The security data pipeline platform.

This map covers the documentation of Tenzir 6.22.0.
Every link below is relative to <https://tenzir.com/docs/v6.22.0/> and leads to the Markdown version of a page, which you can read on its own.

## How to use this skill

Navigate the documentation based on the type of question:

| Question type | Where to look |
|---|---|
| "How do I…" tasks | [Guides](guides.md) — step-by-step instructions organized by task |
| Operator or function syntax | [Operator Index](reference/operators.md) or [Function Index](reference/functions.md), then the specific page |
| Integration setup (Splunk, Kafka, S3…) | <https://tenzir.com/product/integrations.md> — per-product setup and pipeline examples |
| Concepts (nodes, pipelines, deployment) | [Explanations](explanations.md) — architecture and design |
| Learning from scratch | [Tutorials](tutorials.md) — guided lessons |
| TQL language rules | [Language](explanations/language.md), [Expressions](reference/expressions.md), [Statements](reference/statements.md) |

Always read the relevant page before answering. Prefer TQL examples from the
documentation over inventing syntax.

## Beyond the docs

This map covers only the documentation of Tenzir nodes. For anything else
about Tenzir, fetch these live pages on demand instead of answering from
memory:

| Topic | Where to look |
|---|---|
| Release notes, "when was X added/changed" | <https://tenzir.com/changelog.md> |
| Integrations with third-party products | <https://tenzir.com/product/integrations.md> |
| The platform, its API, the Helm chart, and the test and ship frameworks | <https://tenzir.com/docs/llms.txt> — they ship on their own schedule, so only the current documentation has them |
| Blog posts and announcements | <https://tenzir.com/blog.md> |
| Solution use cases | <https://tenzir.com/solutions.md> |
| Company, product, events, everything else | <https://tenzir.com/llms.txt> — the full site index with per-page Markdown links |

## Answer patterns

**Operator syntax question** — *"How does `where` work?"*
→ Read [where](reference/operators/where.md), explain the syntax, show the doc's TQL examples.

**Integration question** — *"How do I send data to Splunk?"*
→ Read <https://tenzir.com/integrations/splunk.md> and [to_splunk](reference/operators/to_splunk.md), provide the pipeline example from the page.

**Task question** — *"How do I parse syslog?"*
→ Read [Parse delimited text](guides/parse/parse-delimited-text.md) and
[read_syslog](reference/operators/read_syslog.md). Combine the guide's approach
with the operator reference.

## [Guides](guides.md)

Guides are practical step-by-step explanation to help you achieve a specific goal.

### Get Started

#### [Quickstart](guides/quickstart.md)

Drowning in logs, alerts, and rigid tools?

#### [Overview](guides/installation.md)

This guide shows you how to install the Tenzir CLI to run pipelines locally or deploy a persistent node.

##### [Create account](guides/installation/create-account.md)

#### [Run pipelines](guides/basic-usage/run-pipelines.md)

You can run a pipeline via the platform, on the command line using the tenzir binary, or as code via the configuration file.

#### [Manage a pipeline](guides/basic-usage/manage-a-pipeline.md)

This guide shows you how to control pipeline lifecycles through the app or API.

### Setup

#### [Overview](guides/ai-workbench.md)

Build your own AI Workbench by bringing an AI agent and configuring it with Tenzir’s agent skills.

##### [Use agent skills](guides/ai-workbench/use-agent-skills.md)

#### [Overview](guides/node-setup.md)

The Tenzir Node is the vehicle to run pipelines.

##### [Provision a node](guides/node-setup/provision-a-node.md)

##### [Size a node](guides/node-setup/size-a-node.md)

##### [Deploy a node](guides/node-setup/deploy-a-node.md)

##### [Configure a node](guides/node-setup/configure-a-node.md)

##### [Configure TLS](guides/node-setup/configure-tls.md)

##### [Start the API](guides/node-setup/start-the-api.md)

##### [Tune performance](guides/node-setup/tune-performance.md)

#### [Overview](guides/platform-setup.md)

The Tenzir Platform acts as a fleet management control plane for Tenzir Nodes.

##### [Deploy on AWS](guides/platform-setup/deploy-on-aws.md)

##### [Choose a scenario](guides/platform-setup/choose-a-scenario.md)

##### [Configure reverse proxy](guides/platform-setup/configure-reverse-proxy.md)

##### [Configure internal services](guides/platform-setup/configure-internal-services.md)

##### [Configure identity provider](guides/platform-setup/configure-identity-provider.md)

##### [Configure database](guides/platform-setup/configure-database.md)

##### [Configure blob storage](guides/platform-setup/configure-blob-storage.md)

##### [Configure secret store](guides/platform-setup/configure-secret-store.md)

##### [Run the platform](guides/platform-setup/run-the-platform.md)

#### [Manage organizations](guides/platform-management/manage-organizations.md)

This guide shows you how to create, configure, and delete organizations in the Tenzir Platform.

#### [Manage organization members](guides/platform-management/manage-organization-members.md)

This guide shows you how to invite people to your organization, manage existing members, and understand the role-based permission model.

#### [Manage organization workspaces](guides/platform-management/manage-organization-workspaces.md)

This guide shows you how to create, view, and delete workspaces that belong to an organization.

#### [Configure workspaces](guides/platform-management/configure-workspaces.md)

Workspaces in the platform logically group nodes, secrets, and dashboards.

#### [Configure dashboards](guides/platform-management/configure-dashboards.md)

You can pre-define dashboards for your static workspaces.

#### [Use ephemeral nodes](guides/platform-management/use-ephemeral-nodes.md)

An ephemeral node is ideal for temporary or auto-scaling deployments.

### Work with Data

#### [Overview](guides/analyze.md)

Summarize event streams and compare current activity with prior behavior.

##### [Aggregate event streams](guides/analyze/aggregate-event-streams.md)

##### [Shape aggregation results](guides/analyze/shape-aggregation-results.md)

##### [Window event streams](guides/analyze/window-event-streams.md)

##### [Calculate aggregate statistics](guides/analyze/calculate-aggregate-statistics.md)

##### [Find unseen and rare values](guides/analyze/find-unseen-and-rare-values.md)

##### [Set adaptive thresholds from a baseline](guides/analyze/set-adaptive-thresholds-from-a-baseline.md)

##### [Identify distribution drift](guides/analyze/identify-distribution-drift.md)

##### [Find cardinality spikes](guides/analyze/find-cardinality-spikes.md)

#### [Overview](guides/collect.md)

Read events and bytes from files, APIs, brokers, stores, and networks.

##### [Read and watch files](guides/collect/read-and-watch-files.md)

##### [Fetch via HTTP and APIs](guides/collect/fetch-via-http-and-apis.md)

##### [Read from message brokers](guides/collect/read-from-message-brokers.md)

##### [Read from data stores](guides/collect/read-from-data-stores.md)

##### [Get data from the network](guides/collect/get-data-from-the-network.md)

#### [Overview](guides/detect.md)

Match security activity and model the resulting findings.

##### [Match events with TQL](guides/detect/match-events-with-tql.md)

##### [Model detections in OCSF](guides/detect/model-detections-in-ocsf.md)

##### [Detect over time windows](guides/detect/detect-over-time-windows.md)

##### [Baseline behavior from stored events](guides/detect/baseline-from-stored-events.md)

##### [Detect periodic behavior](guides/detect/detect-periodic-behavior.md)

##### [Create multi-stage detectors](guides/detect/create-multi-stage-detectors.md)

##### [Execute Sigma rules](guides/detect/execute-sigma-rules.md)

##### [Check Sigma rule compatibility with OCSF](guides/detect/check-sigma-rule-compatibility-with-ocsf.md)

##### [Scan bytes with YARA](guides/detect/scan-bytes-with-yara.md)

#### [Overview](guides/enrich.md)

Add context that the original event does not contain.

##### [Use lookup tables](guides/enrich/use-lookup-tables.md)

##### [Enrich with asset inventory](guides/enrich/enrich-with-asset-inventory.md)

##### [Enrich with threat intel](guides/enrich/enrich-with-threat-intel.md)

##### [Enrich events with AI](guides/enrich/enrich-events-with-ai.md)

#### [Overview](guides/normalize.md)

Map source-specific events into a shared schema.

##### [Map to ASIM](guides/normalize/map-to-asim.md)

##### [Map to CIM](guides/normalize/map-to-cim.md)

##### [Map to ECS](guides/normalize/map-to-ecs.md)

##### [Map to OCSF](guides/normalize/map-to-ocsf.md)

##### [Map to UDM](guides/normalize/map-to-udm.md)

#### [Overview](guides/optimize.md)

Reduce data volume and processing work in a pipeline.

##### [Filter and select data](guides/optimize/filter-and-select-data.md)

##### [Slice and sample data](guides/optimize/slice-and-sample-data.md)

##### [Deduplicate events](guides/optimize/deduplicate-events.md)

#### [Overview](guides/parse.md)

Turn byte streams and text fields into structured events.

##### [Parse delimited text](guides/parse/parse-delimited-text.md)

##### [Parse binary data](guides/parse/parse-binary-data.md)

##### [Parse string fields](guides/parse/parse-string-fields.md)

##### [Clean up values](guides/parse/clean-up-values.md)

#### [Overview](guides/protect.md)

Limit sensitive-data exposure while preserving useful structure.

##### [Mask sensitive data](guides/protect/mask-sensitive-data.md)

##### [Encrypt sensitive data](guides/protect/encrypt-sensitive-data.md)

#### [Overview](guides/replay.md)

Run stored events through live pipelines again.

##### [Replay historical events](guides/replay/replay-historical-events.md)

#### [Overview](guides/route.md)

Deliver event streams to the systems that need them.

##### [Send to destinations](guides/route/send-to-destinations.md)

##### [Expose data as a server](guides/route/expose-data-as-server.md)

##### [Split and merge streams](guides/route/split-and-merge-streams.md)

##### [Fan out with subpipelines](guides/route/fan-out-with-subpipelines.md)

##### [Load-balance pipelines](guides/route/load-balance-pipelines.md)

#### [Overview](guides/search.md)

Query stored events and continue processing the results.

##### [Export from a node](guides/search/export-from-a-node.md)

#### [Overview](guides/shape.md)

Prepare event fields and records for downstream processing.

##### [Transform values](guides/shape/transform-values.md)

##### [Manipulate strings](guides/shape/manipulate-strings.md)

##### [Normalize event timestamps](guides/shape/normalize-event-timestamps.md)

##### [Repair out-of-order events](guides/shape/repair-out-of-order-events.md)

##### [Calculate with time](guides/shape/calculate-with-time.md)

##### [Shape lists](guides/shape/shape-lists.md)

##### [Shape records](guides/shape/shape-records.md)

##### [Reshape complex data](guides/shape/reshape-complex-data.md)

##### [Convert data formats](guides/shape/convert-data-formats.md)

#### [Overview](guides/store.md)

Persist events for later search, replay, and analysis.

##### [Write partitioned files](guides/store/write-partitioned-files.md)

##### [Import into a node](guides/store/import-into-a-node.md)

##### [Show available schemas](guides/store/show-available-schemas.md)

##### [Transform data at rest](guides/store/transform-data-at-rest.md)

### Operate

#### [Overview](guides/observability.md)

Inspect node, pipeline, and host behavior.

##### [Inspect a node](guides/observability/inspect-a-node.md)

##### [Collect metrics](guides/observability/collect-metrics.md)

#### [Overview](guides/troubleshooting.md)

Diagnose compilation issues, pipeline failures, resource growth, and node connectivity.

##### [Debug field values](guides/troubleshooting/debug-field-values.md)

##### [Inspect the compilation output](guides/troubleshooting/inspect-compilation-output.md)

##### [Investigate slow pipelines](guides/troubleshooting/investigate-slow-pipelines.md)

##### [Investigate memory growth](guides/troubleshooting/investigate-memory-growth.md)

##### [Investigate storage growth](guides/troubleshooting/investigate-storage-growth.md)

##### [Reconnect an offline node](guides/troubleshooting/reconnect-an-offline-node.md)

### Build

#### [Install a package](guides/packages/install-a-package.md)

Write your own package

#### [Create a package](guides/packages/create-a-package.md)

This guide shows you how to create a package from scratch.

#### [Test packages](guides/packages/test-packages.md)

This guide shows you how to add tests to your package.

#### [Add operators](guides/packages/add-operators.md)

This guide shows you how to create user-defined operators (UDOs) for your package.

#### [Add pipelines](guides/packages/add-pipelines.md)

This guide shows you how to add deployable pipelines to your package.

#### [Add contexts](guides/packages/add-contexts.md)

This guide shows you how to add enrichment contexts to your package.

#### [Add constants](guides/packages/add-constants.md)

This guide shows you how to define package-wide constants in a constants.tql file and reference them as pkg::$name from the package’s own operators and pipelines, as well as from any pipeline that uses the package.

#### [Configure inputs](guides/packages/configure-inputs.md)

This guide shows you how to make packages configurable with inputs.

#### [Maintain a changelog](guides/packages/maintain-a-changelog.md)

This guide shows you how to manage changelog entries and publish releases with tenzir-ship.

#### [Publish a package](guides/packages/publish-a-package.md)

This guide shows you how to publish your package.

#### [Run tests](guides/testing/run-tests.md)

This guide shows you how to run existing integration tests with the tenzir-test framework.

#### [Write tests](guides/testing/write-tests.md)

This guide shows you how to create integration tests with the tenzir-test framework.

#### [Run fixtures](guides/testing/run-fixtures.md)

This guide shows you how to start fixtures in standalone mode without running tests.

#### [Create fixtures](guides/testing/create-fixtures.md)

This guide shows you how to create a fixture, wire it into the test harness, and use it from a test.

#### [Add custom runners](guides/testing/add-custom-runners.md)

Runners tell tenzir-test how to execute a discovered file.

#### [Configure project hooks](guides/testing/configure-project-hooks.md)

This guide shows you how to configure tenzir-test project hooks for setup and cleanup tasks that belong next to your tests.

### Contribute

#### [Code of Conduct](guides/contribution/code-of-conduct.md)

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

#### [Git and GitHub Workflow](guides/contribution/workflow.md)

The following diagram visualizes our branching model:

#### [Security Policy](guides/contribution/security.md)

Security is a serious matter for us.

#### [Setup syntax highlighting](guides/development/setup-syntax-highlighting.md)

Install TQL language extensions for syntax highlighting in your editor

#### [Build from source](guides/development/build-from-source.md)

Tenzir uses CMake as build system with a C++23 compiler.

### Other

#### [Work with time](guides/shape/work-with-time.md)

We split this guide into focused tasks.

## [Tutorials](tutorials.md)

Tutorials are learning-oriented lessons that take you through a series of steps to complete a project.

### Fundamentals

#### [Learn the data lifecycle](tutorials/learn-the-data-lifecycle.md)

Security data arrives as somebody else’s text and has to end up as something a detection, a dashboard, or an auditor can use.

#### [Learn idiomatic TQL](tutorials/learn-idiomatic-tql.md)

This tutorial teaches you to write TQL that is clear, efficient, and maintainable.

### Development

#### [Onboard a data source](tutorials/onboard-a-data-source.md)

Onboarding a data source means turning one product’s output into events that every later stage of the data lifecycle can use.

#### [Add enrichment contexts](tutorials/add-enrichment-contexts.md)

A context is state, not code.

### Analytics

#### [Plot data with charts](tutorials/plot-data-with-charts.md)

In this tutorial, you will learn how to use pipelines to plot data as charts.

#### [Build an OCSF lake with ClickHouse](tutorials/build-an-ocsf-lake-with-clickhouse.md)

Store OCSF events in ClickHouse, from a table that accepts anything to a tuned lake with typed columns, skip indexes, codecs, and per-class retention.

## [Explanations](explanations.md)

Explanations are big-picture explanations of higher-level Tenzir concepts.

### Architecture

#### [Deployment](explanations/deployment.md)

This page explains Tenzir’s deployment architecture, which separates data processing from management through a layered design.

#### [Pipeline](explanations/pipeline.md)

A Tenzir pipeline is a chain of operators that represents a dataflow.

#### [Node](explanations/node.md)

A node is a running process that manages and executes pipelines.

#### [Platform](explanations/platform.md)

The platform provides fleet management for nodes.

#### [Language](explanations/language.md)

Understand TQL's dataflow model, streaming and batch semantics, and support for events with different schemas.

#### [Executor](explanations/executor.md)

Understand how Tenzir compiles TQL into an execution plan and runs operators with fused handoffs, channels, subpipelines, and parallel jobs.

#### [Data model](explanations/data-model.md)

Understand how Tenzir stores events in columnar batches, keeps events of different shapes and types side by side, and selects rows with bitmaps instead of slicing batches apart.

### Concepts

#### [Configuration](explanations/configuration.md)

This page explains how to configure the Tenzir CLI and Node.

#### [Secrets](explanations/secrets.md)

Operators and functions accept secrets as arguments for sensitive values, such as authentication tokens, passwords, keys, or even URLs.

#### [Normalization](explanations/normalization.md)

Why Tenzir maps every source to OCSF first and translates from there

#### [Enrichment](explanations/enrichment.md)

Enrichment means adding contextual data to events.

#### [Detections](explanations/detections.md)

Understand how Tenzir matches, correlates, and models security evidence as detection results

#### [Packages](explanations/packages.md)

This page explains how packages bundle pipelines, operators, contexts, and examples into a deployable unit.

#### [Encryption](explanations/encryption.md)

Encryption turns a value into ciphertext that only the holders of a key can turn back into the original.

### Help

#### [Glossary](explanations/glossary.md)

This page defines the terms that name things you work with in Tenzir: the components, the entities a pipeline manipulates, and the units we ship.

## [Reference](reference.md)

The reference has nitty-gritty technical descriptions of how Tenzir works.

### Language (TQL)

#### [Type System](reference/types.md)

This page explains TQL’s type system, which provides strong typing with automatic inference.

#### [Expressions](reference/expressions.md)

Expressions form the computational core of TQL.

#### [Statements](reference/statements.md)

TQL programs are a sequence of statements.

#### [Programs](reference/programs.md)

TQL programs compose statements into complete data processing workflows that can execute.

#### [Overview](reference/optimizations.md)

Tenzir runs part of a pipeline where the data lives.

### Components

#### [Configuration](reference/node/configuration.md)

The below example configuration ships with every Tenzir package.

### Security

#### [AWS Authentication](reference/aws-authentication.md)

Tenzir’s AWS operators authenticate with AWS using the AWS SDK’s default credential chain, an OIDC web identity token, or static credentials.

#### [Azure Authentication](reference/azure-authentication.md)

Tenzir’s Azure operators authenticate with Microsoft Entra ID using the Azure SDK’s default credential chain, a shared account key, an application client secret, or workload identity federation.

### API

#### [Overview](reference/api/node/overview.md)

This reference is generated from the OpenAPI specification.

#### [Check node health](reference/api/node/health/ping-node.md)

post/ping

#### [Read pipeline output](reference/api/node/pipeline-output/read-pipeline-output.md)

post/serve

#### [Read multiple pipeline outputs](reference/api/node/pipeline-output/read-multiple-pipeline-outputs.md)

post/serve-multi

#### [Create a new pipeline](reference/api/node/pipelines/create-pipeline.md)

post/pipeline/create

#### [Delete an existing pipeline](reference/api/node/pipelines/delete-pipeline.md)

post/pipeline/delete

#### [Launch a new pipeline](reference/api/node/pipelines/launch-pipeline.md)

post/pipeline/launch

#### [List pipelines](reference/api/node/pipelines/list-pipelines.md)

post/pipeline/list

#### [Reset the TTL of an existing pipeline](reference/api/node/pipelines/reset-pipeline-ttl.md)

post/pipeline/reset-ttl

#### [Update pipeline state](reference/api/node/pipelines/update-pipeline.md)

post/pipeline/update

### Operators

#### [Operators](reference/operators.md)

Tenzir comes with a wide range of built-in pipeline operators.

### Functions

#### [Functions](reference/functions.md)

Functions appear in expressions and take positional and/or named arguments, producing a value as a result of their computation.

### Indexes

For the complete operator listing by category, read [Operator Index](reference/operators.md).

For the complete function listing by category, read [Function Index](reference/functions.md).

#### Node Index

- [Configuration](reference/node/configuration.md)

#### Overview Index

- [ClickHouse](reference/optimizations/clickhouse.md)
- [DuckDB](reference/optimizations/duckdb.md)
- [KQL](reference/optimizations/kql.md)
- [Microsoft SQL Server](reference/optimizations/microsoft-sql.md)
- [MySQL](reference/optimizations/mysql.md)
- [SentinelOne](reference/optimizations/sentinelone.md)
- [SPL](reference/optimizations/spl.md)
