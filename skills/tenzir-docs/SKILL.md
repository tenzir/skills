---
name: tenzir-docs
description: >-
  Answer questions using the Tenzir documentation. Use whenever the user asks
  about TQL syntax, pipeline operators, functions, data parsing or
  transformation, normalization, OCSF mapping, enrichment, lookup tables,
  contexts, packages, nodes, platform setup, deployment, configuration,
  integrations with tools like Splunk, Kafka, S3, Elasticsearch, or any other
  Tenzir feature. Also use when the user asks how to collect, route, filter,
  aggregate, or export security data with Tenzir, or needs help writing or
  debugging TQL pipelines, even if they don't mention 'Tenzir' explicitly but
  are clearly working in a Tenzir context.
---

# Tenzir Documentation Map

> The security data pipeline platform.

## How to use this skill

Navigate the documentation based on the type of question:

| Question type | Where to look |
|---|---|
| "How do I…" tasks | [Guides](guides.md) — step-by-step instructions organized by task |
| Operator or function syntax | [Operator Index](reference/operators-index.md) or [Function Index](reference/functions-index.md), then the specific page |
| Integration setup (Splunk, Kafka, S3…) | [Integrations](integrations.md) — per-product setup and pipeline examples |
| Concepts (nodes, pipelines, deployment) | [Explanations](explanations.md) — architecture and design |
| Learning from scratch | [Tutorials](tutorials.md) — guided lessons |
| TQL language rules | [Language](explanations/language.md), [Expressions](reference/expressions.md), [Statements](reference/statements.md) |

Always read the relevant page before answering. Prefer TQL examples from the
documentation over inventing syntax.

## Answer patterns

**Operator syntax question** — *"How does `where` work?"*
→ Read [where](reference/operators/where.md), explain the syntax, show the doc's TQL examples.

**Integration question** — *"How do I send data to Splunk?"*
→ Read [Splunk](integrations/splunk.md), provide the pipeline example from the page.

**Task question** — *"How do I parse syslog?"*
→ Read [Parse delimited text](guides/parsing/parse-delimited-text.md) and
[read_syslog](reference/operators/read_syslog.md). Combine the guide's approach
with the operator reference.

## [Guides](guides.md)

Guides are practical step-by-step explanation to help you achieve a specific goal.

### Get Started

#### [Create account](guides/installation/create-account.md)

The Tenzir Platform is a web interface for managing pipelines and nodes.

#### [Manage a pipeline](guides/basic-usage/manage-a-pipeline.md)

This guide shows you how to control pipeline lifecycles through the app or API.

#### [Overview](guides/installation.md)

This guide shows you how to install the Tenzir CLI to run pipelines locally or deploy a persistent node.

#### [Quickstart](guides/quickstart.md)

Drowning in logs, alerts, and rigid tools?

#### [Run pipelines](guides/basic-usage/run-pipelines.md)

You can run a pipeline via the platform, on the command line using the tenzir binary, or as code via the configuration file.

#### [Tenzir v6 Migration](guides/tenzir-v6-migration.md)

Learn how to migrate legacy TQL pipelines to Tenzir v6, adopt the new execution patterns, and use temporary compatibility controls while you update.

### Setup

#### [Choose a scenario](guides/platform-setup/choose-a-scenario.md)

We provide several examples of possible platform deployment scenarios.

#### [Configure a node](guides/node-setup/configure-a-node.md)

The default node configuration is optimized for most common scenarios.

#### [Configure blob storage](guides/platform-setup/configure-blob-storage.md)

The blob storage service exists for exchanging files between the platform and nodes.

#### [Configure dashboards](guides/platform-management/configure-dashboards.md)

You can pre-define dashboards for your static workspaces.

#### [Configure database](guides/platform-setup/configure-database.md)

A PostgreSQL database stores the internal state of the platform.

#### [Configure identity provider](guides/platform-setup/configure-identity-provider.md)

The identity provider (IdP) handles authentication for the Tenzir Platform.

#### [Configure internal services](guides/platform-setup/configure-internal-services.md)

This guide shows you how to configure the three internal Tenzir services: the UI, Gateway, and Platform API.

#### [Configure reverse proxy](guides/platform-setup/configure-reverse-proxy.md)

This guide shows you how to configure a reverse proxy for the Tenzir Platform.

#### [Configure secret store](guides/platform-setup/configure-secret-store.md)

The Tenzir Platform provides a secret store for each workspace.

#### [Configure TLS](guides/node-setup/configure-tls.md)

Set up TLS encryption for operators and platform connections

#### [Configure workspaces](guides/platform-management/configure-workspaces.md)

Workspaces in the platform logically group nodes, secrets, and dashboards.

#### [Deploy a node](guides/node-setup/deploy-a-node.md)

Deploying a node means spinning it up in one of the supported runtimes.

#### [Deploy on AWS](guides/platform-setup/deploy-on-aws.md)

This guide walks you through deploying the Tenzir Platform Sovereign Edition on AWS using CloudFormation.

#### [Manage organization members](guides/platform-management/manage-organization-members.md)

This guide shows you how to invite people to your organization, manage existing members, and understand the role-based permission model.

#### [Manage organization workspaces](guides/platform-management/manage-organization-workspaces.md)

This guide shows you how to create, view, and delete workspaces that belong to an organization.

#### [Manage organizations](guides/platform-management/manage-organizations.md)

This guide shows you how to create, configure, and delete organizations in the Tenzir Platform.

#### [Overview](guides/ai-workbench.md)

Build your own AI Workbench by bringing an AI agent and configuring it with Tenzir’s agent skills.

#### [Overview](guides/node-setup.md)

The Tenzir Node is the vehicle to run pipelines.

#### [Overview](guides/platform-setup.md)

The Tenzir Platform acts as a fleet management control plane for Tenzir Nodes.

##### [Provision a node](guides/node-setup/provision-a-node.md)

##### [Run the platform](guides/platform-setup/run-the-platform.md)

##### [Size a node](guides/node-setup/size-a-node.md)

##### [Start the API](guides/node-setup/start-the-api.md)

##### [Tune performance](guides/node-setup/tune-performance.md)

##### [Use agent skills](guides/ai-workbench/use-agent-skills.md)

#### [Use ephemeral nodes](guides/platform-management/use-ephemeral-nodes.md)

An ephemeral node is ideal for temporary or auto-scaling deployments.

### Work with Data

#### [Aggregate event streams](guides/analytics/aggregate-event-streams.md)

This guide shows you how to aggregate event streams with summarize and window.

#### [Clean up values](guides/normalization/clean-up-values.md)

This guide shows you how to clean and normalize values in your data before mapping to a schema.

#### [Collect metrics](guides/analytics/collect-metrics.md)

Tenzir keeps track of metrics about node resource usage, pipeline state, and runtime performance.

#### [Convert data formats](guides/transformation/convert-data-formats.md)

Data comes in many formats.

#### [Deduplicate events](guides/optimization/deduplicate-events.md)

The deduplicate operator provides a powerful mechanism to remove duplicate events in a pipeline.

#### [Enrich events with AI](guides/enrichment/enrich-events-with-ai.md)

Add AI-generated summaries and labels to OCSF events in Tenzir pipelines

#### [Enrich with asset inventory](guides/enrichment/enrich-with-asset-inventory.md)

Add asset inventory context to OCSF endpoint and user fields

#### [Enrich with threat intel](guides/enrichment/enrich-with-threat-intel.md)

Add threat intelligence to OCSF enrichments, observables, and OSINT fields

#### [Execute Sigma rules](guides/enrichment/execute-sigma-rules.md)

Run Sigma detection rules on parsed Windows Event Logs and OCSF process events

#### [Export from a node](guides/edge-storage/export-from-a-node.md)

Exporting (or querying) data can be done by running a pipeline that begins with the export input operator.

#### [Expose data as a server](guides/routing/expose-data-as-server.md)

This guide shows you how to make pipeline data available to external consumers by starting an HTTP server.

#### [Fan out with subpipelines](guides/routing/fan-out-with-subpipelines.md)

This guide shows you how to fan out an event stream into subpipelines with each and group.

#### [Fetch via HTTP and APIs](guides/collecting/fetch-via-http-and-apis.md)

This guide shows you how to interact with HTTP APIs using fromhttp and tohttp operators.

#### [Filter and select data](guides/transformation/filter-and-select-data.md)

Filtering and selecting are fundamental operations when working with data streams.

#### [Get data from the network](guides/collecting/get-data-from-the-network.md)

This guide shows you how to receive data directly from network sources using TQL.

#### [Import into a node](guides/edge-storage/import-into-a-node.md)

Importing (or ingesting) data can be done by running a pipeline that ends with the import output operator.

#### [Load-balance pipelines](guides/routing/load-balance-pipelines.md)

This guide shows you how to distribute events across multiple destinations using the loadbalance operator.

#### [Manipulate strings](guides/transformation/manipulate-strings.md)

String manipulation is essential for cleaning, formatting, and transforming text data.

#### [Map to ASIM](guides/normalization/map-to-asim.md)

This guide shows you how to map events to Microsoft Sentinel Advanced Security Information Model (ASIM) records in TQL.

#### [Map to CIM](guides/normalization/map-to-cim.md)

This guide shows you how to map events to Splunk Common Information Model (CIM) fields in TQL.

#### [Map to ECS](guides/normalization/map-to-ecs.md)

This guide shows you how to map events to Elastic Common Schema (ECS) in TQL.

#### [Map to OCSF](guides/normalization/map-to-ocsf.md)

This guide shows you how to write OCSF mapping operators in TQL.

#### [Map to UDM](guides/normalization/map-to-udm.md)

This guide shows you how to map events to Google SecOps Unified Data Model (UDM) records in TQL.

#### [Mask sensitive data](guides/transformation/mask-sensitive-data.md)

This guide shows you how to mask sensitive fields such as IP addresses, email addresses, account identifiers, and credentials.

#### [Normalize data](guides/normalization.md)

This guide provides an overview of data normalization in TQL.

#### [Overview](guides/collecting.md)

This guide provides an overview of data collection in TQL.

#### [Parse binary data](guides/parsing/parse-binary-data.md)

This guide shows you how to parse binary data formats into structured events.

#### [Parse delimited text](guides/parsing/parse-delimited-text.md)

This guide shows you how to parse text streams into structured events.

#### [Parse string fields](guides/parsing/parse-string-fields.md)

This guide shows you how to extract structured data from string fields using TQL’s parsing functions.

##### [Read and watch files](guides/collecting/read-and-watch-files.md)

##### [Read from data stores](guides/collecting/read-from-data-stores.md)

##### [Read from message brokers](guides/collecting/read-from-message-brokers.md)

#### [Reshape complex data](guides/transformation/reshape-complex-data.md)

Real-world data is rarely flat.

#### [Send to destinations](guides/routing/send-to-destinations.md)

This guide shows you how to send data to various destinations using TQL output operators.

#### [Shape lists](guides/transformation/shape-lists.md)

Lists (arrays) contain ordered sequences of values.

#### [Shape records](guides/transformation/shape-records.md)

Records (objects) contain key-value pairs.

#### [Show available schemas](guides/edge-storage/show-available-schemas.md)

When you write a pipeline, you often reference field names.

#### [Slice and sample data](guides/optimization/slice-and-sample-data.md)

When working with data streams, you often need to control which events flow through your pipeline.

#### [Split and merge streams](guides/routing/split-and-merge-streams.md)

This guide shows you how to connect pipelines using publish and subscribe operators.

#### [Transform data at rest](guides/edge-storage/transform-data-at-rest.md)

This guide shows you how to transform data already stored in a node.

#### [Transform values](guides/transformation/transform-values.md)

Transforming values is a fundamental part of data processing.

#### [Use lookup tables](guides/enrichment/use-lookup-tables.md)

Store reference data in lookup tables and apply it to OCSF events

#### [Work with time](guides/transformation/work-with-time.md)

Time is fundamental in data analysis.

### Build

#### [Add constants](guides/packages/add-constants.md)

This guide shows you how to define package-wide constants in a constants.tql file and reference them as pkg::$name from the package’s own operators and pipelines, as well as from any pipeline that uses the package.

#### [Add contexts](guides/packages/add-contexts.md)

This guide shows you how to add enrichment contexts to your package.

#### [Add custom runners](guides/testing/add-custom-runners.md)

Runners tell tenzir-test how to execute a discovered file.

#### [Add operators](guides/packages/add-operators.md)

This guide shows you how to create user-defined operators (UDOs) for your package.

#### [Add pipelines](guides/packages/add-pipelines.md)

This guide shows you how to add deployable pipelines to your package.

#### [Configure inputs](guides/packages/configure-inputs.md)

This guide shows you how to make packages configurable with inputs.

#### [Configure project hooks](guides/testing/configure-project-hooks.md)

This guide shows you how to configure tenzir-test project hooks for setup and cleanup tasks that belong next to your tests.

#### [Create a package](guides/packages/create-a-package.md)

This guide shows you how to create a package from scratch.

#### [Create fixtures](guides/testing/create-fixtures.md)

This guide shows you how to create a fixture, wire it into the test harness, and use it from a test.

#### [Install a package](guides/packages/install-a-package.md)

Write your own package

#### [Maintain a changelog](guides/packages/maintain-a-changelog.md)

This guide shows you how to manage changelog entries and publish releases with tenzir-ship.

#### [Publish a package](guides/packages/publish-a-package.md)

This guide shows you how to publish your package.

#### [Run fixtures](guides/testing/run-fixtures.md)

This guide shows you how to start fixtures in standalone mode without running tests.

#### [Run tests](guides/testing/run-tests.md)

This guide shows you how to run existing integration tests with the tenzir-test framework.

#### [Test packages](guides/packages/test-packages.md)

This guide shows you how to add tests to your package.

#### [Write tests](guides/testing/write-tests.md)

This guide shows you how to create integration tests with the tenzir-test framework.

### Contribute

#### [Build from source](guides/development/build-from-source.md)

Tenzir uses CMake as build system with a C++23 compiler.

#### [Code of Conduct](guides/contribution/code-of-conduct.md)

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

#### [Git and GitHub Workflow](guides/contribution/workflow.md)

The following diagram visualizes our branching model:

#### [Security Policy](guides/contribution/security.md)

Security is a serious matter for us.

#### [Setup syntax highlighting](guides/development/setup-syntax-highlighting.md)

Install TQL language extensions for syntax highlighting in your editor

#### [Write a node plugin](guides/development/write-a-node-plugin.md)

This guide shows you how to extend Tenzir with custom operators, formats, or connectors by writing a C++ plugin.

## [Tutorials](tutorials.md)

Tutorials are learning-oriented lessons that take you through a series of steps to complete a project.

### Fundamentals

#### [Learn idiomatic TQL](tutorials/learn-idiomatic-tql.md)

This tutorial teaches you to write TQL that is clear, efficient, and maintainable.

#### [Map data to OCSF](tutorials/map-data-to-ocsf.md)

In this tutorial you’ll learn how to map events to Open Cybersecurity Schema Framework (OCSF).

#### [Write a package](tutorials/write-a-package.md)

This tutorial teaches you how packages bundle pipelines, operators, contexts, and examples.

### Analytics

#### [Plot data with charts](tutorials/plot-data-with-charts.md)

In this tutorial, you will learn how to use pipelines to plot data as charts.

## [Explanations](explanations.md)

Explanations are big-picture explanations of higher-level Tenzir concepts.

### Architecture

#### [Deployment](explanations/deployment.md)

This page explains Tenzir’s deployment architecture, which separates data processing from management through a layered design.

#### [Language](explanations/language.md)

The Tenzir Query Language (TQL) is a dataflow language designed for processing of unstructured byte-streams and semi-structured events.

#### [Node](explanations/node.md)

A node is a running process that manages and executes pipelines.

#### [Pipeline](explanations/pipeline.md)

A Tenzir pipeline is a chain of operators that represents a dataflow.

#### [Platform](explanations/platform.md)

The platform provides fleet management for nodes.

### Concepts

#### [Configuration](explanations/configuration.md)

This page explains how to configure the Tenzir CLI and Node.

#### [Enrichment](explanations/enrichment.md)

Enrichment means adding contextual data to events.

#### [Packages](explanations/packages.md)

This page explains how packages bundle pipelines, operators, contexts, and examples into a deployable unit.

#### [Secrets](explanations/secrets.md)

Operators accept secrets as parameters for sensitive values, such as authentication tokens, passwords, or even URLs.

### Help

#### [FAQs](explanations/faqs.md)

This page answers frequently asked questions about Tenzir.

#### [Glossary](explanations/glossary.md)

This page defines central terms in the Tenzir ecosystem.

## [Reference](reference.md)

The reference has nitty-gritty technical descriptions of how Tenzir works.

### Language (TQL)

#### [Expressions](reference/expressions.md)

Expressions form the computational core of TQL.

#### [Programs](reference/programs.md)

TQL programs compose statements into complete data processing workflows that can execute.

#### [Statements](reference/statements.md)

TQL programs are a sequence of statements.

#### [Type System](reference/types.md)

This page explains TQL’s type system, which provides strong typing with automatic inference.

### Components

#### [Command line interface](reference/platform/command-line-interface.md)

The Tenzir Platform command-line interface (CLI) allows you to interact with the Tenzir Platform from the command line to manage organizations, workspaces, and nodes.

#### [Configuration](reference/node/configuration.md)

The below example configuration ships with every Tenzir package.

#### [Configuration](reference/platform/configuration.md)

These settings configure the Tenzir Platform.

#### [Helm chart](reference/node/helm-chart.md)

The Tenzir Helm chart deploys one or more tenzir-node instances on a Kubernetes cluster.

### Tools

#### [Ship Framework](reference/ship-framework.md)

tenzir-ship ships as a Python package that requires Python 3.12 or later.

#### [Test Framework](reference/test-framework.md)

The tenzir-test harness discovers and runs integration tests for pipelines, fixtures, and custom runners.

### Security

#### [AWS Authentication](reference/aws-authentication.md)

Tenzir’s AWS operators authenticate with AWS using the AWS SDK’s default credential chain, an OIDC web identity token, or static credentials.

### API

#### [Overview](reference/api/node/overview.md)

Use the Tenzir REST API to manage pipelines and read pipeline output from a Tenzir node.

#### [Overview](reference/api/platform/overview.md)

API for managing Tenzir Platform workspaces, nodes, and dashboards.

#### [Check node health](reference/api/node/health/ping-node.md)

post/ping

#### [List Nodes](reference/api/platform/nodes/list-nodes.md)

post/user/list-nodes

#### [Create Node](reference/api/platform/nodes/create-node.md)

post/user/create-node

#### [Rename Node](reference/api/platform/nodes/rename-node.md)

post/user/rename-node

#### [Delete Node](reference/api/platform/nodes/delete-node.md)

post/user/delete-node

#### [Get Node Token](reference/api/platform/nodes/get-node-token.md)

post/user/get-node-token

#### [Generate Client Config](reference/api/platform/nodes/generate-client-config.md)

post/user/generate-client-config

#### [Generate Download Url](reference/api/platform/nodes/generate-download-url.md)

post/user/generate-download-url

#### [Create Demo Node](reference/api/platform/nodes/create-demo-node.md)

post/user/create-demo-node

#### [Retire Demo Node](reference/api/platform/nodes/retire-demo-node.md)

post/user/retire-demo-node

#### [Proxy](reference/api/platform/nodes/proxy.md)

post/user/proxy

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-get.md)

get/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-post.md)

post/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-put.md)

put/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-delete.md)

delete/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-patch.md)

patch/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-head.md)

head/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Transparent Proxy](reference/api/platform/nodes/node-proxy-options.md)

options/user/node-proxy/{tenantid}/{nodeid}/{httppath}

#### [Proxy Cached](reference/api/platform/nodes/proxy-cached.md)

post/user/proxy-cached

#### [Read pipeline output](reference/api/node/pipeline-output/read-pipeline-output.md)

post/serve

#### [Store](reference/api/platform/dashboards/store.md)

post/user/dashboard/store

#### [Get](reference/api/platform/dashboards/get.md)

post/user/dashboard/get

#### [Read multiple pipeline outputs](reference/api/node/pipeline-output/read-multiple-pipeline-outputs.md)

post/serve-multi

#### [List](reference/api/platform/dashboards/list.md)

post/user/dashboard/list

#### [Delete](reference/api/platform/dashboards/delete.md)

post/user/dashboard/delete

#### [Add](reference/api/platform/alerts/add.md)

post/user/alert/add

#### [Create a new pipeline](reference/api/node/pipelines/create-pipeline.md)

post/pipeline/create

#### [Delete an existing pipeline](reference/api/node/pipelines/delete-pipeline.md)

post/pipeline/delete

#### [List](reference/api/platform/alerts/list.md)

post/user/alert/list

#### [Delete](reference/api/platform/alerts/delete.md)

post/user/alert/delete

#### [Launch a new pipeline](reference/api/node/pipelines/launch-pipeline.md)

post/pipeline/launch

#### [List pipelines](reference/api/node/pipelines/list-pipelines.md)

post/pipeline/list

#### [Reset the TTL of an existing pipeline](reference/api/node/pipelines/reset-pipeline-ttl.md)

post/pipeline/reset-ttl

#### [Update pipeline state](reference/api/node/pipelines/update-pipeline.md)

post/pipeline/update

#### [Add External Store](reference/api/platform/secrets/add-external-store.md)

post/user/secrets/add-external-store

#### [Set Default Store](reference/api/platform/secrets/select-store.md)

post/user/secrets/select-store

#### [Delete External Store](reference/api/platform/secrets/delete-external-store.md)

post/user/secrets/delete-external-store

#### [List Stores](reference/api/platform/secrets/list-stores.md)

post/user/secrets/list-stores

#### [Add](reference/api/platform/secrets/add.md)

post/user/secrets/add

#### [Update](reference/api/platform/secrets/update.md)

post/user/secrets/update

#### [Remove](reference/api/platform/secrets/remove.md)

post/user/secrets/remove

#### [List](reference/api/platform/secrets/list.md)

post/user/secrets/list

#### [Delete Tenant](reference/api/platform/tenant/delete-tenant.md)

post/user/delete-tenant

#### [Update Tenant Name](reference/api/platform/tenant/rename-tenant.md)

post/user/rename-tenant

#### [Switch Tenant](reference/api/platform/tenant/switch-tenant.md)

post/user/switch-tenant

#### [Health](reference/api/platform/account/health.md)

get/user/health

#### [Get Login Info](reference/api/platform/account/get-login-info.md)

post/user/get-login-info

#### [Get Webapp Key](reference/api/platform/admin/webapp-key.md)

get/admin/webapp-key

#### [Create Tenant](reference/api/platform/admin/create-tenant.md)

post/admin/create-tenant

#### [Generate User Key](reference/api/platform/admin/generate-user-key.md)

post/admin/generate-user-key

#### [Spawn Node](reference/api/platform/admin/spawn-node.md)

post/admin/spawn-node

#### [List Tenants](reference/api/platform/admin/global-tenant-list.md)

get/admin/global-tenant-list

#### [Delete Tenant](reference/api/platform/admin/force-delete-tenant.md)

post/admin/force-delete-tenant

#### [Check Connectivity](reference/api/platform/admin/check-connectivy.md)

post/admin/check-connectivy

#### [Update Tenant Owner](reference/api/platform/admin/update-tenant.md)

post/admin/update-tenant

#### [Add Auth Function](reference/api/platform/admin/add-auth-function.md)

post/admin/add-auth-function

#### [Delete Auth Function](reference/api/platform/admin/delete-auth-function.md)

post/admin/delete-auth-function

### Operators

#### [Operators](reference/operators.md)

Tenzir comes with a wide range of built-in pipeline operators.

### Functions

#### [Functions](reference/functions.md)

Functions appear in expressions and take positional and/or named arguments, producing a value as a result of their computation.

#### Node Index

- [Configuration](reference/node/configuration.md)
- [Helm chart](reference/node/helm-chart.md)

#### Platform Index

- [Command line interface](reference/platform/command-line-interface.md)
- [Configuration](reference/platform/configuration.md)

### Indexes

For the complete operator listing by category, read [Operator Index](reference/operators-index.md).

For the complete function listing by category, read [Function Index](reference/functions-index.md).

## Integrations

#### [Amazon CloudWatch Logs integration](integrations/amazon/cloudwatch.md)

Centralized logging for AWS resources, applications, and custom logs.

#### [Amazon Kinesis integration](integrations/amazon/kinesis.md)

Ingest and process real-time data streams from Amazon Kinesis.

#### [Amazon MSK integration](integrations/amazon/msk.md)

Publish and subscribe to Amazon's managed Kafka service.

#### [Amazon S3 integration](integrations/amazon/s3.md)

Store, retrieve, and manage data objects in a scalable and durable cloud storage service.

#### [Amazon Security Lake integration](integrations/amazon/security-lake.md)

Send OCSF events to Amazon Security Lake.

#### [Amazon SQS integration](integrations/amazon/sqs.md)

Send, receive, and manage messages between distributed applications.

#### [AMQP integration](integrations/amqp.md)

Send and receive messages between systems using a standardized, protocol-based approach.

#### [ArcSight integration](integrations/arcsight.md)

OpenText ArcSight is a SIEM and log management ecosystem.

#### [Azure Blob Storage integration](integrations/microsoft/azure-blob-storage.md)

Store, retrieve, and manage unstructured data at scale.

#### [Azure Event Hubs integration](integrations/microsoft/azure-event-hubs.md)

Real-time data streaming platform and event ingestion service.

#### [ClickHouse integration](integrations/clickhouse.md)

Send structured events to ClickHouse tables.

#### [CrowdStrike integration](integrations/crowdstrike.md)

Provides real-time event data including process, file, and network activity.

#### [Elasticsearch integration](integrations/elasticsearch.md)

Index, search, and analyze data in a distributed and scalable manner.

#### [File integration](integrations/file.md)

Read from and write to files.

#### [Fluent Bit integration](integrations/fluent-bit.md)

Collect, process, and forward logs and metrics from various sources to many sinks.

#### [FTP integration](integrations/ftp.md)

Transfer files between a client and a server using a reliable, connection-based protocol.

#### [Google Cloud Logging integration](integrations/google/cloud-logging.md)

Send events to Google's log management solution

#### [Google Cloud Pub/Sub integration](integrations/google/cloud-pubsub.md)

Send, receive, and process messages between decoupled applications and services.

#### [Google Cloud Storage integration](integrations/google/cloud-storage.md)

Store, retrieve, and manage data objects across a scalable, cloud-based environment.

#### [Google SecOps integration](integrations/google/secops.md)

Send events to Google SecOps

#### [Graph integration](integrations/microsoft/graph.md)

Microsoft Graph is the unified API for Microsoft 365, Microsoft Entra ID, and other Microsoft cloud services.

#### [Graylog integration](integrations/graylog.md)

Collect, index, and analyze log data for monitoring and troubleshooting.

#### [HTTP integration](integrations/http.md)

Transfer and receive data between clients and servers using a request-response protocol.

#### [IBM QRadar integration](integrations/qradar.md)

Send security events to IBM Security QRadar for SIEM analytics and incident investigation.

#### [Kafka integration](integrations/kafka.md)

Publish, subscribe, store, and process streams of records in a distributed messaging system.

#### [Microsoft Defender integration](integrations/microsoft/defender.md)

Detect, prevent, and respond to security threats across endpoints and networks.

#### [Microsoft SQL Server integration](integrations/microsoft/sql-server.md)

Provides audit logs for database activity, logins, and errors.

#### [Microsoft Windows Event Logs integration](integrations/microsoft/windows-event-logs.md)

Collects Security, System, Application, and other critical OS logs.

#### [MySQL integration](integrations/mysql.md)

Connects to MySQL over the network using the MySQL wire protocol.

#### [NATS integration](integrations/nats.md)

NATS is a messaging system for services, edge deployments, and cloud-native applications.

#### [Network Interface Card integration](integrations/nic.md)

Acquire packets from the network and process them with pipelines.

#### [OpenSearch integration](integrations/opensearch.md)

Search, analyze, and visualize data with a distributed, open-source platform.

#### [Prometheus integration](integrations/prometheus.md)

Prometheus is an open-source monitoring system and time-series database.

#### [Sentinel & Log Analytics integration](integrations/microsoft/sentinel-log-analytics.md)

A rapidly growing cloud-native SIEM, tightly integrated with the Azure ecosystem and a strategic destination for Microsoft-centric organizations.

#### [SentinelOne Data Lake integration](integrations/sentinelone-data-lake.md)

Send events to SentinelOne Singularity™ Data Lake

#### [Snowflake integration](integrations/snowflake.md)

Store, analyze, and share structured and semi-structured data with a cloud-based warehouse.

#### [Splunk integration](integrations/splunk.md)

Collect, index, and analyze machine-generated data for monitoring, searching, and troubleshooting.

#### [Suricata integration](integrations/suricata.md)

Detect, log, and analyze network traffic for intrusion detection, prevention, and monitoring.

#### [Syslog integration](integrations/syslog.md)

Send and receive Syslog over UDP, TCP, and other protocols.

#### [TCP integration](integrations/tcp.md)

Establish, maintain, and terminate reliable, connection-oriented communication over IP networks.

#### [UDP integration](integrations/udp.md)

Send and receive lightweight, connectionless datagrams over IP networks.

#### [Velociraptor integration](integrations/velociraptor.md)

Collect, monitor, and analyze endpoint data for digital forensics and incident response.

#### [Wazuh integration](integrations/wazuh.md)

Collects security telemetry and runs detections.

#### [Zeek integration](integrations/zeek.md)

Inspect, log, and analyze network traffic for security and operational insights.

#### [ZeroMQ integration](integrations/zeromq.md)

Send, receive, and route messages asynchronously over various transport protocols.

#### [Zscaler integration](integrations/zscaler.md)

Logs all web, firewall, and DNS traffic for users and locations.
